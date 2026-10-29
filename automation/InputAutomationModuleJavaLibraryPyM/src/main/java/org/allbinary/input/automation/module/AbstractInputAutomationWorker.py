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
from org.allbinary.thread.RunnableInterface import RunnableInterface


class AbstractInputAutomationWorker(RunnableInterface):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.index: int = 0
        self.running: bool = False
        self.inputAutomationActionInterface: InputAutomationActionInterface = None
        self.captureWorkerInterface: CaptureWorkerInterface = None
        self.imageComparisonWorker: ImageComparisonWorker = None
        self.motionRectanglesWorker: MotionRectanglesWorker = None
        self.captureThread: threading.Thread = None
    

    def __init__(self, inputAutomationActionInterface: InputAutomationActionInterface) -> None:
        self._init_fields()
    

    # throws Exception
    def setThread(self, thread: threading.Thread) -> None:
        pass
    

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
    

    def isAnyDataWorkerRunning(self) -> bool:
        with self._lock:
            return self._isAnyDataWorkerRunning_unlocked()

    def _isAnyDataWorkerRunning_unlocked(self) -> bool:
        if self.captureThread is not None and (self.captureThread.isAlive() or self.getCaptureWorker().isRunning() or self.getMotionRectanglesWorker().isRunning() or self.getImageComparisonWorker().isRunning()):
            return True
        return False
    

    # throws Exception
    def startDataWorkers(self) -> None:
        with self._lock:
            return self._startDataWorkers_unlocked()

    def _startDataWorkers_unlocked(self) -> None:
        if not self.isAnyDataWorkerRunning():
            self.captureThread = threading.Thread(target=self.getCaptureWorker().run)
            self.logUtil.putF("Starting CaptureWorkers - Need more images - Thread State: " + str(self.captureThread.getState()), self, "startCaptureWorkers")
            self.captureThread.start()
    

    # throws Exception
    def waitForDataWorkers(self) -> None:
        with self._lock:
            return self._waitForDataWorkers_unlocked()

    def _waitForDataWorkers_unlocked(self) -> None:
        while self.isAnyDataWorkerRunning():
            self.logUtil.putF("Waiting", self, self.commonStrings.RUN)
            time.sleep((250) / 1000)
    

    # throws Exception
    def stopDataWorkers(self) -> None:
        self.getCaptureWorker().setRunning(False)
    

    # throws Exception
    def process(self) -> None:
        raise RuntimeError()
    

    def run(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.RUN)
            self.setRunning(True)
            timeHelper: TimeDelayHelper = TimeDelayHelper(1000)
            while self.isRunning():
                timeHelper.setStartTimeTNT()
                self.process()
                self.index += 1
                self.logUtil.putF(str(CommonLabels.getInstance().ELAPSED + timeHelper.getElapsedTNT()) + " Index: " + str(self.index), self, self.commonStrings.RUN)
            self.stopDataWorkers()
            self.waitForDataWorkers()
            self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
    

    def getInputAutomationActionInterface(self) -> InputAutomationActionInterface:
        return self.inputAutomationActionInterface
    

    def setInputAutomationActionInterface(self, inputAutomationActionInterface: InputAutomationActionInterface) -> None:
        self.inputAutomationActionInterface = inputAutomationActionInterface
    

    def getCaptureWorker(self) -> CaptureWorkerInterface:
        return self.captureWorkerInterface
    

    def setCaptureWorker(self, captureWorkerInterface: CaptureWorkerInterface) -> None:
        self.captureWorkerInterface = captureWorkerInterface
    

    def getImageComparisonWorker(self) -> ImageComparisonWorker:
        return self.imageComparisonWorker
    

    def setImageComparisonWorker(self, imageComparisonWorker: ImageComparisonWorker) -> None:
        self.imageComparisonWorker = imageComparisonWorker
    

    def getMotionRectanglesWorker(self) -> MotionRectanglesWorker:
        return self.motionRectanglesWorker
    

    def setMotionRectanglesWorker(self, motionRectanglesWorker: MotionRectanglesWorker) -> None:
        self.motionRectanglesWorker = motionRectanglesWorker
from org.allbinary.input.media.image.capture.CaptureWorkerInterface import CaptureWorkerInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.media.image.comparison.ImageComparisonWorker import ImageComparisonWorker
from org.allbinary.media.image.comparison.motion.MotionRectanglesWorker import MotionRectanglesWorker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


