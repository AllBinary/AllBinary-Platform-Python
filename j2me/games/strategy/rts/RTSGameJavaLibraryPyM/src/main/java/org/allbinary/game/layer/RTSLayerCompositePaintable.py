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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.graphics.paint.Paintable import Paintable


@java_inherited_overloads
class RTSLayerCompositePaintable(Paintable):
    def _java_defaults(self):
        vars(self).setdefault("upgradeCost", None)
        vars(self).setdefault("downGradeCost", None)
        vars(self).setdefault("UPGRADE", None)
        vars(self).setdefault("DOWNGRADE", None)
        vars(self).setdefault("upgradableRTSLayerHudPaintable", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.upgradeCost: str = StringUtil.getInstance().EMPTY_STRING
        self.downGradeCost: str = StringUtil.getInstance().EMPTY_STRING
        self.UPGRADE: str = "Up: $"
        self.DOWNGRADE: str = "Down: $-"
        if "upgradableRTSLayerHudPaintable" not in vars(self): self.upgradableRTSLayerHudPaintable: UpgradableRTSLayerHudPaintable = None
    

    def __init__(self, upgradableRTSLayerHudPaintable: UpgradableRTSLayerHudPaintable) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.upgradableRTSLayerHudPaintable = upgradableRTSLayerHudPaintable
    

    def update(self, rtsLayer: RTSLayer) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        if java_predicate(rtsLayer, "isUpgradeable"):
            self.setUpgradeCost(str(StringMaker().append(self.UPGRADE).appendint(int(rtsLayer.getUpgradeCost()))))
        else:
            self.setUpgradeCost(StringUtil.getInstance().EMPTY_STRING)
        if java_predicate(rtsLayer, "isDowngradeable"):
            self.setDownGradeCost(str(StringMaker().append(self.DOWNGRADE).appendint(int(rtsLayer.getDowngradeCost()))))
        else:
            self.setDownGradeCost(StringUtil.getInstance().EMPTY_STRING)
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
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
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringMaker import StringMaker


