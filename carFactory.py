from abc import ABC
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class CarFactory(ABC):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on, sensors):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_is_on = warning_light_is_on
        self.sensors = sensors

    
    def create_calliope_carrigan(current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        return Car(CapuletEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date),CarriganTire(sensors))
    
    def create_calliope_octoprime(current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        return Car(CapuletEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date),OctoprimeTire(sensors))

    def create_glissade_carrigan(current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date),CarriganTire(sensors))
    
    def create_glissade_octoprime(current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),SpindlerBattery(current_date, last_service_date),OctoprimeTire(sensors))

    def create_palindrome_carrigan(current_date, last_service_date, warning_light_is_on,sensors):
        return Car(SternmanEngine(warning_light_is_on),SpindlerBattery(current_date, last_service_date),CarriganTire(sensors))
    
    def create_palindrome_octoprime(current_date, last_service_date, warning_light_is_on,sensors):
        return Car(SternmanEngine(warning_light_is_on),SpindlerBattery(current_date, last_service_date),OctoprimeTire(sensors))

    def create_rorschach_carrigan(current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date),CarriganTire(sensors))
    
    def create_rorschach_octoprime(current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date),OctoprimeTire(sensors))

    def create_thovex_carrigan(current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        return Car(CapuletEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date),CarriganTire(sensors))
    
    def create_thovex_octoprime(current_date, last_service_date, current_mileage, last_service_mileage,sensors):
        return Car(CapuletEngine(current_mileage, last_service_mileage),NubbinBattery(current_date, last_service_date),OctoprimeTire(sensors))


