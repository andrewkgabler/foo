import pytest

from condition import condition_data, ConditionedTelemetry
from mock import TELEMETRY_DATA


@pytest.fixture
def conditioned_telemetry():
    """
    Pytest fixture to prepare the result of condition_data.
    """
    conditioned:ConditionedTelemetry = condition_data(TELEMETRY_DATA, frequency=1)
    [print(item) for item in conditioned.data]
    return conditioned
