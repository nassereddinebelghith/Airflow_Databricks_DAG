from airflow import DAG
from airflow.decorators import task
from airflow.providers.databricks.hooks.databricks import DatabricksHook
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, date
from airflow.operators.dummy import DummyOperator
import ast


today = date.today().strftime("%d/%m/%Y")

DATABRICKS_CONNECTION_ID = "databricks_default"

portfolio = {
            "stocks": "MSFT AAPL IBM WMT SHOP GOOGL TSLA GME AMZN COST COKE CBRE NVDA AMD PG"
            }

def _split(data):
        if data == "No Email Required":
            print("LOG: No big movers, no email was sent")
            return 'no_mail'
        else:
            return 'mail'

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
        task_id="Run_Databricks_Job",
        databricks_conn_id=DATABRICKS_CONNECTION_ID,
        job_id=137122987688189,
        do_xcom_push=True,
        notebook_params = portfolio
    )

    @task
    def Retreive_Databricks_Output(id):

        # retreive xcom data using DatabricksHook
        databricks_hook = DatabricksHook()
        model_uri = databricks_hook.get_run_output(id)['notebook_output']['result']

        # conditional statement to decide on the content of the emails
        substring = "[]"
        if substring in model_uri:
            email = "No Email Required"
        else:
            model_uri = ast.literal_eval(model_uri) # convert string to list
            model_uri = [item for sublist in model_uri for item in sublist] # parse list to retreive desired information (its contents)
            model_uri = ' '.join(str(e) for e in model_uri)
            email = "Big movers for today, {today}, are: {df}".format(today = today, df=model_uri) # output email content

        return email

    output = Retreive_Databricks_Output(opr_run_now.output['run_id'])

    branching = BranchPythonOperator(
        task_id='Check_if_Email_is_Needed',
        op_args = [output],
        python_callable=_split,
    )

    no_mail = DummyOperator(
        task_id="No_Email_Required"
    )

    # send email
    mail = EmailOperator(
        task_id='Send_Email',
        to='amir.zahreddine@astronomer.io',
        subject='Daily Movers',
        html_content=output,
        )

opr_run_now >> output >> branching >> [no_mail, mail]
