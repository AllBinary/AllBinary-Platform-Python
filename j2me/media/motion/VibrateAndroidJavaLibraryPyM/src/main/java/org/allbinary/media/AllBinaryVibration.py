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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.media.AllBinaryVibrationME import AllBinaryVibrationME


@java_inherited_overloads
class AllBinaryVibration(AllBinaryVibrationME):
    VIBRATION: AllBinaryVibrationME = None
    def _java_defaults(self):
        vars(self).setdefault("vibrator", None)

    def _init_fields(self) -> None:
        from android.content.Context import Context
        from android.os.Vibrator import Vibrator
        from org.allbinary.data.resource.ResourceUtil import ResourceUtil
        self.vibrator: Vibrator = ResourceUtil.getInstance().getContext().getSystemService(Context.VIBRATOR_SERVICE)
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

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
        self.vibrator.vibrate(duration)
# from android.content.Context import Context
# from android.os.Vibrator import Vibrator
# from org.allbinary.data.resource.ResourceUtil import ResourceUtil
# from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral


def _AllBinaryVibration_VIBRATION() -> object:
    from org.allbinary.media.AllBinaryNoVibration import AllBinaryNoVibration
    return AllBinaryNoVibration.NO_VIBRATION

lazy_static(AllBinaryVibration, "VIBRATION", _AllBinaryVibration_VIBRATION)

