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
# package org.allbinary.graphics.displayable

from __future__ import annotations

import threading
# from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.graphics.displayable.command.MyCommandInterface import MyCommandInterface
from org.allbinary.graphics.displayable.DisplayableInterface import DisplayableInterface


class MyCanvas(Canvas, DisplayableInterface, MyCommandInterface):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.canvasStrings: CanvasStrings = CanvasStrings.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.name: str = None
        self.childNameList: BasicArrayList = None
        self.commandStack: ABStack[object] = None
        self.commandListener: CommandListener = NullCommandListener.NULL_COMMAND_LISTENER
        self.paused: bool = False
        self.touchME: TouchJ2ME = TouchJ2ME()
    

    def __init__(self, name: str, childNameList: BasicArrayList) -> None:
        super().__init__()
        self._init_fields()
        self.logUtil.putF(self.commonStrings.CONSTRUCTOR, self, self.commonStrings.CONSTRUCTOR)
        self.displayInfo.update(self, self.canvasStrings.CONSTRUCTOR)
        self.name = name
        self.childNameList = childNameList
        self.commandStack = StdUtil.getInstance().createStack()
    

    def setFullScreenMode(self, mode: bool) -> None:
        super().setFullScreenMode(mode)
        self.displayInfo.update(self, self.canvasStrings.SET_FULL_SCREEN_MODE)
    

    def sizeChanged(self, w: int, h: int) -> None:
        self.displayInfo.update(self, self.canvasStrings.SIZE_CHANGED)
    

    def getCommandStack(self) -> ABStack[object]:
        return self.commandStack
    

    def isCommand(self, command: Command) -> bool:
        with self._lock:
            return self._isCommand_unlocked(command)

    def _isCommand_unlocked(self, command: Command) -> bool:
        return self.commandStack.contains(command)
    

    def addCommand(self, command: Command) -> None:
        with self._lock:
            return self._addCommand_unlocked(command)

    def _addCommand_unlocked(self, command: Command) -> None:
        if not self.commandStack.contains(command):
            self.commandStack.push(command)
            super().addCommand(command)
    

    def removeCommand(self, command: Command) -> None:
        with self._lock:
            return self._removeCommand_unlocked(command)

    def _removeCommand_unlocked(self, command: Command) -> None:
        self.commandStack.removeElement(command)
        super().removeCommand(command)
    

    def removeAllCommands(self) -> None:
        with self._lock:
            return self._removeAllCommands_unlocked()

    def _removeAllCommands_unlocked(self) -> None:
        size: int = self.commandStack.size()
        for index in range(0, size):
            super().removeCommand(self.commandStack.pop())
    

    def setCommandListener(self, l: CommandListener) -> None:
        super().setCommandListener(l)
        self.commandListener = l
    

    def getCustomCommandListener(self) -> CommandListener:
        return self.commandListener
    

    def isPaused(self) -> bool:
        with self._lock:
            return self._isPaused_unlocked()

    def _isPaused_unlocked(self) -> bool:
        return self.paused
    

    def removePauseCommand(self) -> None:
        self.removeCommand(MyCommandsFactory.getInstance().PAUSE_COMMAND)
    

    def pause(self) -> None:
        with self._lock:
            return self._pause_unlocked()

    def _pause_unlocked(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.canvasStrings.PAUSE)
        self.removePauseCommand()
        self.addCommand(MyCommandsFactory.getInstance().RESUME_COMMAND)
        self.setPaused(True)
    

    def unPause(self) -> None:
        with self._lock:
            return self._unPause_unlocked()

    def _unPause_unlocked(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.canvasStrings.UN_PAUSE)
        self.removeCommand(MyCommandsFactory.getInstance().RESUME_COMMAND)
        self.addCommand(MyCommandsFactory.getInstance().PAUSE_COMMAND)
        self.setPaused(False)
    

    # throws Exception
    def process(self) -> None:
        self.displayInfo.process()
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def draw(self, graphics: Graphics) -> None:
        pass
    

    def hasChild(self, displayable: MyCanvas) -> bool:
        return self.childNameList.contains(displayable.name)
    

    def destroy(self) -> None:
        self.logUtil.putF("Destroyed MyCanvas", self, "destroy")
    

    def setPaused(self, isPaused: bool) -> None:
        self.paused = isPaused
    

    def keyPressedByDevice(self, keyCode: int, deviceId: int) -> None:
        pass
    

    def keyRepeatedByDevice(self, keyCode: int, deviceId: int) -> None:
        pass
    

    def keyReleasedByDevice(self, keyCode: int, deviceId: int) -> None:
        pass
    

    def pointerDragged(self, x: int, y: int) -> None:
        self.touchME.pointerDragged(x, y)
    

    def pointerPressed(self, x: int, y: int) -> None:
        self.touchME.pointerPressed(x, y)
    

    def pointerReleased(self, x: int, y: int) -> None:
        self.touchME.pointerReleased(x, y)
    

    def nextSong(self, nextSongSound: Sound, leftVolume: int, rightVolume: int) -> None:
        pass
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.NullCommandListener import NullCommandListener
from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
from org.allbinary.input.TouchJ2ME import TouchJ2ME
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.media.audio.Sound import Sound
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.util.ABStack import ABStack
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton


