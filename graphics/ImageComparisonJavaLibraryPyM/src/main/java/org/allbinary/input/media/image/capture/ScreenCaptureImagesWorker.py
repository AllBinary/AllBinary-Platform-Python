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

import threading
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler
from org.allbinary.input.media.image.capture.CaptureWorkerInterface import CaptureWorkerInterface


class ScreenCaptureImagesWorker(BasicEventHandler, CaptureWorkerInterface):
    index: int = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.running: bool = False
        self.screenScavangerRobot: ScreenScavangerRobot = None
    

    def __init__(self) -> None:
        from org.allbinary.input.media.image.capture.ScreenScavangerRobot import ScreenScavangerRobot
        from org.allbinary.input.media.image.capture.ProcessingFrameIndexFactory import ProcessingFrameIndexFactory
        super().__init__()
        self._init_fields()
        self.screenScavangerRobot = ScreenScavangerRobot()
        ScreenCaptureImagesWorker.index = ProcessingFrameIndexFactory.next()
    

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
    

    # throws Exception
    def setThread(self, thread: threading.Thread) -> None:
        pass
    

    def run(self) -> None:
        from org.allbinary.input.media.image.capture.CapturedBufferedImagesCacheSingleton import CapturedBufferedImagesCacheSingleton
        from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsEvent import CapturedImageWorkerResultsEvent
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
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.media.image.cache.BufferedImageFrameCacheable import BufferedImageFrameCacheable
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


