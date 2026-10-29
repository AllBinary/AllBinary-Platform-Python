# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles

from __future__ import annotations

import threading


class OpenGLUtil:
    instance: OpenGLUtil = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.renderStrings: RendererStrings = RendererStrings.getInstance()
        self.canvasStrings: CanvasStrings = CanvasStrings.getInstance()
        self.displayInfoSingleton: DisplayInfoSingleton = DisplayInfoSingleton.getInstance()
        self.preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
        self.lockObject: SynchObject = SynchObject()
        self.anyType: SynchObject = SynchObject()
        self.list_: BasicArrayList = BasicArrayListD()
        self.runnableList: BasicArrayList = BasicArrayListD()
        self.created: bool = False
        self.surfaceCreatedAndInitialized: bool = False

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OpenGLUtil:
        return OpenGLUtil.instance
    

    def onSurfaceCreated(self, gl: GL10) -> None:
        from org.allbinary.graphics.opengles.OpenGLCapabilities import OpenGLCapabilities
        try:
            if not self.created:
                self.created = True
                PreLogUtil.put(str(CommonLabels.getInstance().START_LABEL) + str(OpenGLCapabilities.getInstance()), self, self.renderStrings.ON_SURFACE_CREATED)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.renderStrings.ON_SURFACE_CREATED, e)
    

    # Java overloaded method: Python keeps the last definition
    def onSurfaceCreated(self, gl: GL10, loadTextures: LoadTextures) -> None:
        from org.allbinary.graphics.opengles.OpenGLLogUtil import OpenGLLogUtil
        try:
            loadTextures.load(gl)
            OpenGLLogUtil.getInstance().logError(gl)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.renderStrings.ON_SURFACE_CREATED, e)
    

    # throws Exception
    def onSurfaceChanged(self, gl: GL10, graphics: OpenGLESGraphics) -> None:
        if not self.surfaceCreatedAndInitialized:
            graphics.init()
            self.surfaceCreatedAndInitialized = True
        graphics.update()
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        progressCanvas.update(graphics)
        (OpenGLImageCacheFactory.getInstance()).update(gl)
        self.processRunnables()
        self.set(gl)
    

    def addImage(self, image: Image) -> Image:
        encapsulateImage: Image = self.preResourceImageUtil.encapsulate(image)
        if encapsulateImage != image:
            with self._lock:  # synchronized (self.anyType)
                self.list_.add(encapsulateImage)
            return encapsulateImage
        return image
    

    def clear(self) -> None:
        with self._lock:  # synchronized (self.anyType)
            self.list_.clear()
    

    def addRunnable(self, runnable: object) -> None:
        with self._lock:  # synchronized (self.lockObject)
            if not self.runnableList.contains(runnable):
                self.runnableList.add(runnable)
                self.displayInfoSingleton.add(self.canvasStrings.SCALED_IMAGES)
    

    def processRunnables(self) -> None:
        with self._lock:  # synchronized (self.lockObject)
            runnable: object = None
            size: int = self.runnableList.size()
            for index in range(0, size):
                runnable = self.runnableList.get(index)
                runnable.run()
            self.runnableList.clear()
    

    # throws Exception
    def set(self, gl: GL10) -> None:
        size: int = self.list_.size()
        image: object = None
        for index2 in range(0, size):
            image = self.list_.get(index2)
            (image).set(gl)
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
from org.allbinary.device.LoadTextures import LoadTextures
from org.allbinary.device.OpenGLESGraphics import OpenGLESGraphics
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.displayable.DisplayInfoSingleton import DisplayInfoSingleton
from org.allbinary.graphics.opengles.renderer.RendererStrings import RendererStrings
from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
from org.allbinary.image.opengles.OpenGLImageCache import OpenGLImageCache
from org.allbinary.image.opengles.OpenGLImageCacheFactory import OpenGLImageCacheFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.thread.SynchObject import SynchObject
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


OpenGLUtil.instance = OpenGLUtil()

