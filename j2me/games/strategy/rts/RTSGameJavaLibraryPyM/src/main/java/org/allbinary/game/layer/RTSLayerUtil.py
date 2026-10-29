# 
# AllBinary Open License Version 1 
# Copyright (c) 2003 AllBinary 
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



class RTSLayerUtil:
    instance: RTSLayerUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.groupCommonFactory: GroupCommonFactory = GroupCommonFactory.getInstance()
        self.MAX_RELOAD_TIME: int = int(int(2147483647) / 100000)

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RTSLayerUtil:
        return RTSLayerUtil.instance
    

    def createWeaponProperties(self, weaponProperties: WeaponProperties, currentLevel: int, lastLevel: int) -> WeaponProperties:
        reloadTime: int = weaponProperties.getReloadTime()
        if lastLevel > currentLevel:
            reloadTime = reloadTime + 50
        elif lastLevel < currentLevel:
            reloadTime = reloadTime - 50
        newWeaponProperties: WeaponProperties = WeaponProperties(reloadTime, weaponProperties.getTargetingTime(), weaponProperties.getSpeed().getUnscaled(), weaponProperties.getDamage() / lastLevel * currentLevel, weaponProperties.getDissipation())
        return newWeaponProperties
    

    def downgrade(self, rtsLayer: RTSLayer) -> None:
        rtsLayer.setLevel(rtsLayer.getLevel() - 1)
        partInterfaceArray: list[PartInterface] = rtsLayer.getPartInterfaceArray()
        size: int = len(partInterfaceArray)
        partInterface: BasicWeaponPart = None
        index = size
        while (index := index - 1) >= 0:
            partInterface = partInterfaceArray[index]
            partInterface.setWeaponProperties(self.createWeaponProperties(partInterface.getWeaponProperties(), rtsLayer.getLevel(), rtsLayer.getLevel() + 1))
        rtsLayer.select()
    

    def upgrade(self, rtsLayer: RTSLayer) -> None:
        rtsLayer.setLevel(rtsLayer.getLevel() + 1)
        partInterfaceArray: list[PartInterface] = rtsLayer.getPartInterfaceArray()
        size: int = len(partInterfaceArray)
        partInterface: BasicWeaponPart = None
        index = size
        while (index := index - 1) >= 0:
            partInterface = partInterfaceArray[index]
            partInterface.setWeaponProperties(self.createWeaponProperties(partInterface.getWeaponProperties(), rtsLayer.getLevel(), rtsLayer.getLevel() - 1))
        rtsLayer.select()
    

    def getCostExponential(self, cost: int) -> int:
        return (int((cost * cost * cost) / (cost * 1000)))
    

    def getWeaponPropertiesCost(self, weaponProperties: WeaponProperties) -> int:
        cost: int = (weaponProperties.getDamage() + weaponProperties.getRange() + ((self.MAX_RELOAD_TIME / weaponProperties.getReloadTime()) >> 1))
        cost = self.getCostExponential(cost)
        return cost
    

    def getCost(self, rtsLayer: RTSLayer) -> int:
        total: int = 0
        partInterfaceArray: list[PartInterface] = rtsLayer.getPartInterfaceArray()
        size: int = len(partInterfaceArray)
        partInterface: BasicWeaponPart = None
        weaponProperties: WeaponProperties = None
        for index in range(size - 1, 0 - 1, -1):
            partInterface = partInterfaceArray[index]
            weaponProperties = partInterface.getWeaponProperties()
            total += self.getWeaponPropertiesCost(weaponProperties)
        return total
    

    def getDowngradeCost(self, rtsLayer: RTSLayer) -> int:
        partInterfaceArray: list[PartInterface] = rtsLayer.getPartInterfaceArray()
        size: int = len(partInterfaceArray)
        downgradeCost: int = 0
        partInterface: BasicWeaponPart = None
        weaponProperties: WeaponProperties = None
        downgradeWeaponCost: int = 0
        currentWeaponCost: int = 0
        for index in range(size - 1, 0 - 1, -1):
            partInterface = partInterfaceArray[index]
            weaponProperties = partInterface.getWeaponProperties()
            downgradeWeaponCost = self.getWeaponPropertiesCost(self.createWeaponProperties(weaponProperties, rtsLayer.getLevel() - 1, rtsLayer.getLevel()))
            currentWeaponCost = self.getWeaponPropertiesCost(weaponProperties)
            downgradeCost += (currentWeaponCost - downgradeWeaponCost)
        downgradeCost = int(downgradeCost * 9 / 10)
        self.logUtil.putF(str(StringMaker().append("Total Cost: ").appendint(downgradeCost)), self, "getDowngradeCost")
        return downgradeCost
    

    def getUpgradeCost(self, rtsLayer: RTSLayer) -> int:
        upgradeCost: int = 0
        partInterfaceArray: list[PartInterface] = rtsLayer.getPartInterfaceArray()
        size: int = len(partInterfaceArray)
        partInterface: BasicWeaponPart = None
        weaponProperties: WeaponProperties = None
        upgradedWeaponCost: int = 0
        currentWeaponCost: int = 0
        for index in range(size - 1, 0 - 1, -1):
            partInterface = partInterfaceArray[index]
            weaponProperties = partInterface.getWeaponProperties()
            upgradedWeaponCost = self.getWeaponPropertiesCost(self.createWeaponProperties(weaponProperties, rtsLayer.getLevel() + 1, rtsLayer.getLevel()))
            currentWeaponCost = self.getWeaponPropertiesCost(weaponProperties)
            upgradeCost += (upgradedWeaponCost - currentWeaponCost)
        self.logUtil.putF(str(StringMaker().append("Total Cost: ").appendint(upgradeCost)), self, "getUpgradeCost")
        return upgradeCost
    

    # throws Exception
    def destroyAndClear(self, list_: BasicArrayList) -> None:
        rtsLayer: RTSLayer = None
        for index in range(list_.size() - 1, 0 - 1, -1):
            rtsLayer = list_.get(index)
            rtsLayer.setDestroyed(True)
        list_.clear()
    

    def createFakeRTSLayerHashtable(self, baseRaceTrackGeographicMap: BaseRaceTrackGeographicMap) -> ABHashtable[object, object]:
        from org.allbinary.game.layer.FakeLayerManager import FakeLayerManager
        from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager
        hashtable: ABHashtable[object, object] = StdUtil.getInstance().createHashtable()
        layerManager: FakeLayerManager = FakeLayerManager(GameInfo.NONE)
        layerManager.setGeographicMapInterface([baseRaceTrackGeographicMap])
        hashtable.put(AllBinaryGameLayerManager.ID, layerManager)
        hashtable.put(DirectionFactory.getInstance().NAME, DirectionFactory.getInstance().LEFT)
        hashtable.put(self.groupCommonFactory.ID, BasicGroupFactory.getInstance().NONE_ARRAY)
        return hashtable
from org.allbinary.game.identification.GroupCommonFactory import GroupCommonFactory
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.direction.DirectionFactory import DirectionFactory
from org.allbinary.game.GameInfo import GameInfo
from org.allbinary.game.combat.weapon.WeaponProperties import WeaponProperties
from org.allbinary.game.identification.BasicGroupFactory import BasicGroupFactory
from org.allbinary.game.part.PartInterface import PartInterface
from org.allbinary.game.part.weapon.BasicWeaponPart import BasicWeaponPart
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.racetrack.BaseRaceTrackGeographicMap import BaseRaceTrackGeographicMap
from org.allbinary.util.ABHashtable import ABHashtable


RTSLayerUtil.instance = RTSLayerUtil()

