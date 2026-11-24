# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.graphics.threed.min3d.renderer.processor.ObjectThreedOpenGLProcessor import ObjectThreedOpenGLProcessor


class EnableFacesShaderOpenGLProcessor(ObjectThreedOpenGLProcessor):
    instance: EnableFacesShaderOpenGLProcessor = None
    

    @staticmethod
    def getInstance() -> EnableFacesShaderOpenGLProcessor:
        return EnableFacesShaderOpenGLProcessor.instance
    

    def __init__(self) -> None:
        super().__init__()
    

    def process(self, gl: GL10, anyType: object) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        pass
# from javax.microedition.khronos.opengles.GL10 import GL10


def _EnableFacesShaderOpenGLProcessor_instance() -> object:
    return EnableFacesShaderOpenGLProcessor()

lazy_static(EnableFacesShaderOpenGLProcessor, "instance", _EnableFacesShaderOpenGLProcessor_instance)

