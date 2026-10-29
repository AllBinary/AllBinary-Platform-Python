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
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.game.layer.SelectionHudPaintable import SelectionHudPaintable


class UpgradableRTSLayerHudPaintable(SelectionHudPaintable):
    instance: UpgradableRTSLayerHudPaintable = None

    def _init_fields(self) -> None:
        self.PERCENT: str = "%"
        self.rtsLayer: CollidableDestroyableDamageableLayer = CollidableDestroyableDamageableLayer.getNullInstance()
        self.costY: int = 0
        self.costY1: int = 0
        self.percentCompleteX2: int = 0
        self.rtsLayerCompositePaintableLateInit: RTSLayerCompositePaintable = None
        self.charHeight: int = 0
        self.charWidth: int = 0
        self.percentComplete: int = 0
        self.percentCompleteX: int = 0
        self.percentCompleteArray: list[str] = CharArrayFactory.getInstance().getZeroCharArray()
        self.currentTotalDigits: int = 0
    

    @staticmethod
    def getInstance() -> UpgradableRTSLayerHudPaintable:
        return UpgradableRTSLayerHudPaintable.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        super().updateMeasurement(graphics)
        font: Font = graphics.getFont()
        self.charHeight = font.getHeight()
        self.charWidth = MyFontProcessor.defaultCharWidth(font)
    

    def update(self) -> None:
        from org.allbinary.game.layer.RTSLayerCompositePaintable import RTSLayerCompositePaintable
        from org.allbinary.game.layer.UpgradableWideRTSLayerPaintable import UpgradableWideRTSLayerPaintable
        super().update()
        commonButtons: CommonButtons = CommonButtons.getInstance()
        self.costY = (self.y + commonButtons.STANDARD_BUTTON_SIZE)
        self.costY1 = (self.y + commonButtons.STANDARD_BUTTON_SIZE - self.charHeight)
        self.percentCompleteX2 = self.imageX + commonButtons.STANDARD_BUTTON_SIZE - self.charWidth
        displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        if displayInfoSingleton.getLastWidth() > 320:
            self.rtsLayerCompositePaintableLateInit = UpgradableWideRTSLayerPaintable(self)
        else:
            self.rtsLayerCompositePaintableLateInit = RTSLayerCompositePaintable(self)
    

    def updateSelectionInfo(self) -> None:
        rtsLayer: RTSLayer = self.getRtsLayer()
        self.rtsLayerCompositePaintableLateInit.update(rtsLayer)
        self.setAnimationInterface(rtsLayer.getVerticleBuildAnimationInterface())
        self.setName(rtsLayer.getName())
    

    def updateInfo(self) -> None:
        rtsLayer: RTSLayer = self.getRtsLayer()
        self.percentComplete = rtsLayer.getPercentComplete()
        if self.percentComplete < 10:
            self.percentCompleteX = 32
        elif self.percentComplete < 100:
            self.percentCompleteX = 24
        else:
            self.percentCompleteX = 16
        self.percentCompleteArray = self.getPrimitiveLongUtil().getCharArray(self.percentComplete)
        self.currentTotalDigits = self.getPrimitiveLongUtil().getCurrentTotalDigits()
    

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
        self.rtsLayerCompositePaintableLateInit.paint(graphics)
        graphics.drawChars(self.percentCompleteArray, 0, self.currentTotalDigits, self.imageX + self.percentCompleteX, self.costY, 0)
        graphics.drawString(self.PERCENT, self.percentCompleteX2, self.costY, 0)
        self.getAnimationInterface().paintXY(graphics, self.imageX, self.y)
    

    def setRtsLayer(self, rtsLayer: RTSLayer) -> None:
        self.rtsLayer = rtsLayer
    

    def getRtsLayer(self) -> CollidableDestroyableDamageableLayer:
        return self.rtsLayer
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.logic.java.character.CharArrayFactory import CharArrayFactory
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
from org.allbinary.input.motion.button.CommonButtons import CommonButtons


UpgradableRTSLayerHudPaintable.instance = UpgradableRTSLayerHudPaintable()

