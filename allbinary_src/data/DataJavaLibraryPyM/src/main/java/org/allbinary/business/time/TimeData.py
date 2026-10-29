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
# package org.allbinary.business.time

from __future__ import annotations



class TimeData:
    instance: TimeData = None

    def _init_fields(self) -> None:
        self.NAME: str = "TIME_NAME"
        self.START: str = "TIME_START"
        self.END: str = "TIME_END"
    

    @staticmethod
    def getInstance() -> TimeData:
        return TimeData.instance
    

    def __init__(self) -> None:
        self._init_fields()


TimeData.instance = TimeData()

