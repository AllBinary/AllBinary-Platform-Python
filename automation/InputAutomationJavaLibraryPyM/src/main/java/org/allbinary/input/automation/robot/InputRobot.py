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
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.robot: Robot = None
    

    def __init__(self, graphicsDevice: GraphicsDevice) -> None:
        from org.allbinary.input.automation.robot.Robot import Robot
        self._init_fields()
        self.robot = Robot(graphicsDevice)
    

    def getName(self) -> str:
        return InputRobot.NAME
    

    def getHelpSet(self) -> HelpSet:
        return None
    

    def getMousePoint(self) -> Point:
        from org.allbinary.input.automation.robot.MouseInfo import MouseInfo
        point: Point = MouseInfo.getPointerInfo().getLocation()
        return point
    

    # throws Exception
    def mouseMoveToTarget(self, rectangle: Rectangle, x: int, y: int) -> None:
        point: Point = PointHelper.getCenterPoint(rectangle)
        self.robot.mouseMove(point.x + x, point.y + y)
        message: str = str(StringMaker().append("Moved Mouse To: x: ").appendint(int(point.x)).append(" y: ").appendint(int(point.y)).append(" in the middle of: ").append(StringUtil.getInstance().toString(rectangle)))
        self.logUtil.putF(message, self, "moveMouseToTarget")
    

    def mouseMove(self, point: Point) -> None:
        self.mouseMove(point.x, point.y)
    

    # Java overloaded method: Python keeps the last definition
    def mouseMove(self, x: int, y: int) -> None:
        self.robot.mouseMove(x, y)
        message: str = str(StringMaker().append("Moved Mouse To: x: ").appendint(x).append(" y: ").appendint(y))
        self.logUtil.putF(message, self, "moveMouse")
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def mouseMoveToTarget(self, rectangle: Rectangle) -> None:
        self.mouseMoveToTarget(rectangle, 0, 0)
    

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
    

    # Java overloaded method: Python keeps the last definition
    def mouseMove(self, x: int, y: int) -> None:
        self.robot.mouseMove(x, y)
    

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
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
# from javax.help.HelpSet import HelpSet
from org.allbinary.input.automation.PointHelper import PointHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


