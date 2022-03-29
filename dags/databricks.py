from airflow import DAG
# from airflow.providers.databricks.operators.databricks import (
#     DatabricksSubmitRunOperator,
#     DatabricksRunNowOperator,
# )



from airflow.providers.databricks.hooks.databricks import DatabricksHook
from airflow.providers.databricks.operators.databricks import (
    DatabricksSubmitRunOperator,
    DatabricksRunNowOperator,
)




from datetime import datetime, timedelta

# https://docs.databricks.com/workspace/workspace-details.html#job-url-and-id
# https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/operators.html
# https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/operators.html#databricksrunnowoperator




DATABRICKS_CLUSTER_ID = "0222-192411-cnzydi8s"
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
        databricks_conn_id="databricks",
        existing_cluster_id=DATABRICKS_CLUSTER_ID,
        notebook_task=notebook_task,
    )

    opr_run_now = DatabricksRunNowOperator(
        task_id="run_now",
        databricks_conn_id="databricks",
        job_id=1087568806385694,
        # notebook_params=notebook_params,
        do_xcom_push=True ####
    )






    opr_submit_run >> opr_run_now