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
# package org.allbinary.game

from __future__ import annotations



# Java interface
class IntermissionInterface:
    

    def getTimeDelayHelper(self) -> TimeDelayHelper:
        raise NotImplementedError()
    

    def isEnabled(self) -> bool:
        raise NotImplementedError()
    

    def setEnabled(self, value: bool) -> None:
        raise NotImplementedError()
    

    def setListener(self, enableListener: IntermissionEnableListenerInterface) -> None:
        raise NotImplementedError()
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


