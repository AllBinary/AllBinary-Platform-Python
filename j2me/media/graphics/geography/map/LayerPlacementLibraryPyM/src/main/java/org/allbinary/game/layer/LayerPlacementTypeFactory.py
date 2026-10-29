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



class LayerPlacementTypeFactory:
    instance: LayerPlacementTypeFactory = None

    def _init_fields(self) -> None:
        self.MAP: LayerPlacementType = LayerPlacementType(2147483647)
        self.LEFT: LayerPlacementType = LayerPlacementType(DirectionFactory.getInstance().LEFT.getValue())
        self.DOWN: LayerPlacementType = LayerPlacementType(DirectionFactory.getInstance().DOWN.getValue())
        self.UP: LayerPlacementType = LayerPlacementType(DirectionFactory.getInstance().UP.getValue())
        self.RIGHT: LayerPlacementType = LayerPlacementType(DirectionFactory.getInstance().RIGHT.getValue())

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> LayerPlacementTypeFactory:
        return LayerPlacementTypeFactory.instance
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.game.layer.LayerPlacementType import LayerPlacementType


LayerPlacementTypeFactory.instance = LayerPlacementTypeFactory()

