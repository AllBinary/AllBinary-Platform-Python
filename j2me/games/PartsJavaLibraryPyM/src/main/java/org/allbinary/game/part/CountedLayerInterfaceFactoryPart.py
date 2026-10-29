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
# package org.allbinary.game.part

from __future__ import annotations

from org.allbinary.game.layer.pickup.CountedPickedUpLayerInterfaceFactory import CountedPickedUpLayerInterfaceFactory
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.game.part.PartInterface import PartInterface


class CountedLayerInterfaceFactoryPart(PartInterface, UpdateMyFontInterface):
    NULL_COUNTED_LAYER_INTERFACE_FACTORY: CountedLayerInterfaceFactoryPart = None

    def _init_fields(self) -> None:
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.animationInterface: Animation = NullAnimationFactory.getFactoryInstance().getInstance(0)
        self.total: int = 0
        self.totalString: list[str] = NullUtil.getInstance().NULL_CHAR_ARRAY
        self.xOffset: int = 0
        self.countedPickedUpLayerInterfaceFactory: CountedPickedUpLayerInterfaceFactory = CountedPickedUpLayerInterfaceFactory.NULL_COUNTED_PICKUP_LAYER_FACTORY
        self.primitiveLongUtil: PrimitiveLongUtil = None
    

    def __init__(self, total: int, countedPickedUpLayerInterfaceFactory: CountedPickedUpLayerInterfaceFactory) -> None:
        self._init_fields()
        self.primitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(1000)
        self.init(total, countedPickedUpLayerInterfaceFactory)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.setXOffset(font.charsWidth(self.totalString, 0, self.primitiveLongUtil.getCurrentTotalDigits()) + (font.getSize() >> 1))
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def init(self, total: int, countedPickedUpLayerInterfaceFactory: CountedPickedUpLayerInterfaceFactory) -> None:
        self.setCountedPickedUpLayerInterfaceFactory(countedPickedUpLayerInterfaceFactory)
        self.total = total
    

    # throws Exception
    def getInstance(self, hashtable: ABHashtable[object, object], x: int, y: int, z: int) -> AllBinaryLayer:
        if self.total > 0:
            self.setTotal(self.total - 1)
            return self.getCountedPickedUpLayerInterfaceFactory().getNextInstance(hashtable, x, y, z)
        else:
            raise Exception("No more left. Could use a listener to automatically remove")
    

    def getTotal(self) -> int:
        return self.total
    

    def setTotal(self, total: int) -> None:
        self.total = total
        self.totalString = self.primitiveLongUtil.getCharArray(total)
        self.myFontProcessor = self.updateMyFontProcessor
    

    def paint(self, graphics: Graphics) -> None:
        self.myFontProcessor.process(graphics)
    

    def paintThreed(self, graphics: Graphics) -> None:
        pass
    

    def getAnimationInterface(self) -> Animation:
        return self.animationInterface
    

    def setAnimationInterface(self, animationInterface: Animation) -> None:
        self.animationInterface = animationInterface
    

    def getXOffset(self) -> int:
        return self.xOffset
    

    def setXOffset(self, totalStringWidth: int) -> None:
        self.xOffset = totalStringWidth
    

    def getTotalString(self) -> list[str]:
        return self.totalString
    

    def getCountedPickedUpLayerInterfaceFactory(self) -> CountedPickedUpLayerInterfaceFactory:
        return self.countedPickedUpLayerInterfaceFactory
    

    def setCountedPickedUpLayerInterfaceFactory(self, countedPickedUpLayerInterfaceFactory: CountedPickedUpLayerInterfaceFactory) -> None:
        self.countedPickedUpLayerInterfaceFactory = countedPickedUpLayerInterfaceFactory
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.animation.Animation import Animation
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
from org.allbinary.util.ABHashtable import ABHashtable


CountedLayerInterfaceFactoryPart.NULL_COUNTED_LAYER_INTERFACE_FACTORY = CountedLayerInterfaceFactoryPart(0, CountedPickedUpLayerInterfaceFactory.NULL_COUNTED_PICKUP_LAYER_FACTORY)

