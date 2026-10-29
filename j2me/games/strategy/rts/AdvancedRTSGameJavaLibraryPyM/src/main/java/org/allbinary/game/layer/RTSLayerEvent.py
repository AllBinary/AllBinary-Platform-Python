# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
#  
# By agreeing to this license you and any business entity you represent are 
# legally bound to the AllBinary Open License Version 1 legal agreement. 
#  
# You may obtain the AllBinary Open License Version 1 legal agreement from 
# AllBinary or the root directory of AllBinary's AllBinary Platform repository. 
#  
# Created By: Travis Berthelot  
# Generated Code Do Not Modify
# package org.allbinary.game.layer

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class RTSLayerEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.rtsLayer: PathFindingLayerInterface = NullPathFindingLayer.NULL_PATH_FINDING_LAYER
    

    def __init__(self, rtsLayer: PathFindingLayerInterface) -> None:
        super().__init__(rtsLayer)
        self._init_fields()
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("RTSLayerEvent: \n")
        stringBuffer.append("RTSLayer: ")
        stringBuffer.append(str(self.getRtsLayer()))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def getRtsLayer(self) -> PathFindingLayerInterface:
        return self.rtsLayer
    

    def setRtsLayer(self, rtsLayer: PathFindingLayerInterface) -> None:
        self.rtsLayer = rtsLayer
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer


