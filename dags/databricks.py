import logging

from airflow import DAG
from airflow.decorators import task, dag
from airflow.providers.databricks.hooks.databricks import DatabricksHook
from airflow.providers.databricks.operators.databricks import (
    DatabricksSubmitRunOperator,
    DatabricksRunNowOperator,
)
# from include.databricks_helper import get_notebook_output




from datetime import datetime, timedelta

# https://docs.databricks.com/workspace/workspace-details.html#job-url-and-id
# https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/operators.html
# https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/operators.html#databricksrunnowoperator




DATABRICKS_CLUSTER_ID = "0222-192411-cnzydi8s"
DATABRICKS_CONNECTION_ID = "databricks_default"
notebook_task = {
    "notebook_path": "/Shared/data_analyst_dag_scrap",
}

# # Define params for Run Now Operator
# notebook_params = {"Variable": 5}


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
        task_id="run_now",
        databricks_conn_id=DATABRICKS_CONNECTION_ID,
        job_id=1087568806385694,
        do_xcom_push=True
    )

    @task
    def register_model(databricks_run_id: str):


        databricks_hook = DatabricksHook()
        model_uri = databricks_hook.get_run_output(databricks_run_id)['notebook_output']['result']



    # command = "curl --netrc --get https://dbc-0eb40f15-5780.cloud.databricks.com/api/2.0/jobs/runs/get-output --data run_id=3841"
    
    # capture_output = BashOperator(
    # task_id='capture_output',
    # bash_command=command
    # )





    # capture_data =  DatabricksHook(
    #     databricks_conn_id = DATABRICKS_CONNECTION_ID
    # )



    opr_submit_run >> opr_run_now
    # print(opr_run_now.output['run_id'])

    register_model(opr_run_now.output['run_id'])

# model_uri = get_notebook_output(databricks_run_id)
