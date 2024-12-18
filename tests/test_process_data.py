from dataclasses import dataclass
from typing import List

import pytest

from condition import ConditionedTelemetry, Checks


@dataclass
class AnalysisResult:
    altitude_m_average: float
    altitude_m_max: float
    velocity_m_s_max: float
    velocity_m_s_min: float
    acceleration_m_s2_max: float
    acceleration_m_s2_min: float
    temperature_f_max: float
    temperature_f_min: float
    temperature_c_max: float
    temperature_c_min: float


fahrenheit_to_celsius = lambda f: (f - 32) * 5.0 / 9.0


def acceleration_series(telemetry: ConditionedTelemetry) -> List[float]:
    return [(data.velocity_m - telemetry.data[index - 1].velocity_m) for index, data in
            enumerate(telemetry.data)]


def analyze_results(conditioned: ConditionedTelemetry) -> AnalysisResult:
    assert isinstance(conditioned, ConditionedTelemetry), "Data must be conditioned"
    assert [item.name for item in Checks] in conditioned.assertions, "All checks must be set"
    acceleration = acceleration_series(conditioned)
    return AnalysisResult(
        altitude_m_average=sum(telemetry.altitude_m for telemetry in conditioned.data) / len(conditioned.data),
        altitude_m_max=max(telemetry.altitude_m for telemetry in conditioned.data),
        velocity_m_s_max=max(telemetry.velocity_m for telemetry in conditioned.data),
        velocity_m_s_min=min(telemetry.velocity_m for telemetry in conditioned.data),
        temperature_f_max=max(telemetry.temperature_f for telemetry in conditioned.data),
        temperature_f_min=min(telemetry.temperature_f for telemetry in conditioned.data),
        acceleration_m_s2_max=max(acceleration),
        acceleration_m_s2_min=min(acceleration),
    )


@pytest.fixture
def analysis_result(conditioned_telemetry):
    return analyze_results(conditioned_telemetry)


def test_engine_temperature_values(analysis_result):
    """
    Test the engine temperature data.
    """
    assert analysis_result.temperature_f_max == 100, 'Wrong max temperature'



def test_altitude_m_average(analysis_result):
    """
    Test the average altitude.
    """
    assert analysis_result.altitude_m_average == pytest.approx(500.0), "Incorrect average altitude."


def test_altitude_m_max(analysis_result):
    """
    Test the maximum altitude.
    """
    assert analysis_result.altitude_m_max == 1000, "Incorrect maximum altitude."


def test_velocity_m_s_max(analysis_result):
    """
    Test the maximum velocity.
    """
    assert analysis_result.velocity_m_s_max == 150, "Incorrect maximum velocity."


def test_velocity_m_s_min(analysis_result):
    """
    Test the minimum velocity.
    """
    assert analysis_result.velocity_m_s_min == 0, "Incorrect minimum velocity."


def test_acceleration_m_s2_max(analysis_result):
    """
    Test the maximum acceleration.
    """
    assert analysis_result.acceleration_m_s2_max == 3.5, "Incorrect maximum acceleration."


def test_acceleration_m_s2_min(analysis_result):
    """
    Test the minimum acceleration.
    """
    assert analysis_result.acceleration_m_s2_min == -1.2, "Incorrect minimum acceleration."


def test_temperature_f_max(analysis_result):
    """
    Test the maximum temperature in Fahrenheit.
    """
    assert analysis_result.temperature_f_max == 100.0, "Incorrect maximum temperature in Fahrenheit."


def test_temperature_f_min(analysis_result):
    """
    Test the minimum temperature in Fahrenheit.
    """
    assert analysis_result.temperature_f_min == 32.0, "Incorrect minimum temperature in Fahrenheit."


def test_temperature_c_max(analysis_result):
    """
    Test the maximum temperature in Celsius.
    """
    expected_celsius_max = (100.0 - 32) * 5.0 / 9.0  # Fahrenheit to Celsius Conversion
    assert analysis_result.temperature_c_max == expected_celsius_max, "Incorrect maximum temperature in Celsius."


def test_temperature_c_min(analysis_result):
    """
    Test the minimum temperature in Celsius.
    """
    expected_celsius_min = (32.0 - 32) * 5.0 / 9.0  # Fahrenheit to Celsius Conversion
    assert analysis_result.temperature_c_min == expected_celsius_min, "Incorrect minimum temperature in Celsius."
