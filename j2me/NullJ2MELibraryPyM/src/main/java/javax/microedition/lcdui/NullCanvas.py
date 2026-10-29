# Generated Code Do Not Modify
# package javax.microedition.lcdui

from __future__ import annotations

from javax.microedition.lcdui.Canvas import Canvas


class NullCanvas(Canvas):
    NULL_CANVAS: NullCanvas = None
    

    def __init__(self) -> None:
        super().__init__()
    

    def setFullScreenMode(self, mode: bool) -> None:
        pass
    

    def sizeChanged(self, w: int, h: int) -> None:
        pass
    

    def getCommandStack(self) -> list:
        raise RuntimeError()
    

    def isCommand(self, command: Command) -> bool:
        raise RuntimeError()
    

    def addCommand(self, command: Command) -> None:
        pass
    

    def removeCommand(self, command: Command) -> None:
        pass
    

    def removeAllCommands(self) -> None:
        pass
    

    def setCommandListener(self, l: CommandListener) -> None:
        pass
    

    def getCustomCommandListener(self) -> CommandListener:
        raise RuntimeError()
    

    def isPaused(self) -> bool:
        raise RuntimeError()
    

    def removePauseCommand(self) -> None:
        pass
    

    def pause(self) -> None:
        pass
    

    def unPause(self) -> None:
        pass
    

    # throws Exception
    def process(self) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        pass
    

    def destroy(self) -> None:
        pass
    

    def setPaused(self, isPaused: bool) -> None:
        raise RuntimeError()
    

    def pointerDragged(self, x: int, y: int) -> None:
        pass
    

    def pointerPressed(self, x: int, y: int) -> None:
        pass
    

    def pointerReleased(self, x: int, y: int) -> None:
        pass
# from java.util.Stack import Stack


NullCanvas.NULL_CANVAS = NullCanvas()

