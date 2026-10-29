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
# package org.allbinary.input.motion.button

from __future__ import annotations

import threading


class TouchButtonRecognizer:
    _lock = threading.RLock()
    #CurrentlyPressedTouchButtonSingletonDebug.getInstance();
    class ReleaseHelper:
        _lock = threading.RLock()

        def _init_fields(self) -> None:
            self.touchButtonRecognizer: TouchButtonRecognizer = None
        

        def __init__(self, touchButtonRecognizer: TouchButtonRecognizer) -> None:
            self._init_fields()
            self.touchButtonRecognizer = touchButtonRecognizer
        

        # throws Exception
        def release(self, touchButtonInput: TouchButtonInput, deviceId: int) -> None:
            nextTouchButtonInput: TouchButtonInput = None
            gameKeyEvent: GameKeyEvent = None
            for index in range(self.touchButtonRecognizer.currentlyPressedTouchButtonSingleton.size() - 1, 0 - 1, -1):
                nextTouchButtonInput = self.touchButtonRecognizer.currentlyPressedTouchButtonSingleton.get(index)
                gameKeyEvent = nextTouchButtonInput.getGameKeyEvent()
                self.touchButtonRecognizer.upGameKeyEventHandler.fireEvent(gameKeyEvent)
                self.touchButtonRecognizer.upGameKeyEventHandler.getInstanceForDevice(deviceId).fireEvent(gameKeyEvent)
                self.touchButtonRecognizer.currentlyPressedTouchButtonSingleton.removeAt(index)
    class MultitouchReleaseHelper(ReleaseHelper):
        _lock = threading.RLock()
        

        def __init__(self, touchButtonRecognizer: TouchButtonRecognizer) -> None:
            super().__init__(touchButtonRecognizer)
        

        # throws Exception
        def release(self, touchButtonInput: TouchButtonInput, deviceId: int) -> None:
            from org.allbinary.input.motion.button.CancelTouchButtonInputFactory import CancelTouchButtonInputFactory
            cancelTouchButtonInput: TouchButtonInput = CancelTouchButtonInputFactory.getInstance().getCancel(touchButtonInput)
            nextTouchButtonInput: TouchButtonInput = None
            gameKeyEvent: GameKeyEvent = None
            for index in range(self.touchButtonRecognizer.currentlyPressedTouchButtonSingleton.size() - 1, 0 - 1, -1):
                nextTouchButtonInput = self.touchButtonRecognizer.currentlyPressedTouchButtonSingleton.get(index)
                if cancelTouchButtonInput == nextTouchButtonInput:
                    gameKeyEvent = nextTouchButtonInput.getGameKeyEvent()
                    self.touchButtonRecognizer.upGameKeyEventHandler.fireEvent(gameKeyEvent)
                    self.touchButtonRecognizer.upGameKeyEventHandler.getInstanceForDevice(deviceId).fireEvent(gameKeyEvent)
                    self.touchButtonRecognizer.currentlyPressedTouchButtonSingleton.removeAt(index)

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.rectangleCollisionUtil: RectangleCollisionUtil = RectangleCollisionUtil.getInstance()
        self.upGameKeyEventHandler: UpGameKeyEventHandler = UpGameKeyEventHandler.getInstance()
        self.downGameKeyEventHandler: DownGameKeyEventHandler = DownGameKeyEventHandler.getInstance()
        self.lastPressedTouchButtonInput: TouchButtonInput = BasicTouchInputFactory.getInstance().NONE
        self.currentlyPressedTouchButtonSingleton: CurrentlyPressedTouchButtonSingleton = CurrentlyPressedTouchButtonSingleton.getInstance()
        self.releaseHelper: ReleaseHelper = None
    

    def __init__(self) -> None:
        from org.allbinary.input.motion.button.TouchScreenFactory import TouchScreenFactory
        from org.allbinary.input.motion.button.ReleaseHelper import ReleaseHelper
        from org.allbinary.input.motion.button.MultitouchReleaseHelper import MultitouchReleaseHelper
        self._init_fields()
        if TouchScreenFactory.getInstance().isMultiTouch():
            self.releaseHelper = MultitouchReleaseHelper(self)
        else:
            self.releaseHelper = ReleaseHelper(self)
    

    # throws Exception
    def processRelease(self, touchButtonInput: TouchButtonInput, deviceId: int) -> None:
        self.releaseHelper.release(touchButtonInput, deviceId)
        gameKeyEvent: GameKeyEvent = touchButtonInput.getGameKeyEvent()
        self.upGameKeyEventHandler.fireEvent(gameKeyEvent)
        self.upGameKeyEventHandler.getInstanceForDevice(deviceId).fireEvent(gameKeyEvent)
        self.currentlyPressedTouchButtonSingleton.remove(touchButtonInput)
    

    # throws Exception
    def releaseTouchButtonInput(self, x: int, y: int, deviceId: int) -> bool:
        with self._lock:
            return self._releaseTouchButtonInput_unlocked(x, y, deviceId)

    def _releaseTouchButtonInput_unlocked(self, x: int, y: int, deviceId: int) -> bool:
        from org.allbinary.input.motion.button.TouchButtonFactory import TouchButtonFactory
        from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
        touchButtonInput: TouchButtonInput = self.lastPressedTouchButtonInput
        if self.currentlyPressedTouchButtonSingleton.contains(touchButtonInput):
            self.lastPressedTouchButtonInput = BasicTouchInputFactory.getInstance().NONE
            self.processRelease(touchButtonInput, deviceId)
            return True
        else:
            list_: BasicArrayList = TouchButtonFactory.getInstance().getList()
            rectangle: Rectangle = None
            point: GPoint = None
            touchButton: TouchButton = None
            for index in range(list_.size() - 1, 0 - 1, -1):
                touchButton = list_.objectArray[index]
                rectangle = touchButton.getRectangle()
                point = rectangle.getPoint()
                if self.rectangleCollisionUtil.isInside(point.getX(), point.getY(), rectangle.getMaxX(), rectangle.getMaxY(), x, y):
                    touchButtonInput = touchButton.getTouchButtonInput()
                    self.processRelease(touchButtonInput, deviceId)
                    return True
        return False
    

    # throws Exception
    def pressTouchButtonInput(self, x: int, y: int, deviceId: int) -> bool:
        with self._lock:
            return self._pressTouchButtonInput_unlocked(x, y, deviceId)

    def _pressTouchButtonInput_unlocked(self, x: int, y: int, deviceId: int) -> bool:
        from org.allbinary.input.motion.button.TouchButtonFactory import TouchButtonFactory
        list_: BasicArrayList = TouchButtonFactory.getInstance().getList()
        rectangle: Rectangle = None
        point: GPoint = None
        touchButton: TouchButton = None
        touchButtonInput: TouchButtonInput = None
        gameKeyEvent: GameKeyEvent = None
        for index in range(list_.size() - 1, 0 - 1, -1):
            touchButton = list_.objectArray[index]
            rectangle = touchButton.getRectangle()
            point = rectangle.getPoint()
            if self.rectangleCollisionUtil.isInside(point.getX(), point.getY(), rectangle.getMaxX(), rectangle.getMaxY(), x, y):
                touchButtonInput = touchButton.getTouchButtonInput()
                if not self.currentlyPressedTouchButtonSingleton.contains(touchButtonInput):
                    self.releaseHelper.release(touchButtonInput, deviceId)
                    self.lastPressedTouchButtonInput = touchButtonInput
                    self.currentlyPressedTouchButtonSingleton.add(touchButtonInput)
                    gameKeyEvent = touchButtonInput.getGameKeyEvent()
                    self.downGameKeyEventHandler.fireEvent(gameKeyEvent)
                    self.downGameKeyEventHandler.getInstanceForDevice(deviceId).fireEvent(gameKeyEvent)
                return True
        return False
from org.allbinary.game.input.event.DownGameKeyEventHandler import DownGameKeyEventHandler
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.UpGameKeyEventHandler import UpGameKeyEventHandler
from org.allbinary.graphics.GPoint import GPoint
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.math.RectangleCollisionUtil import RectangleCollisionUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
from org.allbinary.input.motion.button.CurrentlyPressedTouchButtonSingleton import CurrentlyPressedTouchButtonSingleton


