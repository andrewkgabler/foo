import asyncio
from enum import Enum
from typing import List, Dict

import pytest

from mock import async_mock_fetch_telemetry_data, TelemetryData, TELEMETRY_DATA
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Example usage
async def main():
    all_telemetry_data: List[TelemetryData] = await fetch_all_data()
    conditioned_telemetry:ConditionedTelemetry=condition_data(all_telemetry_data)



if __name__ == "__main__":
    asyncio.run(main())


async def fetch_all_data():
    token_offset = 0
    accumulated_data: List[TelemetryData] = []
    while token_offset is not None:
        # connection errors are handled by the mock using backoff
        page = await async_mock_fetch_telemetry_data(token_offset=token_offset)
        logger.info(f'Fetched with offset {token_offset}')
        accumulated_data.extend(page.data)
        token_offset = page.next_token
    return accumulated_data


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
        return cls(telemetry_data, assertions)

    def __init__(self, data: List[TelemetryData], assertions: Assertions):
        self.data: List[TelemetryData] = data
        self.assertions: Assertions = assertions if assertions else {}
    @staticmethod
    def _assert_timestamps_sorted(data: List[TelemetryData],assertions: Assertions):
        # inplace sort
        data.sort(key=lambda x: x.timestamp)
        assertions[Checks.TIMESTAMPS_SORTED] = True


def condition_data(telemetry_data: List[TelemetryData], frequency: int = 1):
    """
    Function to condition telemetry data.
    :param telemetry_data: List of TelemetryData objects
    :param frequency: in Hz. Values above 1 would need some method for rounding fractional seconds.
    """
    return ConditionedTelemetry.from_telemetry_data(telemetry_data)


@pytest.fixture
def conditioned_telemetry():
    """
    Pytest fixture to prepare the result of condition_data.
    """
    return condition_data(TELEMETRY_DATA, frequency=1)
