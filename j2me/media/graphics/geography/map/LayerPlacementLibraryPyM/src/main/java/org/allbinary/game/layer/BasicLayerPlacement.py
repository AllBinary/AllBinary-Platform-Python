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
# package org.allbinary.game.layer

from __future__ import annotations



class BasicLayerPlacement:

    def _init_fields(self) -> None:
        self.layerType: LayerPlacementType = None
        self.width: int = None
        self.height: int = None
    

    def __init__(self, layerType: LayerPlacementType, width: int, height: int) -> None:
        self._init_fields()
        self.layerType = layerType
        self.width = width
        self.height = height
    

    def getWidth(self) -> int:
        return self.width
    

    def getHeight(self) -> int:
        return self.height
    

    def getLayerType(self) -> LayerPlacementType:
        return self.layerType
    

    def setLayerType(self, layerType: LayerPlacementType) -> None:
        self.layerType = layerType


