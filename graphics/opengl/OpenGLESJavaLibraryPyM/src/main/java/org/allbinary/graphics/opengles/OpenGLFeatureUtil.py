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



class OpenGLFeatureUtil:
    instance: OpenGLFeatureUtil = None

    def _init_fields(self) -> None:
        self.anyThreed: bool = None
    

    @staticmethod
    def getInstance() -> OpenGLFeatureUtil:
        return OpenGLFeatureUtil.instance
    

    def __init__(self) -> None:
        from org.allbinary.graphics.opengles.OpenGLConfiguration import OpenGLConfiguration
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        self._init_fields()
        openGLConfiguration: OpenGLConfiguration = OpenGLConfiguration.getInstance()
        features: Features = Features.getInstance()
        openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
        self.anyThreed = openGLConfiguration.isOpenGL() and (features.isFeature(openGLFeatureFactory.OPENGL_2D_AND_3D) or features.isFeature(openGLFeatureFactory.OPENGL_3D))
    

    def isAnyThreed(self) -> bool:
        return self.anyThreed
from org.allbinary.game.configuration.feature.Features import Features


OpenGLFeatureUtil.instance = OpenGLFeatureUtil()

