import asyncio
import random
from typing import List, Optional
from dataclasses import dataclass


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


# Mock TelemetryData list
TELEMETRY_DATA = [
    TelemetryData(timestamp="2023-10-01T12:00:00Z", altitude_m=1000, velocity_m=300, temperature_f=85),
    TelemetryData(timestamp="2023-10-01T12:01:00Z", altitude_m=1100, velocity_m=320, temperature_f=87),
    TelemetryData(timestamp="2023-10-01T12:02:00Z", altitude_m=1200, velocity_m=310, temperature_f=86),
    TelemetryData(timestamp="2023-10-01T12:03:00Z", altitude_m=1150, velocity_m=315, temperature_f=89),
    TelemetryData(timestamp="2023-10-01T12:04:00Z", altitude_m=1300, velocity_m=330, temperature_f=90),
    # Add more mock data as needed
]


async def async_mock_fetch_telemetry_data(token_offset: int) -> PaginatedResponse:
    """
    Mock async function to simulate fetching telemetry data from a remote service.

    Args:
        token_offset (int): Offset for pagination to start fetching telemetry data.

    Returns:
        PaginatedResponse: A paginated response containing the next token and telemetry data.

    Raises:
        MockConnectionError: 10% of the time to simulate a connection failure.
    """
    # Introduce a random delay of up to 50ms
    random_delay = random.uniform(0, 0.05)  # Delay in seconds (0 to 50ms)
    await asyncio.sleep(random_delay)

    # Simulate a connection error 10% of the time
    if random.random() < 0.1:  # 10% chance
        raise MockConnectionError("Mock connection failure")

    # Pagination logic: assume each "page" contains 2 items
    page_size = 2
    start_index = token_offset * page_size
    end_index = start_index + page_size

    # Get data for the current page
    data = TELEMETRY_DATA[start_index:end_index]

    # Determine the next token; if there are no more pages, it's None
    next_token = token_offset + 1 if end_index < len(TELEMETRY_DATA) else None

    return PaginatedResponse(next_token=next_token, data=data)


# Example usage
async def main():
    token_offset = 0

    # Loop through pages until there are no more pages
    while True:
        try:
            response = await async_mock_fetch_telemetry_data(token_offset=token_offset)
            print(f"Page {token_offset + 1}: {response.data}")

            # Check if there's a next token. If not, break the loop.
            if response.next_token is None:
                print("No more pages to fetch.")
                break

            # Update token_offset to the next token
            token_offset = response.next_token

        except MockConnectionError as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    asyncio.run(main())
