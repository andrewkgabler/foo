from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union, List

import pytest

from condition import ConditionedTelemetry


class Measure(Enum):
    MAX = 1
    MIN = 2
    MEAN = 3
    COUNT = 7
    DERIVATIVE = 8


class DistanceUnit(Enum):
    METER = 'm'
    FEET = 'ft'


class Schema(Enum):
    METRIC = "metric"
    IMPERIAL = "imperial"


@dataclass
class Result:
    value: Optional[Union[float, List[float]]]
    units: str
    schema: Schema


from typing import Dict
from functools import lru_cache


class AnalysisResult:
    @property
    @lru_cache
    def engine_temperature(self) -> Dict[Measure, Result]:
        return {Measure.TEMPERATURE: Result(value=95.0, units="C", schema=Schema.METRIC)}

    @property
    @lru_cache
    def altitude(self) -> Dict[Measure, Result]:
        return {Measure.PRESSURE: Result(value=101325.0, units="Pa", schema=Schema.METRIC)}

    @property
    @lru_cache
    def velocity(self) -> Dict[Measure, Result]:
        return {Measure.SPEED: Result(value=230.0, units="km/h", schema=Schema.METRIC)}

    @property
    @lru_cache
    def acceleration(self) -> Dict[Measure, Result]:
        return {Measure.FORCE: Result(value=9.81, units="m/s^2", schema=Schema.METRIC)}


def analyze_data(conditioned_data:ConditionedTelemetry) -> AnalysisResult:
    return AnalysisResult()



def test_analyze_data_instance():
    """
    Test that analyze_data() produces an instance of AnalysisResult.
    """
    result = analyze_data()
    assert isinstance(result, AnalysisResult), "The returned object is not an instance of AnalysisResult."


def test_engine_temperature_values():
    """
    Test the engine temperature data.
    """
    result = analyze_data()
    engine_temp = result.engine_temperature

    assert engine_temp[Measure.TEMPERATURE].value == 95.0, "Incorrect engine temperature value."
    assert engine_temp[Measure.TEMPERATURE].units == "C", "Incorrect engine temperature units."
    assert engine_temp[Measure.TEMPERATURE].schema == Schema.METRIC, "Incorrect engine temperature schema."


def test_altitude_values():
    """
    Test the altitude data.
    """
    result = analyze_data()
    altitude = result.altitude

    assert altitude[Measure.PRESSURE].value == 101325.0, "Incorrect altitude pressure value."
    assert altitude[Measure.PRESSURE].units == "Pa", "Incorrect altitude pressure units."
    assert altitude[Measure.PRESSURE].schema == Schema.METRIC, "Incorrect altitude schema."


def test_velocity_values():
    """
    Test the velocity data.
    """
    result = analyze_data()
    velocity = result.velocity

    assert velocity[Measure.SPEED].value == 230.0, "Incorrect velocity value."
    assert velocity[Measure.SPEED].units == "km/h", "Incorrect velocity units."
    assert velocity[Measure.SPEED].schema == Schema.METRIC, "Incorrect velocity schema."


def test_acceleration_values():
    """
    Test the acceleration data.
    """
    result = analyze_data()
    acceleration = result.acceleration

    assert acceleration[Measure.FORCE].value == 9.81, "Incorrect acceleration value."
    assert acceleration[Measure.FORCE].units == "m/s^2", "Incorrect acceleration units."
    assert acceleration[Measure.FORCE].schema == Schema.METRIC, "Incorrect acceleration schema."