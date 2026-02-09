from datetime import datetime

from django.utils import timezone


class TimeUtility:
    def __init__(self):
        self.offset = timezone.timedelta(hours=7)
        self.date_time_format = '%Y-%m-%d %H:%M:%S'

    def format(self, timestamp: datetime) -> str:
        local_time = timestamp + self.offset
        return local_time.strftime(self.date_time_format)