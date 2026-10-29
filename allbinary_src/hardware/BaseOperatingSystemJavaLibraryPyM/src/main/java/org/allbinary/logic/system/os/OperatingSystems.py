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



class OperatingSystems:
    instance: OperatingSystems = None

    def _init_fields(self) -> None:
        self.LINUX: str = "Linux"
        self.WINDOWS: str = "Windows"
        self.SOLARIS: str = "Solaris"
        self.WINDOWS2000: str = "Windows 2000"
        self.WINDOWS_NT: str = "Windows NT"
        self.WINDOWS_10: str = "Windows 10"
        self.WINDOWS_11: str = "Windows 11"
        self.WINDOWS_VISTA: str = "Windows Vista"
        self.WINDOWS_XP: str = "Windows XP"
        self.ANDROID: str = self.LINUX
        self.HARMONY: str = "HarmonyOS"
        self.unknownSpecificOSAllowed: bool = True
    

    def __init__(self) -> None:
        self._init_fields()
    

    def isUnknownSpecificOSAllowed(self) -> bool:
        return self.unknownSpecificOSAllowed
    

    def setUnknownSpecificOSAllowed(self, aUnknownSpecificOSAllowed: bool) -> None:
        self.unknownSpecificOSAllowed = aUnknownSpecificOSAllowed
    

    @staticmethod
    def getInstance() -> OperatingSystems:
        return OperatingSystems.instance


OperatingSystems.instance = OperatingSystems()

