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

class SimpleDateFormat:
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern.replace("yyyy", "%Y").replace("MM", "%m").replace("dd", "%d").replace("HH", "%H").replace("mm", "%M").replace("ss", "%S").replace("SSS", "%f")

    def format(self, value: datetime.datetime) -> str:
        pattern = self.pattern
        if "%f" in pattern:
            pattern = pattern.replace("%f", f"{value.microsecond:06d}"[:3])
        return value.strftime(pattern)



#ActualPlatform
class TimeStampUtil:
    instance: TimeStampUtil = None

    def _init_fields(self) -> None:
        self.simpleDataFormat: SimpleDateFormat = SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS")
    

    @staticmethod
    def getInstance() -> TimeStampUtil:
        return TimeStampUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getAsString(self) -> str:
        calendar: datetime.datetime = datetime.datetime.now()
        date: datetime.datetime = calendar
        return self.simpleDataFormat.format(date)
# from java.text.SimpleDateFormat import SimpleDateFormat
# from java.util.Calendar import Calendar
# from java.util.Date import Date


TimeStampUtil.instance = TimeStampUtil()

