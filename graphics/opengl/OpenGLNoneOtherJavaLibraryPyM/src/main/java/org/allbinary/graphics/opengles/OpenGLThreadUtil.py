# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class OpenGLThreadUtil:
    instance: OpenGLThreadUtil = None
    

    @staticmethod
    def getInstance() -> OpenGLThreadUtil:
        return OpenGLThreadUtil.instance
    

    def set(self, glSurfaceView: object) -> None:
        pass
    

    def onPause(self) -> None:
        pass
    

    def onResume(self) -> None:
        pass


def _OpenGLThreadUtil_instance() -> object:
    return OpenGLThreadUtil()

lazy_static(OpenGLThreadUtil, "instance", _OpenGLThreadUtil_instance)

