# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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
# package org.allbinary.game.layer.item

from __future__ import annotations

from org.allbinary.game.rts.technology.event.TechEventListenerInterface import TechEventListenerInterface
from org.allbinary.animation.Animation import Animation
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface


class RTSLayerCostAnimation(Animation, TechEventListenerInterface, UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.primitiveLongUtil: PrimitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(10000)
        self.DOLLAR: str = "$"
        self.image: Image = None
        self.layerInterfaceFactoryInterface: CostLayerInterfaceFactoryInterface = None
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.costString: list[str] = NullUtil.getInstance().NULL_CHAR_ARRAY
        self.len_: int = 0
        self.adjustedCostX: int = 0
        self.fontHeight: int = 0
    

    def __init__(self, image: Image, layerInterfaceFactoryInterface: CostLayerInterfaceFactoryInterface) -> None:
        super().__init__()
        self._init_fields()
        self.image = image
        self.layerInterfaceFactoryInterface = layerInterfaceFactoryInterface
        self.update()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        font: Font = graphics.getFont()
        self.fontHeight = font.getHeight()
        self.adjustedCostX = font.stringWidth(self.DOLLAR)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def onEvent(self, event: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onTechEvent(self, event: AllBinaryEventObject) -> None:
        try:
            self.update()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "onTechEvent", e)
    

    # throws Exception
    def update(self) -> None:
        self.len_ = 0
        self.costString = self.primitiveLongUtil.getCharArray(self.layerInterfaceFactoryInterface.getCost())
        self.len_ = self.primitiveLongUtil.getCurrentTotalDigits()
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        self.myFontProcessor.process(graphics)
        super().paintXY(graphics, x, y)
        adjustedCostY: int = self.image.getHeight() - self.fontHeight
        xa: int = x + 2
        graphics.drawString(self.DOLLAR, xa, y + adjustedCostY, 0)
        graphics.drawChars(self.costString, 0, self.len_, x + self.adjustedCostX, y + adjustedCostY, 0)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.game.layer.CostLayerInterfaceFactoryInterface import CostLayerInterfaceFactoryInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
from org.allbinary.logic.util.event.EventStrings import EventStrings


