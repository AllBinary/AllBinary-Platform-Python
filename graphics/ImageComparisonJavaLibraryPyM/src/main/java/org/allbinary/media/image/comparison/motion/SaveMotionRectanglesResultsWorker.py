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

import threading
from org.allbinary.media.image.comparison.motion.MotionRectanglesResultsListener import MotionRectanglesResultsListener


class SaveMotionRectanglesResultsWorker(MotionRectanglesResultsListener):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.running: bool = False
        self.motionRectanglesVector: BasicArrayList = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.motionRectanglesVector = BasicArrayListD()
    

    def getMotionRectanglesVector(self) -> BasicArrayList:
        return self.motionRectanglesVector
    

    def onMotionRectanglesImageComparisonResultsEvent(self, motionRectanglesResultsEvent: MotionRectanglesResultsEvent) -> None:
        self.getMotionRectanglesVector().add(motionRectanglesResultsEvent)
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
        from org.allbinary.media.image.comparison.motion.MotionRectanglesImageInputOutput import MotionRectanglesImageInputOutput
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.RUN)
            self.setRunning(True)
            timeHelper: TimeDelayHelper = TimeDelayHelper(1000)
            timeHelper.setStartTimeTNT()
            motionRectanglesResultsEvent: MotionRectanglesResultsEvent = self.getMotionRectanglesVector().get(0)
            motionRectangles: MotionRectangles = motionRectanglesResultsEvent.getMotionRectangles()
            MotionRectanglesImageInputOutput().save(motionRectangles, motionRectanglesResultsEvent.getFrame())
            self.getMotionRectanglesVector().remove(motionRectangles)
            self.logUtil.putF(CommonLabels.getInstance().ELAPSED + timeHelper.getElapsedTNT(), self, self.commonStrings.RUN)
            self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


