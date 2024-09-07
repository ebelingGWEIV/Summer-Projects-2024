from . import Thermometer
import random

class ThermometerMock(Thermometer):
    def __init__(self, pin: list, name: str):
        self.Name = name
    def GetCurrentValue() -> float:
        temp = random.range(22, 27, 1)
        return temp