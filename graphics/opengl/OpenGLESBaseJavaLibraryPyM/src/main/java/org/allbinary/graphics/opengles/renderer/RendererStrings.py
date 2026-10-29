# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.graphics.opengles.renderer

from __future__ import annotations



class RendererStrings:
    instance: RendererStrings = None

    def _init_fields(self) -> None:
        self.ON_SURFACE_CREATED: str = "onSurfaceCreated"
        self.ON_SURFACE_CHANGED: str = "onSurfaceChanged"
        self.ON_DRAW_FRAME: str = "onDrawFrame"
        self.ON_DRAW_FRAME_THREED: str = "onDrawFrameThreed"
        self.ON_DRAW_FRAME_2D: str = "onDrawFrame2d"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> RendererStrings:
        return RendererStrings.instance


RendererStrings.instance = RendererStrings()

