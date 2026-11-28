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
# package org.allbinary.media.image.search

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.util.event.handler.BasicEventHandler import BasicEventHandler
from org.allbinary.media.image.comparison.ImageComparisonResultsListener import ImageComparisonResultsListener


@java_inherited_overloads
class ImageComparisonSearchWorker(*java_bases(BasicEventHandler, ImageComparisonResultsListener)):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("imageComparisonInfoVector", None)
        vars(self).setdefault("index", 0)
        vars(self).setdefault("running", False)
        vars(self).setdefault("imageSearchConstraintsInterface", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "imageComparisonInfoVector" not in vars(self): self.imageComparisonInfoVector: BasicArrayList = None
        if "index" not in vars(self): self.index: int = 0
        if "running" not in vars(self): self.running: bool = False
        if "imageSearchConstraintsInterface" not in vars(self): self.imageSearchConstraintsInterface: ImageComparisonSearchConstraintsInterface = None
    

    def __init__(self, imageSearchConstraintsInterface: ImageComparisonSearchConstraintsInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        super().__init__()
        __class__._init_fields(self)
        self.imageComparisonInfoVector = BasicArrayListD()
        self.imageSearchConstraintsInterface = imageSearchConstraintsInterface
    

    def onImageComparisonResultsEvent(self, imageComparisonResultsEvent: ImageComparisonResultsEvent) -> None:
        from org.allbinary.media.image.comparison.ImageComparisonResultsEvent import ImageComparisonResultsEvent
        self.imageComparisonInfoVector.add(imageComparisonResultsEvent.getImageComparisonResult())
        self.run()
    

    def onEvent(self, allBinaryEventObject: AllBinaryEventObject) -> None:
        from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
        from org.allbinary.media.image.comparison.ImageComparisonResultsEvent import ImageComparisonResultsEvent
        self.onImageComparisonResultsEvent(allBinaryEventObject)
    

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
        from org.allbinary.media.image.comparison.ImageComparisonResult import ImageComparisonResult
        from org.allbinary.string.CommonLabels import CommonLabels
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.RUN)
            self.setRunning(True)
            timeHelper: TimeDelayHelper = TimeDelayHelper(1000)
            timeHelper.setStartTimeTNT()
            imageComparisonInfo: ImageComparisonResult = self.imageComparisonInfoVector.get(0)
            self.logUtil.putF(str(imageComparisonInfo), self, self.commonStrings.RUN)
            latestBufferedImage: BufferedImage = imageComparisonInfo.getBufferedImages()[1]
            self.imageComparisonInfoVector.remove(imageComparisonInfo)
            self.index += 1
            self.logUtil.putF(CommonLabels.getInstance().ELAPSED + timeHelper.getElapsedTNT(), self, self.commonStrings.RUN)
            self.setRunning(False)
            self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.RUN)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.RUN, e)
# from java.awt.image.BufferedImage import BufferedImage
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.util.event.AllBinaryEventObject import AllBinaryEventObject
# from org.allbinary.media.image.comparison.ImageComparisonResult import ImageComparisonResult
# from org.allbinary.media.image.comparison.ImageComparisonResultsEvent import ImageComparisonResultsEvent
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


