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

import threading
from org.allbinary.game.layer.AllBinaryGameLayer import AllBinaryGameLayer
from org.allbinary.game.input.GameInputInterface import GameInputInterface


class TestingInputSingleton(AllBinaryGameLayer, GameInputInterface):
    instance: TestingInputSingleton = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.inputProcessorArray: list[GameInputProcessor] = [None] * (InputFactory.getInstance().MAX)
        self.paintable: PaintableInterface = NullPaintable.getInstance()
    

    @staticmethod
    def getInstance() -> TestingInputSingleton:
        return TestingInputSingleton.instance
    

    def __init__(self) -> None:
        from org.allbinary.game.input.GameInputProcessorUtil import GameInputProcessorUtil
        super().__init__(StringUtil.getInstance().EMPTY_STRING, RectangleFactory.SINGLETON, ViewPosition.getInstanceD())
        self._init_fields()
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
        testInputInterface: TestInputInterface = aTestInputInterface
        self.paintable = testInputInterface
        self.inputProcessorArray[Canvas.UP] = (GameInputProcessor()  # Java anonymous class body:
#             
# 
#             # throws Exception
#             def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
#                 testInputInterface.up()
)
        self.inputProcessorArray[Canvas.DOWN] = (GameInputProcessor()  # Java anonymous class body:
#             
# 
#             # throws Exception
#             def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
#                 testInputInterface.down()
)
        self.inputProcessorArray[Canvas.LEFT] = (GameInputProcessor()  # Java anonymous class body:
#             
# 
#             # throws Exception
#             def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
#                 testInputInterface.left()
)
        self.inputProcessorArray[Canvas.RIGHT] = (GameInputProcessor()  # Java anonymous class body:
#             
# 
#             # throws Exception
#             def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
#                 testInputInterface.right()
)
        self.inputProcessorArray[Canvas.KEY_NUM7] = (GameInputProcessor()  # Java anonymous class body:
#             
# 
#             # throws Exception
#             def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
#                 testInputInterface.strafeLeft()
)
        self.inputProcessorArray[Canvas.KEY_NUM9] = (GameInputProcessor()  # Java anonymous class body:
#             
# 
#             # throws Exception
#             def processEvent(self, allbinaryLayerManager: AllBinaryLayerManager, gameKeyEvent: GameKeyEvent) -> None:
#                 testInputInterface.strafeRight()
)
        GameInputProcessorUtil.init(self.inputProcessorArray)
    

    # throws Exception
    def processInputList(self, allbinaryLayerManager: AllBinaryLayerManager, list_: BasicArrayList) -> None:
        with self._lock:
            return self._processInputList_unlocked(allbinaryLayerManager, list_)

    def _processInputList_unlocked(self, allbinaryLayerManager: AllBinaryLayerManager, list_: BasicArrayList) -> None:
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
            return self._processInput_unlocked(allbinaryLayerManager)

    def _processInput_unlocked(self, allbinaryLayerManager: AllBinaryLayerManager) -> None:
        self.processInputList(allbinaryLayerManager, self.getGameKeyEventList())
        self.getGameKeyEventList().clear()
    

    def paint(self, graphics: Graphics) -> None:
        self.paintable.paint(graphics)
    

    def implmentsGameInputInterface(self) -> bool:
        return True
# from javax.microedition.lcdui.Canvas import Canvas
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.graphics.paint.NullPaintable import NullPaintable
from org.allbinary.graphics.paint.PaintableInterface import PaintableInterface
from org.allbinary.layer.AllBinaryLayerManager import AllBinaryLayerManager
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.view.ViewPosition import ViewPosition
from org.allbinary.game.input.InputFactory import InputFactory


TestingInputSingleton.instance = TestingInputSingleton()

