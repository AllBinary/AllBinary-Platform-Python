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



class OrthogonalLightingOpenGLProcessorFactory:
    instance: OrthogonalLightingOpenGLProcessorFactory = None

    def _init_fields(self) -> None:
        self.sceneLightingOrthogonalModeOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()
        self.sceneLightsOrthogonalModeOpenGLProcessor: OpenGLProcessor = NullOpenGLProcessorFactory.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> OrthogonalLightingOpenGLProcessorFactory:
        return OrthogonalLightingOpenGLProcessorFactory.instance
from org.allbinary.graphics.opengles.NullOpenGLProcessorFactory import NullOpenGLProcessorFactory


OrthogonalLightingOpenGLProcessorFactory.instance = OrthogonalLightingOpenGLProcessorFactory()

