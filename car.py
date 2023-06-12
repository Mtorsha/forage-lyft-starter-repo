from abc import ABC
from engine import Engine
from battery import Battery
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()