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
# package org.allbinary.game.graphics.hud

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface


class BasicHud_1(UpdateMyFontInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.canvasStrings: CanvasStrings = CanvasStrings.getInstance()
        self.basicSetColorUtil: BasicColorSetUtil = BasicColorSetUtil.getInstance()
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.updateMyFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.myFontProcessor: MyFontProcessor = self.updateMyFontProcessor
        self.location: int = 0
        self.direction: int = 0
        self.bufferZone: int = 0
        self.hudGraphicsPosition: HudGraphicsPosition = HudGraphicsPosition.NULL_HUD_GRAPHICS_POSITION
        self.x: int = 0
        self.y: int = 0
        self.basicColor: BasicColor = BasicColorFactory.getInstance().BLACK
        self.color: int = None
        self.updateMaxWidth: int = 0
        self.updateMaxHeight: int = 0
        self.offsetY: int = 0
    

    def __init__(self, location: int, direction: int, bufferZone: int, basicColor: BasicColor) -> None:
        self._init_fields()
        self.setLocation(location)
        self.setDirection(direction)
        self.setBufferZone(bufferZone)
        self.onDisplayChangeEvent(DisplayInfoSingleton.getInstance().displayChangeEvent)
        self.setBasicColorP(basicColor)
        self.color = int(basicColor)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        try:
            self.hudGraphicsPosition = self.getHudGraphicsPositionWH(self.displayInfo.getLastWidth(), self.displayInfo.getLastHeight(), self.updateMaxWidth, self.updateMaxHeight)
            self.x = self.hudGraphicsPosition.getPoint().getX()
            self.setY(self.hudGraphicsPosition.getPoint().getY())
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, self.canvasStrings.ON_DISPLAY_CHANGE_EVENT, e)
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def getLocation(self) -> int:
        return self.location
    

    def getDirection(self) -> int:
        return self.direction
    

    # throws Exception
    def getHudGraphicsPositionWH(self, width: int, height: int, maxWidth: int, maxHeight: int) -> HudGraphicsPosition:
        from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
        from org.allbinary.game.graphics.hud.HudGraphicsPosition import HudGraphicsPosition
        x: int = 0
        y: int = 0
        anchor: int = 0
        basicHudFactory: BasicHudFactory = BasicHudFactory.getInstance()
        if basicHudFactory.BOTTOMLEFT == self.getLocation():
            x = self.bufferZone + 2
            y = height - maxHeight - self.bufferZone
            anchor = Graphics.BOTTOM & Graphics.LEFT
        elif basicHudFactory.BOTTOMRIGHT == self.getLocation():
            x = width - maxWidth
            y = height - maxHeight - self.bufferZone
            anchor = Graphics.BOTTOM & Graphics.RIGHT
        elif basicHudFactory.TOPLEFT == self.getLocation():
            x = self.bufferZone + 2
            y = self.bufferZone + 5
            anchor = Anchor.TOP_LEFT
        elif basicHudFactory.TOPRIGHT == self.getLocation():
            x = width - maxWidth
            y = self.bufferZone + 5
            anchor = Graphics.TOP & Graphics.RIGHT
        elif basicHudFactory.TOPCENTER == self.getLocation():
            x = (int((width - maxWidth) / 2))
            y = self.bufferZone + 5
            anchor = Graphics.TOP & Graphics.HCENTER
        elif basicHudFactory.BOTTOMCENTER == self.getLocation():
            x = (int((width - maxWidth) / 2))
            y = height - maxHeight - self.bufferZone
            anchor = Graphics.BOTTOM & Graphics.HCENTER
        elif basicHudFactory.ABSOLUTE == self.getLocation():
            x = maxHeight
            y = maxWidth
            anchor = 0
        return HudGraphicsPosition(self.getPoint(x, y), anchor)
    

    def onEvent(self, eventObject: AllBinaryEventObject) -> None:
        ForcedLogUtil.log(EventStrings.getInstance().PERFORMANCE_MESSAGE, self)
    

    def onDisplayChangeEvent(self, displayChangeEvent: DisplayChangeEvent) -> None:
        self.myFontProcessor = self.updateMyFontProcessor
    

    def getPoint(self, x: int, y: int) -> GPoint:
        return PointFactory.getInstance().createXY(x, y)
    

    def getBufferZone(self) -> int:
        return self.bufferZone
    

    def setBufferZone(self, bufferZone: int) -> None:
        self.bufferZone = bufferZone
    

    def setLocation(self, location: int) -> None:
        self.location = location
    

    def setDirection(self, direction: int) -> None:
        self.direction = direction
    

    def getHudGraphicsPosition(self) -> HudGraphicsPosition:
        return self.hudGraphicsPosition
    

    def getColor(self) -> int:
        return self.color
    

    def getX(self) -> int:
        return self.x
    

    def setX(self, x: int) -> None:
        self.x = x
    

    def setBasicColorP(self, basicColor: BasicColor) -> None:
        self.basicColor = basicColor
    

    def getBasicColorP(self) -> BasicColor:
        return self.basicColor
    

    def setY(self, y: int) -> None:
        self.y = y
    

    def getY(self) -> int:
        return self.y
    

    def paintSSO(self, graphics: Graphics, string: str, string2: str, offset: int) -> None:
        self.myFontProcessor.process(graphics)
        self.basicSetColorUtil.setBasicColorP(graphics, self.getBasicColorP())
        graphics.drawString(string, self.x, self.getY(), self.hudGraphicsPosition.getAnchor())
        graphics.drawString(string2, self.x + offset, self.getY(), self.hudGraphicsPosition.getAnchor())
    

    def paintSSOO(self, graphics: Graphics, string: str, string2: str, offset: int, offset2: int) -> None:
        self.myFontProcessor.process(graphics)
        graphics.setColor(self.getColor())
        graphics.drawString(string, self.x + offset, self.getY(), self.hudGraphicsPosition.getAnchor())
        graphics.drawString(string2, self.x + offset2, self.getY(), self.hudGraphicsPosition.getAnchor())
    

    def paintDXY(self, graphics: Graphics, charArray: list[str], offset: int, len_: int, charArray2: list[str], offset2: int, len2: int, xOffset: int, xOffset2: int) -> None:
        self.myFontProcessor.process(graphics)
        self.basicSetColorUtil.setBasicColorP(graphics, self.getBasicColorP())
        y: int = self.getY()
        graphics.drawChars(charArray, offset, len_, self.x + xOffset, y, self.hudGraphicsPosition.getAnchor())
        graphics.drawChars(charArray2, offset2, len2, self.x + xOffset2, y, self.hudGraphicsPosition.getAnchor())
    

    def paintDX(self, graphics: Graphics, charArray: list[str], offset: int, len_: int, charArray2: list[str], offset2: int, len2: int, xOffset: int) -> None:
        self.myFontProcessor.process(graphics)
        self.basicSetColorUtil.setBasicColorP(graphics, self.getBasicColorP())
        y: int = self.getY()
        graphics.drawChars(charArray, offset, len_, self.x, y, self.hudGraphicsPosition.getAnchor())
        graphics.drawChars(charArray2, offset2, len2, self.x + xOffset, y, self.hudGraphicsPosition.getAnchor())
    

    def paintOffsetAndLength(self, graphics: Graphics, charArray: list[str], offset: int, len_: int) -> None:
        self.myFontProcessor.process(graphics)
        self.basicSetColorUtil.setBasicColorP(graphics, self.getBasicColorP())
        y: int = self.getY()
        graphics.drawChars(charArray, offset, len_, self.x, y, self.hudGraphicsPosition.getAnchor())
    

    def paintString(self, graphics: Graphics, string: str) -> None:
        self.myFontProcessor.process(graphics)
        self.basicSetColorUtil.setBasicColorP(graphics, self.getBasicColorP())
        y: int = self.getY() + self.offsetY
        graphics.drawString(string, self.x, y, self.hudGraphicsPosition.getAnchor())
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.graphics.Anchor import Anchor
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
from org.allbinary.graphics.color.BasicColorSetUtil import BasicColorSetUtil
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.displayable.event.DisplayChangeEvent import DisplayChangeEvent
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.logic.util.event.EventStrings import EventStrings
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.game.graphics.hud.HudGraphicsPosition import HudGraphicsPosition


