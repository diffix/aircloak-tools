from os import environ
from typing import Iterator

import pytest

from aircloak_tools import __version__, aircloak_api

from aircloak_tools.aircloak_api import AircloakConnection


# Test parameters
AIRCLOAK_PG_HOST = "covid-db.aircloak.com"
AIRCLOAK_PG_PORT = 9432

AIRCLOAK_PG_USER = environ.get("AIRCLOAK_PG_USER")
if AIRCLOAK_PG_USER is None:
    AIRCLOAK_PG_USER = "covid-19-5BCFDEEB3CDD876492CD"
AIRCLOAK_PG_PASSWORD = environ.get("AIRCLOAK_PG_PASSWORD")
if AIRCLOAK_PG_PASSWORD is None:
    AIRCLOAK_PG_PASSWORD = "RjV+coInOrmahmEUDorvLL9XPNLEDgdsU4Zl1wr3cMpt04ojx5bH/1bnFLw4/WMf/yHpSXFIKkdMiMl2D4KrGQ=="

TEST_DATASET = "cov_clear"


def test_version():
    assert __version__ == '0.1.1'


@pytest.fixture(scope='module')
def covid_dataset() -> Iterator[AircloakConnection]:
    with aircloak_api.connect(host=AIRCLOAK_PG_HOST, port=AIRCLOAK_PG_PORT,
                              user=AIRCLOAK_PG_USER, password=AIRCLOAK_PG_PASSWORD, dataset=TEST_DATASET) as conn:

        yield conn

    assert(not conn.is_connected())


def test_connection_established(covid_dataset) -> None:
    assert(covid_dataset.is_connected())


def test_get_tables(covid_dataset) -> None:
    tables = covid_dataset.get_tables()

    assert(len(tables) > 0)
