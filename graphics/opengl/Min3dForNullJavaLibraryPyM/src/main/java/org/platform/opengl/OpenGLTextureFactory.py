# Generated Code Do Not Modify
# package org.platform.opengl

from __future__ import annotations

from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory


class OpenGLTextureFactory(PlatformTextureBaseFactory):
    instance: OpenGLTextureFactory = None

    def _init_fields(self) -> None:
        self.gluUtils: OpenGLGLUUtils = OpenGLGLUUtils.getInstance()
    

    @staticmethod
    def getInstance() -> OpenGLTextureFactory:
        return OpenGLTextureFactory.instance
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def load(self, gl: GL10, target: int, level: int, image: Image, border: int, flip: bool) -> None:
        raise RuntimeError()
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
from org.platform.opengl.OpenGLGLUUtils import OpenGLGLUUtils


OpenGLTextureFactory.instance = OpenGLTextureFactory()

