from airflow import DAG
from airflow.decorators import task
from airflow.providers.databricks.hooks.databricks import DatabricksHook
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime

DATABRICKS_CONNECTION_ID = "databricks_default"

portfolio = {
            "stocks": "MSFT AAPL IBM WMT SHOP GOOGL TSLA GME AMZN COST COKE CBRE NVDA AMD PG"
            }

with DAG(
    "databricks_dag",
    start_date=datetime(2021, 1, 1),
    schedule_interval='1 4 * * 1-5',
    catchup=False,
    default_args={
        "email_on_failure": False,
        "email_on_retry": False,
    },
) as dag:

    # run the databricks job
    opr_run_now = DatabricksRunNowOperator(
        task_id="run_job",
        databricks_conn_id=DATABRICKS_CONNECTION_ID,
        job_id=137122987688189,
        do_xcom_push=True,
        notebook_params = portfolio
    )

    # retreive xcom data from databricks endpoint
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

opr_run_now >> retrieve_xcom(opr_run_now.output['run_id']) >> mail