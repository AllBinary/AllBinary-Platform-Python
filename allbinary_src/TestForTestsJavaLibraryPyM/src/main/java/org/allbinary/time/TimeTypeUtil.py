# Generated Code Do Not Modify
# package org.allbinary.time

from __future__ import annotations

import datetime


class TimeTypeUtil:
    instance: TimeTypeUtil = None

    def _init_fields(self) -> None:
        self.NIGHT: str = "Night"
        self.DAY: str = "Day"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TimeTypeUtil:
        return TimeTypeUtil.instance
    

    def isNight(self) -> bool:
        hoursOfDay: int = self.getHourOfDay()
        return hoursOfDay < 6 or hoursOfDay > 18
    

    def getHourOfDay(self) -> int:
        calendar: datetime.datetime = datetime.datetime.now()
        return calendar.get(Calendar.HOUR_OF_DAY)
    

    def getNightOrDay(self) -> str:
        return (self.NIGHT if self.isNight() else self.DAY)
    

    # Java overloaded method: Python keeps the last definition
    def getHourOfDay(self, timeInMillis: int) -> int:
        calendar: datetime.datetime = datetime.datetime.now()
        calendar.setTimeInMillis(timeInMillis)
        return calendar.get(Calendar.HOUR_OF_DAY)
    

    # Java overloaded method: Python keeps the last definition
    def isNight(self, timeInMillis: int) -> bool:
        hoursOfDay: int = self.getHourOfDay(timeInMillis)
        return hoursOfDay < 6 or hoursOfDay > 18
    

    # Java overloaded method: Python keeps the last definition
    def getNightOrDay(self, timeInMillis: int) -> str:
        return (self.NIGHT if self.isNight(timeInMillis) else self.DAY)
# from java.util.Calendar import Calendar
# from java.util.TimeZone import TimeZone


TimeTypeUtil.instance = TimeTypeUtil()

