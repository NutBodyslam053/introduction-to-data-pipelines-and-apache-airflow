from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator

with DAG(
    "everyday_dag",
    schedule="0 0 * * *",
    start_date=timezone.datetime(2024, 1, 20),
):
    my_first_task = EmptyOperator(task_id="my_first_task")
    my_second_task = EmptyOperator(task_id="my_second_task")

    my_first_task >> my_second_task