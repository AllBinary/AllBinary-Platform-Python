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
# package org.allbinary.system

from __future__ import annotations



#ActualPlatform
class Memory:
    

    @staticmethod
    def getInfo() -> str:
        stringBuffer: StringMaker = StringMaker()
        maxUtilizedMemoryAvailable: int = Runtime.getRuntime().maxMemory()
        memoryUsed: int = Runtime.getRuntime().totalMemory()
        stringBuffer.append("APK Memory: Available: ")
        stringBuffer.appendlong(maxUtilizedMemoryAvailable)
        stringBuffer.append("/")
        stringBuffer.appendlong(int(Runtime.getRuntime().maxMemory()))
        stringBuffer.append(" Used: ")
        stringBuffer.appendlong(memoryUsed)
        stringBuffer.append(" Free: ")
        stringBuffer.appendlong(maxUtilizedMemoryAvailable - memoryUsed)
        stringBuffer.append("/")
        stringBuffer.appendlong(int(Runtime.getRuntime().maxMemory() - memoryUsed))
        return str(stringBuffer)
from org.allbinary.logic.string.StringMaker import StringMaker


