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
# package org.allbinary.input.automation.robot

from __future__ import annotations



# Java interface
class InputRobotInterface:
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def getHelpSet(self) -> HelpSet:
        raise NotImplementedError()
    

    def createScreenCapture(self, screenRect: Rectangle) -> BufferedImage:
        raise NotImplementedError()
    

    def delay(self, ms: int) -> None:
        raise NotImplementedError()
    

    def getAutoDelay(self) -> int:
        raise NotImplementedError()
    

    def getPixelColor(self, x: int, y: int) -> Color:
        raise NotImplementedError()
    

    def isAutoWaitForIdle(self) -> bool:
        raise NotImplementedError()
    

    def keyPress(self, keycode: int) -> None:
        raise NotImplementedError()
    

    def keyRelease(self, keycode: int) -> None:
        raise NotImplementedError()
    

    def getMousePoint(self) -> Point:
        raise NotImplementedError()
    

    def mouseMove_j2(self, x: int, y: int) -> None:
        raise NotImplementedError()
    

    def mousePress(self, buttons: int) -> None:
        raise NotImplementedError()
    

    def mouseRelease(self, buttons: int) -> None:
        raise NotImplementedError()
    

    def mouseWheel(self, wheelAmt: int) -> None:
        raise NotImplementedError()
    

    def setAutoDelay(self, ms: int) -> None:
        raise NotImplementedError()
    

    def setAutoWaitForIdle(self, isOn: bool) -> None:
        raise NotImplementedError()
    

    def toString(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.toString()
    

    def waitForIdle(self) -> None:
        raise NotImplementedError()
    

    def mouseMove_j1(self, point: Point) -> None:
        raise NotImplementedError()

    def mouseMove(self, *args):
        implementation = __class__.__dict__.get("mouseMove_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().mouseMove(*args)
    

    # throws Exception
    def mouseMoveToTarget_j1(self, rectangle: Rectangle) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def mouseMoveToTarget_j3(self, rectangle: Rectangle, x: int, y: int) -> None:
        raise NotImplementedError()

    def mouseMoveToTarget(self, *args):
        implementation = __class__.__dict__.get("mouseMoveToTarget_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().mouseMoveToTarget(*args)
# from java.awt.Rectangle import Rectangle
# from java.awt.Color import Color
# from java.awt.Point import Point
# from java.awt.image.BufferedImage import BufferedImage
# from javax.help.HelpSet import HelpSet


