from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


BASELINE_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def reset_activities_state():
    app_module.activities = deepcopy(BASELINE_ACTIVITIES)
    yield
    app_module.activities = deepcopy(BASELINE_ACTIVITIES)
