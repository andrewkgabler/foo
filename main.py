import asyncio
from typing import List

from mock import async_mock_fetch_telemetry_data, TelemetryData
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Mock TelemetryData list


# Example usage
async def main():
    all_telemetry_data: List[TelemetryData] = await fetch_all_data()


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
