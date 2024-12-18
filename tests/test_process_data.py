from analyze import analysis_result


def test_altitude_m_average(analysis_result):
    """
    Test the average altitude.
    """
    assert analysis_result.altitude_m_average == 1049.0, "Incorrect average altitude."


def test_altitude_m_max(analysis_result):
    """
    Test the maximum altitude.
    """
    assert analysis_result.altitude_m_max == 1450, "Incorrect maximum altitude."


def test_velocity_m_s_max(analysis_result):
    """
    Test the maximum velocity.
    """
    assert analysis_result.velocity_m_s_max == 360, "Incorrect maximum velocity."


def test_velocity_m_s_min(analysis_result):
    """
    Test the minimum velocity.
    """
    assert analysis_result.velocity_m_s_min == 50, "Incorrect minimum velocity."


def test_acceleration_m_s2_max(analysis_result):
    """
    Test the maximum acceleration.
    """
    assert analysis_result.acceleration_m_s2_max == 230, "Incorrect maximum acceleration."


def test_acceleration_m_s2_min(analysis_result):
    """
    Test the minimum acceleration.
    """
    assert analysis_result.acceleration_m_s2_min == -1.2, "Incorrect minimum acceleration."


def test_temperature_f_max(analysis_result):
    """
    Test the maximum temperature in Fahrenheit.
    """
    assert analysis_result.temperature_f_max == 95, "Incorrect maximum temperature in Fahrenheit."


def test_temperature_f_min(analysis_result):
    """
    Test the minimum temperature in Fahrenheit.
    """
    assert analysis_result.temperature_f_min == 60.0, "Incorrect minimum temperature in Fahrenheit."


def test_temperature_c_max(analysis_result):
    """
    Test the maximum temperature in Celsius.
    """
    expected_celsius_max = (95 - 32) * 5.0 / 9.0  # Fahrenheit to Celsius Conversion
    assert analysis_result.temperature_c_max == expected_celsius_max, "Incorrect maximum temperature in Celsius."


def test_temperature_c_min(analysis_result):
    """
    Test the minimum temperature in Celsius.
    """
    expected_celsius_min = (60 - 32) * 5.0 / 9.0  # Fahrenheit to Celsius Conversion
    assert analysis_result.temperature_c_min == expected_celsius_min, "Incorrect minimum temperature in Celsius."
