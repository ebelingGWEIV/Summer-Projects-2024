from . import Processor
from ..HardwareInterface import Anemometer
from threading import Thread
from time import sleep


class AnemometerProcessor(Processor):
    # Miles per hour
    CurrentWindSpeed: int
    Device: Anemometer
    PollingThread: Thread
    Running: bool
    def __init__(self, device: Anemometer) -> None:
        self.Device = device
        self.CurrentWindSpeed = 0

    def Stop(self):
        """
        Stop measuring wind speed
        """
        self.Running = False
        self.PollingThread.join()

    def Start(self):
        """
        Start a thread to measure wind speed
        """
        self.Running = True
        self.PollingThread = Thread(target = self._PollData)
        self.PollingThread.start()

    def _PollData(self):
        while self.Running:
            pulsesInTheLastSecond = self.Device.GetCurrentValue()
            mps =  self.Device.ConvertPulsesToMPS(pulsesInTheLastSecond)
            mph = round((mps * 3600) / 1609.34)
            self.CurrentWindSpeed = mph
            sleep(1)
    
    def GetCurrentValue(self):
        return self.CurrentWindSpeed    

