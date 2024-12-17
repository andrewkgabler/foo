import pytest
import logging

from main import fetch_all_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from mock import TELEMETRY_DATA


@pytest.mark.asyncio
async def test_fetch_all_data():
    """Test that fetch_all_data fetches all telemetry data and matches TELEMETRY_DATA."""
    # Act: Call fetch_all_data
    result = await fetch_all_data()

    # Assert: Validate the result has all the telemetry data from TELEMETRY_DATA
    assert len(result) == len(TELEMETRY_DATA), "The result length does not match TELEMETRY_DATA length."
    for data in TELEMETRY_DATA:
        # this only works because the objects are passed in memory otherwise a more advanced equality is required
        assert data in result, f"Telemetry data {data} is missing in the result."
