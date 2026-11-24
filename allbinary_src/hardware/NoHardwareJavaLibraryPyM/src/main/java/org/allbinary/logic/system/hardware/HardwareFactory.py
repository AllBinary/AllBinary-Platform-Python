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
# package org.allbinary.logic.system.hardware

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class HardwareFactory:
    instance: HardwareFactory = None

    def _init_fields(self) -> None:
        self.SINGLETON: HardwareInterface = NoHardware.getInstance()
    

    @staticmethod
    def getInstance_j0() -> HardwareFactory:
        return HardwareFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getInstance_j1(self, os: OperatingSystemInterface) -> HardwareInterface:
        from org.allbinary.logic.system.os.OperatingSystemInterface import OperatingSystemInterface
        try:
            return self.SINGLETON
        except Exception as e:
            raise e

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from org.allbinary.logic.system.os.OperatingSystemInterface import OperatingSystemInterface


def _HardwareFactory_instance() -> object:
    return HardwareFactory()

lazy_static(HardwareFactory, "instance", _HardwareFactory_instance)

