#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
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



class OpenGLFeatureFactory:
    instance: OpenGLFeatureFactory = None

    def _init_fields(self) -> None:
        self.OPENGL_OPTIONS: OpenGLFeature = OpenGLFeature("OpenGL Options")
        self.OPENGL: OpenGLFeature = OpenGLFeature("OpenGL")
        self.OPENGL_SURFACE_VIEW: OpenGLFeature = OpenGLFeature("GLSurfaceView")
        self.OPENGL_2D: OpenGLFeature = OpenGLFeature("OpenGL 2D")
        self.OPENGL_3D: OpenGLFeature = OpenGLFeature("OpenGL 3D")
        self.OPENGL_2D_AND_3D: OpenGLFeature = OpenGLFeature("OpenGL 2D/3D")
        self.OPENGL_AUTO_SELECT: OpenGLFeature = OpenGLFeature("Auto Select")
        self.OPENGL_MINIMUM: OpenGLFeature = OpenGLFeature("Minimum")
        self.OPENGL_AS_GAME_THREAD: OpenGLFeature = OpenGLFeature("As game thread")
        self.OPENGL_AND_GAME_HAVE_DIFFERENT_THREADS: OpenGLFeature = OpenGLFeature("As different threads")
        self.IMAGE_COLOR_DEPTH_4444: OpenGLFeature = OpenGLFeature("4444")
        self.IMAGE_COLOR_DEPTH_8888: OpenGLFeature = OpenGLFeature("8888")
        self.IMAGE_COLOR_DEPTH_565: OpenGLFeature = OpenGLFeature("565")
        self.OPENGL_COLOR_DEPTH_4444: OpenGLFeature = OpenGLFeature("4444")
        self.OPENGL_COLOR_DEPTH_8888: OpenGLFeature = OpenGLFeature("8888")
        self.OPENGL_COLOR_DEPTH_565: OpenGLFeature = OpenGLFeature("565")
        self.OPENGL_DRAW_TEXTURE: OpenGLFeature = OpenGLFeature("GL_OES_draw_texture")
        self.OPENGL_VERTEX_BUFFER_OBJECT: OpenGLFeature = OpenGLFeature("vertex_buffer_object")
        self.OPENGL_SIMPLE_OBJECT3D_PROCESSOR: OpenGLFeature = OpenGLFeature("Simple Object3d Processor")
        self.OPENGL_COMPLEX_OBJECT3D_PROCESSOR: OpenGLFeature = OpenGLFeature("Complex Object3d Processor")
        self.OPENGL_SIMPLE_TEXTURE_PROCESSOR: OpenGLFeature = OpenGLFeature("Simple Texture Processor")
        self.OPENGL_COMPLEX_TEXTURE_PROCESSOR: OpenGLFeature = OpenGLFeature("Complex Texture Processor")
    

    @staticmethod
    def getInstance() -> OpenGLFeatureFactory:
        return OpenGLFeatureFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.graphics.opengles.OpenGLFeature import OpenGLFeature


OpenGLFeatureFactory.instance = OpenGLFeatureFactory()

