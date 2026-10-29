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
# package org.allbinary.input.automation.module

from __future__ import annotations

import time
import threading
from org.allbinary.input.automation.module.AbstractInputAutomationWorker import AbstractInputAutomationWorker


class TestInputAutomationActionWorker(AbstractInputAutomationWorker):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.sleep: int = None
    

    def __init__(self, sleep: int, inputAutomationActionInterface: InputAutomationActionInterface, imageComparatorConstraintsInterface: ImageComparatorConstraintsInterface, motionRectangleConstraintsInterface: MotionRectangleConstraintsInterface) -> None:
        super().__init__(inputAutomationActionInterface)
        self._init_fields()
        self.logUtil.putF("BasicTestAttackWorder", self, self.commonStrings.CONSTRUCTOR)
        self.sleep = sleep
    

    # throws Exception
    def processBetweenWorkers(self) -> None:
        time.sleep((2000) / 1000)
    

    # throws Exception
    def process(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.PROCESS)
        hashtable: ABHashtable[object, object] = InputRobotFactory.getInstance().get()
        set: Set = hashtable.keySet()
        inputTypeNameArray: list[object] = set.toArray()
        size: int = len(inputTypeNameArray)
        for index in range(0, size):
            inputTypeNameString: str = inputTypeNameArray[index]
            robot: InputRobotInterface = hashtable.get(inputTypeNameString)
            if self.sleep > 0:
                time.sleep((self.sleep) / 1000)
# from java.util.Set import Set
from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.media.image.comparison.ImageComparatorConstraintsInterface import ImageComparatorConstraintsInterface
from org.allbinary.media.image.comparison.motion.MotionRectangleConstraintsInterface import MotionRectangleConstraintsInterface
from org.allbinary.util.ABHashtable import ABHashtable


