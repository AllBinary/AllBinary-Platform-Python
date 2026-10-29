# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.game.behavior.topview

from __future__ import annotations



# Java interface
class TopViewCharacterInterface:
    

    def terrainMove(self, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], x: int, y: int) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def terrainEvent(self, x: int, y: int, geographicMapInterfaceArray: list[BasicGeographicMap], geographicMapCellTypeArray: list[GeographicMapCellType], geographicMapCellPosition: GeographicMapCellPosition) -> None:
        raise NotImplementedError()
    

    def move(self) -> None:
        raise NotImplementedError()
    

    def upp(self) -> None:
        raise NotImplementedError()
    

    def leftp(self) -> None:
        raise NotImplementedError()
    

    def rightp(self) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def reset(self) -> None:
        raise NotImplementedError()
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
from org.allbinary.media.graphics.geography.map.GeographicMapCellType import GeographicMapCellType


