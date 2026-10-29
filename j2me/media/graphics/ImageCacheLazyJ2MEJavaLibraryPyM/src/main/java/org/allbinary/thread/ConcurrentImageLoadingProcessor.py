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

from org.allbinary.thread.BaseImageLoadingProcessor import BaseImageLoadingProcessor


class ConcurrentImageLoadingProcessor(BaseImageLoadingProcessor):
    class ImageCacheRunnable(ABRunnable):

        def _init_fields(self) -> None:
            self.imageCache: ImageCache = None
        

        def __init__(self, imageCache: ImageCache) -> None:
            super().__init__()
            self._init_fields()
            self.imageCache = imageCache
        

        def run(self) -> None:
            logUtil: LogUtil = LogUtil.getInstance()
            try:
                self.setRunning(True)
                self.imageCache.waitForLoadNow()
                self.imageCache.loadImages()
                self.imageCache.loadRemainingAnimations()
                self.setRunning(False)
                progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
                if not progressCanvas.inProgress:
                    progressCanvas.endFromInitialLazyLoadingComplete()
            except Exception as e:
                self.setRunning(False)
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.runnable: ABRunnable = None
    

    def __init__(self, imageCache: ImageCache) -> None:
        from org.allbinary.thread.ImageCacheRunnable import ImageCacheRunnable
        super().__init__()
        self._init_fields()
        self.runnable = ImageCacheRunnable(imageCache)
    

    def runTask(self) -> None:
        from org.allbinary.thread.ImageThreadPool import ImageThreadPool
        if not self.runnable.isRunning():
            ImageThreadPool.getInstance().runTask(self.runnable)
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


