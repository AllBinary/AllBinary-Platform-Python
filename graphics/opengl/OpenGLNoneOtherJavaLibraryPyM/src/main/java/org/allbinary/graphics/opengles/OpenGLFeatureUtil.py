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
    

    @staticmethod
    def getInstance() -> OpenGLFeatureUtil:
        return OpenGLFeatureUtil.instance
    

    def __init__(self) -> None:
        pass
    

    def isAnyThreed(self) -> bool:
        return False


OpenGLFeatureUtil.instance = OpenGLFeatureUtil()

