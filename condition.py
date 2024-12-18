from enum import Enum
from typing import Dict, List

from mock import TelemetryData


class Checks(Enum):
    TIMESTAMPS_SORTED = 1
    NO_DUPLICATE_TIMESTAMPS = 2
    FIXED_FREQUENCY_TIMESTAMPS = 3


Assertions = Dict[Checks, bool]


class ConditionedTelemetry:
    @classmethod
    def from_telemetry_data(cls, telemetry_data: List[TelemetryData]):
        assertions: Assertions = {}
        cls._assert_timestamps_sorted(telemetry_data, assertions)
        cls._assert_no_duplicate_timestamps(telemetry_data, assertions)
        return cls(telemetry_data, assertions)

    def __init__(self, data: List[TelemetryData], assertions: Assertions):
        self.data: List[TelemetryData] = data
        self.assertions: Assertions = assertions if assertions else {}
    @staticmethod
    def _assert_timestamps_sorted(data: List[TelemetryData],assertions: Assertions):
        # inplace sort
        data.sort(key=lambda x: x.timestamp)
        assertions[Checks.TIMESTAMPS_SORTED] = True
    @staticmethod
    def _assert_no_duplicate_timestamps(data: List[TelemetryData], assertions: Assertions):
        # Group by timestamp and filter duplicates based on positive acceleration
        filtered_data = {}
        for item in data:
            if item.timestamp not in filtered_data and item.altitude_m > 0:
                filtered_data[item.timestamp] = item
        # Update the data list to only contain the filtered items
        data.clear()
        data.extend(filtered_data.values())
        assertions[Checks.NO_DUPLICATE_TIMESTAMPS] = True

def condition_data(telemetry_data: List[TelemetryData], frequency: int = 1):
    """
    Function to condition telemetry data.
    :param telemetry_data: List of TelemetryData objects
    :param frequency: in Hz. Values above 1 would need some method for rounding fractional seconds.
    """
    return ConditionedTelemetry.from_telemetry_data(telemetry_data)
