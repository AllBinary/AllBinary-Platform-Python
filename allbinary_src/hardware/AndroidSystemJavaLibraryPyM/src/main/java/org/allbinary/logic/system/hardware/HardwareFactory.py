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
        from org.allbinary.TsUtil import TsUtil
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tsUtil: TsUtil = TsUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> HardwareFactory:
        return HardwareFactory.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def getInstance_j1(self, os: GenericOperatingSystem) -> HardwareInterface:
        from org.allbinary.logic.system.hardware.NoHardware import NoHardware
        from org.allbinary.logic.system.hardware.android.AndroidHardware import AndroidHardware
        from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
        from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            operatingSystems: OperatingSystems = OperatingSystems.getInstance()
            if ((os.getName() > operatingSystems.ANDROID) - (os.getName() < operatingSystems.ANDROID)) == 0:
                return AndroidHardware()
            elif ((os.getName() > operatingSystems.HARMONY) - (os.getName() < operatingSystems.HARMONY)) == 0:
                return AndroidHardware()
            raise Exception("No Hardware Imp for: " + os.getName())
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put("Ignoring Exception Returning NoHardware", self, commonStrings.GET_INSTANCE, e)
            return NoHardware()

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from org.allbinary.TsUtil import TsUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.hardware.android.AndroidHardware import AndroidHardware
# from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
# from org.allbinary.logic.system.os.OperatingSystems import OperatingSystems
# from org.allbinary.string.CommonStrings import CommonStrings


def _HardwareFactory_instance() -> object:
    return HardwareFactory()

lazy_static(HardwareFactory, "instance", _HardwareFactory_instance)

