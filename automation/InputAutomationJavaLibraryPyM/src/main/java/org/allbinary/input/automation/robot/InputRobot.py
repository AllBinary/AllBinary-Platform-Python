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

from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface


class InputRobot(InputRobotInterface):
    NAME: str = "Java Robot"

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.robot: Robot = None
    

    def __init__(self, graphicsDevice: GraphicsDevice) -> None:
        self._init_fields()
        self.robot = Robot(graphicsDevice)
    

    def getName(self) -> str:
        return InputRobot.NAME
    

    def getHelpSet(self) -> HelpSet:
        return None
    

    def getMousePoint(self) -> Point:
        point: Point = MouseInfo.getPointerInfo().getLocation()
        return point
    

    # throws Exception
    def mouseMoveToTarget_j3(self, rectangle: Rectangle, x: int, y: int) -> None:
        from org.allbinary.input.automation.PointHelper import PointHelper
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        point: Point = PointHelper.getCenterPoint(rectangle)
        self.robot.mouseMove(point.x + x, point.y + y)
        message: str = str(StringMaker().append("Moved Mouse To: x: ").appendint(int(point.x)).append(" y: ").appendint(int(point.y)).append(" in the middle of: ").append(StringUtil.getInstance().toString(rectangle)))
        self.logUtil.putF(message, self, "moveMouseToTarget")
    

    def mouseMove_j1(self, point: Point) -> None:
        self.mouseMove(point.x, point.y)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def mouseMove_j2_1(self, x: int, y: int) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        self.robot.mouseMove(x, y)
        message: str = str(StringMaker().append("Moved Mouse To: x: ").appendint(x).append(" y: ").appendint(y))
        self.logUtil.putF(message, self, "moveMouse")
    

    # throws Exception
    def mouseMoveToTarget_j1(self, rectangle: Rectangle) -> None:
        self.mouseMoveToTarget(rectangle, 0, 0)

    def mouseMoveToTarget(self, *args):
        return getattr(self, "mouseMoveToTarget_j" + str(len(args)))(*args)
    

    def createScreenCapture(self, screenRect: Rectangle) -> BufferedImage:
        return self.robot.createScreenCapture(screenRect)
    

    def delay(self, ms: int) -> None:
        self.robot.delay(ms)
    

    def getAutoDelay(self) -> int:
        return self.robot.getAutoDelay()
    

    def getPixelColor(self, x: int, y: int) -> Color:
        return self.robot.getPixelColor(x, y)
    

    def isAutoWaitForIdle(self) -> bool:
        return self.robot.isAutoWaitForIdle()
    

    def keyPress(self, keycode: int) -> None:
        self.robot.keyPress(keycode)
    

    def keyRelease(self, keycode: int) -> None:
        self.robot.keyRelease(keycode)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def mouseMove_j2_2(self, x: int, y: int) -> None:
        self.robot.mouseMove(x, y)

    def mouseMove(self, *args):
        if len(args) == 2 and True and isinstance(args[0], int) and not isinstance(args[0], bool) and isinstance(args[1], int) and not isinstance(args[1], bool):
            return self.mouseMove_j2_1(*args)
        if len(args) == 2:
            return self.mouseMove_j2_2(*args)
        return getattr(self, "mouseMove_j" + str(len(args)))(*args)
    

    def mousePress(self, buttons: int) -> None:
        self.robot.mousePress(buttons)
    

    def mouseRelease(self, buttons: int) -> None:
        self.robot.mouseRelease(buttons)
    

    def mouseWheel(self, wheelAmt: int) -> None:
        self.robot.mouseWheel(wheelAmt)
    

    def setAutoDelay(self, ms: int) -> None:
        self.robot.setAutoDelay(ms)
    

    def setAutoWaitForIdle(self, isOn: bool) -> None:
        self.robot.setAutoWaitForIdle(isOn)
    

    def toString(self) -> str:
        return str(self.robot)

    def __str__(self) -> str:
        return self.toString()
    

    def waitForIdle(self) -> None:
        self.robot.waitForIdle()
    

    def on(self) -> None:
        pass
    

    def off(self) -> None:
        pass
# from java.awt.Robot import Robot
# from java.awt.GraphicsDevice import GraphicsDevice
# from java.awt.MouseInfo import MouseInfo
# from java.awt.Point import Point
# from java.awt.Rectangle import Rectangle
# from java.awt.Color import Color
# from java.awt.image.BufferedImage import BufferedImage
# from javax.help.HelpSet import HelpSet
# from org.allbinary.input.automation.PointHelper import PointHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil


