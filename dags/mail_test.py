import airflow 
from datetime import timedelta 
from airflow import DAG 
from datetime import datetime, timedelta 
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.email_operator import EmailOperator


# email_backend = airflow.utils.email.send_email_smtp

with DAG(
    "mail_test",
    start_date=datetime(2021, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "email_on_failure": False,
        "email_on_retry": False,
    },
) as dag:


    mail_test = EmailOperator(
        task_id='mail',
        to='amir.zahreddine@astronomer.io',
        subject='Daily Movers',
        html_content="""<h3>Email Test</h3>"""
    )

    mail_test