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

from org.allbinary.game.input.InputProcessor import InputProcessor


class FormInputProcessor(InputProcessor):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.gameKeyEventFactory: GameKeyEventFactory = GameKeyEventFactory.getInstance()
        self.downKeyEventHandler: DownKeyEventHandler = DownKeyEventHandler.getInstance()
        self.upGameKeyEventHandler: UpGameKeyEventHandler = UpGameKeyEventHandler.getInstance()
        self.inputFactory: InputFactory = InputFactory.getInstance()
        self.platformKeyFactory: PlatformKeyFactory = PlatformKeyFactory.getInstance()
        self.allBinaryGameCanvas: AllBinaryGameCanvas = None
    

    def __init__(self, allBinaryGameCanvas: AllBinaryGameCanvas) -> None:
        super().__init__()
        self._init_fields()
        self.allBinaryGameCanvas = allBinaryGameCanvas
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        try:
            PreLogUtil.put(str(StringMaker().append(self.inputFactory.KEY_CODE_LABEL).appendint(keyCode).append(CommonSeps.getInstance().SPACE).append(self.inputFactory.DEVICE_ID_LABEL).appendint(deviceId)), self, self.gameInputStrings.KEY_PRESSED)
            input: Input = self.inputFactory.getInstanceById(keyCode)
            gameKeyEvent: GameKeyEvent = self.gameKeyEventFactory.getInstanceForInput(self.allBinaryGameCanvas, input)
            self.downKeyEventHandler.fireEventForGameKeyEvent(gameKeyEvent)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.gameInputStrings.ADD_KEY_EVENT, e)
    

    def keyReleasedByDevice(self, canvas: Canvas, keyCode: int, deviceId: int) -> None:
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
from org.allbinary.game.input.GameKey import GameKey
from org.allbinary.game.input.GameKeyEventSourceInterface import GameKeyEventSourceInterface
from org.allbinary.game.input.GameKeyFactory import GameKeyFactory
from org.allbinary.game.input.Input import Input
from org.allbinary.game.input.InputFactory import InputFactory
from org.allbinary.game.input.PlatformKeyFactory import PlatformKeyFactory
from org.allbinary.game.input.event.DownKeyEventHandler import DownKeyEventHandler
from org.allbinary.game.input.event.GameKeyEvent import GameKeyEvent
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.game.input.event.UpGameKeyEventHandler import UpGameKeyEventHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


