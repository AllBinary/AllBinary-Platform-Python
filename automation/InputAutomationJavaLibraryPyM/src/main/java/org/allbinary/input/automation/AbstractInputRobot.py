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
# package org.allbinary.input.automation

from __future__ import annotations



class AbstractInputRobot:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.helpSet: HelpSet = None
    

    def __init__(self, helpSet: HelpSet) -> None:
        self._init_fields()
        self.setHelpSet(helpSet)
    

    def getHelpSet(self) -> HelpSet:
        return self.helpSet
    

    def mouseMove(self, point: Point) -> None:
        self.mouseMove(point.x, point.y)
        self.logUtil.putF("Moved Mouse To: x: " + str(point.x) + " y: " + str(point.y), self, "moveMouse")
    

    # throws Exception
    def mouseMoveToTarget(self, rectangle: Rectangle, x: int, y: int) -> None:
        from org.allbinary.input.automation.PointHelper import PointHelper
        point: Point = PointHelper.getCenterPoint(rectangle)
        self.mouseMove(point.x + x, point.y + y)
        self.logUtil.putF("Moved Mouse To: x: " + str(point.x) + " y: " + str(point.y) + " in the middle of: " + str(rectangle), self, "moveMouseToTarget")
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def mouseMoveToTarget(self, rectangle: Rectangle) -> None:
        self.mouseMoveToTarget(rectangle, 0, 0)
    

    # Java overloaded method: Python keeps the last definition
    def mouseMove(self, x: int, y: int) -> None:
        raise RuntimeError()
    

    def setHelpSet(self, helpSet: HelpSet) -> None:
        self.helpSet = helpSet
# from java.awt import *
# from javax.help.HelpSet import HelpSet
from org.allbinary.logic.communication.log.LogUtil import LogUtil


