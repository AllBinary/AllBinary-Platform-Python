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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.game.input.InputProcessor import InputProcessor


@java_inherited_overloads
class GameCanvasInputProcessor(InputProcessor):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("allBinaryGameCanvas", None)
        vars(self).setdefault("downGameKeyEventHandler", None)
        vars(self).setdefault("upGameKeyEventHandler", None)
        vars(self).setdefault("downKeyEventHandler", None)
        vars(self).setdefault("smallIntegerSingletonFactory", None)
        vars(self).setdefault("inputToGameKeyMapping", None)
        vars(self).setdefault("NONE", None)
        vars(self).setdefault("gameKeyEventFactory", None)

    def _init_fields(self) -> None:
        from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
        from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
        from org.allbinary.game.input.event.DownGameKeyEventHandler import DownGameKeyEventHandler
        from org.allbinary.game.input.event.DownKeyEventHandler import DownKeyEventHandler
        from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
        from org.allbinary.game.input.event.UpGameKeyEventHandler import UpGameKeyEventHandler
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "allBinaryGameCanvas" not in vars(self): self.allBinaryGameCanvas: AllBinaryGameCanvas = None
        self.downGameKeyEventHandler: DownGameKeyEventHandler = DownGameKeyEventHandler.getInstance()
        self.upGameKeyEventHandler: UpGameKeyEventHandler = UpGameKeyEventHandler.getInstance()
        self.downKeyEventHandler: DownKeyEventHandler = DownKeyEventHandler.getInstance()
        self.smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        self.inputToGameKeyMapping: InputToGameKeyMapping = PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance().getInputMapping()
        self.NONE: GameKey = GameKeyFactory.getInstance().NONE
        self.gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
    

    def __init__(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.allBinaryGameCanvas = allBinaryGameCanvas
        self.inputToGameKeyMapping.init(self.allBinaryGameCanvas)
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        from org.allbinary.game.input.GameKey import GameKey
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        from org.allbinary.logic.string.StringMaker import StringMaker
        try:
            gameKey: GameKey = self.inputToGameKeyMapping.getInstanceForCanvas(self.allBinaryGameCanvas, keyCode)
            if gameKey != self.NONE:
                gameKeyEvent: GameKeyEvent = self.gameKeyEventFactory.getInstanceForInput(self.allBinaryGameCanvas, gameKey)
                self.downGameKeyEventHandler.fireEvent(gameKeyEvent)
                self.downGameKeyEventHandler.getInstanceForDevice(deviceId).fireEvent(gameKeyEvent)
            else:
                self.logUtil.putF(str(StringMaker().append(self.gameInputStrings.NO_KEY).appendint(keyCode)), self, self.gameInputStrings.ADD_KEY_EVENT)
            keyCodeAsInteger: int = self.smallIntegerSingletonFactory.getAtNoThrow(keyCode)
            self.downKeyEventHandler.fireEventI(keyCodeAsInteger)
            self.downKeyEventHandler.getInstanceForDevice(deviceId).fireEventI(keyCodeAsInteger)
        except Exception as e:
            self.logUtil.put("Key Event Error", self, self.gameInputStrings.ADD_KEY_EVENT, e)
    

    def keyReleasedByDevice(self, canvas: Canvas, keyCode: int, deviceId: int) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        self.removeGameKeyEvent(canvas, keyCode, deviceId, False)
    

    def removeGameKeyEvent(self, canvas: Canvas, keyCode: int, deviceId: int, repeated: bool) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.game.input.GameKey import GameKey
        from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        from org.allbinary.logic.string.StringMaker import StringMaker
        try:
            gameKey: GameKey = self.inputToGameKeyMapping.getInstanceForCanvas(canvas, keyCode)
            if gameKey != self.NONE:
                gameKeyEventSourceInterface: GameKeyEventSourceInterface = canvas
                gameKeyEvent: GameKeyEvent = self.gameKeyEventFactory.getInstanceForInput(gameKeyEventSourceInterface, gameKey)
                self.upGameKeyEventHandler.fireEvent(gameKeyEvent)
                self.upGameKeyEventHandler.getInstanceForDevice(deviceId).fireEvent(gameKeyEvent)
            else:
                self.logUtil.putF(str(StringMaker().append(self.gameInputStrings.NO_KEY).appendint(keyCode)), self, self.gameInputStrings.REMOVE_KEY_EVENT)
        except Exception as e:
            self.logUtil.put("Key Event Error", self, self.gameInputStrings.REMOVE_KEY_EVENT, e)
# from javax.microedition.lcdui.Canvas import Canvas
# from org.allbinary.game.input.GameKey import GameKey
# from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface
# from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
# from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
# from org.allbinary.game.input.event.DownGameKeyEventHandler import DownGameKeyEventHandler
# from org.allbinary.game.input.event.DownKeyEventHandler import DownKeyEventHandler
# from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
# from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
# from org.allbinary.game.input.event.UpGameKeyEventHandler import UpGameKeyEventHandler
# from org.allbinary.game.input.mapping.InputToGameKeyMapping import InputToGameKeyMapping
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
# from org.allbinary.logic.string.StringMaker import StringMaker


