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
# package org.allbinary.game.layer.geological.resources

from __future__ import annotations

from org.allbinary.game.layer.waypoint.WaypointInfoHudPaintable import WaypointInfoHudPaintable


class GeologicalResourceInfoHudPaintable(WaypointInfoHudPaintable):
    RESOURCES: str = "Resources: "

    def _init_fields(self) -> None:
        self.keyvalueDrawString: KeyValueDrawCharArray = None
        self.fontHeight: int = 0
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.keyvalueDrawString = KeyValueDrawCharArray(GeologicalResourceInfoHudPaintable.RESOURCES, self.textX)
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        super().updateMeasurement(graphics)
        font: Font = graphics.getFont()
        self.fontHeight = (2 * font.getHeight())
    

    def updateSelectionInfo(self) -> None:
        super().updateSelectionInfo()
        rtsLayer: RTSLayer = self.rtsLayerP
        list_: BasicArrayList = rtsLayer.geographicMapCellPositionAreaBase.getOccupyingGeographicMapCellPositionList()
        total: int = 0
        index = list_.size()
        while (index := index - 1) >= 0:
            geographicMapCellPosition: GeologicalGeographicMapCellPosition = list_.get(index)
            total += geographicMapCellPosition.getGeologicalResource().getTotal()
        self.keyvalueDrawString.update(self.getPrimitiveLongUtil().getCharArray(total), self.getPrimitiveLongUtil().getCurrentTotalDigits())
    

    def paint(self, graphics: Graphics) -> None:
        super().paint(graphics)
        self.keyvalueDrawString.paint(graphics, (self.y + self.fontHeight))
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.graphics.draw.KeyValueDrawCharArray import KeyValueDrawCharArray


