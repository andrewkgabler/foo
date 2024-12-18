import asyncio
from typing import List

from condition import ConditionedTelemetry, condition_data
from fetch import fetch_all_data
from mock import TelemetryData
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Example usage
async def main():
    all_telemetry_data: List[TelemetryData] = await fetch_all_data()
    conditioned_telemetry: ConditionedTelemetry = condition_data(all_telemetry_data)



if __name__ == "__main__":
    asyncio.run(main())



