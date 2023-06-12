from abc import ABC
from datetime import datetime
from tire import Tire


class CarriganTire(Tire, ABC):
    def __init__(self, sensors):
        # super().__init__(last_service_date)
        self.sensors = sensors

    def needs_service(self):
        return (any(s>=0.9) for s in self.sensors)

