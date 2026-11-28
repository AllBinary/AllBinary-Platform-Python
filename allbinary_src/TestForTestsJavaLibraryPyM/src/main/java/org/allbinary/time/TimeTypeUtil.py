# Generated Code Do Not Modify
# package org.allbinary.time

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate
import datetime
from java.lang.JavaRuntimeStatic import lazy_static


class TimeTypeUtil:
    instance: TimeTypeUtil = None

    def _init_fields(self) -> None:
        self.NIGHT: str = "Night"
        self.DAY: str = "Day"

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> TimeTypeUtil:
        return TimeTypeUtil.instance
    

    def isNight_j0(self) -> bool:
        hoursOfDay: int = self.getHourOfDay()
        return hoursOfDay < 6 or hoursOfDay > 18
    

    def getHourOfDay_j0(self) -> int:
        calendar: datetime.datetime = datetime.datetime.now()
        return calendar.get(Calendar.HOUR_OF_DAY)
    

    def getNightOrDay_j0(self) -> str:
        return (self.NIGHT if java_predicate(self, "isNight") else self.DAY)
    

    def getHourOfDay_j1(self, timeInMillis: int) -> int:
        calendar: datetime.datetime = datetime.datetime.now()
        calendar.setTimeInMillis(timeInMillis)
        return calendar.get(Calendar.HOUR_OF_DAY)

    def getHourOfDay(self, *args):
        implementation = __class__.__dict__.get("getHourOfDay_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getHourOfDay(*args)
    

    def isNight_j1(self, timeInMillis: int) -> bool:
        hoursOfDay: int = self.getHourOfDay(timeInMillis)
        return hoursOfDay < 6 or hoursOfDay > 18

    def isNight(self, *args):
        implementation = __class__.__dict__.get("isNight_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().isNight(*args)
    

    def getNightOrDay_j1(self, timeInMillis: int) -> str:
        return (self.NIGHT if self.isNight(timeInMillis) else self.DAY)

    def getNightOrDay(self, *args):
        implementation = __class__.__dict__.get("getNightOrDay_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getNightOrDay(*args)
# from java.util.Calendar import Calendar
# from java.util.TimeZone import TimeZone


def _TimeTypeUtil_instance() -> object:
    return TimeTypeUtil()

lazy_static(TimeTypeUtil, "instance", _TimeTypeUtil_instance)

