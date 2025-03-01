from abc import ABC
from datetime import datetime
from battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, current_date, last_service_date):
        # super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date() :
            return True
        else:
            return False

