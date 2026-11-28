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
# package org.allbinary.logic.system

from __future__ import annotations



class SoftwareInformation:

    def _init_fields(self) -> None:
        if "name" not in vars(self): self.name: str = None
        if "shortName" not in vars(self): self.shortName: str = None
        if "version" not in vars(self): self.version: str = None
    

    def __init__(self, name: str, version: str, shortName: str) -> None:
        from org.allbinary.KotlinUtil import KotlinUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        __class__._init_fields(self)
        self.name = name
        self.version = version
        self.shortName = str(StringMaker().append(shortName).append(KotlinUtil.getShortName()))
    

    def getName(self) -> str:
        return self.name
    

    def getVersion(self) -> str:
        return self.version
    

    def toShortString(self) -> str:
        return self.shortName
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        NAME: str = "Name: "
        VERSION: str = "Version: "
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(NAME)
        stringBuffer.append(self.getName())
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(VERSION)
        stringBuffer.append(self.getVersion())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.KotlinUtil import KotlinUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps


