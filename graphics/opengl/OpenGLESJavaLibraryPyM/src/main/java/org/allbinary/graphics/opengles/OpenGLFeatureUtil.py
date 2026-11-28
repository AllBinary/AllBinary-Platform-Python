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

from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import lazy_static


class OpenGLFeatureUtil:
    instance: OpenGLFeatureUtil = None

    def _init_fields(self) -> None:
        if "anyThreed" not in vars(self): self.anyThreed: bool = False
    

    @staticmethod
    def getInstance() -> OpenGLFeatureUtil:
        return OpenGLFeatureUtil.instance
    

    def __init__(self) -> None:
        from org.allbinary.graphics.opengles.OpenGLConfiguration import OpenGLConfiguration
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.game.configuration.feature.Features import Features
        __class__._init_fields(self)
        openGLConfiguration: OpenGLConfiguration = OpenGLConfiguration.getInstance()
        features: Features = Features.getInstance()
        openGLFeatureFactory: OpenGLFeatureFactory = OpenGLFeatureFactory.getInstance()
        self.anyThreed = java_predicate(openGLConfiguration, "isOpenGL") and (features.isFeature(openGLFeatureFactory.OPENGL_2D_AND_3D) or features.isFeature(openGLFeatureFactory.OPENGL_3D))
    

    def isAnyThreed(self) -> bool:
        return self.anyThreed
# from org.allbinary.game.configuration.feature.Features import Features


def _OpenGLFeatureUtil_instance() -> object:
    return OpenGLFeatureUtil()

lazy_static(OpenGLFeatureUtil, "instance", _OpenGLFeatureUtil_instance)

