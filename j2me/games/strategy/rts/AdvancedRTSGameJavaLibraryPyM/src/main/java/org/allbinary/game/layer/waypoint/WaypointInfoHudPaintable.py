# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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
# package org.allbinary.game.layer.waypoint

from __future__ import annotations

from org.allbinary.game.layer.SelectionHudPaintable import SelectionHudPaintable


class WaypointInfoHudPaintable(SelectionHudPaintable):

    def _init_fields(self) -> None:
        self.keyvalueDrawString: KeyValueDrawString = None
        self.rtsLayerP: PathFindingLayerInterface = NullPathFindingLayer.NULL_PATH_FINDING_LAYER
        self.textLine2Y: int = 0
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.keyvalueDrawString = KeyValueDrawString("Owner: ", self.textX)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        super().updateMeasurement(graphics)
        font: Font = graphics.getFont()
        self.textLine2Y = (self.y + font.getHeight())
    

    def updateSelectionInfo(self) -> None:
        rtsLayer: RTSLayer = self.rtsLayerP
        self.setName(rtsLayer.getName())
        self.setAnimationInterface(rtsLayer.getVerticleBuildAnimationInterface())
        self.keyvalueDrawString.update(rtsLayer.getParentLayer().getName())
    

    def setRtsLayer(self, rtsLayer: RTSLayer) -> None:
        self.rtsLayerP = rtsLayer
    

    def getRtsLayer(self) -> PathFindingLayerInterface:
        return self.rtsLayerP
    

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
        self.keyvalueDrawString.paint(graphics, self.textLine2Y)
        self.getAnimationInterface().paintXY(graphics, self.imageX, self.y)
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer
from org.allbinary.game.layer.PathFindingLayerInterface import PathFindingLayerInterface
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.graphics.draw.KeyValueDrawString import KeyValueDrawString


