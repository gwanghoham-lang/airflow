import datetime
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
import random

with DAG(
    dag_id="dags_python_opeartor",
    schedule="0 0  * * *",
    start_date=pendulum.datetime(2025 , 8, 23, tz="Asia/Seoul"),
    catchup=False
) as dag:
    def select_fruit():
        fruit = ['apple','banana','orange','avocado']
        rand_int = random.randint(0,3)
        print(fruit[rand_int])
    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )
    py_t1