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
# package org.allbinary.media.image.comparison.motion

from __future__ import annotations

import time
import threading
from org.allbinary.media.image.comparison.motion.MotionRectanglesResultsListener import MotionRectanglesResultsListener


class TestInputForMotionRectanglesResultsWorker(MotionRectanglesResultsListener):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.index: int = 0
        self.running: bool = False
        self.motionRectanglesVector: BasicArrayList = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.motionRectanglesVector = BasicArrayListD()
    

    def getMotionRectanglesVector(self) -> BasicArrayList:
        return self.motionRectanglesVector
    

    def onMotionRectanglesImageComparisonResultsEvent(self, motionRectanglesImageComparisonResultsEvent: MotionRectanglesResultsEvent) -> None:
        self.getMotionRectanglesVector().add(motionRectanglesImageComparisonResultsEvent.getMotionRectangles())
        self.run()
    

    def onEvent(self, allBinaryEventObject: AllBinaryEventObject) -> None:
        self.onMotionRectanglesImageComparisonResultsEvent(allBinaryEventObject)
    

    def isRunning(self) -> bool:
        with self._lock:
            return self._isRunning_unlocked()

    def _isRunning_unlocked(self) -> bool:
        return self.running
    

    def setRunning(self, running: bool) -> None:
        with self._lock:
            return self._setRunning_unlocked(running)

    def _setRunning_unlocked(self, running: bool) -> None:
        self.running = running
    

    def run(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.RUN)
            self.setRunning(True)
            timeHelper: TimeDelayHelper = TimeDelayHelper(1000)
            timeHelper.setStartTimeTNT()
            motionRectangles: MotionRectangles = self.getMotionRectanglesVector().get(0)
            motionRectangleVector: BasicArrayList = motionRectangles.getVector()
            if motionRectangleVector.size() > 0:
                rectangle: Rectangle = motionRectangleVector.get(0)
                robotHashtable: ABHashtable[object, object] = InputRobotFactory.getInstance().get()
                inputTypeNameArray: list[object] = robotHashtable.keySet().toArray()
                size: int = len(inputTypeNameArray)
                for index in range(0, size):
                    inputTypeNameString: str = inputTypeNameArray[index]
                    inputRobotInterface: InputRobotInterface = robotHashtable.get(inputTypeNameString)
                    inputRobotInterface.mouseMoveToTarget(rectangle)
                    if inputRobotInterface.getName().compareTo(TempInputRobotNames.DX_NAME) == 0:
                        inputRobotInterface.mousePress(InputEvent.BUTTON1_MASK)
                        time.sleep((300) / 1000)
                        inputRobotInterface.mouseRelease(InputEvent.BUTTON1_MASK)
                        inputRobotInterface.mousePress(InputEvent.BUTTON2_MASK)
                        time.sleep((300) / 1000)
                        inputRobotInterface.mouseRelease(InputEvent.BUTTON2_MASK)
                        inputRobotInterface.mousePress(InputEvent.BUTTON3_MASK)
                        time.sleep((300) / 1000)
                        inputRobotInterface.mouseRelease(InputEvent.BUTTON3_MASK)
                        inputRobotInterface.keyPress(KeyEvent.VK_1)
                        time.sleep((300) / 1000)
                        inputRobotInterface.keyRelease(KeyEvent.VK_1)
                        inputRobotInterface.keyPress(KeyEvent.VK_2)
                        time.sleep((300) / 1000)
                        inputRobotInterface.keyRelease(KeyEvent.VK_2)
                        inputRobotInterface.keyPress(KeyEvent.VK_3)
                        time.sleep((300) / 1000)
                        inputRobotInterface.keyRelease(KeyEvent.VK_3)
                        inputRobotInterface.keyPress(KeyEvent.VK_4)
                        time.sleep((300) / 1000)
                        inputRobotInterface.keyRelease(KeyEvent.VK_4)
                        inputRobotInterface.keyPress(KeyEvent.VK_F1)
                        time.sleep((300) / 1000)
                        inputRobotInterface.keyRelease(KeyEvent.VK_F1)
            self.index += 1
            self.getMotionRectanglesVector().remove(motionRectangles)
            self.logUtil.putF(CommonLabels.getInstance().ELAPSED + timeHelper.getElapsedTNT(), self, self.commonStrings.RUN)
            self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
# from java.awt.Rectangle import Rectangle
# from java.awt.event.InputEvent import InputEvent
# from java.awt.event.KeyEvent import KeyEvent
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
from org.allbinary.input.automation.robot.TempInputRobotNames import TempInputRobotNames
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.ABHashtable import ABHashtable


