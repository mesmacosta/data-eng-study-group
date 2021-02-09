reference: https://towardsdatascience.com/an-apache-airflow-mvp-complete-guide-for-a-basic-production-installation-using-localexecutor-beb10e4886b2

# Env
docker-compose up

# connect
docker run -it --rm --network local_airflow postgres psql -h postgres -U airflow

# create schema
CREATE USER airflow PASSWORD 'airflow';
CREATE DATABASE airflow;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO airflow;

# Set venv
pyenv local 3.7.0
virtualenv venv --python 3.7.0
source ./venv/bin/activate

# Install airflow
- Mac users error: `xcode-select --install`

# Tutorial
http://airflow.apache.org/docs/apache-airflow/stable/start/local.html

# default sqllite
pip install apache-airflow

## postgresql
pip install apache-airflow['postgresql']
pip install psycopg2-binary

# Init airflow
airflow db init
airflow scheduler
airflow webserver

airflow users create -r Admin -u admin -e admin@example.com -f admin -l user -p test

# Dags default
/Users/costamarcelo/airflow/


## Dags
Place your DAGs in the /root/airflow/dags