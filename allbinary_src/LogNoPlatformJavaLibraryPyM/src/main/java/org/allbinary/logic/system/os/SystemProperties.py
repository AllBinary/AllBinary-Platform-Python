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



#NoPlatform
class SystemProperties:
    instance: SystemProperties = None
    

    @staticmethod
    def getInstance() -> SystemProperties:
        return SystemProperties.instance
    

    def __init__(self) -> None:
        pass
    

    def getName(self) -> str:
        raise RuntimeError()
    

    def getArch(self) -> str:
        raise RuntimeError()
    

    def getVersion(self) -> str:
        raise RuntimeError()
    

    def getUserHomePath(self) -> str:
        raise RuntimeError()


SystemProperties.instance = SystemProperties()

