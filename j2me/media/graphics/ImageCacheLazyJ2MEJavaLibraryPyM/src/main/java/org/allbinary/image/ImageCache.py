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
# package org.allbinary.image

from __future__ import annotations

import time
from java.lang.JavaMonitor import java_monitor, java_wait
from java.lang.JavaRuntimeStatic import java_new_inner
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.canvas.Processor import Processor
from org.allbinary.image.ImageCacheBase import ImageCacheBase


@java_inherited_overloads
class ImageCache(ImageCacheBase):
    NULL_IMAGE_CACHE: ImageCache = None
    _lock = threading.RLock()
    @java_inherited_overloads
    class NotHTMLProcessor(Processor):

        def __init__(self) -> None:
            super().__init__()
        

        def process(self) -> None:
            self._java_outer.concurrentImageLoadingProcessor.runTask()
    @java_inherited_overloads
    class NotHTMLEndProcessor(Processor):

        def __init__(self) -> None:
            super().__init__()
        

        def process(self) -> None:
            from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
            from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
            progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
            progressCanvas.endIfPaintedSinceStart()
    @java_inherited_overloads
    class HTMLEndProcessor(Processor):

        def __init__(self) -> None:
            super().__init__()
        

        def process(self) -> None:
            from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
            from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
            size: int = self._java_outer.gdResources.currentLayoutRequiredTotal
            if size == 0:
                progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
                progressCanvas.endIfPaintedSinceStart()
            elif self._java_outer.totalLoaded > int(size / 12):
                progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
                progressCanvas.endIfPaintedSinceStart()
                self._java_outer.endProcessor = java_new_inner(self, ImageCache.NotHTMLEndProcessor)
    @java_inherited_overloads
    class FirstProcessor(Processor):

        def __init__(self) -> None:
            super().__init__()
        

        def process(self) -> None:
            self._java_outer.firstProcess()
    def _java_defaults(self):
        vars(self).setdefault("tsUtil", None)
        vars(self).setdefault("concurrentImageLoadingProcessor", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("commonSeps", None)
        vars(self).setdefault("resourceUtil", None)
        vars(self).setdefault("gameGlobalsFactory", None)
        vars(self).setdefault("gdResources", None)
        vars(self).setdefault("loadNowList", None)
        vars(self).setdefault("loadSoonList", None)
        vars(self).setdefault("loadList", None)
        vars(self).setdefault("loadAfterList", None)
        vars(self).setdefault("lock", None)
        vars(self).setdefault("firstTime", False)
        vars(self).setdefault("totalLoaded", 0)
        vars(self).setdefault("progressEnded", False)
        vars(self).setdefault("hasAnyLazyAnimationFactories", False)
        vars(self).setdefault("processor", None)
        vars(self).setdefault("endProcessor", None)
        vars(self).setdefault("LOAD_IMAGE_FOR_ANIMATION", None)

    def _init_fields(self) -> None:
        from org.allbinary.TsUtil import TsUtil
        from org.allbinary.canvas.GameGlobalsFactory import GameGlobalsFactory
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.data.resource.ResourceUtil import ResourceUtil
        from org.allbinary.game.gd.resource.GDResources import GDResources
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.thread.ConcurrentImageLoadingProcessor import ConcurrentImageLoadingProcessor
        from org.allbinary.thread.SynchObject import SynchObject
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.tsUtil: TsUtil = TsUtil.getInstance()
        self.concurrentImageLoadingProcessor: BaseImageLoadingProcessor = ConcurrentImageLoadingProcessor(self)
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.resourceUtil: ResourceUtil = ResourceUtil.getInstance()
        self.gameGlobalsFactory: GameGlobalsFactory = GameGlobalsFactory.getInstance()
        self.gdResources: GDResources = GDResources.getInstance()
        self.loadNowList: BasicArrayList = BasicArrayListD()
        self.loadSoonList: BasicArrayList = BasicArrayListD()
        self.loadList: BasicArrayList = BasicArrayListD()
        self.loadAfterList: BasicArrayList = BasicArrayListD()
        self.lock: SynchObject = SynchObject()
        self.firstTime: bool = True
        self.totalLoaded: int = 0
        self.progressEnded: bool = False
        self.hasAnyLazyAnimationFactories: bool = False
        self.processor: Processor = java_new_inner(self, FirstProcessor)
        self.endProcessor: Processor = Processor.getInstance()
        self.LOAD_IMAGE_FOR_ANIMATION: str = "Load Image Animation"
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def firstProcess(self) -> None:
        from org.allbinary.J2MEUtil import J2MEUtil
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        logUtil: LogUtil = LogUtil.getInstance()
        isHTML: bool = java_predicate(J2MEUtil, "isHTML")
        if isHTML:
            self.processor = Processor.getInstance()
            self.endProcessor = java_new_inner(self, ImageCache.HTMLEndProcessor)
        else:
            self.processor = java_new_inner(self, ImageCache.NotHTMLProcessor)
            self.endProcessor = java_new_inner(self, ImageCache.NotHTMLEndProcessor)
            try:
                self.runTask()
            except Exception as e:
                logUtil.putF(self.commonStrings.EXCEPTION, self, self.commonStrings.END_METHOD_NAME)
    

    def addListener(self, renderer: object) -> None:
        pass
    

    # throws Exception
    def waitForLoadNow(self) -> None:
        from org.allbinary.game.canvas.ABToGBUtil import ABToGBUtil
        from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
        if self.firstTime:
            abToGBUtil: ABToGBUtil = ABToGBUtil.getInstance()
            abCanvas: AllBinaryGameCanvas = abToGBUtil.abCanvas
            while java_predicate(self.loadNowList, "isEmpty") and (not (java_predicate(abCanvas, "isInitialized")) or (java_predicate(abCanvas, "isInitialized") and self.hasAnyLazyAnimationFactories)) and not (self.progressEnded):
                time.sleep((120) / 1000)
            self.firstTime = False
    

    # throws Exception
    def loadImageForAnimation(self) -> None:
        from org.allbinary.J2MEUtil import J2MEUtil
        from org.allbinary.animation.image.LazyImageRotationAnimation import LazyImageRotationAnimation
        from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
        from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
        from org.allbinary.util.BasicArrayList import BasicArrayList
        lazyImageRotationAnimation: LazyImageRotationAnimation = None
        with java_monitor(self.lock):
            if java_predicate(self.loadNowList, "isEmpty"):
                self.endProcessor.process()
                if java_predicate(self.loadSoonList, "isEmpty"):
                    if java_predicate(self.loadAfterList, "isEmpty"):
                        if self.firstTime:
                            pass
                        elif self.gameGlobalsFactory.newCanvas:
                            pass
                        else:
                            self.loadNextImage()
                        return
                    else:
                        lazyImageRotationAnimation = self.loadAfterList.get(0)
                        if self.loadImageForLazyAnimation(lazyImageRotationAnimation):
                            self.loadAfterList.remove(lazyImageRotationAnimation)
                else:
                    lazyImageRotationAnimation = self.loadSoonList.get(0)
                    if self.loadImageForLazyAnimation(lazyImageRotationAnimation):
                        self.loadSoonList.remove(lazyImageRotationAnimation)
                return
            lazyImageRotationAnimation = self.loadNowList.get(0)
        if self.loadImageForLazyAnimation(lazyImageRotationAnimation):
            with java_monitor(self.lock):
                self.loadNowList.remove(lazyImageRotationAnimation)
            if lazyImageRotationAnimation.layoutIndex != 0:
                list_: BasicArrayList = self.getAssociated(lazyImageRotationAnimation)
                with java_monitor(self.lock):
                    size: int = list_.size()
                    if size > 0:
                        self.loadSoonList.addAllList(list_)
            progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
            isHTML: bool = java_predicate(J2MEUtil, "isHTML")
            if java_predicate(self.loadNowList, "isEmpty") and (not (isHTML) or self.firstTime):
                progressCanvas.endFromInitialLazyLoadingComplete()
            else:
                if self.totalLoaded % 10 == 0:
                    progressCanvas.addNormalPortion(1, self.LOAD_IMAGE_FOR_ANIMATION)
    

    # throws Exception
    def loadImages(self) -> None:
        while not (java_predicate(self.loadList, "isEmpty")) or not (java_predicate(self.loadNowList, "isEmpty")):
            self.loadImageForAnimations()
            self.loadNextImage()
    

    # throws Exception
    def loadImageForAnimations(self) -> None:
        while not (java_predicate(self.loadNowList, "isEmpty")):
            self.loadImageForAnimation()
    

    # throws Exception
    def loadRemainingAnimations(self) -> None:
        from org.allbinary.animation.image.LazyImageRotationAnimation import LazyImageRotationAnimation
        while not (java_predicate(self.loadAfterList, "isEmpty")) or not (java_predicate(self.loadNowList, "isEmpty")):
            while not (java_predicate(self.loadNowList, "isEmpty")):
                self.loadImageForAnimation()
            lazyImageRotationAnimation: LazyImageRotationAnimation = None
            with java_monitor(self.lock):
                if not (java_predicate(self.loadAfterList, "isEmpty")):
                    lazyImageRotationAnimation = self.loadAfterList.removeAt(0)
            if lazyImageRotationAnimation is not None:
                self.loadImageForLazyAnimation(lazyImageRotationAnimation)
    

    # throws Exception
    def loadImageForLazyAnimation(self, lazyImageRotationAnimation: LazyImageRotationAnimation) -> bool:
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.animation.image.LazyImageRotationAnimation import LazyImageRotationAnimation
        image: Image = lazyImageRotationAnimation.animationInterfaceFactoryInterface.getImage()
        if self.loadImage(image):
            lazyImageRotationAnimation.setRealAnimation()
            return True
        return False
    

    # throws Exception
    def loadNextImage(self) -> None:
        from javax.microedition.lcdui.Image import Image
        image: Image = None
        with java_monitor(self.lock):
            if self.loadList.size() == 0:
                return
            image = self.loadList.removeAt(0)
        self.loadImage(image)
    

    # throws Exception
    def loadImage(self, image: Image) -> bool:
        from javax.microedition.lcdui.Image import Image
        if java_predicate(image, "isReady"):
            return True
        else:
            if image.getImage() is not None:
                if image.setReady():
                    if java_predicate(image, "isReady"):
                        self.totalLoaded += 1
                        return True
            else:
                key: str = image.getName()
                image2: Image = self.creatImage(key)
                if java_predicate(image2, "isReady"):
                    self.init(image, image2)
                    return True
                else:
                    image.setImage(image2.getImage())
        return False
    

    # throws Exception
    def init(self, image: Image, image2: Image) -> None:
        from javax.microedition.lcdui.Image import Image
        image.init(image2.getImage())
    

    # throws Exception
    def creatImage(self, key: str) -> Image:
        from org.allbinary.image.ImageFactory import ImageFactory
        from java.io.InputStream import InputStream
        from javax.microedition.lcdui.Image import Image
        inputStream: InputStream = self.resourceUtil.getResourceAsStream(key)
        image: Image = ImageFactory.getInstance().createImageFromInputStream(inputStream)
        image.setName(key)
        return image
    

    # throws Exception
    def get(self, caller: str, width: int, height: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.NullImage import NullImage
        foundIndex: int = self.getIndexWH(width, height)
        image: Image = self.getFromAvailable(foundIndex, width, height)
        if image == NullImage.NULL_IMAGE:
            self.volume += width * height
            if self.volume > 32000:
                self.tsUtil.gc()
                self.volume = 0
            image = self.createImage(caller, width, height)
            if self.nextIndex > len(self.widths) - 1:
                if foundIndex == -1:
                    foundIndex = self.nextIndex
                    self.widths[self.nextIndex] = width
                    self.heights[self.nextIndex] = height
                    self.nextIndex += 1
                self.listOfList[foundIndex].add(image)
        return image
    

    # throws Exception
    def getWithKey(self, key: object) -> Image:
        from java.io.InputStream import InputStream
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.NullImage import NullImage
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.system.Memory import Memory
        image: Image = self.getImage(key)
        if image == NullImage.NULL_IMAGE:
            inputStream: InputStream = None
            try:
                image = self.createImageFromInputStream(key, inputStream)
            except Exception as e:
                self.logUtil.put("Exception: Trying Again After GC", self, self.commonStrings.GET, e)
                self.logUtil.putF(str(StringMaker().append("InputStream: ").append(StringUtil.getInstance().toString(inputStream))), self, self.commonStrings.GET)
                self.tsUtil.gc()
                self.tsUtil.gc()
                self.logUtil.putF(Memory.getInfo(), self, self.commonStrings.GET)
                time.sleep((100) / 1000)
                image = self.createImageFromInputStream(key, inputStream)
            self.hashtable.put(key, image)
        return image
    

    def getIndex(self, key: object) -> int:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.game.gd.resource.GDResources import GDResources
        from org.allbinary.logic.string.StringUtil import StringUtil
        gdResources: GDResources = GDResources.getInstance()
        resourceStringArray: list[str] = gdResources.resourceStringArray
        size: int = len(resourceStringArray)
        for index in range(0, size):
            if resourceStringArray[index] == key:
                return index
        self.logUtil.putF(str(StringMaker().append("unable to find key: ").append(StringUtil.getInstance().toString(key))), self, self.commonStrings.RUN)
        raise RuntimeError()
    

    # throws Exception
    def createImageFromInputStream(self, key: object, inputStream: InputStream) -> Image:
        from java.io.InputStream import InputStream
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.game.gd.resource.GDLazyResources import GDLazyResources
        gdLazyResources: GDLazyResources = GDLazyResources.getInstance()
        resourceStringArray: list[str] = gdLazyResources.requiredResourcesBeforeLoadingArray
        size: int = len(resourceStringArray)
        for index in range(0, size):
            if key == resourceStringArray[index]:
                return self.creatImage(key)
        self.runTask()
        index: int = self.getIndex(key)
        width: int = gdLazyResources.imageResourceWidthArray[index]
        height: int = gdLazyResources.imageResourceHeightArray[index]
        image: Image = self.createImageLater(key, width, height)
        with java_monitor(self.lock):
            self.loadList.add(image)
        return image
    

    # throws Exception
    def createImageLater(self, key: str, width: int, height: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        return Image.createImageLater(key, width, height)
    

    def getAssociated(self, lazyImageRotationAnimation: LazyImageRotationAnimation) -> BasicArrayList:
        from org.allbinary.animation.image.LazyImageRotationAnimation import LazyImageRotationAnimation
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        list_: BasicArrayList = BasicArrayListD()
        with java_monitor(self.lock):
            lazyImageRotationAnimation2: LazyImageRotationAnimation = None
            size: int = self.loadAfterList.size()
            for index in range(0, size):
                lazyImageRotationAnimation2 = self.loadAfterList.get(index)
                if lazyImageRotationAnimation2.instanceId == lazyImageRotationAnimation.instanceId:
                    list_.add(lazyImageRotationAnimation2)
            size2: int = list_.size()
            for index in range(0, size2):
                self.loadAfterList.remove(list_.get(index))
        return list_
    

    def add(self, lazyImageRotationAnimation: LazyImageRotationAnimation) -> None:
        from org.allbinary.animation.image.LazyImageRotationAnimation import LazyImageRotationAnimation
        with java_monitor(self.lock):
            self.loadAfterList.add(lazyImageRotationAnimation)
    

    # throws Exception
    def insertFirst(self, lazyImageRotationAnimation: LazyImageRotationAnimation) -> None:
        from org.allbinary.animation.image.LazyImageRotationAnimation import LazyImageRotationAnimation
        if self.loadNowList.contains(lazyImageRotationAnimation):
            pass
        else:
            with java_monitor(self.lock):
                self.loadNowList.add(lazyImageRotationAnimation)
                self.loadAfterList.remove(lazyImageRotationAnimation)
        self.runTask()
    

    def progressEnded(self) -> None:
        self.progressEnded = True
    

    # throws Exception
    def runTask(self) -> None:
        self.processor.process()
    

    def initProgress(self) -> None:
        if self.firstTime:
            self.firstTime = False
    

    def isLazy(self) -> bool:
        return True
# from java.io.InputStream import InputStream
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
# from org.allbinary.J2MEUtil import J2MEUtil
# from org.allbinary.TsUtil import TsUtil
# from org.allbinary.animation.image.LazyImageRotationAnimation import LazyImageRotationAnimation
# from org.allbinary.canvas.GameGlobalsFactory import GameGlobalsFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.data.resource.ResourceUtil import ResourceUtil
# from org.allbinary.game.canvas.ABToGBUtil import ABToGBUtil
# from org.allbinary.game.displayable.canvas.AllBinaryGameCanvas import AllBinaryGameCanvas
# from org.allbinary.game.gd.resource.GDLazyResources import GDLazyResources
# from org.allbinary.game.gd.resource.GDResources import GDResources
# from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
# from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.system.Memory import Memory
# from org.allbinary.thread.BaseImageLoadingProcessor import BaseImageLoadingProcessor
# from org.allbinary.thread.ConcurrentImageLoadingProcessor import ConcurrentImageLoadingProcessor
# from org.allbinary.thread.SynchObject import SynchObject
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.ABSystemWrapper import ABSystemWrapper


def _ImageCache_NULL_IMAGE_CACHE() -> object:
    return ImageCache()

lazy_static(ImageCache, "NULL_IMAGE_CACHE", _ImageCache_NULL_IMAGE_CACHE)

