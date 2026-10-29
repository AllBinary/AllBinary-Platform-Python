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
# package org.allbinary.game.terrain

from __future__ import annotations

from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject


class TerrainEvent(AllBinaryEventObject):

    def _init_fields(self) -> None:
        self.basicTerrainInfo: BasicTerrainInfo = BasicTerrainInfo.NULL_BASIC_TERRAIN_INFO
    

    def __init__(self, basicTerrainInfo: object) -> None:
        super().__init__(basicTerrainInfo)
        self._init_fields()
        self.setBasicTerrainInfo(self.basicTerrainInfo)
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("TerrainEvent: \n")
        stringBuffer.append("LayerInterface: ")
        stringBuffer.append(str(self.basicTerrainInfo))
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def getBasicTerrainInfo(self) -> BasicTerrainInfo:
        return self.basicTerrainInfo
    

    def setBasicTerrainInfo(self, basicTerrainInfo: BasicTerrainInfo) -> None:
        self.basicTerrainInfo = basicTerrainInfo
    

    def setBasicTerrainInfoForCircularStaticPool(self, basicTerrainInfo: BasicTerrainInfo) -> None:
        self.basicTerrainInfo = basicTerrainInfo
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.game.terrain.BasicTerrainInfo import BasicTerrainInfo


