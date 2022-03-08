from battery import Battery

class Spindler(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        days_since = self.current_date - self.last_service_date
        print(days_since)
        if (days_since >= (365*2)):
            return True
        else:
            return False