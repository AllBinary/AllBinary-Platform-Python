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
# package org.allbinary.game.combat.damage

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.combat.damage.DamageFloaters import DamageFloaters


@java_inherited_overloads
class AnimationDamageFloaters(DamageFloaters):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("layerInterface", None)
        vars(self).setdefault("animationInterfaceArray", None)
        vars(self).setdefault("circularIndexUtil", None)
        vars(self).setdefault("dx", 0)
        vars(self).setdefault("dy", 0)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "layerInterface" not in vars(self): self.layerInterface: AllBinaryLayer = None
        if "animationInterfaceArray" not in vars(self): self.animationInterfaceArray: list[IndexedAnimation] = None
        if "circularIndexUtil" not in vars(self): self.circularIndexUtil: CircularIndexUtil = None
        if "dx" not in vars(self): self.dx: int = 0
        if "dy" not in vars(self): self.dy: int = 0
    

    def __init__(self, layerInterface: AllBinaryLayer, animationInterfaceArray: list[IndexedAnimation], dx: int, dy: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.animation.IndexedAnimation import IndexedAnimation
        from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
        from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
        super().__init__()
        __class__._init_fields(self)
        self.animationInterfaceArray = animationInterfaceArray
        for index in range(len(self.animationInterfaceArray) - 1, 0 - 1, -1):
            self.animationInterfaceArray[index].setFrame(self.animationInterfaceArray[index].getSize() - 1)
        self.layerInterface = layerInterface
        self.circularIndexUtil = CircularIndexUtil.createInstance(len(self.animationInterfaceArray))
        self.dx = dx
        self.dy = dy
    

    def add(self, damage: int) -> None:
        i: int = self.circularIndexUtil.getIndex()
        self.animationInterfaceArray[i].setFrame(0)
        self.circularIndexUtil.next()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.animation.IndexedAnimation import IndexedAnimation
        from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.view.ViewPositionBase import ViewPositionBase
        try:
            viewPosition: ViewPositionBase = self.layerInterface.getViewPosition()
            x: int = viewPosition.getX()
            y: int = viewPosition.getY()
            for index in range(0, len(self.animationInterfaceArray)):
                animationInterface: IndexedAnimation = self.animationInterfaceArray[index]
                if animationInterface.getFrame() < animationInterface.getAnimationSize() - 1:
                    delta: int = animationInterface.getFrame() * 20
                    animationInterface.paintXY(graphics, x + self.dx, y - delta + self.dy)
                    animationInterface.nextFrame()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            canvasStrings: CanvasStrings = CanvasStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, canvasStrings.PAINT, e)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.animation.IndexedAnimation import IndexedAnimation
# from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
# from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
# from org.allbinary.view.ViewPosition import ViewPosition
# from org.allbinary.view.ViewPositionBase import ViewPositionBase


