from car import Car
from datetime import datetime # datetime.today().date()
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import Spindler
from battery.nubbin_battery import NubbinBattery

class CarFactory():
    def __init__(self):
        super()

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        calliope = Car()
        calliope.setBattery(Spindler(last_service_date, current_date))
        calliope.setEngine(CapuletEngine(current_mileage, last_service_mileage))
        return calliope

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        glissade = Car()
        glissade.setBattery(WilloughbyEngine(current_mileage, last_service_mileage))
        glissade.setEngine(Spindler(last_service_date, current_date))
        return glissade

    def create_palindrome(current_date, last_service_date, warning_light_on): 
        palindrome = Car()
        palindrome.setBattery(SternmanEngine(warning_light_on))
        palindrome.setEngine(Spindler(last_service_date, current_date))
        return palindrome

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        rorschach = Car()
        rorschach.setBattery(WilloughbyEngine(current_mileage, last_service_mileage))
        rorschach.setEngine(NubbinBattery(last_service_date, current_date))
        return rorschach

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        thovex = Car()
        thovex.setEngine(CapuletEngine(current_mileage, last_service_mileage))
        thovex.setBattery(NubbinBattery(last_service_date, current_date))
        return thovex




