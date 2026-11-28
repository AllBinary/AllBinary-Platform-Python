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

from java.lang.JavaThread import JavaThread
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
import threading
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler
from org.allbinary.input.media.image.capture.CaptureWorkerInterface import CaptureWorkerInterface


@java_inherited_overloads
class ScreenCaptureImagesWorker(*java_bases(BasicEventHandler, CaptureWorkerInterface)):
    index: int = 0
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("running", False)
        vars(self).setdefault("screenScavangerRobot", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "running" not in vars(self): self.running: bool = False
        if "screenScavangerRobot" not in vars(self): self.screenScavangerRobot: ScreenScavangerRobot = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.media.image.capture.ScreenScavangerRobot import ScreenScavangerRobot
        from org.allbinary.input.media.image.capture.ProcessingFrameIndexFactory import ProcessingFrameIndexFactory
        super().__init__()
        __class__._init_fields(self)
        self.screenScavangerRobot = ScreenScavangerRobot()
        ScreenCaptureImagesWorker.index = ProcessingFrameIndexFactory.next()
    

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
    

    # throws Exception
    def setThread(self, thread: JavaThread) -> None:
        pass
    

    def run(self) -> None:
        from org.allbinary.input.media.image.capture.CapturedBufferedImagesCacheSingleton import CapturedBufferedImagesCacheSingleton
        from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsEvent import CapturedImageWorkerResultsEvent
        from org.allbinary.media.image.cache.BufferedImageFrameCacheable import BufferedImageFrameCacheable
        from org.allbinary.string.CommonLabels import CommonLabels
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.RUN)
            self.setRunning(True)
            timeHelper: TimeDelayHelper = TimeDelayHelper(1000)
            while self.isRunning():
                timeHelper.setStartTimeTNT()
                bufferedImage: BufferedImage = self.screenScavangerRobot.getScreenAsBufferedImages()[0]
                frame: int = int(ScreenCaptureImagesWorker.index)
                ScreenCaptureImagesWorker.index += 1
                CapturedBufferedImagesCacheSingleton.getInstance().add(BufferedImageFrameCacheable(bufferedImage, frame))
                capturedImageEvent: CapturedImageWorkerResultsEvent = CapturedImageWorkerResultsEvent(self, frame, bufferedImage)
                self.fireEvent(capturedImageEvent)
                self.logUtil.putF(CommonLabels.getInstance().ELAPSED + timeHelper.getElapsedTNT(), self, self.commonStrings.RUN)
                self.setRunning(False)
            self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
# from java.awt.image.BufferedImage import BufferedImage
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.media.image.cache.BufferedImageFrameCacheable import BufferedImageFrameCacheable
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


