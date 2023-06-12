from abc import ABC
from engine import Engine
from battery import Battery
from serviceable import Serviceable
from tire import Tire

class Car(Serviceable):
    def __init__(self, Engine, Battery, Tire):
        self.engine = Engine
        self.battery = Battery
        self.tire = Tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()