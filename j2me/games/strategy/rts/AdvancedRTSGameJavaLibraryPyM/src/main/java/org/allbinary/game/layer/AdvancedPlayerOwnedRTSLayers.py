# 
# AllBinary Open License Version 1 
# Copyright (c) 2006 AllBinary 
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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.layer.PlayerOwnedRTSLayers import PlayerOwnedRTSLayers


@java_inherited_overloads
class AdvancedPlayerOwnedRTSLayers(PlayerOwnedRTSLayers):
    def _java_defaults(self):
        vars(self).setdefault("unitsList", None)
        vars(self).setdefault("waypointsList", None)
        vars(self).setdefault("buildingList", None)
        vars(self).setdefault("baseList", None)
        vars(self).setdefault("garrisonList", None)
        vars(self).setdefault("houseList", None)
        vars(self).setdefault("labList", None)
        vars(self).setdefault("factoryList", None)

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.unitsList: BasicArrayList = BasicArrayListD()
        self.waypointsList: BasicArrayList = BasicArrayListD()
        self.buildingList: BasicArrayList = BasicArrayListD()
        self.baseList: BasicArrayList = BasicArrayListD()
        self.garrisonList: BasicArrayList = BasicArrayListD()
        self.houseList: BasicArrayList = BasicArrayListD()
        self.labList: BasicArrayList = BasicArrayListD()
        self.factoryList: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def addUnit(self, rtsLayer: RTSLayer) -> None:
        self.unitsList.add(rtsLayer)
        self.rtsLayerList.add(rtsLayer)
    

    def addWaypoint(self, rtsLayer: RTSLayer) -> None:
        self.waypointsList.add(rtsLayer)
        self.rtsLayerList.add(rtsLayer)
    

    def addBase(self, rtsLayer: RTSLayer) -> None:
        self.baseList.add(rtsLayer)
        self.buildingList.add(rtsLayer)
        self.rtsLayerList.add(rtsLayer)
    

    def addGarrison(self, rtsLayer: RTSLayer) -> None:
        self.garrisonList.add(rtsLayer)
        self.buildingList.add(rtsLayer)
        self.rtsLayerList.add(rtsLayer)
    

    def addHouse(self, rtsLayer: RTSLayer) -> None:
        self.houseList.add(rtsLayer)
        self.buildingList.add(rtsLayer)
        self.rtsLayerList.add(rtsLayer)
    

    def addLab(self, rtsLayer: RTSLayer) -> None:
        self.labList.add(rtsLayer)
        self.buildingList.add(rtsLayer)
        self.rtsLayerList.add(rtsLayer)
    

    def addFactory(self, rtsLayer: RTSLayer) -> None:
        self.factoryList.add(rtsLayer)
        self.buildingList.add(rtsLayer)
        self.rtsLayerList.add(rtsLayer)
    

    def removeUnit(self, gameLayer: AllBinaryGameLayer) -> None:
        self.unitsList.remove(gameLayer)
        self.rtsLayerList.remove(gameLayer)
    

    def removeWaypoint(self, gameLayer: AllBinaryGameLayer) -> None:
        self.waypointsList.remove(gameLayer)
        self.rtsLayerList.remove(gameLayer)
    

    def getUnitsList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.unitsList
    

    def getWaypointsList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.waypointsList
    

    def getBaseList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.baseList
    

    def getGarrisonList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.garrisonList
    

    def getHouseList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.houseList
    

    def getLabList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.labList
    

    def getFactoryList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.factoryList
    

    def getTotalBuildings(self) -> int:
        return self.baseList.size() + self.garrisonList.size() + self.houseList.size() + self.labList.size() + self.factoryList.size()
    

    def removeBuilding(self, layerInterface: AllBinaryGameLayer) -> None:
        self.buildingList.add(layerInterface)
        if self.getBaseList().remove(layerInterface):
            self.rtsLayerList.remove(layerInterface)
        elif self.getFactoryList().remove(layerInterface):
            self.rtsLayerList.remove(layerInterface)
        elif self.getGarrisonList().remove(layerInterface):
            self.rtsLayerList.remove(layerInterface)
        elif self.getLabList().remove(layerInterface):
            self.rtsLayerList.remove(layerInterface)
        elif self.getHouseList().remove(layerInterface):
            self.rtsLayerList.remove(layerInterface)
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(java_super_call(super(), "toString"))
        stringBuffer.append(" Bases: ")
        stringBuffer.appendint(self.getBaseList().size())
        stringBuffer.append(" Factory: ")
        stringBuffer.appendint(self.getFactoryList().size())
        stringBuffer.append(" Garrison: ")
        stringBuffer.appendint(self.getGarrisonList().size())
        stringBuffer.append(" Labs: ")
        stringBuffer.appendint(self.getLabList().size())
        stringBuffer.append(" Houses: ")
        stringBuffer.appendint(self.getHouseList().size())
        stringBuffer.append(" Waypoints: ")
        stringBuffer.appendint(self.getWaypointsList().size())
        stringBuffer.append(" Units: ")
        stringBuffer.appendint(self.getUnitsList().size())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
    

    def getBuildingList(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.buildingList
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


