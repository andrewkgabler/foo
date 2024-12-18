from typing import List
import logging

from mock import TelemetryData, async_mock_fetch_telemetry_data
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


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
