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
# package org.allbinary.media

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.media.AllBinaryVibrationME import AllBinaryVibrationME


class AllBinaryNoVibration(AllBinaryVibrationME):
    NO_VIBRATION: AllBinaryVibrationME = None

    def __init__(self) -> None:
        super().__init__()
    

    def vibrate(self, duration: int, type_: int, volume: int) -> None:
        pass


def _AllBinaryNoVibration_NO_VIBRATION() -> object:
    return AllBinaryNoVibration()

lazy_static(AllBinaryNoVibration, "NO_VIBRATION", _AllBinaryNoVibration_NO_VIBRATION)

