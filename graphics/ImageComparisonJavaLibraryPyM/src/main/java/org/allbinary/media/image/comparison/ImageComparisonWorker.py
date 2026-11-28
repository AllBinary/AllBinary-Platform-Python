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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsListener import CapturedImageWorkerResultsListener
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


@java_inherited_overloads
class ImageComparisonWorker(*java_bases(BasicEventHandler, CapturedImageWorkerResultsListener)):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("bufferedImageVector", None)
        vars(self).setdefault("imageComparatorConstraintsInterface", None)
        vars(self).setdefault("imageComparator", None)
        vars(self).setdefault("running", False)
        vars(self).setdefault("index2", 0)

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.bufferedImageVector: BasicArrayList = BasicArrayListD()
        if "imageComparatorConstraintsInterface" not in vars(self): self.imageComparatorConstraintsInterface: ImageComparatorConstraintsInterface = None
        if "imageComparator" not in vars(self): self.imageComparator: ImageComparator = None
        if "running" not in vars(self): self.running: bool = False
        if "index2" not in vars(self): self.index2: int = 0
    

    def __init__(self, imageComparatorConstraintsInterface: ImageComparatorConstraintsInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.media.image.comparison.ImageComparator import ImageComparator
        super().__init__()
        __class__._init_fields(self)
        self.imageComparatorConstraintsInterface = imageComparatorConstraintsInterface
        self.imageComparator = ImageComparator(imageComparatorConstraintsInterface)
    

    def isRunning(self) -> bool:
        with self._lock:
            return __class__.__dict__["_isRunning_unlocked"].__get__(self, __class__)()

    def _isRunning_unlocked(self) -> bool:
        return self.running
    

    def setRunning(self, running: bool) -> None:
        with self._lock:
            return __class__.__dict__["_setRunning_unlocked"].__get__(self, __class__)(running)

    def _setRunning_unlocked(self, running: bool) -> None:
        self.running = running
    

    def onCaptureEvent(self, capturedImageWorkerResultsEvent: CapturedImageWorkerResultsEvent) -> None:
        with self._lock:
            return __class__.__dict__["_onCaptureEvent_unlocked"].__get__(self, __class__)(capturedImageWorkerResultsEvent)

    def _onCaptureEvent_unlocked(self, capturedImageWorkerResultsEvent: CapturedImageWorkerResultsEvent) -> None:
        from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsEvent import CapturedImageWorkerResultsEvent
        self.bufferedImageVector.add(capturedImageWorkerResultsEvent)
        if self.bufferedImageVector.size() > 1:
            self.run()
    

    def onEvent(self, allBinaryEventObject: AllBinaryEventObject) -> None:
        with self._lock:
            return __class__.__dict__["_onEvent_unlocked"].__get__(self, __class__)(allBinaryEventObject)

    def _onEvent_unlocked(self, allBinaryEventObject: AllBinaryEventObject) -> None:
        from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsEvent import CapturedImageWorkerResultsEvent
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        self.onCaptureEvent(allBinaryEventObject)
    

    def run(self) -> None:
        from org.allbinary.media.image.comparison.ImageComparisonResultFrameCacheable import ImageComparisonResultFrameCacheable
        from org.allbinary.media.image.comparison.ImageComparisonResultCacheSingleton import ImageComparisonResultCacheSingleton
        from org.allbinary.media.image.comparison.ImageComparisonResultsEvent import ImageComparisonResultsEvent
        from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsEvent import CapturedImageWorkerResultsEvent
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonLabels import CommonLabels
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
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
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsEvent import CapturedImageWorkerResultsEvent
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


