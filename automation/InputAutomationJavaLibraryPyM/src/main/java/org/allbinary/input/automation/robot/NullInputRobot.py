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

from org.allbinary.input.automation.AbstractInputRobot import AbstractInputRobot
from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface


class NullInputRobot(AbstractInputRobot, InputRobotInterface):
    LIBRARY_NAME: str = "null"
    NAME: str = "NULL"

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__(None)
        self._init_fields()
    

    def getName(self) -> str:
        return NullInputRobot.NAME
    

    def getHelpSet(self) -> HelpSet:
        return None
    

    def getMousePoint(self) -> Point:
        return PointFactory.getInstance(0, 0)
    

    def keyPress(self, keycode: int) -> None:
        self.logUtil.putF("KeyCode: " + str(keycode), self, "keyPress")
    

    def keyRelease(self, keycode: int) -> None:
        self.logUtil.putF("KeyCode: " + str(keycode), self, "keyRelease")
    

    def mouseMove(self, x: int, y: int) -> None:
        self.logUtil.putF("X: " + str(x) + " Y: " + str(y), self, "mouseMove")
    

    def mousePress(self, buttons: int) -> None:
        self.logUtil.putF("Buttons: " + str(buttons), self, "mousePress")
    

    def mouseRelease(self, buttons: int) -> None:
        self.logUtil.putF("Buttons: " + str(buttons), self, "mouseRelease")
    

    def createScreenCapture(self, screenRect: Rectangle) -> BufferedImage:
        return None
    

    def delay(self, ms: int) -> None:
        pass
    

    def getAutoDelay(self) -> int:
        return -1
    

    def getPixelColor(self, x: int, y: int) -> Color:
        return None
    

    def isAutoWaitForIdle(self) -> bool:
        return False
    

    def mouseWheel(self, wheelAmt: int) -> None:
        pass
    

    def setAutoDelay(self, ms: int) -> None:
        pass
    

    def setAutoWaitForIdle(self, isOn: bool) -> None:
        pass
    

    def toString(self) -> str:
        return "DirectXWindowsInputRobot"

    def __str__(self) -> str:
        return self.toString()
    

    def waitForIdle(self) -> None:
        pass
# from java.awt import *
# from java.awt.image.BufferedImage import BufferedImage
# from javax.help.HelpSet import HelpSet
from org.allbinary.input.automation.PointFactory import PointFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil


