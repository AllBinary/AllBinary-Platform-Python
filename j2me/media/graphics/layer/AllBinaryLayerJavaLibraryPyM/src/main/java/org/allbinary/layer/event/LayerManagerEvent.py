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
# package org.allbinary.layer.event

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class LayerManagerEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.layerInterface: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
        self.crud: str = None
    

    def __init__(self, layerManager: LayerManager, crud: str) -> None:
        super().__init__(layerManager)
        self._init_fields()
        self.crud = crud
    

    def getLayerInterface(self) -> AllBinaryLayer:
        return self.layerInterface
    

    def setLayerInterface(self, layerInterface: AllBinaryLayer) -> None:
        self.layerInterface = layerInterface
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("LayerManagerEvent: \n")
        stringBuffer.append("LayerInterface: ")
        stringBuffer.append(str(self.getLayerInterface()))
        stringBuffer.append("\nCRUD: ")
        stringBuffer.append(self.crud)
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.LayerManager import LayerManager
from org.allbinary.logic.string.StringMaker import StringMaker


