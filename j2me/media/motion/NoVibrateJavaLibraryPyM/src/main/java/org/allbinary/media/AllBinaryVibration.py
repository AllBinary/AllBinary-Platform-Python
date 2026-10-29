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

from org.allbinary.media.AllBinaryVibrationME import AllBinaryVibrationME
from org.allbinary.media.AllBinaryNoVibration import AllBinaryNoVibration


class AllBinaryVibration(AllBinaryVibrationME):
    VIBRATION: AllBinaryVibrationME = AllBinaryNoVibration.NO_VIBRATION
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> AllBinaryVibrationME:
        return AllBinaryVibration.VIBRATION
    

    @staticmethod
    def init() -> None:
        from org.allbinary.media.AllBinaryNoVibration import AllBinaryNoVibration
        if int(GameConfigurationCentral.getInstance().VIBRATION.getValue()) == 0:
            AllBinaryVibration.VIBRATION = AllBinaryNoVibration.NO_VIBRATION
        else:
            AllBinaryVibration.VIBRATION = AllBinaryVibration()
    

    def vibrate(self, duration: int, type_: int, volume: int) -> None:
        pass
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral


