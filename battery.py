from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self):
        # self.last_service_date = last_service_date
        pass

    @abstractmethod
    def needs_service(self):
        pass
