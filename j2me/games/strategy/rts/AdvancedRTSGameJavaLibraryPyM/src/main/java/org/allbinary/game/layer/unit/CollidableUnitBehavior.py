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
# package org.allbinary.game.layer.unit

from __future__ import annotations

from org.allbinary.game.layer.CollidableRTSBehavior import CollidableRTSBehavior


class CollidableUnitBehavior(CollidableRTSBehavior):
    class SimpleSteeringVisitor(SteeringVisitor):

        def __init__(self) -> None:
            super().__init__()
        

        def visit(self, anyType: object) -> object:
            logUtil: LogUtil = LogUtil.getInstance()
            try:
                ownerLayer: CollidableCompositeLayer = anyType
                if self.getList().size() > 0:
                    allbinaryLayer: CollidableCompositeLayer = self.getList().get(0)
                    clear: bool = self.steer(ownerLayer, allbinaryLayer)
                    if clear:
                        self.getList().clear()
                        return NullUtil.getInstance().NULL_OBJECT
                    return BooleanFactory.getInstance().TRUE
                return NullUtil.getInstance().NULL_OBJECT
            except Exception as e:
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, self, "visit", e)
                return NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.layerPartialCellPositionsUtil: LayerPartialCellPositionsUtil = LayerPartialCellPositionsUtil.getInstance()
        self.simpleSteeringVisitor: SimpleSteeringVisitor = SimpleSteeringVisitor()
    

    def __init__(self, collidable: bool) -> None:
        super().__init__(collidable)
        self._init_fields()
    

    # throws Exception
    def collideNone(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> None:
        from org.allbinary.game.layer.unit.UnitLayer import UnitLayer
        self.chase(ownerLayer, collidableInterfaceCompositeInterface)
        rtsLayer: AdvancedRTSGameLayer = collidableInterfaceCompositeInterface
        if rtsLayer.getType() == UnitLayer.getStaticType():
            self.collideUnit(ownerLayer, rtsLayer)
    

    # throws Exception
    def steer(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> bool:
        ownerUnitLayer: UnitLayer = ownerLayer
        unitLayer: UnitLayer = collidableInterfaceCompositeInterface
        angleInfo2: AngleInfo = unitLayer.getRotationAnimationInterface().getAngleInfoP()
        angleInfo: AngleInfo = ownerUnitLayer.getRotationAnimationInterface().getAngleInfoP()
        angle: int = angleInfo.getAngle() - angleInfo2.getAngle()
        if angle < 90 or angle > 270:
            return True
        elif angle >= 90 or angle <= 270:
            ownerUnitLayer.getGameKeyEventList().add(GameKeyEventFactory.getInstance().getInstanceForKey(ownerUnitLayer, Canvas.RIGHT))
            return False
        raise Exception("Error")
    

    # throws Exception
    def chase(self, ownerLayer: CollidableCompositeLayer, collidableInterfaceCompositeInterface: CollidableCompositeLayer) -> None:
        from org.allbinary.game.layer.unit.UnitLayer import UnitLayer
        rtsLayer: AdvancedRTSGameLayer = collidableInterfaceCompositeInterface
        if rtsLayer.getType() == UnitLayer.getStaticType():
            if not self.simpleSteeringVisitor.getList().contains(collidableInterfaceCompositeInterface):
                self.simpleSteeringVisitor.getList().add(collidableInterfaceCompositeInterface)
            ownerUnitLayer: UnitLayer = ownerLayer
            list_: BasicArrayList = ownerUnitLayer.getUnitWaypointBehavior().getSteeringVisitorList()
            if not list_.contains(self.simpleSteeringVisitor):
                list_.add(self.simpleSteeringVisitor)
    

    # throws Exception
    def collideUnit(self, ownerLayer: CollidableCompositeLayer, unitLayer: UnitLayer) -> None:
        from org.allbinary.game.layer.unit.UnitLayer import UnitLayer
        ownerUnitLayer: UnitLayer = ownerLayer
        partialPositionList: BasicArrayList = UnitLayer.getPartialpositionlist()
        geographicMapCompositeInterface: GeographicMapCompositeInterface = ownerUnitLayer.allBinaryGameLayerManagerP
        geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
        basicGeographicMap: BasicGeographicMap = geographicMapInterface
        dropCellPositionHistory: DropCellPositionHistory = DropCellPositionHistory.getInstance()
        tiledLayerUtil: TiledLayerUtil = TiledLayerUtil.getInstance()
        tiledLayer: AllBinaryTiledLayer = basicGeographicMap.getAllBinaryTiledLayer()
        if ownerLayer.getXP() < unitLayer.getXP() and ownerLayer.getX2() > unitLayer.getXP():
            diff: int = ownerLayer.getWidth() + 1
            self.layerPartialCellPositionsUtil.getAllDXY(basicGeographicMap, ownerLayer, -diff, 0, partialPositionList)
            if not dropCellPositionHistory.anyCellPositionWithDrop(partialPositionList):
                x: int = unitLayer.getXP() - diff
                y: int = ownerLayer.getYP()
                x = tiledLayerUtil.keepOnMapX(tiledLayer, x, ownerLayer.getWidth())
                y = tiledLayerUtil.keepOnMapY(tiledLayer, y, ownerLayer.getHeight())
                ownerLayer.setPosition(x, y, ownerLayer.getZP())
            self.layerPartialCellPositionsUtil.getAllDXY(basicGeographicMap, unitLayer, diff, 0, partialPositionList)
            if not dropCellPositionHistory.anyCellPositionWithDrop(partialPositionList):
                x: int = unitLayer.getXP() + diff
                y: int = unitLayer.getYP()
                x = tiledLayerUtil.keepOnMapX(tiledLayer, x, unitLayer.getWidth())
                y = tiledLayerUtil.keepOnMapY(tiledLayer, y, unitLayer.getHeight())
                unitLayer.setPosition(x, y, unitLayer.getZP())
        if ownerLayer.getYP() < unitLayer.getYP() and ownerLayer.getY2() > unitLayer.getYP():
            diff: int = ownerLayer.getHeight() + 1
            self.layerPartialCellPositionsUtil.getAllDXY(basicGeographicMap, ownerLayer, 0, -diff, partialPositionList)
            if not dropCellPositionHistory.anyCellPositionWithDrop(partialPositionList):
                x: int = ownerLayer.getXP()
                y: int = unitLayer.getYP() - diff
                x = tiledLayerUtil.keepOnMapX(tiledLayer, x, ownerLayer.getWidth())
                y = tiledLayerUtil.keepOnMapY(tiledLayer, y, ownerLayer.getHeight())
                ownerLayer.setPosition(x, y, ownerLayer.getZP())
            self.layerPartialCellPositionsUtil.getAllDXY(basicGeographicMap, unitLayer, 0, diff, partialPositionList)
            if not dropCellPositionHistory.anyCellPositionWithDrop(partialPositionList):
                x: int = unitLayer.getXP()
                y: int = unitLayer.getYP() + diff
                x = tiledLayerUtil.keepOnMapX(tiledLayer, x, unitLayer.getWidth())
                y = tiledLayerUtil.keepOnMapY(tiledLayer, y, unitLayer.getHeight())
                unitLayer.setPosition(x, y, unitLayer.getZP())
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.layer.SteeringVisitor import SteeringVisitor
from org.allbinary.game.layer.AdvancedRTSGameLayer import AdvancedRTSGameLayer
from org.allbinary.game.layer.CollidableCompositeLayer import CollidableCompositeLayer
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
from org.allbinary.game.layer.TiledLayerUtil import TiledLayerUtil
from org.allbinary.game.layer.geographic.map.LayerPartialCellPositionsUtil import LayerPartialCellPositionsUtil
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.math.AngleInfo import AngleInfo
from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
from org.allbinary.media.graphics.geography.map.drop.DropCellPositionHistory import DropCellPositionHistory
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.game.layer.unit.SimpleSteeringVisitor import SimpleSteeringVisitor


