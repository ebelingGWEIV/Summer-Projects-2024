from . import Barometer
import random

class BarometerMock(Barometer):
    def __init___(self, pin: list, name: str):
        self.Name = name
    def GetCurrentValue(self) -> float:
        airPressure = random(29, 31, .1)
        return airPressure
    