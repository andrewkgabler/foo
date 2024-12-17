from typing import List

import pytest

from mock import TelemetryData, TELEMETRY_DATA


# Example classes to resemble the implementation


class ConditionedTelemetry:
    def __init__(self, data: List[TelemetryData]):
        self.data: List[TelemetryData] = data


# Function to be tested
def condition_data(telemetry_data: List[TelemetryData], frequency: int = 1):
    """Function to condition telemetry data.
    :arg telemetry_data : list of TelemetryData objects
    :arg frequency : in Hz. Values above 1 would need some method of taking rounding fractional seconds t fixed interval seconds
    """
    return ConditionedTelemetry(telemetry_data)


# Test
def test_condition_data():
    # Mock telemetry data

    # Call the function
    result: ConditionedTelemetry = condition_data(TELEMETRY_DATA, frequency=1)

    # Extract timestamps and validate
    timestamps = [data.timestamp for data in result.data]

    # Check timestamps are sorted
    assert timestamps == sorted(timestamps), "Timestamps are not sorted"

    # Check for duplicates
    assert len(timestamps) == len(set(timestamps)), "Duplicate timestamps found"

    # Check for fixed-frequency timestamps
    # todo later
    # time_difference_seconds = (max_datetime - min_datetime).total_seconds()
    # assert len(timestamps) == list(range(min(timestamps), max(timestamps) )), "Missing timestamps"
