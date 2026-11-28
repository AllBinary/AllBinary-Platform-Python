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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.animation.Animation import Animation


@java_inherited_overloads
class PathAnimation(Animation):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("linePathAnimation", None)
        vars(self).setdefault("pathFindingLayer", None)
        vars(self).setdefault("allBinaryGameLayerManagerP", None)
        vars(self).setdefault("startColor", None)
        vars(self).setdefault("middleColor", None)
        vars(self).setdefault("endColor", None)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "linePathAnimation" not in vars(self): self.linePathAnimation: LinePathAnimation = None
        if "pathFindingLayer" not in vars(self): self.pathFindingLayer: PathFindingLayerInterface = None
        self.allBinaryGameLayerManagerP: AllBinaryGameLayerManager = AllBinaryGameLayerManager.getNullInstance()
        self.startColor: BasicColor = BasicColorFactory.getInstance().RED
        self.middleColor: BasicColor = BasicColorFactory.getInstance().BLUE
        self.endColor: BasicColor = BasicColorFactory.getInstance().GREEN
    

    def __init__(self, pathFindingLayer: PathFindingLayerInterface, linePathAnimation: LinePathAnimation) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.pathFindingLayer = pathFindingLayer
        self.linePathAnimation = linePathAnimation
    

    # throws Exception
    def setAllBinaryGameLayerManager(self, allBinaryGameLayerManager: AllBinaryGameLayerManager) -> None:
        self.allBinaryGameLayerManagerP = allBinaryGameLayerManager
    

    # throws Exception
    def nextFrame(self) -> None:
        pass
    

    def paintXY(self, graphics: Graphics, x: int, y: int) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.GPoint import GPoint
        from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
        from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
        from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
        from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
        from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
        from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
        from org.allbinary.util.BasicArrayList import BasicArrayList
        try:
            waypointBehaviorBase: WaypointBehaviorBase = self.pathFindingLayer.getWaypointBehavior()
            if waypointBehaviorBase is not None:
                geographicMapCellHistory: GeographicMapCellHistory = waypointBehaviorBase.getCurrentGeographicMapCellHistory()
                list_: BasicArrayList = geographicMapCellHistory.getTracked()
                size: int = list_.size()
                if size > 0:
                    geographicMapCompositeInterface: GeographicMapCompositeInterface = self.allBinaryGameLayerManagerP
                    geographicMapInterface: BasicGeographicMap = geographicMapCompositeInterface.getGeographicMapInterface()[0]
                    tiledLayer: AllBinaryTiledLayer = geographicMapInterface.getAllBinaryTiledLayer()
                    geographicMapCellPosition: GeographicMapCellPosition = SimpleGeographicMapCellPositionFactory.NULL_GEOGRAPHIC_MAP_CELL_POSITION
                    nextPoint: GPoint = None
                    point: GPoint = None
                    start: int = size - 2
                    for index in range(0, size - 1):
                        if index == start:
                            self.setBasicColorP(self.startColor)
                            self.basicSetColorUtil.setBasicColorP3(graphics, self.getBasicColorP(), self.getColor())
                        elif geographicMapCellHistory.isVisited(geographicMapCellPosition):
                            self.setBasicColorP(self.endColor)
                            self.basicSetColorUtil.setBasicColorP3(graphics, self.getBasicColorP(), self.getColor())
                        else:
                            self.setBasicColorP(self.middleColor)
                            self.basicSetColorUtil.setBasicColorP3(graphics, self.getBasicColorP(), self.getColor())
                        geographicMapCellPosition = list_.get(index)
                        point = geographicMapCellPosition.getMidPoint()
                        geographicMapCellPosition = list_.get(index + 1)
                        nextPoint = geographicMapCellPosition.getMidPoint()
                        self.linePathAnimation.paint(graphics, point, nextPoint, tiledLayer)
        except Exception as e:
            self.logUtil.putF("Cleared Target", self, CanvasStrings.getInstance().PAINT)
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.media.graphics.geography.map.BasicGeographicMap import BasicGeographicMap
# from org.allbinary.media.graphics.geography.map.GeographicMapCellHistory import GeographicMapCellHistory
# from org.allbinary.media.graphics.geography.map.GeographicMapCellPosition import GeographicMapCellPosition
# from org.allbinary.media.graphics.geography.map.GeographicMapCompositeInterface import GeographicMapCompositeInterface
# from org.allbinary.media.graphics.geography.map.SimpleGeographicMapCellPositionFactory import SimpleGeographicMapCellPositionFactory
# from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.game.layer.AllBinaryGameLayerManager import AllBinaryGameLayerManager


