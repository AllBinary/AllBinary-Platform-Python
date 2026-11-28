# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.thread

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_new_inner
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.thread.BaseImageLoadingProcessor import BaseImageLoadingProcessor
from org.allbinary.thread.ABRunnable import ABRunnable


@java_inherited_overloads
class ConcurrentImageLoadingProcessor(BaseImageLoadingProcessor):
    @java_inherited_overloads
    class ImageCacheRunnable(ABRunnable):
        def _java_defaults(self):
            vars(self).setdefault("imageCache", None)

        def _init_fields(self) -> None:
            if "imageCache" not in vars(self): self.imageCache: ImageCache = None
        

        def __init__(self, imageCache: ImageCache) -> None:
            __class__._java_defaults(self)
            from org.allbinary.image.ImageCache import ImageCache
            super().__init__()
            __class__._init_fields(self)
            self.imageCache = imageCache
        

        def run(self) -> None:
            from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
            from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.string.CommonStrings import CommonStrings
            logUtil: LogUtil = LogUtil.getInstance()
            try:
                self.setRunning(True)
                self.imageCache.waitForLoadNow()
                self.imageCache.loadImages()
                self.imageCache.loadRemainingAnimations()
                self.setRunning(False)
                progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
                if not (progressCanvas.inProgress):
                    progressCanvas.endFromInitialLazyLoadingComplete()
            except Exception as e:
                self.setRunning(False)
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("runnable", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "runnable" not in vars(self): self.runnable: ABRunnable = None
    

    def __init__(self, imageCache: ImageCache) -> None:
        __class__._java_defaults(self)
        from org.allbinary.image.ImageCache import ImageCache
        super().__init__()
        __class__._init_fields(self)
        self.runnable = java_new_inner(self, ConcurrentImageLoadingProcessor.ImageCacheRunnable, imageCache)
    

    def runTask(self) -> None:
        from org.allbinary.thread.ImageThreadPool import ImageThreadPool
        if not (java_predicate(self.runnable, "isRunning")):
            ImageThreadPool.getInstance().runTask(self.runnable)
# from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
# from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
# from org.allbinary.image.ImageCache import ImageCache
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings


