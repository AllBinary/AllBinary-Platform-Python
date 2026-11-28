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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.rts.technology.event.TechEventListenerInterface import TechEventListenerInterface
from org.allbinary.animation.Animation import Animation
from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface


@java_inherited_overloads
class RTSLayerCostAnimation(*java_bases(Animation, TechEventListenerInterface, UpdateMyFontInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("primitiveLongUtil", None)
        vars(self).setdefault("DOLLAR", None)
        vars(self).setdefault("image", None)
        vars(self).setdefault("layerInterfaceFactoryInterface", None)
        vars(self).setdefault("myFontProcessor", None)
        vars(self).setdefault("costString", None)
        vars(self).setdefault("len_", 0)
        vars(self).setdefault("adjustedCostX", 0)
        vars(self).setdefault("fontHeight", 0)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.primitiveLongUtil: PrimitiveLongUtil = PrimitiveLongUtil.createPowerOfTen(10000)
        self.DOLLAR: str = "$"
        if "image" not in vars(self): self.image: Image = None
        if "layerInterfaceFactoryInterface" not in vars(self): self.layerInterfaceFactoryInterface: CostLayerInterfaceFactoryInterface = None
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.costString: list[str] = NullUtil.getInstance().NULL_CHAR_ARRAY
        if "len_" not in vars(self): self.len_: int = 0
        if "adjustedCostX" not in vars(self): self.adjustedCostX: int = 0
        self.fontHeight: int = 0
    

    def __init__(self, image: Image, layerInterfaceFactoryInterface: CostLayerInterfaceFactoryInterface) -> None:
        __class__._java_defaults(self)
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.game.layer.CostLayerInterfaceFactoryInterface import CostLayerInterfaceFactoryInterface
        super().__init__()
        __class__._init_fields(self)
        self.image = image
        self.layerInterfaceFactoryInterface = layerInterfaceFactoryInterface
        self.update()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        font: Font = graphics.getFont()
        self.fontHeight = font.getHeight()
        self.adjustedCostX = font.stringWidth(self.DOLLAR)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def onEvent(self, event: AllBinaryEventObject) -> None:
        from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.logic.util.event.EventStrings import EventStrings
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onTechEvent(self, event: AllBinaryEventObject) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
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
        from javax.microedition.lcdui.Graphics import Graphics
        self.myFontProcessor.process(graphics)
        java_super_call(super(), "paintXY", graphics, x, y)
        adjustedCostY: int = self.image.getHeight() - self.fontHeight
        xa: int = x + 2
        graphics.drawString(self.DOLLAR, xa, y + adjustedCostY, 0)
        graphics.drawChars(self.costString, 0, self.len_, x + self.adjustedCostX, y + adjustedCostY, 0)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.game.layer.CostLayerInterfaceFactoryInterface import CostLayerInterfaceFactoryInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.logic.math.PrimitiveLongUtil import PrimitiveLongUtil
# from org.allbinary.logic.util.event.EventStrings import EventStrings


