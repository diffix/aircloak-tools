from os import environ

import aircloak_tools as ac

AIRCLOAK_PG_HOST = "covid-db.aircloak.com"
AIRCLOAK_PG_PORT = 9432
AIRCLOAK_PG_USER = environ.get("AIRCLOAK_PG_USER")
AIRCLOAK_PG_PASSWORD = environ.get("AIRCLOAK_PG_PASSWORD")
DATASET = "cov_clear"

with ac.connect(AIRCLOAK_PG_HOST, AIRCLOAK_PG_PORT, AIRCLOAK_PG_USER, AIRCLOAK_PG_PASSWORD, DATASET) as conn:
    tables = conn.get_tables()
    print(tables)
