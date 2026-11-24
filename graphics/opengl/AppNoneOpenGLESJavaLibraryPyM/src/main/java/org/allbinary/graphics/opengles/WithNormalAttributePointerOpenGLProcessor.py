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
# package org.allbinary.graphics.opengles

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.graphics.threed.min3d.renderer.processor.ObjectThreedOpenGLProcessor import ObjectThreedOpenGLProcessor


class WithNormalAttributePointerOpenGLProcessor(ObjectThreedOpenGLProcessor):
    instance: WithNormalAttributePointerOpenGLProcessor = None
    

    @staticmethod
    def getInstance() -> WithNormalAttributePointerOpenGLProcessor:
        return WithNormalAttributePointerOpenGLProcessor.instance
    

    def __init__(self) -> None:
        super().__init__()
    

    def process(self, gl: GL10, aObject3d: object) -> None:
        from javax.microedition.khronos.opengles.GL10 import GL10
        raise RuntimeError()
# from javax.microedition.khronos.opengles.GL10 import GL10


def _WithNormalAttributePointerOpenGLProcessor_instance() -> object:
    return WithNormalAttributePointerOpenGLProcessor()

lazy_static(WithNormalAttributePointerOpenGLProcessor, "instance", _WithNormalAttributePointerOpenGLProcessor_instance)

