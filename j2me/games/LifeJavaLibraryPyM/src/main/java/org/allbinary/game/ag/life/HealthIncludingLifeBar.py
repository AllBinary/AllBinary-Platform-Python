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
# package org.allbinary.game.ag.life

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.health.HealthListenerInterface import HealthListenerInterface
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class HealthIncludingLifeBar(*java_bases(Paintable, HealthListenerInterface)):
    def _java_defaults(self):
        vars(self).setdefault("animationInterface", None)
        vars(self).setdefault("life", None)
        vars(self).setdefault("healthInterface", None)
        vars(self).setdefault("allbinaryLayer", None)

    def _init_fields(self) -> None:
        if "animationInterface" not in vars(self): self.animationInterface: HealthBarAnimation = None
        if "life" not in vars(self): self.life: Life = None
        if "healthInterface" not in vars(self): self.healthInterface: HealthInterface = None
        if "allbinaryLayer" not in vars(self): self.allbinaryLayer: AllBinaryLayer = None
    

    # throws Exception
    @staticmethod
    def createHealthIncludingLifeBar(layerInterface: AllBinaryLayer, life: Life, healthInterface: Health, location: int, direction: int) -> HealthIncludingLifeBar:
        from org.allbinary.game.health.Health import Health
        from org.allbinary.game.health.HealthBarTwodAnimation import HealthBarTwodAnimation
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        return HealthIncludingLifeBar(layerInterface, life, healthInterface, HealthBarTwodAnimation(layerInterface, location), direction)
    

    def __init__(self, layerInterface: AllBinaryLayer, life: Life, healthInterface: Health, animationInterface: HealthBarAnimation, direction: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.health.Health import Health
        from org.allbinary.game.health.HealthBarAnimation import HealthBarAnimation
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        super().__init__()
        __class__._init_fields(self)
        self.allbinaryLayer = layerInterface
        self.animationInterface = animationInterface
        self.life = life
        self.healthInterface = healthInterface
        self.healthInterface.addListener(self)
        self.onHealthChange()
    

    def onHealthChange(self) -> None:
        self.animationInterface.onHealthChange(java_divide(((self.healthInterface.getHealth() + (self.healthInterface.getMaxHealth() * self.life.get())) * self.allbinaryLayer.getWidth()), (self.healthInterface.getMaxHealth() + (self.healthInterface.getMaxHealth() * self.life.getStartLives()))))
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.animationInterface.paintXY(graphics, 0, 0)
    

    def paintThreed(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.animationInterface.paintThreedXYZ(graphics, 0, 0, 0)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.game.health.Health import Health
# from org.allbinary.game.health.HealthBarAnimation import HealthBarAnimation
# from org.allbinary.game.health.HealthBarTwodAnimation import HealthBarTwodAnimation
# from org.allbinary.game.health.HealthInterface import HealthInterface
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


