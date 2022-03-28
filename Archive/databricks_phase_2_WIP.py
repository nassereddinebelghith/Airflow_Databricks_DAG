from airflow import DAG
from airflow.providers.databricks.operators.databricks import (
    DatabricksSubmitRunOperator,
    DatabricksRunNowOperator,
)
from datetime import datetime, timedelta

# https://docs.databricks.com/workspace/workspace-details.html#job-url-and-id
# https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/operators.html
# https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/operators.html#databricksrunnowoperator


existing_cluster_id = "0222-192411-cnzydi8s"


notebook_task = {
    "notebook_path": "/Shared/dag-workshop",
}

# Define params for Run Now Operator
notebook_params = {"Variable": 5}


with DAG(
    "databricks_dag2",
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
        databricks_conn_id="databricks",
        existing_cluster_id=existing_cluster_id,
        notebook_task=notebook_task,
    )

    opr_run_now = DatabricksRunNowOperator(
        task_id="run_now",
        databricks_conn_id="databricks",
        job_id=368,
        notebook_params=notebook_params,
    )

    opr_submit_run >> opr_run_now


# 1 databricks entirely

# 2 create s3 connection in airflow for databricks aws connection
# snowflake operator
# 1. make s3 connection in airflow
# 2. s3 hook (import from provider aws hook) which takes connection ID into the bucket
# can then load files


'''
############ Phase 1 ############
1. A cluster is ran in Databricks
2. Within Databricks, a .ipynb(ish) file is ran. This outputs two dataframs, which will be used for further processing within the DAG
############ End of Phase 1 ############


############ Phase 2 ############
3. 


############ End of Phase 2 ############



'''




















