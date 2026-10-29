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

from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.game.layer.Aggression import Aggression


class Driver:
    NULL_DRIVER: Driver = None

    def _init_fields(self) -> None:
        self.turnSpeed: int = SmallIntegerSingletonFactory.getInstance().getAt(0)
        self.trackPathSelectionSkill: int = SmallIntegerSingletonFactory.getInstance().getAt(0)
        self.aggression: Aggression = None
    

    def __init__(self, turnSpeed: int, trackPathSelectionSkill: int, aggression: Aggression) -> None:
        self._init_fields()
        self.setTurnSpeed(turnSpeed)
        self.setTrackPathSelectionSkill(trackPathSelectionSkill)
        self.aggression = aggression
    

    def getTurnSpeed(self) -> int:
        return self.turnSpeed
    

    def setTurnSpeed(self, turnSpeed: int) -> None:
        self.turnSpeed = turnSpeed
    

    def getTrackPathSelectionSkill(self) -> int:
        return self.trackPathSelectionSkill
    

    def setTrackPathSelectionSkill(self, trackPathSelectionSkill: int) -> None:
        self.trackPathSelectionSkill = trackPathSelectionSkill
    

    def getAggression(self) -> Aggression:
        return self.aggression
    

    def setAggression(self, aggression: Aggression) -> None:
        self.aggression = aggression


Driver.NULL_DRIVER = Driver(SmallIntegerSingletonFactory.getInstance().getAt(0), SmallIntegerSingletonFactory.getInstance().getAt(0), Aggression(SmallIntegerSingletonFactory.getInstance().getAt(0), SmallIntegerSingletonFactory.getInstance().getAt(0), SmallIntegerSingletonFactory.getInstance().getAt(0)))

