from os import environ
from typing import Iterator

import pytest

from aircloak_tools import __version__, explorer

from aircloak_tools.explorer import ExplorerSession, Exploration
from aircloak_tools.explorer_client import ExplorerError


def test_version():
    assert __version__ == "0.2.2"


@pytest.fixture(scope="module")
def explorer_session() -> ExplorerSession:
    return explorer.explorer_session(base_url="http://explorer", port=80)


def test_exploration_run(explorer_session) -> None:
    result = explorer.explore(
        explorer_session, "gda_banking", "loans", ["amount", "duration"]
    )

    assert len(result) > 0
    assert result["status"] == "Complete"


def test_exploration_error(explorer_session) -> None:
    threw = False

    try:
        result = explorer.explore(
            explorer_session, "bogus_dataset", "fake_table", ["made", "up", "columns"]
        )

    except ExplorerError as err:
        threw = True
        assert len(err.detail["errors"]) > 0

    assert threw
