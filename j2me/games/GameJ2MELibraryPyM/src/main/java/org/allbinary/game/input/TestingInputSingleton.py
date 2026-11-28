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
# package org.allbinary.game.input

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
from org.allbinary.game.input.GameInputInterface import GameInputInterface


@java_inherited_overloads
class TestingInputSingleton(*java_bases(AllBinaryGameLayer, GameInputInterface)):
    instance: TestingInputSingleton = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("inputProcessorArray", None)
        vars(self).setdefault("testInputPaintable", None)

    def _init_fields(self) -> None:
        from org.allbinary.graphics.paint.NullPaintable import NullPaintable
        self.inputProcessorArray: list[GameInputProcessor] = [None] * (InputFactory.getInstance().MAX)
        self.testInputPaintable: PaintableInterface = NullPaintable.getInstance()
    

    @staticmethod
    def getInstance() -> TestingInputSingleton:
        return TestingInputSingleton.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.game.input.GameInputProcessorUtil import GameInputProcessorUtil
        from org.allbinary.graphics.RectangleFactory import RectangleFactory
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.view.ViewPosition import ViewPosition
        super().__init__(StringUtil.getInstance().EMPTY_STRING, RectangleFactory.SINGLETON, ViewPosition.getInstanceD())
        __class__._init_fields(self)
        GameInputProcessorUtil.init(self.inputProcessorArray)
    

    def initInputProcessors(self) -> None:
        pass
    

    def initInputProcessorsForTestInput(self, aTestInputInterface: TestInputInterface) -> None:
        from org.allbinary.game.input.GameInputProcessor import GameInputProcessor
        from org.allbinary.game.input.GameInputProcessor import GameInputProcessor
        from org.allbinary.game.input.GameInputProcessor import GameInputProcessor
        from org.allbinary.game.input.GameInputProcessor import GameInputProcessor
        from org.allbinary.game.input.GameInputProcessor import GameInputProcessor
        from org.allbinary.game.input.GameInputProcessor import GameInputProcessor
        from org.allbinary.game.input.GameInputProcessorUtil import GameInputProcessorUtil
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        testInputInterface: TestInputInterface = aTestInputInterface
        self.testInputPaintable = testInputInterface
        _java_listener_owner = self
        class _JavaListenerN66410(GameInputProcessor):
            
            

            # throws Exception
            def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
                from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
                from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
                testInputInterface.up()
        self.inputProcessorArray[Canvas.UP] = _JavaListenerN66410()
            
        _java_listener_owner = self
        class _JavaListenerN66558(GameInputProcessor):
            
            

            # throws Exception
            def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
                from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
                from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
                testInputInterface.down()
        self.inputProcessorArray[Canvas.DOWN] = _JavaListenerN66558()
            
        _java_listener_owner = self
        class _JavaListenerN66706(GameInputProcessor):
            
            

            # throws Exception
            def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
                from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
                from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
                testInputInterface.left()
        self.inputProcessorArray[Canvas.LEFT] = _JavaListenerN66706()
            
        _java_listener_owner = self
        class _JavaListenerN66854(GameInputProcessor):
            
            

            # throws Exception
            def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
                from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
                from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
                testInputInterface.right()
        self.inputProcessorArray[Canvas.RIGHT] = _JavaListenerN66854()
            
        _java_listener_owner = self
        class _JavaListenerN67002(GameInputProcessor):
            
            

            # throws Exception
            def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
                from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
                from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
                testInputInterface.strafeLeft()
        self.inputProcessorArray[Canvas.KEY_NUM7] = _JavaListenerN67002()
            
        _java_listener_owner = self
        class _JavaListenerN67150(GameInputProcessor):
            
            

            # throws Exception
            def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
                from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
                from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
                testInputInterface.strafeRight()
        self.inputProcessorArray[Canvas.KEY_NUM9] = _JavaListenerN67150()
            
        GameInputProcessorUtil.init(self.inputProcessorArray)
    

    # throws Exception
    def processInputList(self, allbinaryLayerManager: AllBinaryLayerManager, list_: BasicArrayList) -> None:
        with self._lock:
            return __class__.__dict__["_processInputList_unlocked"].__get__(self, __class__)(allbinaryLayerManager, list_)

    def _processInputList_unlocked(self, allbinaryLayerManager: AllBinaryLayerManager, list_: BasicArrayList) -> None:
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        from org.allbinary.util.BasicArrayList import BasicArrayList
        key: int = 0
        gameKeyEvent: GameKeyEvent = None
        size: int = list_.size()
        for index in range(0, size):
            gameKeyEvent = (list_.objectArray[index])
            key = gameKeyEvent.getKey()
            self.inputProcessorArray[key].processEvent(allbinaryLayerManager, GameKeyEvent.NONE)
    

    # throws Exception
    def processInput(self, allbinaryLayerManager: AllBinaryLayerManager) -> None:
        with self._lock:
            return __class__.__dict__["_processInput_unlocked"].__get__(self, __class__)(allbinaryLayerManager)

    def _processInput_unlocked(self, allbinaryLayerManager: AllBinaryLayerManager) -> None:
        from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
        self.processInputList(allbinaryLayerManager, self.getGameKeyEventList())
        self.getGameKeyEventList().clear()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        self.testInputPaintable.paint(graphics)
    

    def implmentsGameInputInterface(self) -> bool:
        return True
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
# from org.allbinary.graphics.RectangleFactory import RectangleFactory
# from org.allbinary.graphics.paint.NullPaintable import NullPaintable
# from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
# from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.view.ViewPosition import ViewPosition
from org.allbinary.game.input.InputFactory import InputFactory


def _TestingInputSingleton_instance() -> object:
    return TestingInputSingleton()

lazy_static(TestingInputSingleton, "instance", _TestingInputSingleton_instance)

