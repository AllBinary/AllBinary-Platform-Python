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
# package org.allbinary.input.automation.module.generic

from __future__ import annotations

from java.lang.JavaThread import JavaThread
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
import threading
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.media.image.capture.CaptureWorkerInterface import CaptureWorkerInterface
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler


@java_inherited_overloads
class SavedCaptureImagesWorker(*java_bases(BasicEventHandler, CaptureWorkerInterface)):
    index: int = 0
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("running", False)
        vars(self).setdefault("screenScavangerRobot", None)
        vars(self).setdefault("savedCaptureGenericProfileDataWorkerType", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "running" not in vars(self): self.running: bool = False
        if "screenScavangerRobot" not in vars(self): self.screenScavangerRobot: ScreenScavangerRobot = None
        if "savedCaptureGenericProfileDataWorkerType" not in vars(self): self.savedCaptureGenericProfileDataWorkerType: SavedCaptureGenericProfileDataWorkerType = None
    

    def __init__(self, savedCaptureGenericProfileDataWorkerType: SavedCaptureGenericProfileDataWorkerType) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.automation.module.generic.configuration.profile.SavedCaptureGenericProfileDataWorkerType import SavedCaptureGenericProfileDataWorkerType
        from org.allbinary.input.media.image.capture.ProcessingFrameIndexFactory import ProcessingFrameIndexFactory
        from org.allbinary.input.media.image.capture.ScreenScavangerRobot import ScreenScavangerRobot
        super().__init__()
        __class__._init_fields(self)
        self.savedCaptureGenericProfileDataWorkerType = savedCaptureGenericProfileDataWorkerType
        self.screenScavangerRobot = ScreenScavangerRobot()
        SavedCaptureImagesWorker.index = ProcessingFrameIndexFactory.next()
    

    # throws Exception
    def setThread(self, thread: JavaThread) -> None:
        pass
    

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
    

    def run(self) -> None:
        from java.io.File import File
        from org.allbinary.input.media.image.capture.CapturedBufferedImagesCacheSingleton import CapturedBufferedImagesCacheSingleton
        from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsEvent import CapturedImageWorkerResultsEvent
        from org.allbinary.logic.java.number.LongUtil import LongUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.visual.media.MediaDataFactory import MediaDataFactory
        from org.allbinary.media.image.cache.BufferedImageFrameCacheable import BufferedImageFrameCacheable
        from org.allbinary.string.CommonLabels import CommonLabels
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.RUN)
            self.setRunning(True)
            timeHelper: TimeDelayHelper = TimeDelayHelper(1000)
            while java_predicate(self, "isRunning"):
                timeHelper.setStartTimeTNT()
                frame: int = int(SavedCaptureImagesWorker.index)
                filePathStringBuffer: StringMaker = StringMaker()
                filePathStringBuffer.append(self.savedCaptureGenericProfileDataWorkerType.getPath())
                filePathStringBuffer.append(LongUtil.fillIn(str(frame)))
                filePathStringBuffer.append(MediaDataFactory.getInstance().JPG.getExtension())
                filePath: str = str(filePathStringBuffer)
                self.logUtil.putF("Loading Image File Path: " + filePath, self, self.commonStrings.RUN)
                file: File = File(filePath)
                if java_predicate(file, "isFile"):
                    bufferedImage: BufferedImage = ImageIO.read(file)
                    SavedCaptureImagesWorker.index += 1
                    CapturedBufferedImagesCacheSingleton.getInstance().add(BufferedImageFrameCacheable(bufferedImage, frame))
                    capturedImageEvent: CapturedImageWorkerResultsEvent = CapturedImageWorkerResultsEvent(self, frame, bufferedImage)
                    self.fireEvent(capturedImageEvent)
                else:
                    self.logUtil.putF("Could Not Load File: " + filePath, self, self.commonStrings.RUN)
                self.logUtil.putF(CommonLabels.getInstance().ELAPSED + timeHelper.getElapsedTNT(), self, self.commonStrings.RUN)
                self.setRunning(False)
            self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
# from java.awt.image.BufferedImage import BufferedImage
# from java.io.File import File
# from javax.imageio.ImageIO import ImageIO
# from org.allbinary.input.automation.module.generic.configuration.profile.SavedCaptureGenericProfileDataWorkerType import SavedCaptureGenericProfileDataWorkerType
# from org.allbinary.input.media.image.capture.CapturedBufferedImagesCacheSingleton import CapturedBufferedImagesCacheSingleton
# from org.allbinary.input.media.image.capture.CapturedImageWorkerResultsEvent import CapturedImageWorkerResultsEvent
# from org.allbinary.input.media.image.capture.ProcessingFrameIndexFactory import ProcessingFrameIndexFactory
# from org.allbinary.input.media.image.capture.ScreenScavangerRobot import ScreenScavangerRobot
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.number.LongUtil import LongUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.visual.media.MediaDataFactory import MediaDataFactory
# from org.allbinary.media.image.cache.BufferedImageFrameCacheable import BufferedImageFrameCacheable
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


