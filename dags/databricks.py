import logging

from airflow import DAG
from airflow.decorators import task, dag
from airflow.providers.databricks.hooks.databricks import DatabricksHook
from airflow.providers.databricks.operators.databricks import (
    DatabricksSubmitRunOperator,
    DatabricksRunNowOperator,
)
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator



from datetime import datetime, timedelta






DATABRICKS_CLUSTER_ID = "0222-192411-cnzydi8s"
DATABRICKS_CONNECTION_ID = "databricks_default"
notebook_task = {
    "notebook_path": "/Shared/data_analyst_dag_scrap",
}


SQL_INSERT_STATEMENT="""

INSERT INTO SCRAP (Name, Value) 
VALUES ('test', '1');

"""





SNOWFLAKE_WAREHOUSE="DEMO"
SNOWFLAKE_DATABASE="SANDBOX"
SNOWFLAKE_SCHEMA="AMIRZAHREDDINE"
SNOWFLAKE_ROLE="AMIRZAHREDDINE"






with DAG(
    "databricks_dag",
    start_date=datetime(2021, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "email_on_failure": False,
        "email_on_retry": False,
    },
) as dag:

    opr_submit_run = DatabricksSubmitRunOperator(
        task_id="start_cluster",
        databricks_conn_id=DATABRICKS_CONNECTION_ID,
        existing_cluster_id=DATABRICKS_CLUSTER_ID,
        notebook_task=notebook_task,
    )

    opr_run_now = DatabricksRunNowOperator(
        task_id="run_job",
        databricks_conn_id=DATABRICKS_CONNECTION_ID,
        job_id=1087568806385694,
        do_xcom_push=True
    )


    @task
    def register_model(databricks_run_id: str):
        databricks_hook = DatabricksHook()
        model_uri = databricks_hook.get_run_output(databricks_run_id)['notebook_output']['result']


    # inserting data from model_uri to snowflake
    snowflake_op_with_params = SnowflakeOperator(
        task_id='snowflake_op_with_params',
        dag=dag,
        sql=SQL_INSERT_STATEMENT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
        role=SNOWFLAKE_ROLE,
    )



# https://airflow.apache.org/docs/apache-airflow-providers-snowflake/stable/_modules/airflow/providers/snowflake/example_dags/example_snowflake.html

# operator to refresh BI tool with new snowflake data

# SNOWFLAKE_SLACK_MESSAGE = (
#     "Results in an ASCII table:\n```{{ results_df | tabulate(tablefmt='pretty', headers='keys') }}```"
# )




    opr_submit_run >> opr_run_now >> register_model(opr_run_now.output['run_id']) >> snowflake_op_with_params
    
# snowflake_op_with_params