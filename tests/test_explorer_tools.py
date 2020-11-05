from os import environ
from typing import Iterator

import pytest

from aircloak_tools import __version__, explorer

from aircloak_tools.explorer import ExplorerSession, Exploration


def test_version():
    assert __version__ == '0.2.1'


@pytest.fixture(scope='module')
def explorer_session() -> ExplorerSession:
    return explorer.explorer_session(base_url="http://explorer", port=80)


def test_exploration_run(explorer_session) -> None:
    result = explorer.explore(explorer_session, "gda_banking",
                              "loans", ["amount", "duration"])

    assert len(result) > 0
    assert result['status'] == 'Complete'
