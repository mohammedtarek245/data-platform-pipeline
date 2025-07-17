from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
from datetime import timedelta

local_tz = pendulum.timezone("Africa/Cairo")

DEFAULT_ARGS = {
    "owner": "",
    "email": [""],    
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="local_kafka_spark_etl",
    description="ETL pipeline from Kafka → Spark → Archive JSON",
    default_args=DEFAULT_ARGS,
    schedule="0 14 * * *",  # 2 PM Cairo time
    start_date=pendulum.datetime(2025, 7, 15, 14, 0, tz=local_tz),
    catchup=False,
    tags=["etl", "spark", "kafka"],
) as dag:

    run_producer = BashOperator(
        task_id="run_producer_scripts",
        bash_command="python /opt/airflow/dags/producers/producer.py"
    )

    run_spark = BashOperator(
        task_id="run_spark_job",
        bash_command="spark-submit /opt/airflow/dags/spark_jobs/spark_consumer.py",
        env={
            "PYSPARK_PYTHON": "/usr/bin/python",
        },
    )

    archive_outputs = BashOperator(
        task_id="archive_json_outputs",
        bash_command=(
            "mkdir -p /opt/airflow/archive && "
            "ts=$(date +%Y%m%d_%H%M%S) && "
            "mkdir -p /opt/airflow/archive/${ts} && "
            "mv /opt/airflow/output/*.json /opt/airflow/archive/${ts}/ 2>/dev/null || true"
        ),
    )

    run_producer >> run_spark >> archive_outputs
