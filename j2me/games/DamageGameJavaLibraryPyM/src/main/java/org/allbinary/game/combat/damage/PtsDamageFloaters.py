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

from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorArrayIndexer import BasicColorArrayIndexer
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.game.combat.damage.DamageFloaters import DamageFloaters


class PtsDamageFloaters(DamageFloaters):
    basicColorArrayIndexer: BasicColorArrayIndexer = BasicColorArrayIndexer([BasicColorFactory.getInstance().WHITE, BasicColorFactory.getInstance().RED, BasicColorFactory.getInstance().YELLOW, BasicColorFactory.getInstance().BLUE])

    def _init_fields(self) -> None:
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.layerInterface: AllBinaryLayer = None
        self.lastDamage: list[int] = [0] * (5)
        self.lastDamageString: list[list[str]] = [['\0'] * (0) for _ in range(5)]
        self.lastDamageStringSizeArray: list[int] = [0] * (5)
        self.circularIndexUtil: CircularIndexUtil = CircularIndexUtil.createInstance(5)
        self.primitiveLongUtil: PrimitiveLongUtil = None
        self.myRandomFactory: MyRandomFactory = MyRandomFactory.getInstance()
    

    def __init__(self, layerInterface: AllBinaryLayer) -> None:
        super().__init__()
        self._init_fields()
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(100000)
        self.layerInterface = layerInterface
        CHAR_ARRAY: list[str] = CharArrayFactory.getInstance().getZeroCharArray()
        for index in range(len(self.lastDamageString) - 1, 0 - 1, -1):
            self.lastDamageString[index] = CHAR_ARRAY
    

    def add(self, damage: int) -> None:
        index: int = self.circularIndexUtil.getIndex()
        self.lastDamage[index] = damage
        self.lastDamageString[index] = self.primitiveLongUtil.getCharArray(self.lastDamage[index])
        self.lastDamageStringSizeArray[index] = self.primitiveLongUtil.getCurrentTotalDigits()
        self.circularIndexUtil.next()
    

    def paint(self, graphics: Graphics) -> None:
        viewPosition: ViewPositionBase = self.layerInterface.getViewPosition()
        x: int = viewPosition.getX()
        y: int = viewPosition.getY()
        for index in range(len(self.lastDamage) - 1, 0 - 1, -1):
            if self.lastDamage[index] != 0:
                delta: int = 10 * (index + 2)
                self.basicSetColorUtil.setBasicColorP(graphics, PtsDamageFloaters.basicColorArrayIndexer.get())
                graphics.drawChars(self.lastDamageString[index], 0, self.lastDamageStringSizeArray[index], x - self.myRandomFactory.getNextInt(delta), y - delta, 0)
                PtsDamageFloaters.basicColorArrayIndexer.next()
            self.lastDamage[index] = 0
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.rand.MyRandomFactory import MyRandomFactory
from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.java.character.CharArrayFactory import CharArrayFactory
from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
from org.allbinary.util.CircularIndexUtil import CircularIndexUtil
from org.allbinary.view.ViewPosition import ViewPosition
from org.allbinary.view.ViewPositionBase import ViewPositionBase


