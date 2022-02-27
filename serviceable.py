from abc import ABC, abstractmethod


class Serviceable(ABC):
    def __init__(self):
        this.self = self
        
    @abstractmethod
    def needs_service(self):
        pass
