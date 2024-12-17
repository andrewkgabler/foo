from datetime import datetime
import pytest
from mock import TelemetryData, TELEMETRY_DATA
from typing import List, Dict

from enum import Enum


class Checks(Enum):
    TIMESTAMPS_SORTED = 1
    NO_DUPLICATE_TIMESTAMPS = 2
    FIXED_FREQUENCY_TIMESTAMPS = 3


Assertions = Dict[Checks, bool]


# Example classes and function from your context
class ConditionedTelemetry:
    @classmethod
    def from_telemetry_data(cls, telemetry_data: List[TelemetryData]):
        assertions: Assertions = {}
        return cls(telemetry_data, assertions)

    def __init__(self, data: List[TelemetryData], assertions: Assertions):
        self.data: List[TelemetryData] = data
        self.assertions: Assertions = assertions if assertions else {}


def condition_data(telemetry_data: List[TelemetryData], frequency: int = 1):
    """
    Function to condition telemetry data.
    :param telemetry_data: List of TelemetryData objects
    :param frequency: in Hz. Values above 1 would need some method for rounding fractional seconds.
    """
    return ConditionedTelemetry(telemetry_data)


# ----------------------
# Pytest Fixture
# ----------------------


@pytest.fixture
def conditioned_telemetry():
    """
    Pytest fixture to prepare the result of condition_data.
    """
    return condition_data(TELEMETRY_DATA, frequency=1)


# ----------------------
# Individual Tests
# ----------------------


def test_timestamps_sorted(conditioned_telemetry):
    """
    Test that timestamps are sorted in ascending order.
    """
    timestamps = [data.timestamp for data in conditioned_telemetry.data]
    assert timestamps == sorted(timestamps), "Timestamps are not sorted."


def test_no_duplicate_timestamps(conditioned_telemetry):
    """
    Test that there are no duplicate timestamps.
    """
    timestamps = [data.timestamp for data in conditioned_telemetry.data]
    assert len(timestamps) == len(set(timestamps)), "Duplicate timestamps found."


def test_fixed_frequency_timestamps(conditioned_telemetry):
    """
    Test that timestamps align with the fixed frequency.
    """
    # Extract and compute relevant timestamps
    assert False, "Implement this test."
    # timestamps = [data.timestamp for data in conditioned_telemetry.data]
    # min_timestamp = min(timestamps)
    # max_timestamp = max(timestamps)

    # Compute time difference in seconds
    # time_difference_seconds = (max_timestamp - min_timestamp).total_seconds()
    # expected_length = int(time_difference_seconds) +
