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
# package org.allbinary.time

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class LicenseStupidTimerFactory:
    instance: StupidTimer = None
    

    @staticmethod
    def getInstance() -> StupidTimer:
        return LicenseStupidTimerFactory.instance


def _LicenseStupidTimerFactory_instance() -> object:
    from org.allbinary.time.StupidTimer import StupidTimer
    return StupidTimer()

lazy_static(LicenseStupidTimerFactory, "instance", _LicenseStupidTimerFactory_instance)

