from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

dag = DAG(
    'dag_use_case_1',
    default_args=default_args,
    description='Use case 1 Data Eng Study Group',
    schedule_interval='@daily',
    start_date=days_ago(1),
    tags=['dag_use_case_1'],
)

task_extract_dataset = BashOperator(
    task_id='extract_dataset',
    bash_command='curl -L https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.csv --output ~/airflow/source_data/owid-covid-data.csv',
    retries=3,
    dag=dag,
)

task_load_dataset = BashOperator(
    task_id='load_dataset',
    bash_command='cp ~/airflow/source_data/owid-covid-data.csv ~/airflow/dest_data/owid-covid-data.csv',
    retries=3,
    dag=dag,
)

task_extract_dataset >> task_load_dataset