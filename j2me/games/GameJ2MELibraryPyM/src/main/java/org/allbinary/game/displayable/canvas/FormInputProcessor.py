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
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.game.input.InputProcessor import InputProcessor


@java_inherited_overloads
class FormInputProcessor(InputProcessor):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("gameKeyEventFactory", None)
        vars(self).setdefault("downKeyEventHandler", None)
        vars(self).setdefault("upGameKeyEventHandler", None)
        vars(self).setdefault("inputFactory", None)
        vars(self).setdefault("platformKeyFactory", None)
        vars(self).setdefault("allBinaryGameCanvas", None)

    def _init_fields(self) -> None:
        from org.allbinary.game.input.InputFactory import InputFactory
        from org.allbinary.game.input.PlatformKeyFactory import PlatformKeyFactory
        from org.allbinary.game.input.event.DownKeyEventHandler import DownKeyEventHandler
        from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
        from org.allbinary.game.input.event.UpGameKeyEventHandler import UpGameKeyEventHandler
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
        self.downKeyEventHandler: DownKeyEventHandler = DownKeyEventHandler.getInstance()
        self.upGameKeyEventHandler: UpGameKeyEventHandler = UpGameKeyEventHandler.getInstance()
        self.inputFactory: InputFactory = InputFactory.getInstance()
        self.platformKeyFactory: PlatformKeyFactory = PlatformKeyFactory.getInstance()
        if "allBinaryGameCanvas" not in vars(self): self.allBinaryGameCanvas: AllBinaryGameCanvas = None
    

    def __init__(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.allBinaryGameCanvas = allBinaryGameCanvas
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        from org.allbinary.game.input.Input import Input
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        try:
            PreLogUtil.put(str(StringMaker().append(self.inputFactory.KEY_CODE_LABEL).appendint(keyCode).append(CommonSeps.getInstance().SPACE).append(self.inputFactory.DEVICE_ID_LABEL).appendint(deviceId)), self, self.gameInputStrings.KEY_PRESSED)
            input: Input = self.inputFactory.getInstanceById(keyCode)
            gameKeyEvent: GameKeyEvent = self.gameKeyEventFactory.getInstanceForInput(self.allBinaryGameCanvas, input)
            self.downKeyEventHandler.fireEventForGameKeyEvent(gameKeyEvent)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.ADD_KEY_EVENT, e)
    

    def keyReleasedByDevice(self, canvas: Canvas, keyCode: int, deviceId: int) -> None:
        from javax.microedition.lcdui.Canvas import Canvas
        from org.allbinary.game.input.GameKey import GameKey
        from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface
        from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
        from org.allbinary.game.input.Input import Input
        from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        try:
            input: Input = self.inputFactory.getInstanceById(keyCode)
            if self.platformKeyFactory.isEnter(input):
                PreLogUtil.put(str(StringMaker().append(self.inputFactory.KEY_CODE_LABEL).appendint(keyCode).append(CommonSeps.getInstance().SPACE).append(self.inputFactory.DEVICE_ID_LABEL).appendint(deviceId)), self, self.gameInputStrings.KEY_RELEASED)
                gameKey: GameKey = GameKeyFactory.getInstance().KEY_NUM0
                gameKeyEventSourceInterface: GameKeyEventSourceInterface = canvas
                gameKeyEvent: GameKeyEvent = self.gameKeyEventFactory.getInstanceForInput(gameKeyEventSourceInterface, gameKey)
                self.upGameKeyEventHandler.fireEvent(gameKeyEvent)
                self.upGameKeyEventHandler.getInstanceForDevice(deviceId).fireEvent(gameKeyEvent)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.ADD_KEY_EVENT, e)
# from javax.microedition.lcdui.Canvas import Canvas
# from org.allbinary.game.input.GameKey import GameKey
# from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface
# from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
# from org.allbinary.game.input.Input import Input
# from org.allbinary.game.input.InputFactory import InputFactory
# from org.allbinary.game.input.PlatformKeyFactory import PlatformKeyFactory
# from org.allbinary.game.input.event.DownKeyEventHandler import DownKeyEventHandler
# from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
# from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
# from org.allbinary.game.input.event.UpGameKeyEventHandler import UpGameKeyEventHandler
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings


