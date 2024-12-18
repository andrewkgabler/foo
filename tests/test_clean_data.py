from main import conditioned_telemetry


def test_timestamps_sorted(conditioned_telemetry):
    """
    Test that timestamps are sorted in ascending order.
    """
    timestamps = [data.timestamp for data in conditioned_telemetry.data]
    assert timestamps == sorted(timestamps), "Timestamps are not sorted."


def test_no_duplicate_timestamps(conditioned_telemetry):
    """
    Test that there are no duplicate timestamps.
    """
    timestamps = [data.timestamp for data in conditioned_telemetry.data]
    assert len(timestamps) == len(set(timestamps)), "Duplicate timestamps found."


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
