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
# package org.allbinary.input.media.image.capture

from __future__ import annotations



class ScreenScavangerRobot:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getScreenAsBufferedImages(self) -> list[BufferedImage]:
        self.logUtil.putF(self.commonStrings.START, self, "getScreenAsBufferedImages")
        dimScreenSize: Dimension = Toolkit.getDefaultToolkit().getScreenSize()
        rectScreenSize: Rectangle = Rectangle(dimScreenSize)
        robotHashtable: ABHashtable[object, object] = InputRobotFactory.getInstance().get()
        bufferedImageArray: list[BufferedImage] = [None] * (1)
        index: int = 0
        inputRobotInterface: InputRobotInterface = robotHashtable.get("Java Robot")
        bufferedImageArray[index] = inputRobotInterface.createScreenCapture(rectScreenSize)
        self.logUtil.putF("Finish", self, "getScreenAsBufferedImages")
        return bufferedImageArray
# from java.awt.Dimension import Dimension
# from java.awt.Rectangle import Rectangle
# from java.awt.Toolkit import Toolkit
# from java.awt.image.BufferedImage import BufferedImage
from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable


