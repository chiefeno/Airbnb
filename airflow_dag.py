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

    get_airbnb = BashOperator(
        task_id='airbnb',
        bash_command='python air_bnb.py',
    )

    get_customers = BashOperator(
        task_id='company',
        bash_command='python get_companies_data.py',
    )

    map_city_companies = BashOperator(
        task_id='map_city',
        bash_command='python map_trick.py',
    )

    insert_db = BashOperator(
        task_id='insert_db',
        bash_command='python insert.py',
    )

    get_airbnb >> get_customers >> map_city_companies >> insert_db