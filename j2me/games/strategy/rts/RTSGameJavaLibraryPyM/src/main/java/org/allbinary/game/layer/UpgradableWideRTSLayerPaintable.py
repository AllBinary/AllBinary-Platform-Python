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

from org.allbinary.game.layer.RTSLayerCompositePaintable import RTSLayerCompositePaintable


class UpgradableWideRTSLayerPaintable(RTSLayerCompositePaintable):

    def _init_fields(self) -> None:
        self.cost: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, upgradableRTSLayerHudPaintable: UpgradableRTSLayerHudPaintable) -> None:
        super().__init__(upgradableRTSLayerHudPaintable)
        self._init_fields()
    

    def update(self, rtsLayer: RTSLayer) -> None:
        super().update(rtsLayer)
        self.setCost(str(StringMaker().append(self.getUpgradeCost()).append(CommonSeps.getInstance().SPACE).append(self.getDownGradeCost())))
    

    def paint(self, graphics: Graphics) -> None:
        graphics.drawString(self.getCost(), self.upgradableRTSLayerHudPaintable.textX, self.upgradableRTSLayerHudPaintable.costY, 0)
    

    def setCost(self, cost: str) -> None:
        self.cost = cost
    

    def getCost(self) -> str:
        return self.cost
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


