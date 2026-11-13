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

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem


class NoOperatingSystem(GenericOperatingSystem):
    NO_OPERATING_SYSTEM: GenericOperatingSystem = None
    

    def __init__(self) -> None:
        super().__init__()


def _NoOperatingSystem_NO_OPERATING_SYSTEM() -> object:
    from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
    return GenericOperatingSystem()

lazy_static(NoOperatingSystem, "NO_OPERATING_SYSTEM", _NoOperatingSystem_NO_OPERATING_SYSTEM)

