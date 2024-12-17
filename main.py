import asyncio

from tests.mock import MockConnectionError, async_mock_fetch_telemetry_data

# Mock TelemetryData list


# Example usage
async def main():
    token_offset = None  # Start with no token offset

    # Loop through pages until there are no more pages
    while True:
        try:
            response = await async_mock_fetch_telemetry_data(token_offset=token_offset)
            print(f"Page {token_offset + 1 if token_offset is not None else 1}: {response.data}")

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
