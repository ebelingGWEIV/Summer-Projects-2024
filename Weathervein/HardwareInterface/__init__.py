class HardwareDevice:
    Name: str = "Hardware Device"
    def GetName(self) -> str:
        return self.Name
    def GetCurrentValue(self) -> float:
        pass
    def __init__(self, pin: list, name: str):
        pass
        
class Anemometer(HardwareDevice):
    PulsesPerRotation: int
    MetersPerRotation: float

    def GetCurrentValue(self) -> float:
        """
        Returns the number of pulses received since the last call 
        """
        return super().GetCurrentValue()

    def __init__(self, pin, name, pulsesPerRotation, distancePerRotation):
        super.__init__(pin, name)
        self.PulsesPerRotation = pulsesPerRotation
        self.MetersPerRotation = distancePerRotation

    def SetCurrentValue(self) -> float:
        pass

    def ConvertPulsesToMPS(self, pulsesInOneSecond) -> float:
        """
        Convert pulses per second to meters per second
        """
        constant = self.MetersPerRotation / self.PulsesPerRotation
        return (pulsesInOneSecond * constant)

class Thermometer(HardwareDevice):
    def __init__(self, pin: list, name: str):
        super().__init__(pin, name)

    def SetCurrentValue(self) -> float:
        """
        Returns the voltage on the thermometer
        """
        pass

class Barometer(HardwareDevice):
    """
    Returns pressure in hecta-pascals?
    """
    def SetCurrentValue(self) -> float:
        pass





