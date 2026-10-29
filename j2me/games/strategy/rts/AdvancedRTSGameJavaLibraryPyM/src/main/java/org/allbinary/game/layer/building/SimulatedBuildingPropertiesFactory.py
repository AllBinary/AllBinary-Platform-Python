# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.game.layer.building

from __future__ import annotations

from org.allbinary.game.layer.building.BuildingPropertiesFactory import BuildingPropertiesFactory


class SimulatedBuildingPropertiesFactory(BuildingPropertiesFactory):
    instanceC: SimulatedBuildingPropertiesFactory = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> SimulatedBuildingPropertiesFactory:
        return SimulatedBuildingPropertiesFactory.instanceC
    

    def getEfficiencyPerLevel(self, buildingLayer: BuildingLayer) -> int:
        return 0
    

    def getDamageFloaters(self, buildingLayer: BuildingLayer) -> DamageFloaters:
        damageFloaters: DamageFloaters = DamageFloaters.getInstance()
        self.damageFloatersPaintableInterface = damageFloaters
        return damageFloaters
    

    # throws Exception
    def getHealthBar(self, buildingLayer: BuildingLayer) -> Paintable:
        return NullPaintable.getInstance()
    

    def getHashtable(self) -> ABHashtable[object, object]:
        return StdUtil.getInstance().NULL_TABLE
    

    def getTrackingEvent(self, buildingLayer: BuildingLayer) -> TrackingEvent:
        return TrackingEvent(TrackingEventHandler.getInstance())
from org.allbinary.game.combat.damage.DamageFloaters import DamageFloaters
from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
from org.allbinary.game.tracking.TrackingEventHandler import TrackingEventHandler
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable


SimulatedBuildingPropertiesFactory.instanceC = SimulatedBuildingPropertiesFactory()

