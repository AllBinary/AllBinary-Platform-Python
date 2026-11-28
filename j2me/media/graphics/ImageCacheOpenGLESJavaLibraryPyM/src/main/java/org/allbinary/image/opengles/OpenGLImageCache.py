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
# package org.allbinary.image.opengles

from __future__ import annotations

from java.lang.JavaMonitor import java_monitor, java_wait
from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from org.allbinary.image.ImageCache import ImageCache


#ImageCacheOpenGLESJavaLibrary
@java_inherited_overloads
class OpenGLImageCache(ImageCache):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("imageCache", None)
        vars(self).setdefault("preResourceImageUtil", None)
        vars(self).setdefault("gl", None)
        vars(self).setdefault("lock", None)
        vars(self).setdefault("list_", None)
        vars(self).setdefault("renderer", None)

    def _init_fields(self) -> None:
        from org.allbinary.device.NullGL10 import NullGL10
        from org.allbinary.graphics.opengles.renderer.AllBinaryRendererBase3 import AllBinaryRendererBase3
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
        from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
        from org.allbinary.thread.SynchObject import SynchObject
        self.imageCache: ImageCache = ImageCacheFactory.getInstance()
        self.preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
        self.gl: GL10 = NullGL10.NULL_GL10
        self.lock: SynchObject = SynchObject()
        self.list_: BasicArrayList = BasicArrayListD()
        self.renderer: AllBinaryRendererBase3 = AllBinaryRendererBase3()
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def addListener(self, renderer: object) -> None:
        from org.allbinary.graphics.opengles.renderer.AllBinaryRendererBase3 import AllBinaryRendererBase3
        self.renderer = renderer
    

    # throws Exception
    def update(self, gl: GL10) -> None:
        from org.allbinary.image.opengles.OpenGLESImage import OpenGLESImage
        from javax.microedition.khronos.opengles.GL10 import GL10
        self.gl = gl
        with java_monitor(self.lock):
            for index in range(self.list_.size() - 1, 0 - 1, -1):
                openGLESImage: OpenGLESImage = (self.list_.objectArray[index])
                if openGLESImage != OpenGLESImage.NULL_OPENGL_IMAGE:
                    openGLESImage.set(gl)
    

    # throws Exception
    def createImage(self, caller: str, width: int, height: int) -> Image:
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.NullImage import NullImage
        textureSize: int = width
        if height > width:
            textureSize = height
        while (textureSize % 4) != 0:
            textureSize += 1
        width = textureSize
        height = textureSize
        image2: Image = self.imageCache.get(caller, width, height)
        image: Image = self.preResourceImageUtil.encapsulate(image2)
        with java_monitor(self.lock):
            if image != NullImage.NULL_IMAGE:
                self.list_.add(image)
        return image
    

    # throws Exception
    def createImageFromInputStream(self, key: object, inputStream: InputStream) -> Image:
        from java.io.InputStream import InputStream
        from javax.microedition.lcdui.Image import Image
        from javax.microedition.lcdui.NullImage import NullImage
        cachedImage: Image = self.imageCache.getWithKey(key)
        image: Image = self.preResourceImageUtil.encapsulate(cachedImage)
        with java_monitor(self.lock):
            if image != NullImage.NULL_IMAGE:
                self.list_.add(image)
        return image
    

    def getGlP(self) -> GL10:
        from javax.microedition.khronos.opengles.GL10 import GL10
        return self.gl
    

    def init(self, image: Image) -> None:
        from javax.microedition.lcdui.Image import Image
        try:
            with java_monitor(self.lock):
                if self.list_.contains(image):
                    raise RuntimeError()
                self.list_.add(image)
            self.renderer.add(image)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
# from java.io.InputStream import InputStream
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
# from javax.microedition.lcdui.NullImage import NullImage
# from org.allbinary.device.NullGL10 import NullGL10
# from org.allbinary.graphics.opengles.renderer.AllBinaryRendererBase3 import AllBinaryRendererBase3
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.image.ImageCacheFactory import ImageCacheFactory
# from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
# from org.allbinary.thread.SynchObject import SynchObject


