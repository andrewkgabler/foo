import asyncio
import logging
from typing import List

import backoff
import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from tests.mock import async_mock_fetch_telemetry_data, TelemetryData, MockConnectionError, TELEMETRY_DATA


async def fetch_all_data():
    token_offset = 0
    accumulated_data: List[TelemetryData] = []
    while token_offset is not None:
        # connection errors are handled by the mock using backoff
        page = await async_mock_fetch_telemetry_data(token_offset=token_offset)
        logger.info(f'Fetched with offset {token_offset}')
        accumulated_data.extend(page.data)
        token_offset=page.next_token
    return accumulated_data


@pytest.mark.asyncio
async def test_fetch_all_data():
    """Test that fetch_all_data fetches all telemetry data and matches TELEMETRY_DATA."""
    # Act: Call fetch_all_data
    result = await fetch_all_data()

    # Assert: Validate the result has all the telemetry data from TELEMETRY_DATA
    assert len(result) == len(TELEMETRY_DATA), "The result length does not match TELEMETRY_DATA length."

    for data in TELEMETRY_DATA:
        assert data in result, f"Telemetry data {data} is missing in the result."
