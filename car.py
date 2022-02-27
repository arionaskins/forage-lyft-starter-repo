import Serviceable, Engine, Battery

class Car(Serviceable):
    def __init__(self):
        super()
        this.self = self
        self.engine = None
        self.battery = None

    def __init__(self, Engine, Battery):
        super()
        this.self = self
        self.engine = Engine
        self.battery = Battery    
        
    def setBattery(Battery):
        self.battery = Battery
    
    def setEngine(Engine):
        self.engine = Engine
    
    def needs_service():
        if (self.engine.needs_service() == True or self.battery.needs_service() == True):
            return True
        else: 
            return False