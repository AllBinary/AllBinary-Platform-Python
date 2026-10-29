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

import os
import platform


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
        self._init_fields()
    

    def getName(self) -> str:
        return {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get(self.OS_NAME, os.environ.get(str(self.OS_NAME)))
    

    def getArch(self) -> str:
        return {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get(self.OS_ARCH, os.environ.get(str(self.OS_ARCH)))
    

    def getVersion(self) -> str:
        return {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get(self.OS_VERSION, os.environ.get(str(self.OS_VERSION)))
    

    def getUserHomePath(self) -> str:
        return {"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get(self.USER_HOME, os.environ.get(str(self.USER_HOME)))


SystemProperties.instance = SystemProperties()

