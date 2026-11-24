# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.graphics.opengles.vbo

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.graphics.threed.min3d.renderer.processor.ObjectThreedOpenGLProcessor import ObjectThreedOpenGLProcessor


class ColorAttributePointerVBOOpenGLProcessor(ObjectThreedOpenGLProcessor):
    instance: ColorAttributePointerVBOOpenGLProcessor = None
    

    @staticmethod
    def getInstance() -> ColorAttributePointerVBOOpenGLProcessor:
        return ColorAttributePointerVBOOpenGLProcessor.instance
    

    def __init__(self) -> None:
        super().__init__()
    

    def process(self, gl: GL10, anyType: object) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        raise RuntimeError()
# from javax.microedition.khronos.opengles.GL10 import GL10


def _ColorAttributePointerVBOOpenGLProcessor_instance() -> object:
    return ColorAttributePointerVBOOpenGLProcessor()

lazy_static(ColorAttributePointerVBOOpenGLProcessor, "instance", _ColorAttributePointerVBOOpenGLProcessor_instance)

