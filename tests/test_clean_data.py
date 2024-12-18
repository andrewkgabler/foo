from condition import Checks, condition_data
from mock import TELEMETRY_DATA
import pytest

@pytest.fixture
def conditioned_telemetry():
    """
    Pytest fixture to prepare the result of condition_data.
    """
    return condition_data(TELEMETRY_DATA, frequency=1)
def test_timestamps_sorted(conditioned_telemetry):
    """
    Test that timestamps are sorted in ascending order.
    """
    timestamps = [data.timestamp for data in conditioned_telemetry.data]
    assert timestamps == sorted(timestamps), "Timestamps are not sorted."
    assert conditioned_telemetry.assertions[Checks.TIMESTAMPS_SORTED], 'Assertion not set'


def test_no_duplicate_timestamps(conditioned_telemetry):
    """
    Test that there are no duplicate timestamps.
    """
    timestamps = [data.timestamp for data in conditioned_telemetry.data]
    assert len(timestamps) == len(set(timestamps)), "Duplicate timestamps found."
    assert conditioned_telemetry.assertions[Checks.NO_DUPLICATE_TIMESTAMPS], 'Assertion not set'

@pytest.mark.skip(reason="Not yet doing as it gets complicated to do well quick")
def test_fixed_frequency_timestamps(conditioned_telemetry):
    """
    Test that timestamps align with the fixed frequency.
    """
    # Extract and compute relevant timestamps
    assert False, "Implement this test."
    # timestamps = [data.timestamp for data in conditioned_telemetry.data]
    # min_timestamp = min(timestamps)
    # max_timestamp = max(timestamps)

    # Compute time difference in seconds
    # time_difference_seconds = (max_timestamp - min_timestamp).total_seconds()
    # expected_length = int(time_difference_seconds) +
