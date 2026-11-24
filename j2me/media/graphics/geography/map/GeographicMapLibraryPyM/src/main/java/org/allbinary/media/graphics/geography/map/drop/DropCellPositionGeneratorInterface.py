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



# Java interface
class DropCellPositionGeneratorInterface:
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def update(self, allBinaryGameLayerManager: AllBinaryGameLayerManager, geographicMapInterface: BasicGeographicMap) -> None:
        from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        raise NotImplementedError()
    

    # throws Exception
    def processTick(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        raise NotImplementedError()
    

    # throws Exception
    def isDropAllowedAt(self, geographicMapCellPosition: GeographicMapCellPosition) -> bool:
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        raise NotImplementedError()
# from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition


