import logging

from airflow import DAG
from airflow.decorators import task, dag
from airflow.providers.databricks.hooks.databricks import DatabricksHook
from airflow.providers.databricks.operators.databricks import (
    DatabricksSubmitRunOperator,
    DatabricksRunNowOperator,
)
# from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
# from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.email_operator import EmailOperator


from datetime import datetime, timedelta

DATABRICKS_CLUSTER_ID = "0222-192411-cnzydi8s"
DATABRICKS_CONNECTION_ID = "databricks_default"
notebook_task = {
    "notebook_path": "/Shared/dag-workshop",
}

# SQL_INSERT_STATEMENT="""

# INSERT INTO SCRAP (Name, Value) 
# VALUES ('test', '1');

# """
# SNOWFLAKE_WAREHOUSE="DEMO"
# SNOWFLAKE_DATABASE="SANDBOX"
# SNOWFLAKE_SCHEMA="AMIRZAHREDDINE"
# SNOWFLAKE_ROLE="AMIRZAHREDDINE" ['COKE', 'WMT', 'IBM', 'WMT', 'SHOP']



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
        notebook_task={
            'notebook_path': "/Shared/dag-workshop",
            'base_parameters': {
                'portfolio': 'SHOP'
            }
        }
    )

    opr_run_now = DatabricksRunNowOperator(
        task_id="run_job",
        databricks_conn_id=DATABRICKS_CONNECTION_ID,
        job_id=137122987688189,
        do_xcom_push=True
    )

    # get value from databricks from xcom
    @task
    def retrieve_xcom(databricks_run_id: str):
        databricks_hook = DatabricksHook()
        model_uri = databricks_hook.get_run_output(databricks_run_id)['notebook_output']['result']
        return model_uri

    # send email
    mail = EmailOperator(
        task_id='mail',
        to='amir.zahreddine@astronomer.io',
        subject='Daily Movers',
        html_content="{{ task_instance.xcom_pull(task_ids='retrieve_xcom') }}",
        )


    opr_submit_run >> opr_run_now >> retrieve_xcom(opr_run_now.output['run_id']) >> mail
