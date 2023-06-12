from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    @abstractmethod
    def needs_service(self):
        pass
