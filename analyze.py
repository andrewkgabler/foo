from dataclasses import dataclass
from typing import List

import pytest

from condition import ConditionedTelemetry


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
            list(enumerate(telemetry.data))[1:]]


def analyze_results(conditioned: ConditionedTelemetry) -> AnalysisResult:
    assert isinstance(conditioned, ConditionedTelemetry), "Data must be conditioned"
    # need to assert different tests are true for different calcs
    # assert [item.name for item in Checks] in conditioned.assertions, "All checks must be set"
    acceleration = acceleration_series(conditioned)
    print(acceleration)
    return AnalysisResult(
        altitude_m_average=sum(telemetry.altitude_m for telemetry in conditioned.data) / len(conditioned.data),
        altitude_m_max=max(telemetry.altitude_m for telemetry in conditioned.data),
        velocity_m_s_max=max(telemetry.velocity_m for telemetry in conditioned.data),
        velocity_m_s_min=min(telemetry.velocity_m for telemetry in conditioned.data),
        temperature_f_max=max(telemetry.temperature_f for telemetry in conditioned.data),
        temperature_f_min=min(telemetry.temperature_f for telemetry in conditioned.data),
        temperature_c_max=fahrenheit_to_celsius(max(telemetry.temperature_f for telemetry in conditioned.data)),
        temperature_c_min=fahrenheit_to_celsius(min(telemetry.temperature_f for telemetry in conditioned.data)),
        acceleration_m_s2_max=max(acceleration),
        acceleration_m_s2_min=min(acceleration),
    )


@pytest.fixture
def analysis_result(conditioned_telemetry):
    return analyze_results(conditioned_telemetry)
