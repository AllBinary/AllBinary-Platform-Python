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


class AllBinaryVibration(AllBinaryVibrationME):
    VIBRATION: AllBinaryVibrationME = None
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> AllBinaryVibrationME:
        return AllBinaryVibration.VIBRATION
    

    @staticmethod
    def init() -> None:
        from org.allbinary.media.AllBinaryNoVibration import AllBinaryNoVibration
        from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
        if int(GameConfigurationCentral.getInstance().VIBRATION.getValue()) == 0:
            AllBinaryVibration.VIBRATION = AllBinaryNoVibration.NO_VIBRATION
        else:
            AllBinaryVibration.VIBRATION = AllBinaryVibration()
    

    def vibrate(self, duration: int, type_: int, volume: int) -> None:
        pass
# from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral


def _AllBinaryVibration_VIBRATION() -> object:
    from org.allbinary.media.AllBinaryNoVibration import AllBinaryNoVibration
    return AllBinaryNoVibration.NO_VIBRATION

lazy_static(AllBinaryVibration, "VIBRATION", _AllBinaryVibration_VIBRATION)

