# Generated Code Do Not Modify
# package org.allbinary.graphics.opengles

from __future__ import annotations

from org.allbinary.graphics.threed.min3d.renderer.processor.ObjectThreedOpenGLProcessor import ObjectThreedOpenGLProcessor


class EnableFacesShaderOpenGLProcessor(ObjectThreedOpenGLProcessor):
    instance: EnableFacesShaderOpenGLProcessor = None
    

    @staticmethod
    def getInstance() -> EnableFacesShaderOpenGLProcessor:
        return EnableFacesShaderOpenGLProcessor.instance
    

    def __init__(self) -> None:
        super().__init__()
    

    def process(self, gl: GL10, anyType: object) -> None:
        pass
# from javax.microedition.khronos.opengles.GL10 import GL10


EnableFacesShaderOpenGLProcessor.instance = EnableFacesShaderOpenGLProcessor()

