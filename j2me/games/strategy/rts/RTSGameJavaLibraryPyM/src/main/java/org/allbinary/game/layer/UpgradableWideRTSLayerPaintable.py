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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.layer.RTSLayerCompositePaintable import RTSLayerCompositePaintable


@java_inherited_overloads
class UpgradableWideRTSLayerPaintable(RTSLayerCompositePaintable):
    def _java_defaults(self):
        vars(self).setdefault("cost", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.cost: str = StringUtil.getInstance().EMPTY_STRING
    

    def __init__(self, upgradableRTSLayerHudPaintable: UpgradableRTSLayerHudPaintable) -> None:
        __class__._java_defaults(self)
        super().__init__(upgradableRTSLayerHudPaintable)
        __class__._init_fields(self)
    

    def update(self, rtsLayer: RTSLayer) -> None:
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.logic.string.StringMaker import StringMaker
        java_super_call(super(), "update", rtsLayer)
        self.setCost(str(StringMaker().append(self.getUpgradeCost()).append(CommonSeps.getInstance().SPACE).append(self.getDownGradeCost())))
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        graphics.drawString(self.getCost(), self.upgradableRTSLayerHudPaintable.textX, self.upgradableRTSLayerHudPaintable.costY, 0)
    

    def setCost(self, cost: str) -> None:
        self.cost = cost
    

    def getCost(self) -> str:
        return self.cost
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil


