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
# package org.allbinary.media.image.comparison

from __future__ import annotations

import threading
from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsListener import CapturedImageWorkerResultsListener
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


class ImageComparisonWorker(BasicEventHandler, CapturedImageWorkerResultsListener):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.bufferedImageVector: BasicArrayList = BasicArrayListD()
        self.imageComparatorConstraintsInterface: ImageComparatorConstraintsInterface = None
        self.imageComparator: ImageComparator = None
        self.running: bool = False
        self.index2: int = 0
    

    def __init__(self, imageComparatorConstraintsInterface: ImageComparatorConstraintsInterface) -> None:
        from org.allbinary.media.image.comparison.ImageComparator import ImageComparator
        super().__init__()
        self._init_fields()
        self.imageComparatorConstraintsInterface = imageComparatorConstraintsInterface
        self.imageComparator = ImageComparator(imageComparatorConstraintsInterface)
    

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
    

    def onCaptureEvent(self, capturedImageWorkerResultsEvent: CapturedImageWorkerResultsEvent) -> None:
        with self._lock:
            return self._onCaptureEvent_unlocked(capturedImageWorkerResultsEvent)

    def _onCaptureEvent_unlocked(self, capturedImageWorkerResultsEvent: CapturedImageWorkerResultsEvent) -> None:
        self.bufferedImageVector.add(capturedImageWorkerResultsEvent)
        if self.bufferedImageVector.size() > 1:
            self.run()
    

    def onEvent(self, allBinaryEventObject: AllBinaryEventObject) -> None:
        with self._lock:
            return self._onEvent_unlocked(allBinaryEventObject)

    def _onEvent_unlocked(self, allBinaryEventObject: AllBinaryEventObject) -> None:
        self.onCaptureEvent(allBinaryEventObject)
    

    def run(self) -> None:
        from org.allbinary.media.image.comparison.ImageComparisonResultFrameCacheable import ImageComparisonResultFrameCacheable
        from org.allbinary.media.image.comparison.ImageComparisonResultCacheSingleton import ImageComparisonResultCacheSingleton
        from org.allbinary.media.image.comparison.ImageComparisonResultsEvent import ImageComparisonResultsEvent
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.RUN)
            self.setRunning(True)
            timeHelper: TimeDelayHelper = TimeDelayHelper(1000)
            timeHelper.setStartTimeTNT()
            if self.imageComparatorConstraintsInterface.isFrameAllowed(self.index2):
                capturedImageWorkerResultsEvent: list[CapturedImageWorkerResultsEvent] = [None] * (2)
                capturedImageWorkerResultsEvent[0] = self.bufferedImageVector.get(0)
                capturedImageWorkerResultsEvent[1] = self.bufferedImageVector.get(1)
                if self.imageComparatorConstraintsInterface.isImageValid(capturedImageWorkerResultsEvent[0].getBufferedImage()) and self.imageComparatorConstraintsInterface.isImageValid(capturedImageWorkerResultsEvent[1].getBufferedImage()):
                    imageComparisonResult: ImageComparisonResult = self.imageComparator.compare(capturedImageWorkerResultsEvent[0].getBufferedImage(), capturedImageWorkerResultsEvent[1].getBufferedImage(), capturedImageWorkerResultsEvent[0].getFrame(), capturedImageWorkerResultsEvent[1].getFrame(), 0)
                    frame: int = capturedImageWorkerResultsEvent[1].getFrame()
                    imageComparisonResultFrameCacheable: ImageComparisonResultFrameCacheable = ImageComparisonResultFrameCacheable(imageComparisonResult, frame)
                    ImageComparisonResultCacheSingleton.getInstance().add(imageComparisonResultFrameCacheable)
                    self.fireEvent(ImageComparisonResultsEvent(self, imageComparisonResult))
                    self.logUtil.putF(str(StringMaker().append("Image Comparison Result: ").append(str(imageComparisonResult)).append(" for frame: ").appendlong(frame)), self, self.commonStrings.RUN)
                else:
                    self.logUtil.putF("An Image Was Not Valid: Image Worker Event Processing terminated", self, self.commonStrings.RUN)
            self.bufferedImageVector.remove(0)
            self.index2 += 1
            message: str = str(StringMaker().append("Frame: ").appendint(self.index2).append(CommonLabels.getInstance().ELAPSED).appendlong(int(timeHelper.getElapsedTNT())))
            self.logUtil.putF(message, self, self.commonStrings.RUN)
            self.setRunning(False)
            self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsEvent import CapturedImageWorkerResultsEvent
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


