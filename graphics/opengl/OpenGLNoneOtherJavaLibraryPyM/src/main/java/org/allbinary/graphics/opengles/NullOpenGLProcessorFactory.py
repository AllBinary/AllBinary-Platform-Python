# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles

from __future__ import annotations

from org.allbinary.graphics.opengles.OpenGLProcessor import OpenGLProcessor


class NullOpenGLProcessorFactory:
    instance: OpenGLProcessor = OpenGLProcessor()
    

    @staticmethod
    def getInstance() -> OpenGLProcessor:
        return NullOpenGLProcessorFactory.instance


