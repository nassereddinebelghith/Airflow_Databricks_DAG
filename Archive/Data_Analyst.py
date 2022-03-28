from airflow import DAG

from airflow.decorators import dag, task # DAG and task decorators for interfacing with the TaskFlow API
from airflow.providers.databricks.operators.databricks import (
    DatabricksSubmitRunOperator,
    DatabricksRunNowOperator,
)
from datetime import datetime, timedelta

# https://registry.astronomer.io/dags/databricks-tutorial

# Define params for Submit Run Operator

notebook_task = {
    "notebook_path": "/Workspace/Shared/dag-workshop",
}

# Define params for Run Now Operator
notebook_params = {"Variable": 5}


with DAG(
    "databricks_dag",
    start_date=datetime(2021, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 0,
        "retry_delay": timedelta(minutes=2),
    },
) as dag:

    # opr_submit_run = DatabricksSubmitRunOperator(
    #     task_id="submit_run",
    #     databricks_conn_id="databricks",
    #     new_cluster=new_cluster,
    #     notebook_task=notebook_task,
    # )

    opr_run_now = DatabricksRunNowOperator(
        task_id="run_now",
        databricks_conn_id="databricks",
        # job_id=5,
        notebook_params=notebook_params,
    )

    opr_run_now