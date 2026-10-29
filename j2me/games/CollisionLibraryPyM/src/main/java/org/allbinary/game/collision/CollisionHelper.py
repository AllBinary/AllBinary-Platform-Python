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
# package org.allbinary.game.collision

from __future__ import annotations



class CollisionHelper:

    def _init_fields(self) -> None:
        self.sourceLayerInterface: AllBinaryLayer = None
    

    def __init__(self, sourceLayerInterface: AllBinaryLayer) -> None:
        self._init_fields()
        self.sourceLayerInterface = sourceLayerInterface
    

    def isCollidable(self, layerInterface: CollidableCompositeLayer) -> bool:
        return True
    

    def getOwnerLayerInterface(self) -> AllBinaryLayer:
        return self.sourceLayerInterface
    

    def setOwnerLayerInterface(self, sourceLayerInterface: AllBinaryLayer) -> None:
        self.sourceLayerInterface = sourceLayerInterface
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer


