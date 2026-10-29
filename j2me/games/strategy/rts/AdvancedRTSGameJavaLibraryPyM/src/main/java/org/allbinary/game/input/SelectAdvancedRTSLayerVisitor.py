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
# package org.allbinary.game.input

from __future__ import annotations

from org.allbinary.logic.util.visitor.Visitor import Visitor


class SelectAdvancedRTSLayerVisitor(Visitor):

    def _init_fields(self) -> None:
        self.selectedRTSLayersPlayerGameInput: SelectedRTSLayersPlayerGameInput = None
    

    def __init__(self, selectedRTSLayersPlayerGameInput: SelectedRTSLayersPlayerGameInput) -> None:
        super().__init__()
        self._init_fields()
        self.selectedRTSLayersPlayerGameInput = selectedRTSLayersPlayerGameInput
    

    def visit(self, anyType: object) -> object:
        selectedLayer: CollidableDestroyableDamageableLayer = anyType
        if selectedLayer != CollidableDestroyableDamageableLayer.getNullInstance() and selectedLayer.getType() == BuildingLayer.getStaticType():
            rtsGameLayer: AdvancedRTSGameLayer = selectedLayer
            assignWaypointsUtil: AssignWaypointsUtil = AssignWaypointsUtil.getInstance()
            list_: BasicArrayList = self.selectedRTSLayersPlayerGameInput.getSelectedBasicArrayList()
            currentRTSLayer: RTSLayer = None
            unitLayer: UnitLayer = None
            for index in range(list_.size() - 1, 0 - 1, -1):
                currentRTSLayer = list_.get(index)
                if currentRTSLayer.getType() == UnitLayer.getStaticType():
                    unitLayer = currentRTSLayer
                    unitLayer.setParentLayer(rtsGameLayer)
                    assignWaypointsUtil.set(unitLayer, rtsGameLayer)
        return NullUtil.getInstance().NULL_OBJECT
from org.allbinary.game.input.form.AssignWaypointsUtil import AssignWaypointsUtil
from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
from org.allbinary.game.layer.RTSLayer import RTSLayer
from org.allbinary.game.layer.building.BuildingLayer import BuildingLayer
from org.allbinary.game.layer.special.CollidableDestroyableDamageableLayer import CollidableDestroyableDamageableLayer
from org.allbinary.game.layer.unit.UnitLayer import UnitLayer
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.util.BasicArrayList import BasicArrayList


