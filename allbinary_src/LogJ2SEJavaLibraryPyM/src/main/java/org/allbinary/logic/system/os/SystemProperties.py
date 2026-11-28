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

from java.lang.System import System
import os
import platform
from java.lang.JavaRuntimeStatic import lazy_static


#ActualPlatform
class SystemProperties:
    instance: SystemProperties = None

    def _init_fields(self) -> None:
        self.OS_NAME: str = "os.name"
        self.OS_ARCH: str = "os.arch"
        self.OS_VERSION: str = "os.version"
        self.USER_HOME: str = "user.home"
    

    @staticmethod
    def getInstance() -> SystemProperties:
        return SystemProperties.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getName(self) -> str:
        return System.getProperty(self.OS_NAME)
    

    def getArch(self) -> str:
        return System.getProperty(self.OS_ARCH)
    

    def getVersion(self) -> str:
        return System.getProperty(self.OS_VERSION)
    

    def getUserHomePath(self) -> str:
        return System.getProperty(self.USER_HOME)


def _SystemProperties_instance() -> object:
    return SystemProperties()

lazy_static(SystemProperties, "instance", _SystemProperties_instance)

