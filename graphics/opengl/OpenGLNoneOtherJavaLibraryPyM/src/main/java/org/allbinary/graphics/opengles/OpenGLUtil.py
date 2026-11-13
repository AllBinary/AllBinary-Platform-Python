# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class OpenGLUtil:
    instance: OpenGLUtil = None
    

    @staticmethod
    def getInstance() -> OpenGLUtil:
        return OpenGLUtil.instance
    

    def addImage(self, image: Image) -> Image:
        from javax.microedition.lcdui.Image import Image
        return image
    

    def clear(self) -> None:
        pass
    

    def addRunnable(self, runnable: object) -> None:
        pass
# from javax.microedition.lcdui.Image import Image


def _OpenGLUtil_instance() -> object:
    return OpenGLUtil()

lazy_static(OpenGLUtil, "instance", _OpenGLUtil_instance)

