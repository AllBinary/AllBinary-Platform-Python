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
# package org.allbinary.game.ag.ai.scroller

from __future__ import annotations

from org.allbinary.game.ai.BasicAI import BasicAI


class FlockingAI(BasicAI):

    def _init_fields(self) -> None:
        self.allowedDistance: int = None
    

    def __init__(self, hashtable: ABHashtable[object, object], ownerLayerInterface: AllBinaryLayer, gameInput: GameInput) -> None:
        from org.allbinary.game.ag.ai.scroller.BasePatrolAI import BasePatrolAI
        super().__init__(ownerLayerInterface, gameInput)
        self._init_fields()
        allowedDistance: int = hashtable.get(BasePatrolAI.MAX_DISTANCE)
        self.allowedDistance = int(allowedDistance)
    

    # throws Exception
    def processAI(self, allBinaryLayerManager: AllBinaryLayerManager) -> None:
        maxDistance: int = 0
        farAllbinaryLayer: AllBinaryLayer = AllBinaryLayer.NULL_ALLBINARY_LAYER
        groupLayerManagerListener: GroupLayerManagerListener = GroupLayerManagerListener.getInstance()
        list_: BasicArrayList = groupLayerManagerListener.getList(BasicGroupFactory.getInstance().ENEMY)
        size: int = list_.size()
        allBinaryLayer: AllBinaryLayer = None
        ownerLayerInterface: AllBinaryLayer = None
        for index in range(0, size):
            allBinaryLayer = list_.get(index)
            if allBinaryLayer.getType() != WeaponLayer.getStaticType():
                distance: int = self.getXYDistance(allBinaryLayer)
                if distance > maxDistance:
                    maxDistance = distance
                    farAllbinaryLayer = allBinaryLayer
                    if distance > self.allowedDistance:
                        break
        if maxDistance > self.allowedDistance:
            if farAllbinaryLayer != AllBinaryLayer.NULL_ALLBINARY_LAYER:
                ownerLayerInterface = self.getOwnerLayerInterface()
                if farAllbinaryLayer.getXP() < ownerLayerInterface.getXP():
                    self.processKeyAI(Canvas.LEFT)
                elif farAllbinaryLayer.getXP() > ownerLayerInterface.getXP():
                    self.processKeyAI(Canvas.RIGHT)
                elif farAllbinaryLayer.getYP() > ownerLayerInterface.getYP():
                    self.processKeyAI(Canvas.UP)
                elif farAllbinaryLayer.getYP() < ownerLayerInterface.getYP():
                    self.processKeyAI(Canvas.DOWN)
    

    def getXYDistance(self, allBinaryLayer: AllBinaryLayer) -> int:
        ownerLayerInterface: AllBinaryLayer = self.getOwnerLayerInterface()
        xTotalDistance: int = (allBinaryLayer.getXP() + allBinaryLayer.getHalfWidth()) - (ownerLayerInterface.getXP() + ownerLayerInterface.getHalfWidth())
        yTotalDistance: int = (allBinaryLayer.getYP() + allBinaryLayer.getHalfHeight()) - (ownerLayerInterface.getYP() + ownerLayerInterface.getHalfHeight())
        mathUtil: MathUtil = MathUtil.getInstance()
        totalDistance: int = mathUtil.abs(xTotalDistance) + mathUtil.abs(yTotalDistance)
        return totalDistance
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.identification.BasicGroupFactory import BasicGroupFactory
from org.allbinary.game.input.GameInput import GameInput
from org.allbinary.game.layer.identification.GroupLayerManagerListener import GroupLayerManagerListener
from org.allbinary.game.layer.weapon.WeaponLayer import WeaponLayer
from org.allbinary.layer.AllBinaryLayer import AllBinaryLayer
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.math.MathUtil import MathUtil
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList


