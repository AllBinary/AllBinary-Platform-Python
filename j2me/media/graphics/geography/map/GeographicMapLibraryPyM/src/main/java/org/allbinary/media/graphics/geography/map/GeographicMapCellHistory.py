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
# package org.allbinary.media.graphics.geography.map

from __future__ import annotations

from org.allbinary.graphics.font.UpdateMyFontInterface import UpdateMyFontInterface


class GeographicMapCellHistory(UpdateMyFontInterface):
    NULL_GEOGRPAHIC_MAP_HISTORY_ARRAY: list[GeographicMapCellHistory] = [None] * (0)

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        from org.allbinary.animation.Animation import Animation
        from org.allbinary.animation.AnimationBehavior import AnimationBehavior
        from org.allbinary.animation.text.TextAnimation import TextAnimation
        from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.booleanFactory: BooleanFactory = BooleanFactory.getInstance()
        self.list_: BasicArrayList = None
        self.visitedList: BasicArrayList = None
        self.MISSED_INFO: str = "Missed"
        self.animation: Animation = TextAnimation(self.MISSED_INFO, AnimationBehavior.getInstance())
        self.myFontProcessor: MyFontProcessor = UpdateMyFontProcessor(self)
        self.totalVisited: int = 0
        self.halfWidth: int = 0
        self.fontHeight: int = 0
        self.RED: int = int(BasicColorFactory.getInstance().RED)
    

    def __init__(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self._init_fields()
        self.list_ = BasicArrayListD()
        self.visitedList = BasicArrayListD()
        self.init()
    

    def updateMeasurement(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Font import Font
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
        font: Font = graphics.getFont()
        self.fontHeight = font.getHeight()
        self.myFontProcessor = MyFontProcessor.getInstance()
    

    def getTotalVisited(self) -> int:
        return self.totalVisited
    

    def getTotalNotVisited(self) -> int:
        return self.getSize() - self.totalVisited
    

    def getSize(self) -> int:
        return self.list_.size()
    

    def trackAll(self, list_: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        size: int = list_.size()
        self.list_.ensureCapacity(size)
        self.visitedList.ensureCapacity(size)
        geographicMapCellPosition: GeographicMapCellPosition = None
        for index in range(0, size):
            geographicMapCellPosition = list_.get(index)
            self.track(geographicMapCellPosition)
    

    def track(self, geographicMapCellPosition: GeographicMapCellPosition) -> None:
        if not self.list_.contains(geographicMapCellPosition):
            self.list_.add(geographicMapCellPosition)
            self.visitedList.add(self.booleanFactory.FALSE)
    

    def getTracked(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.list_
    

    def getVisited(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.visitedList
    

    def getAfterIfNotLast(self, geographicMapCellPosition: GeographicMapCellPosition) -> GeographicMapCellPosition:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        localList: BasicArrayList = self.list_
        index: int = localList.indexOf(geographicMapCellPosition)
        if localList.size() > index + 1:
            return localList.get(index + 1)
        return geographicMapCellPosition
    

    def getFirstUnvisited(self) -> GeographicMapCellPosition:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        localList: BasicArrayList = self.list_
        localVisitedList: BasicArrayList = self.visitedList
        size: int = localVisitedList.size()
        value: bool = None
        for index in range(0, size):
            value = self.visitedList.get(index)
            if value == self.booleanFactory.FALSE:
                return localList.get(index)
        return localList.get(0)
    

    def getFirstUnvisitedIndex(self) -> int:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        localVisitedList: BasicArrayList = self.visitedList
        size: int = localVisitedList.size()
        value: bool = None
        for index in range(0, size):
            value = self.visitedList.get(index)
            if value == self.booleanFactory.FALSE:
                return index
        return 0
    

    def getInPathButNotTracked(self, pathList: BasicArrayList) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        inPathButNotTrackedList: BasicArrayList = BasicArrayListD()
        localList: BasicArrayList = self.list_
        size: int = pathList.size()
        geographicMapCellPosition: GeographicMapCellPosition = None
        for index in range(0, size):
            geographicMapCellPosition = pathList.get(index)
            if not localList.contains(geographicMapCellPosition):
                inPathButNotTrackedList.add(geographicMapCellPosition)
        return inPathButNotTrackedList
    

    def isVisited(self, geographicMapCellPosition: GeographicMapCellPosition) -> bool:
        index: int = self.list_.indexOf(geographicMapCellPosition)
        if index != -1:
            value: bool = self.visitedList.get(index)
            if value == self.booleanFactory.TRUE:
                return True
        else:
            pass
        return False
    

    def visit(self, geographicMapCellPosition: GeographicMapCellPosition) -> bool:
        index: int = self.list_.indexOf(geographicMapCellPosition)
        value: bool = None
        if index != -1:
            value = self.visitedList.get(index)
            TRUE: bool = self.booleanFactory.TRUE
            if value != TRUE:
                self.visitedList.set(index, TRUE)
                self.totalVisited += 1
                return True
        else:
            pass
        return False
    

    # throws Exception
    def isAllVisited(self) -> bool:
        if self.totalVisited == self.getSize() - 1:
            return True
        else:
            return False
    

    # throws Exception
    def isAllVisited2(self) -> bool:
        if self.totalVisited == self.getSize():
            return True
        else:
            return False
    

    # throws Exception
    def isPortionVisited(self, basicDecimal: BasicDecimal) -> bool:
        from org.allbinary.logic.math.BasicDecimal import BasicDecimal
        size: int = self.getSize()
        numberRequired: int = int((size << basicDecimal.getScaledFactor()) / int(basicDecimal.getUnscaled()))
        numberNotVisited: int = self.getSize() - 1 - self.totalVisited
        if size - numberNotVisited > numberRequired:
            return True
        else:
            return False
    

    # throws Exception
    def reset(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        localVisitedList: BasicArrayList = self.visitedList
        localFalseBoolean: bool = self.booleanFactory.FALSE
        size: int = localVisitedList.size()
        for index in range(size - 1, 0 - 1, -1):
            localVisitedList.set(index, localFalseBoolean)
        self.totalVisited = 0
    

    def paintNotVisitedRelativeToPoint(self, graphics: Graphics, tiledLayer: AllBinaryTiledLayer, point: GPoint) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
        from org.allbinary.graphics.GPoint import GPoint
        x: int = point.getX() - tiledLayer.getXP()
        y: int = point.getY() - tiledLayer.getYP()
        if self.halfWidth == 0:
            self.halfWidth = (graphics.getFont().stringWidth(self.MISSED_INFO) >> 1)
        height: int = 2 * self.fontHeight
        self.animation.paintXY(graphics, x + self.halfWidth, y + (height))
    

    def paintNotVisited(self, graphics: Graphics, geographicMapInterface: BasicGeographicMap) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            self.myFontProcessor.process(graphics)
            graphics.setColor(self.RED)
            localVisitedList: BasicArrayList = self.visitedList
            size: int = localVisitedList.size()
            geographicMapCellPosition: GeographicMapCellPosition = None
            isCellVisitedBoolean: bool = None
            index = size
            while (index := index - 1) >= 0:
                geographicMapCellPosition = self.list_.get(index)
                isCellVisitedBoolean = localVisitedList.get(index)
                if not isCellVisitedBoolean:
                    self.paintNotVisitedRelativeToPoint(graphics, geographicMapInterface.getAllBinaryTiledLayer(), geographicMapCellPosition.getPoint())
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, "paintNotVisited", e)
    

    def init(self) -> None:
        self.list_.clear()
        self.visitedList.clear()
        self.totalVisited = 0
# from javax.microedition.lcdui.Font import Font
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
# from org.allbinary.animation.Animation import Animation
# from org.allbinary.animation.AnimationBehavior import AnimationBehavior
# from org.allbinary.animation.text.TextAnimation import TextAnimation
# from org.allbinary.game.layer.AllBinaryTiledLayer import AllBinaryTiledLayer
# from org.allbinary.graphics.GPoint import GPoint
# from org.allbinary.graphics.color.BasicColorFactory import BasicColorFactory
# from org.allbinary.graphics.font.MyFontProcessor import MyFontProcessor
# from org.allbinary.graphics.font.UpdateMyFontProcessor import UpdateMyFontProcessor
# from org.allbinary.logic.math.BasicDecimal import BasicDecimal


