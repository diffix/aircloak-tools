from os import environ
from typing import Iterator

import pytest

from aircloak_tools import __version__, explorer

from aircloak_tools.explorer import ExplorerSession, Exploration


def test_version():
    assert __version__ == '0.2.0'


def test_exploration_run() -> None:
    session = explorer.explorer_session(base_url="http://explorer", port=80)
    result = explorer.explore(session, "gda_banking",
                              "loans", ["amount", "duration"])

    assert True
