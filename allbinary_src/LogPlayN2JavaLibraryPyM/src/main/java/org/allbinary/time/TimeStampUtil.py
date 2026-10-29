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


#ActualPlatform
class TimeStampUtil:
    instance: TimeStampUtil = None
    

    @staticmethod
    def getInstance() -> TimeStampUtil:
        return TimeStampUtil.instance
    

    def __init__(self) -> None:
        pass
    

    def getAsString(self) -> str:
        simpleDataFormat: DateTimeFormat = DateTimeFormat.getFormat("yyyy-MM-dd HH:mm:ss.SSS")
        date: datetime.datetime = datetime.datetime()
        return simpleDataFormat.format(date)
from com.google.gwt.i18n.client.DateTimeFormat import DateTimeFormat
# from java.util.Date import Date


TimeStampUtil.instance = TimeStampUtil()

