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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


@java_inherited_overloads
class RTSLayerEvent(AllBinaryEventObject):
    def _java_defaults(self):
        vars(self).setdefault("rtsLayer", None)

    def _init_fields(self) -> None:
        self.rtsLayer: PathFindingLayerInterface = NullPathFindingLayer.NULL_PATH_FINDING_LAYER
    

    def __init__(self, rtsLayer: PathFindingLayerInterface) -> None:
        __class__._java_defaults(self)
        super().__init__(rtsLayer)
        __class__._init_fields(self)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
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
# from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.game.layer.NullPathFindingLayer import NullPathFindingLayer


