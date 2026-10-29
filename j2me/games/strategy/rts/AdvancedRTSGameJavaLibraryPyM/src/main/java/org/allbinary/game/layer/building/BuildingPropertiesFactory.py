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



class BuildingPropertiesFactory:
    instance: BuildingPropertiesFactory = None

    def _init_fields(self) -> None:
        self.damageFloatersPaintableInterface: Paintable = NullPaintable.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BuildingPropertiesFactory:
        return BuildingPropertiesFactory.instance
    

    def getEfficiencyPerLevel(self, buildingLayer: BuildingLayer) -> int:
        return 10000 / buildingLayer.getMaxLevel() + 10000 % buildingLayer.getMaxLevel()
    

    def getDamageFloaters(self, buildingLayer: BuildingLayer) -> DamageFloaters:
        damageFloaters: DamageFloaters = DamageFloaters.getInstance()
        if Features.getInstance().isFeature(GameFeatureFactory.getInstance().DAMAGE_FLOATERS):
            damageFloaters = PtsDamageFloaters(buildingLayer)
            self.damageFloatersPaintableInterface = damageFloaters
        else:
            damageFloaters = DamageFloaters()
        return damageFloaters
    

    # throws Exception
    def getHealthBar(self, buildingLayer: BuildingLayer) -> Paintable:
        healthBar: Paintable = NullPaintable.getInstance()
        if Features.getInstance().isFeature(GameFeatureFactory.getInstance().HEALTH_BARS):
            healthBar = HealthBar(buildingLayer, buildingLayer.getHealthInterface(), HealthBarTwodAnimation(buildingLayer, BasicHudFactory.getInstance().BOTTOMLEFT), -1)
        return healthBar
    

    def getHashtable(self) -> ABHashtable[object, object]:
        return StdUtil.getInstance().createHashtable()
    

    def getTrackingEvent(self, buildingLayer: BuildingLayer) -> TrackingEvent:
        return TrackingEvent(buildingLayer)
from org.allbinary.game.combat.damage.DamageFloaters import DamageFloaters
from org.allbinary.game.combat.damage.PtsDamageFloaters import PtsDamageFloaters
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
from org.allbinary.game.graphics.hud.BasicHudFactory import BasicHudFactory
from org.allbinary.game.health.HealthBar import HealthBar
from org.allbinary.game.health.HealthBarTwodAnimation import HealthBarTwodAnimation
from org.allbinary.game.tracking.TrackingEvent import TrackingEvent
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.Paintable import Paintable
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABHashtable import ABHashtable


BuildingPropertiesFactory.instance = BuildingPropertiesFactory()

