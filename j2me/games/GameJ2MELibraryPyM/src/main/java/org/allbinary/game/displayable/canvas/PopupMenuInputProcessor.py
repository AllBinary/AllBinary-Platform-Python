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
# package org.allbinary.game.displayable.canvas

from __future__ import annotations

from org.allbinary.game.displayable.canvas.BasicMenuInputProcessor import BasicMenuInputProcessor


class PopupMenuInputProcessor(BasicMenuInputProcessor):

    def _init_fields(self) -> None:
        self.rectangleCollisionUtil: RectangleCollisionUtil = RectangleCollisionUtil.getInstance()
        self.CLICK_DELAY: int = 120
        self.clickTimeHelper: TimeDelayHelper = TimeDelayHelper(self.CLICK_DELAY)
        self.rectangle: Rectangle = None
    

    def __init__(self, gameKeyEventList: BasicArrayList, playerInputId: int, gameCanvas: MyCanvas, rectangle: Rectangle) -> None:
        super().__init__(gameKeyEventList, playerInputId, gameCanvas)
        self._init_fields()
        self.rectangle = rectangle
    

    def init(self, rectangle: Rectangle) -> None:
        self.rectangle = rectangle
    

    # throws Exception
    def processInput(self, key: int) -> int:
        if key == Canvas.KEY_STAR:
            gameCanvas: AllBinaryGameCanvas = self.getCanvas()
            gameCanvas.toggleMenu()
            return 1
        return 0
    

    # throws Exception
    def processInputList(self) -> int:
        try:
            motionInputsIndex: int = self.processMotionInputs()
            list_: BasicArrayList = self.getGameKeyEventList()
            size: int = list_.size()
            key: int = 0
            gameKeyEvent: GameKeyEvent = None
            for index in range(0, size):
                gameKeyEvent = list_.objectArray[index]
                if gameKeyEvent is not None:
                    key = gameKeyEvent.getKey()
                    if self.processInput(key) == 1:
                        break
            self.clear()
            if size > 0 or motionInputsIndex >= 0:
                return 1
            else:
                return -1
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, GameInputStrings.getInstance().PROCESS_INPUT, e)
            return -1
    

    # throws Exception
    def processMotionInputs(self) -> int:
        lastIndex: int = self.motionGestureEventList.size() - 1
        if lastIndex >= 0:
            motionGestureEvent: MotionGestureEvent = self.motionGestureEventList.objectArray[lastIndex]
            self.processMotionInput(motionGestureEvent)
        self.motionGestureEventList.clear()
        return lastIndex
    

    # throws Exception
    def processMotionInput(self, motionGestureEvent: MotionGestureEvent) -> None:
        if motionGestureEvent is None:
            self.logUtil.putF("Exception: Bug", self, self.gameInputStrings.PROCESS_MOTION_INPUT)
            return
        touchMotionGestureFactory: TouchMotionGestureFactory = TouchMotionGestureFactory.getInstance()
        motionGestureInput: MotionGestureInput = motionGestureEvent.getMotionGesture()
        if motionGestureInput == touchMotionGestureFactory.RELEASED:
            point: GPoint = motionGestureEvent.getCurrentPoint()
            rectPoint: GPoint = self.rectangle.getPoint()
            if self.rectangleCollisionUtil.isInside(rectPoint.getX(), rectPoint.getY(), self.rectangle.getMaxX() + 20, self.rectangle.getMaxY(), point.getX(), point.getY()):
                if self.clickTimeHelper.isTimeTNT():
                    gameCanvas: AllBinaryGameCanvas = self.getCanvas()
                    gameCanvas.toggleMenu()
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.game.input.GameInputStrings import GameInputStrings
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.input.motion.gesture.MotionGestureInput import MotionGestureInput
from org.allbinary.input.motion.gesture.TouchMotionGestureFactory import TouchMotionGestureFactory
from org.allbinary.input.motion.gesture.observer.MotionGestureEvent import MotionGestureEvent
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.math.RectangleCollisionUtil import RectangleCollisionUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.BasicArrayList import BasicArrayList


