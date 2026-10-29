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

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface
from org.allbinary.game.layer.SelectionHudPaintable import SelectionHudPaintable


class RTSLayerHudPaintable(SelectionHudPaintable, UpdateMyFontInterface):
    instance: RTSLayerHudPaintable = None

    def _init_fields(self) -> None:
        self.weaponProperties: list[str] = StringUtil.getInstance().getArrayInstance()
        self.rtsLayer: CollidableDestroyableDamageableLayer = CollidableDestroyableDamageableLayer.getNullInstance()
        self.costY: int = 0
        self.costY1: int = 0
        self.fontHeight: int = 0
    

    @staticmethod
    def getInstance() -> RTSLayerHudPaintable:
        return RTSLayerHudPaintable.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        super().updateMeasurement(graphics)
        font: Font = graphics.getFont()
        self.fontHeight = font.getHeight()
        self.costY1 = (self.y + ((len(self.weaponProperties) + 1) * self.fontHeight))
        if not AndroidUtil.isAndroid():
            self.costY = self.costY1
        else:
            self.costY = (self.y + ((len(self.weaponProperties) + 2) * self.fontHeight))
    

    def updateSelectionInfo(self) -> None:
        self.setName(self.getRtsLayer().getName())
        partInterface: BasicWeaponPart = self.getRtsLayer().getPartInterfaceArray()[0]
        self.weaponProperties = partInterface.getWeaponProperties().toStringArray()
        self.myFontProcessor = self.updateMyFontProcessor
    

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
        size: int = len(self.weaponProperties)
        for index in range(0, size):
            graphics.drawString(self.weaponProperties[index], self.textX, self.y + ((index + 1) * self.fontHeight), 0)
    

    def setRtsLayer(self, rtsLayer: RTSLayer) -> None:
        self.rtsLayer = rtsLayer
    

    def getRtsLayer(self) -> CollidableDestroyableDamageableLayer:
        return self.rtsLayer
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.AndroidUtil import AndroidUtil
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.game.part.weapon.BasicWeaponPart import BasicWeaponPart


RTSLayerHudPaintable.instance = RTSLayerHudPaintable()

