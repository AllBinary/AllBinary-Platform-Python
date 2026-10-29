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
# package org.allbinary.media.graphics.geography.map.drop

from __future__ import annotations

from org.allbinary.media.graphics.geography.map.drop.DropCellPositionGeneratorInterface import DropCellPositionGeneratorInterface


class BaseDropCellPositionGenerator(DropCellPositionGeneratorInterface):
    

    def getName(self) -> str:
        return type(self).__module__ + "." + type(self).__qualname__
    

    # throws Exception
    def update(self, allBinaryGameLayerManager: AllBinaryGameLayerManager, geographicMapInterface: BasicGeographicMap) -> None:
        pass
    

    # throws Exception
    def isDropAllowedAt(self, geographicMapCellPosition: GeographicMapCellPosition) -> bool:
        return True
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        pass
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap


