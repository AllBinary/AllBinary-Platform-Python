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
# package org.allbinary.logic.system.os

from __future__ import annotations



# Java interface
class OperatingSystemInterface:
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def getVersion(self) -> str:
        raise NotImplementedError()
    

    def getArch(self) -> str:
        raise NotImplementedError()
    

    def getCharacterSet(self) -> CharacterSet:
        raise NotImplementedError()
    

    def isOverScan(self) -> bool:
        raise NotImplementedError()
    

    def getOverScanXPercent(self) -> int:
        raise NotImplementedError()
    

    def getOverScanYPercent(self) -> int:
        raise NotImplementedError()
    

    def isScalable(self) -> bool:
        raise NotImplementedError()
    

    def isAutoHide(self) -> bool:
        raise NotImplementedError()
    

    def toString(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.java.character.CharacterSet import CharacterSet


