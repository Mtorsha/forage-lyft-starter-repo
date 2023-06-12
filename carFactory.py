from abc import ABC
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class CarFactory(ABC):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_is_on = warning_light_is_on

    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date))
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date))
    
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        return Car(SternmanEngine(warning_light_is_on),SpindlerBattery(current_date, last_service_date))
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date))
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date))
    

