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

from org.allbinary.game.combat.damage.DamageFloaters import DamageFloaters


class AnimationDamageFloaters(DamageFloaters):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.layerInterface: AllBinaryLayer = None
        self.animationInterfaceArray: list[IndexedAnimation] = None
        self.circularIndexUtil: CircularIndexUtil = None
        self.dx: int = None
        self.dy: int = None
    

    def __init__(self, layerInterface: AllBinaryLayer, animationInterfaceArray: list[IndexedAnimation], dx: int, dy: int) -> None:
        super().__init__()
        self._init_fields()
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
from org.allbinary.animation.IndexedAnimation import IndexedAnimation
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
from org.allbinary.view.ViewPosition import ViewPosition
from org.allbinary.view.ViewPositionBase import ViewPositionBase


