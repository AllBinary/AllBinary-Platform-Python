# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.game.layer

from __future__ import annotations



class AdvancedRTSProperties:

    def _init_fields(self) -> None:
        self.shakeListener: ShakeAnimationListener = None
        self.vibration: AllBinaryVibrationME = None
        self.duration: int = None
        self.waypointBehaviorBase: TickableInterface = None
    

    @staticmethod
    def createPropertiesSimulated() -> AdvancedRTSProperties:
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        return AdvancedRTSProperties(NoShakeAnimationListener.NO_SHAKE_ANIMATION_LISTENER, AllBinaryNoVibration.NO_VIBRATION, 0, WaypointBehaviorBase())
    

    @staticmethod
    def createProperties() -> AdvancedRTSProperties:
        from org.allbinary.game.layer.WaypointBehaviorBase import WaypointBehaviorBase
        return AdvancedRTSProperties(ShakeAnimationListenerFactory.getInstance(), AllBinaryVibration.getInstance(), int(GameConfigurationCentral.getInstance().VIBRATION.getValue()) * 100, WaypointBehaviorBase())
    

    def __init__(self, shakeListener: ShakeAnimationListener, vibration: AllBinaryVibrationME, duration: int, waypointBehaviorBase: TickableInterface) -> None:
        self._init_fields()
        self.shakeListener = shakeListener
        self.vibration = vibration
        self.duration = duration
        self.waypointBehaviorBase = waypointBehaviorBase
from org.allbinary.animation.transition.shake.NoShakeAnimationListener import NoShakeAnimationListener
from org.allbinary.animation.transition.shake.ShakeAnimationListener import ShakeAnimationListener
from org.allbinary.animation.transition.shake.ShakeAnimationListenerFactory import ShakeAnimationListenerFactory
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
from org.allbinary.game.tick.TickableInterface import TickableInterface
from org.allbinary.media.AllBinaryNoVibration import AllBinaryNoVibration
from org.allbinary.media.AllBinaryVibration import AllBinaryVibration
from org.allbinary.media.AllBinaryVibrationME import AllBinaryVibrationME


