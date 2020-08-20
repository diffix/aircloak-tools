[![GitHub license](https://img.shields.io/github/license/diffix/aircloak-tools)](https://github.com/diffix/aircloak-tools/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/diffix/aircloak-tools)](https://github.com/diffix/aircloak-tools/issues)

# Python Aircloak Tools

Tools for querying an Aircloak api. 

This package contains two main components:
- (Aircloak Api)[#aircloak-api]: Wrapper around psycopg to query Aircloak directly.
- (Explorer)[#explorer]: An interface to Diffix Explorer for data analytics.

## Aircloak Api

The main aim is to provide an Aircloak-friendly wrapper around `psycopg2`, and in particular to
provide clear error messages when something doesn't go as planned. 

Query results are returned as `pandas` dataframes. 

## Explorer

Uses [Diffix Explorer](https://github.com/diffix/explorer) to return enhanced statistics. Please see the project homepage for further information about Explorer. This feature should be considered a work-in-progress.

## Installation

The package can be installed in youir local environment using pip:
```
pip install aircloak-tools
```

To use Explorer Features you will also need to run [Diffix Explorer](https://github.com/diffix/explorer).

## Example

The following code shows how to initiate a connection and execute a query.

As a pre-requisite you should have a username and password for the postgres interface of an
Aircloak installation (ask your admin for these). Assign these values to `AIRCLOAK_PG_USER`
and `AIRCLOAK_PG_PASSWORD` environment variables. 

> Note the call to ``ac.connect()`` can be used as a context manager: Using the ``with`` statement, the connection 
> is automatically closed cleanly when it it goes out of scope.

```python
import aircloak_tools as ac

AIRCLOAK_PG_HOST = "covid-db.aircloak.com"
AIRCLOAK_PG_PORT = 9432

AIRCLOAK_PG_USER = environ.get("AIRCLOAK_PG_USER")
AIRCLOAK_PG_PASSWORD = environ.get("AIRCLOAK_PG_PASSWORD")

TEST_DATASET = "cov_clear"

with ac.connect(host=AIRCLOAK_PG_HOST, port=AIRCLOAK_PG_PORT,
                user=AIRCLOAK_PG_USER, password=AIRCLOAK_PG_PASSWORD, dataset=TEST_DATASET) as conn:

    assert(conn.is_connected())

    tables = conn.get_tables()

    print(tables)

    feeling_now_counts = conn.query('''
    select feeling_now, count(*), count_noise(*)
    from survey
    group by 1
    order by 1 desc
    ''')
```
