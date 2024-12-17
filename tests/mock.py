import asyncio
import random
from dataclasses import dataclass
from typing import Optional, List

import backoff
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class TelemetryData:
    """Represents a single telemetry data point."""
    timestamp: str
    altitude_m: int
    velocity_m: int
    temperature_f: int


@dataclass
class PaginatedResponse:
    """Represents a paginated response from the telemetry service."""
    next_token: Optional[int]
    data: List[TelemetryData]


class MockConnectionError(Exception):
    """Custom exception to simulate a connection error to the remote service."""
    pass


# Add a logging function for backoff events
def log_backoff(details):
    logger.info(
        f"Retrying after exception: {details['exception']} "
        f"(try {details['tries']} of args {details['args']}, "")"
    )

# backoff supports async/snc and elegant callback loggers on different events
@backoff.on_exception(backoff.expo, MockConnectionError, max_tries=3,on_backoff=log_backoff)
async def async_mock_fetch_telemetry_data(token_offset: Optional[int] = 0) -> PaginatedResponse:
    """
    Mock async function to simulate fetching telemetry data from a remote service.

    Args:
        token_offset (Optional[int]): Offset for pagination to start fetching telemetry data. Defaults to 0.

    Returns:
        PaginatedResponse: A paginated response containing the next token and telemetry data.

    Raises:
        MockConnectionError: 10% of the time to simulate a connection failure.
    """
    # Set token_offset to 0 if it is None
    token_offset = token_offset or 0

    # Introduce a random delay of up to 50ms
    random_delay = random.uniform(0, 0.05)  # Delay in seconds (0 to 50ms)
    await asyncio.sleep(random_delay)

    # Simulate a connection error 10% of the time
    if random.random() < 0.1:  # 10% chance
        raise MockConnectionError("Mock connection failure")

    # Pagination logic: assume each "page" contains 2 items
    page_size = 2
    start_index = token_offset
    end_index = start_index + page_size

    # Get data for the current page
    data = TELEMETRY_DATA[start_index:end_index]

    # Determine the next token; if there are no more pages, it's None
    next_token = end_index if end_index < len(TELEMETRY_DATA) else None

    return PaginatedResponse(next_token=next_token, data=data)


TELEMETRY_DATA = [
    TelemetryData(timestamp="2023-10-01T12:00:00Z", altitude_m=1000, velocity_m=300, temperature_f=85),
    TelemetryData(timestamp="2023-10-01T12:00:00Z", altitude_m=-1, velocity_m=10, temperature_f=70),
    # Same timestamp as above
    TelemetryData(timestamp="2023-10-01T12:01:00Z", altitude_m=1100, velocity_m=320, temperature_f=87),
    TelemetryData(timestamp="2023-10-01T12:02:00Z", altitude_m=1200, velocity_m=310, temperature_f=86),
    TelemetryData(timestamp="2023-10-01T12:03:00Z", altitude_m=1150, velocity_m=315, temperature_f=89),
    TelemetryData(timestamp="2023-10-01T12:04:00Z", altitude_m=1300, velocity_m=330, temperature_f=90),
    # Additional 5 data points (out-of-sequence timestamps)
    TelemetryData(timestamp="2023-09-30T11:59:00Z", altitude_m=900, velocity_m=280, temperature_f=80),
    TelemetryData(timestamp="2023-10-01T12:05:00Z", altitude_m=1400, velocity_m=350, temperature_f=92),
    TelemetryData(timestamp="2023-10-01T11:58:00Z", altitude_m=800, velocity_m=270, temperature_f=78),
    TelemetryData(timestamp="2023-10-01T12:06:00Z", altitude_m=1450, velocity_m=360, temperature_f=95),
    TelemetryData(timestamp="2023-09-30T11:57:00Z", altitude_m=100, velocity_m=50, temperature_f=60),
]
