# Generated Code Do Not Modify
# package org.allbinary.device

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class OpenGLESNullGraphicsFactory:
    instance: OpenGLESGraphics = None
    

    @staticmethod
    def getInstance() -> OpenGLESGraphics:
        return OpenGLESNullGraphicsFactory.instance


def _OpenGLESNullGraphicsFactory_instance() -> object:
    from org.allbinary.device.OpenGLESGraphics import OpenGLESGraphics
    return OpenGLESGraphics()

lazy_static(OpenGLESNullGraphicsFactory, "instance", _OpenGLESNullGraphicsFactory_instance)

