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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import java_bases
from javax.microedition.lcdui.Canvas import Canvas
from org.allbinary.graphics.displayable.command.MyCommandInterface import MyCommandInterface
from org.allbinary.graphics.displayable.DisplayableInterface import DisplayableInterface


@java_inherited_overloads
class MyCanvas(*java_bases(Canvas, DisplayableInterface, MyCommandInterface)):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("canvasStrings", None)
        vars(self).setdefault("stringUtil", None)
        vars(self).setdefault("displayInfo", None)
        vars(self).setdefault("name", None)
        vars(self).setdefault("childNameList", None)
        vars(self).setdefault("commandStack", None)
        vars(self).setdefault("commandListener", None)
        vars(self).setdefault("paused", False)
        vars(self).setdefault("touchME", None)

    def _init_fields(self) -> None:
        from javax.microedition.lcdui.NullCommandListener import NullCommandListener
        from org.allbinary.input.TouchJ2ME import TouchJ2ME
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.canvasStrings: CanvasStrings = CanvasStrings.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.displayInfo: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        if "name" not in vars(self): self.name: str = None
        if "childNameList" not in vars(self): self.childNameList: BasicArrayList = None
        if "commandStack" not in vars(self): self.commandStack: ABStack[object] = None
        self.commandListener: CommandListener = NullCommandListener.NULL_COMMAND_LISTENER
        if "paused" not in vars(self): self.paused: bool = False
        self.touchME: TouchJ2ME = TouchJ2ME()
    

    def __init__(self, name: str, childNameList: BasicArrayList) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.StdUtil import StdUtil
        super().__init__()
        __class__._init_fields(self)
        self.logUtil.putF(self.commonStrings.CONSTRUCTOR, self, self.commonStrings.CONSTRUCTOR)
        self.displayInfo.update(self, self.canvasStrings.CONSTRUCTOR)
        self.name = name
        self.childNameList = childNameList
        self.commandStack = StdUtil.getInstance().createStack()
    

    def getWidth(self) -> int:
        return java_super_call(super(), "getWidth")
    

    def getHeight(self) -> int:
        return java_super_call(super(), "getHeight")
    

    def setFullScreenMode(self, mode: bool) -> None:
        java_super_call(super(), "setFullScreenMode", mode)
        self.displayInfo.update(self, self.canvasStrings.SET_FULL_SCREEN_MODE)
    

    def sizeChanged(self, w: int, h: int) -> None:
        self.displayInfo.update(self, self.canvasStrings.SIZE_CHANGED)
    _declared_sizeChanged = sizeChanged
    def sizeChanged(self, *args, **kwargs):
        if len(args) + len(kwargs) == 2 and (kwargs or (True and isinstance(args[0], int) and not isinstance(args[0], bool) and isinstance(args[1], int) and not isinstance(args[1], bool))): return __class__._declared_sizeChanged(self, *args, **kwargs)
        return super().sizeChanged(*args, **kwargs)
    

    def getCommandStack(self) -> ABStack[object]:
        from org.allbinary.util.ABStack import ABStack
        return self.commandStack
    

    def isCommand(self, command: Command) -> bool:
        with self._lock:
            return __class__.__dict__["_isCommand_unlocked"].__get__(self, __class__)(command)

    def _isCommand_unlocked(self, command: Command) -> bool:
        from javax.microedition.lcdui.Command import Command
        return self.commandStack.contains(command)
    

    def addCommand(self, command: Command) -> None:
        with self._lock:
            return __class__.__dict__["_addCommand_unlocked"].__get__(self, __class__)(command)

    def _addCommand_unlocked(self, command: Command) -> None:
        from javax.microedition.lcdui.Command import Command
        if not (self.commandStack.contains(command)):
            self.commandStack.push(command)
            java_super_call(super(), "addCommand", command)
    

    def removeCommand(self, command: Command) -> None:
        with self._lock:
            return __class__.__dict__["_removeCommand_unlocked"].__get__(self, __class__)(command)

    def _removeCommand_unlocked(self, command: Command) -> None:
        from javax.microedition.lcdui.Command import Command
        self.commandStack.removeElement(command)
        java_super_call(super(), "removeCommand", command)
    

    def removeAllCommands(self) -> None:
        with self._lock:
            return __class__.__dict__["_removeAllCommands_unlocked"].__get__(self, __class__)()

    def _removeAllCommands_unlocked(self) -> None:
        from javax.microedition.lcdui.Command import Command
        size: int = self.commandStack.size()
        for index in range(0, size):
            java_super_call(super(), "removeCommand", self.commandStack.pop())
    

    def setCommandListener(self, l: CommandListener) -> None:
        from javax.microedition.lcdui.CommandListener import CommandListener
        java_super_call(super(), "setCommandListener", l)
        self.commandListener = l
    

    def getCustomCommandListener(self) -> CommandListener:
        from javax.microedition.lcdui.CommandListener import CommandListener
        return self.commandListener
    

    def isPaused(self) -> bool:
        with self._lock:
            return __class__.__dict__["_isPaused_unlocked"].__get__(self, __class__)()

    def _isPaused_unlocked(self) -> bool:
        return self.paused
    

    def removePauseCommand(self) -> None:
        from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
        self.removeCommand(MyCommandsFactory.getInstance().PAUSE_COMMAND)
    

    def pause(self) -> None:
        with self._lock:
            return __class__.__dict__["_pause_unlocked"].__get__(self, __class__)()

    def _pause_unlocked(self) -> None:
        from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
        self.logUtil.putF(self.commonStrings.START, self, self.canvasStrings.PAUSE)
        self.removePauseCommand()
        self.addCommand(MyCommandsFactory.getInstance().RESUME_COMMAND)
        self.setPaused(True)
    

    def unPause(self) -> None:
        with self._lock:
            return __class__.__dict__["_unPause_unlocked"].__get__(self, __class__)()

    def _unPause_unlocked(self) -> None:
        from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
        self.logUtil.putF(self.commonStrings.START, self, self.canvasStrings.UN_PAUSE)
        self.removeCommand(MyCommandsFactory.getInstance().RESUME_COMMAND)
        self.addCommand(MyCommandsFactory.getInstance().PAUSE_COMMAND)
        self.setPaused(False)
    

    # throws Exception
    def process(self) -> None:
        self.displayInfo.process()
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
    

    def draw(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
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
        from org.allbinary.media.audio.Sound import Sound
        pass
# from javax.microedition.lcdui.Command import Command
# from javax.microedition.lcdui.CommandListener import CommandListener
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.NullCommandListener import NullCommandListener
# from org.allbinary.graphics.displayable.command.MyCommandsFactory import MyCommandsFactory
# from org.allbinary.input.TouchJ2ME import TouchJ2ME
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.media.audio.Sound import Sound
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.util.ABStack import ABStack
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton


