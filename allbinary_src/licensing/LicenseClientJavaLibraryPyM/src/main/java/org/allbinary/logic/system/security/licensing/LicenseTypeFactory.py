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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class LicenseTypeFactory:
    instance: LicenseTypeFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.UNKNOWN: LicenseType = LicenseType(CommonStrings.getInstance().UNKNOWN)
        self.DEMO: LicenseType = LicenseType("Demo")
        self.NORMAL: LicenseType = LicenseType("Normal")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance_j0() -> LicenseTypeFactory:
        return LicenseTypeFactory.instance
    

    def getInstance_j1(self, name: str) -> LicenseType:
        if self.DEMO.getName().compareTo(name) == 0:
            return self.DEMO
        elif self.NORMAL.getName().compareTo(name) == 0:
            return self.NORMAL
        return self.UNKNOWN

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.system.security.licensing.LicenseType import LicenseType


def _LicenseTypeFactory_instance() -> object:
    return LicenseTypeFactory()

lazy_static(LicenseTypeFactory, "instance", _LicenseTypeFactory_instance)

