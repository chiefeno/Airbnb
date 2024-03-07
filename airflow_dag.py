from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 5, 6, 0, 0),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'daily_scripts',
    default_args=default_args,
    description='Run daily scripts at 6 AM',
    schedule_interval='0 6 * * *',  
) as dag:

    pipeline_execution = BashOperator(
        task_id='airbnb',
        bash_command='python pipeline_execution.py',
    )


    pipeline_execution
