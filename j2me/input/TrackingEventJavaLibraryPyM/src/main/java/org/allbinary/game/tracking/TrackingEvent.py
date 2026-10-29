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
# package org.allbinary.game.tracking

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class TrackingEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.layerInterface: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
    

    def __init__(self, allBinaryLayerInterface: object) -> None:
        from org.allbinary.game.tracking.TrackingEventHandler import TrackingEventHandler
        super().__init__(allBinaryLayerInterface)
        self._init_fields()
        if allBinaryLayerInterface != TrackingEventHandler.getInstance():
            self.setLayerInterface(allBinaryLayerInterface)
    

    def init(self, anyType: object) -> None:
        self.setSource(anyType)
    

    def getLayerInterface(self) -> AllBinaryLayer:
        return self.layerInterface
    

    def setLayerInterface(self, layerInterface: AllBinaryLayer) -> None:
        self.layerInterface = layerInterface
    

    def setLayerInterfaceForCircularStaticPool(self, layerInterface: AllBinaryLayer) -> None:
        self.layerInterface = layerInterface
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("TrackingEvent: \n")
        stringBuffer.append("LayerInterface: ")
        stringBuffer.append(str(self.layerInterface))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.string.StringMaker import StringMaker


