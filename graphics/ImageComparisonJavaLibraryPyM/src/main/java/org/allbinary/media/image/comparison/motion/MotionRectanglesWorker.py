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
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler
from org.allbinary.media.image.comparison.ImageComparisonResultsListener import ImageComparisonResultsListener


class MotionRectanglesWorker(BasicEventHandler, ImageComparisonResultsListener):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.imageComparisonInfoVector: BasicArrayList = BasicArrayListD()
        self.motionRectangleConstraintsInterface: MotionRectangleConstraintsInterface = None
        self.index: int = 0
        self.running: bool = False
    

    def __init__(self, motionRectangleConstraintsInterface: MotionRectangleConstraintsInterface) -> None:
        super().__init__()
        self._init_fields()
        self.motionRectangleConstraintsInterface = motionRectangleConstraintsInterface
    

    def onImageComparisonResultsEvent(self, imageComparisonResultsEvent: ImageComparisonResultsEvent) -> None:
        self.imageComparisonInfoVector.add(imageComparisonResultsEvent)
        self.run()
    

    def onEvent(self, allBinaryEventObject: AllBinaryEventObject) -> None:
        self.onImageComparisonResultsEvent(allBinaryEventObject)
    

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
        from org.allbinary.media.image.comparison.motion.AllMotionRectangles import AllMotionRectangles
        from org.allbinary.media.image.comparison.motion.AllMotionRectanglesResultsCacheSingleton import AllMotionRectanglesResultsCacheSingleton
        from org.allbinary.media.image.comparison.motion.MotionRectanglesResultsFrameCacheable import MotionRectanglesResultsFrameCacheable
        from org.allbinary.media.image.comparison.motion.ConsolidateMotionRectangles import ConsolidateMotionRectangles
        from org.allbinary.media.image.comparison.motion.ConsolidatedMotionRectanglesResultsCacheSingleton import ConsolidatedMotionRectanglesResultsCacheSingleton
        from org.allbinary.media.image.comparison.motion.MotionRectanglesResultsFrameCacheable import MotionRectanglesResultsFrameCacheable
        from org.allbinary.media.image.comparison.motion.ConstrainedMotionRectangles import ConstrainedMotionRectangles
        from org.allbinary.media.image.comparison.motion.ConstrainedMotionRectanglesResultsCacheSingleton import ConstrainedMotionRectanglesResultsCacheSingleton
        from org.allbinary.media.image.comparison.motion.MotionRectanglesResultsFrameCacheable import MotionRectanglesResultsFrameCacheable
        from org.allbinary.media.image.comparison.motion.MotionRectanglesResultsEvent import MotionRectanglesResultsEvent
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.RUN)
            self.setRunning(True)
            timeHelper: TimeDelayHelper = TimeDelayHelper(1000)
            timeHelper.setStartTimeTNT()
            imageComparisonResultsEvent: ImageComparisonResultsEvent = self.imageComparisonInfoVector.get(0)
            imageComparisonInfo: ImageComparisonResult = imageComparisonResultsEvent.getImageComparisonResult()
            self.logUtil.putF(str(imageComparisonInfo), self, self.commonStrings.RUN)
            allMotionRectangles: AllMotionRectangles = AllMotionRectangles(imageComparisonInfo)
            AllMotionRectanglesResultsCacheSingleton.getInstance().add(MotionRectanglesResultsFrameCacheable(allMotionRectangles, imageComparisonInfo.getFrameTwo()))
            consolidatedMotionRectangles: ConsolidateMotionRectangles = ConsolidateMotionRectangles(allMotionRectangles)
            ConsolidatedMotionRectanglesResultsCacheSingleton.getInstance().add(MotionRectanglesResultsFrameCacheable(consolidatedMotionRectangles, imageComparisonInfo.getFrameTwo()))
            constrainedMotionRectangles: ConstrainedMotionRectangles = ConstrainedMotionRectangles(self.motionRectangleConstraintsInterface, consolidatedMotionRectangles)
            constrainedMotionRectangles.applyMotionRectangleConstraints(consolidatedMotionRectangles)
            ConstrainedMotionRectanglesResultsCacheSingleton.getInstance().add(MotionRectanglesResultsFrameCacheable(constrainedMotionRectangles, imageComparisonInfo.getFrameTwo()))
            self.fireEvent(MotionRectanglesResultsEvent(self, imageComparisonInfo.getFrameTwo(), constrainedMotionRectangles))
            self.imageComparisonInfoVector.remove(imageComparisonResultsEvent)
            self.index += 1
            self.logUtil.putF(CommonLabels.getInstance().ELAPSED + timeHelper.getElapsedTNT(), self, self.commonStrings.RUN)
            self.setRunning(False)
            self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.media.image.comparison.ImageComparisonResult import ImageComparisonResult
from org.allbinary.media.image.comparison.ImageComparisonResultsEvent import ImageComparisonResultsEvent
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


