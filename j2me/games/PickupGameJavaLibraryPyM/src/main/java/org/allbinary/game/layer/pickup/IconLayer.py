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
# package org.allbinary.game.layer.pickup

from __future__ import annotations

from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


class IconLayer(AllBinaryLayer):
    NULL_ICON_LAYER: IconLayer = None

    def _init_fields(self) -> None:
        self.animationInterface: Animation = None
    

    def __init__(self, animationInterface: Animation, width: int, height: int) -> None:
        super().__init__(StringUtil.getInstance().EMPTY_STRING, Rectangle(PointFactory.getInstance().ZERO_ZERO, width, height), ViewPosition.getInstanceD())
        self._init_fields()
        self.animationInterface = animationInterface
    

    def paint(self, graphics: Graphics) -> None:
        self.animationInterface.paintXY(graphics, self.x, self.y)
    

    def paintThreed(self, graphics: Graphics) -> None:
        self.animationInterface.paintThreedXYZ(graphics, self.x, self.y, self.z)
    

    def getAnimationInterface(self) -> Animation:
        return self.animationInterface
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.view.ViewPosition import ViewPosition


IconLayer.NULL_ICON_LAYER = IconLayer(NullAnimationFactory.getFactoryInstance().getInstance(0), 0, 0)

