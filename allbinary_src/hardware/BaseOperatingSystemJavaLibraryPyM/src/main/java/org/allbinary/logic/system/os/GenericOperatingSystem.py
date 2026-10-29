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

from org.allbinary.logic.system.os.OperatingSystemInterface import OperatingSystemInterface


class GenericOperatingSystem(OperatingSystemInterface):

    def _init_fields(self) -> None:
        self.osName: str = None
        self.osArch: str = None
        self.osVersion: str = None
        self.characterSet: CharacterSet = CharacterSet()
        self.scalable: bool = False
    

    def __init__(self) -> None:
        from org.allbinary.logic.system.os.SystemProperties import SystemProperties
        self._init_fields()
        systemProperties: SystemProperties = SystemProperties.getInstance()
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        if stringValidationUtil.isEmpty(systemProperties.getName()):
            self.osName = EMPTY_STRING
        else:
            self.osName = systemProperties.getName()
        if stringValidationUtil.isEmpty(systemProperties.getArch()):
            self.osArch = EMPTY_STRING
        else:
            self.osArch = systemProperties.getArch()
        if stringValidationUtil.isEmpty(systemProperties.getVersion()):
            self.osVersion = EMPTY_STRING
        else:
            self.osVersion = systemProperties.getVersion()
    

    def getName(self) -> str:
        return self.osName
    

    def getVersion(self) -> str:
        return self.osVersion
    

    def getArch(self) -> str:
        return self.osArch
    

    def getCharacterSet(self) -> CharacterSet:
        return self.characterSet
    

    def isOverScan(self) -> bool:
        return False
    

    def getOverScanXPercent(self) -> int:
        return 100
    

    def getOverScanYPercent(self) -> int:
        return 100
    

    def isScalable(self) -> bool:
        return self.scalable
    

    def isAutoHide(self) -> bool:
        return False
    

    def toString(self) -> str:
        NEW_LINE: str = CommonSeps.getInstance().NEW_LINE
        osBuffer: StringMaker = StringMaker()
        osBuffer.append("Operating System Info: \n")
        osBuffer.append(self.getName())
        osBuffer.append(NEW_LINE)
        osBuffer.append(self.getArch())
        osBuffer.append(NEW_LINE)
        osBuffer.append(self.getVersion())
        osBuffer.append(NEW_LINE)
        osBuffer.append(StringUtil.getInstance().toString(self.getCharacterSet()))
        osBuffer.append(NEW_LINE)
        return str(osBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.java.character.CharacterSet import CharacterSet
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonSeps import CommonSeps


