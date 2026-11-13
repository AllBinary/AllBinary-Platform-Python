#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.time

from __future__ import annotations

import datetime
from java.lang.JavaRuntimeStatic import lazy_static


class TimeUtil:
    instance: TimeUtil = None
    calendar: datetime.datetime = None
    

    @staticmethod
    def getInstance() -> TimeUtil:
        return TimeUtil.instance
    

    def setCalendar(self, calendar: datetime.datetime, yearString: str, monthString: str, dayString: str, hourString: str) -> None:
        year: int = int(int(yearString))
        month: int = int(int(monthString))
        day: int = int(int(dayString))
        hour: int = int(int(hourString))
        calendar.set(year, month, day, hour, 0)
    

    def setCalendarWithTime(self, calendar: datetime.datetime, yearString: str, monthString: str, dayString: str, hourString: str, minuteString: str, secondString: str) -> None:
        year: int = int(int(yearString))
        month: int = int(int(monthString))
        day: int = int(int(dayString))
        hour: int = int(int(hourString))
        minute: int = int(int(minuteString))
        second: int = int(int(secondString))
        calendar.set(year, month, day, hour, minute, second)
    

    def setExpirationCalendar(self, calendar: datetime.datetime, yearsString: str, monthsString: str, daysString: str, hoursString: str, minutesString: str, secondsString: str) -> None:
        year: int = calendar.get(Calendar.YEAR) + int(int(yearsString))
        month: int = calendar.get(Calendar.MONTH) + int(int(monthsString))
        day: int = calendar.get(Calendar.DAY_OF_MONTH) + int(int(daysString))
        hour: int = calendar.get(Calendar.HOUR) + int(int(hoursString))
        minute: int = calendar.get(Calendar.MINUTE) + int(int(minutesString))
        second: int = calendar.get(Calendar.SECOND) + int(int(secondsString))
        calendar.set(year, month, day, hour, minute, second)
    

    def getTotalTime(self, yearString: str, monthString: str, dayString: str, hourString: str, minuteString: str, secondString: str) -> int:
        time: int = TimeUtil.calendar.getTimeInMillis()
        self.setExpirationCalendar(TimeUtil.calendar, yearString, monthString, dayString, hourString, minuteString, secondString)
        timeDelta: int = TimeUtil.calendar.getTimeInMillis()
        return timeDelta - time
# from java.util.Calendar import Calendar


def _TimeUtil_instance() -> object:
    return TimeUtil()

lazy_static(TimeUtil, "instance", _TimeUtil_instance)

def _TimeUtil_calendar() -> object:
    return datetime.datetime.now()

lazy_static(TimeUtil, "calendar", _TimeUtil_calendar)

