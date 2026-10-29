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

from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


class NoTimeDelayHelper(TimeDelayHelper):
    SINGLETON: NoTimeDelayHelper = None
    

    def __init__(self) -> None:
        super().__init__(0)
    

    def isTimeTNT(self) -> bool:
        return True
    

    def isTimeSinceTNT(self, delay: int) -> bool:
        return True
    

    def isTime(self, currentTime: int) -> bool:
        return True
    

    def isTimeSince(self, delay: int, currentTime: int) -> bool:
        return True


NoTimeDelayHelper.SINGLETON = NoTimeDelayHelper()

