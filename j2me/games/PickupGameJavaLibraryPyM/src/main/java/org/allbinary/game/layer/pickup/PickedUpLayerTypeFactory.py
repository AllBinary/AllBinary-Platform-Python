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
# package org.allbinary.game.layer.pickup

from __future__ import annotations



class PickedUpLayerTypeFactory:
    instance: PickedUpLayerTypeFactory = None

    def _init_fields(self) -> None:
        self.NONE: PickedUpLayerType = PickedUpLayerType(StringUtil.getInstance().NULL_STRING)
        self.BEAM: PickedUpLayerType = PickedUpLayerType("BEAM")
        self.MINE: PickedUpLayerType = PickedUpLayerType("MINE")
        self.PROJECTILE: PickedUpLayerType = PickedUpLayerType("PROJECTILE")
        self.ENHANCEMENT: PickedUpLayerType = PickedUpLayerType("Enhancement")
        self.MORPH: PickedUpLayerType = PickedUpLayerType("Morph")
        self.PART: PickedUpLayerType = PickedUpLayerType("Part")
        self.HEAL: PickedUpLayerType = PickedUpLayerType("Heal")
        self.LIFE: PickedUpLayerType = PickedUpLayerType("Life")
        self.POINTS: PickedUpLayerType = PickedUpLayerType("Points")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PickedUpLayerTypeFactory:
        return PickedUpLayerTypeFactory.instance
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.game.layer.pickup.PickedUpLayerType import PickedUpLayerType


PickedUpLayerTypeFactory.instance = PickedUpLayerTypeFactory()

