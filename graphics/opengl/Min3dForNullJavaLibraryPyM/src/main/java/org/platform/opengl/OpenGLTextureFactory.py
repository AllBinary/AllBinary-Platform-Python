# Generated Code Do Not Modify
# package org.platform.opengl

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.platform.opengles.PlatformTextureBaseFactory import PlatformTextureBaseFactory


@java_inherited_overloads
class OpenGLTextureFactory(PlatformTextureBaseFactory):
    instance: OpenGLTextureFactory = None
    def _java_defaults(self):
        vars(self).setdefault("gluUtils", None)

    def _init_fields(self) -> None:
        self.gluUtils: OpenGLGLUUtils = OpenGLGLUUtils.getInstance()
    

    @staticmethod
    def getInstance() -> OpenGLTextureFactory:
        return OpenGLTextureFactory.instance
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def load(self, gl: GL10, target: int, level: int, image: Image, border: int, flip: bool) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        from javax.microedition.lcdui.Image import Image
        raise RuntimeError()
# from javax.microedition.khronos.opengles.GL10 import GL10
# from javax.microedition.lcdui.Image import Image
from org.platform.opengl.OpenGLGLUUtils import OpenGLGLUUtils


def _OpenGLTextureFactory_instance() -> object:
    return OpenGLTextureFactory()

lazy_static(OpenGLTextureFactory, "instance", _OpenGLTextureFactory_instance)

