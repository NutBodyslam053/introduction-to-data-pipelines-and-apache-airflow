# Workspace

## Running Airflow in Docker

Before we run Airflow, let's create these folders below first. Please note that if you're using Windows, you can skip this step.

```sh
mkdir -p mnt/dags mnt/logs mnt/plugins mnt/tests
```

On **Linux**, please make sure to configure the Airflow user for the docker-compose:

```sh
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

```sh
docker compose build
docker compose up
```

To stop Airflow, run:

```bash
docker compose down
```

Airflow commands
```bash
airflow dags list
airflow dags backfill --start-date 2024-02-09 --end-date 2024-02-10 weather_api_dag --reset-dagruns
airflow tasks test weather_api_dag get_weather_data
```