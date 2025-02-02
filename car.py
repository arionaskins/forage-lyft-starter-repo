from engine import Engine
from battery import Battery
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self):
        super()
        self.engine = None
        self.battery = None

    def __init__(self, Engine, Battery):
        super()
        self.engine = Engine
        self.battery = Battery    
        
    def setBattery(self, Battery):
        self.battery = Battery
    
    def setEngine(self, Engine):
        self.engine = Engine
        
    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()