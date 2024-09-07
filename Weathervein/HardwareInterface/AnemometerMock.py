from . import Anemometer
import random

class AnemometerMock(Anemometer):

    def GetCurrentValue(self) -> float:
        pulses = random(10, 1420, 1)
        return pulses