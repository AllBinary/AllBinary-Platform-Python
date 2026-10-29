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

from org.allbinary.graphics.paint.Paintable import Paintable


class RTSLayerCompositePaintable(Paintable):

    def _init_fields(self) -> None:
        self.upgradeCost: str = StringUtil.getInstance().EMPTY_STRING
        self.downGradeCost: str = StringUtil.getInstance().EMPTY_STRING
        self.UPGRADE: str = "Up: $"
        self.DOWNGRADE: str = "Down: $-"
        self.upgradableRTSLayerHudPaintable: UpgradableRTSLayerHudPaintable = None
    

    def __init__(self, upgradableRTSLayerHudPaintable: UpgradableRTSLayerHudPaintable) -> None:
        super().__init__()
        self._init_fields()
        self.upgradableRTSLayerHudPaintable = upgradableRTSLayerHudPaintable
    

    def update(self, rtsLayer: RTSLayer) -> None:
        if rtsLayer.isUpgradeable():
            self.setUpgradeCost(str(StringMaker().append(self.UPGRADE).appendint(int(rtsLayer.getUpgradeCost()))))
        else:
            self.setUpgradeCost(StringUtil.getInstance().EMPTY_STRING)
        if rtsLayer.isDowngradeable():
            self.setDownGradeCost(str(StringMaker().append(self.DOWNGRADE).appendint(int(rtsLayer.getDowngradeCost()))))
        else:
            self.setDownGradeCost(StringUtil.getInstance().EMPTY_STRING)
    

    def paint(self, graphics: Graphics) -> None:
        graphics.drawString(self.getDownGradeCost(), self.upgradableRTSLayerHudPaintable.textX, self.upgradableRTSLayerHudPaintable.costY1, 0)
        graphics.drawString(self.getUpgradeCost(), self.upgradableRTSLayerHudPaintable.textX, self.upgradableRTSLayerHudPaintable.costY, 0)
    

    def setUpgradeCost(self, upgradeCost: str) -> None:
        self.upgradeCost = upgradeCost
    

    def getUpgradeCost(self) -> str:
        return self.upgradeCost
    

    def setDownGradeCost(self, downGradeCost: str) -> None:
        self.downGradeCost = downGradeCost
    

    def getDownGradeCost(self) -> str:
        return self.downGradeCost
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringMaker import StringMaker


