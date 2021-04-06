from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import requests

default_args = {
    'start_date': datetime(2020, 1, 1) # when the task will start
}

COVID_DATA_URL = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
COVID_DATA_DST = '/home/airflow/covid_data'

def _is_data_available():
    request = requests.get(COVID_DATA_URL)
    if request.status_code != 200:
      raise Exception('Covid data not found')

with DAG('covid_processing',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False) as dag:

    is_data_available = PythonOperator(
        task_id='is_data_available',
        python_callable=_is_data_available
    )

    fetching_data = BashOperator(
        task_id='fetching_data',
        bash_command='curl -L {} > /tmp/covid_data.csv'.format(COVID_DATA_URL)
    )

    saving_data_to_dst = BashOperator(
        task_id='saving_data_to_dst',
        bash_command='mkdir -p {} && cp /tmp/covid_data.csv {}/covid_data.csv'.format(COVID_DATA_DST, COVID_DATA_DST)
    )

    is_data_available >> fetching_data >> saving_data_to_dst


