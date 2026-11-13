# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class NullOpenGLProcessorFactory:
    instance: OpenGLProcessor = None
    

    @staticmethod
    def getInstance() -> OpenGLProcessor:
        return NullOpenGLProcessorFactory.instance


def _NullOpenGLProcessorFactory_instance() -> object:
    from org.allbinary.graphics.opengles.OpenGLProcessor import OpenGLProcessor
    return OpenGLProcessor()

lazy_static(NullOpenGLProcessorFactory, "instance", _NullOpenGLProcessorFactory_instance)

