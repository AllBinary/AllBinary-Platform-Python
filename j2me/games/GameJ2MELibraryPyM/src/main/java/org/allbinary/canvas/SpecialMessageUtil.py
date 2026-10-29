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
# package org.allbinary.canvas

from __future__ import annotations



class SpecialMessageUtil:
    SINGLETON: SpecialMessageUtil = None
    

    @staticmethod
    def getInstance() -> SpecialMessageUtil:
        return SpecialMessageUtil.SINGLETON
    

    def get(self) -> str:
        from org.allbinary.canvas.GameStatisticsFactory import GameStatisticsFactory
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(Memory.getInfo())
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(str(GameStatisticsFactory.getInstance()))
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(" Option: ")
        if Features.getInstance().isDefault(OpenGLFeatureFactory.getInstance().OPENGL_AUTO_SELECT):
            stringBuffer.append(OpenGLFeatureFactory.getInstance().OPENGL_AUTO_SELECT.getName())
        else:
            stringBuffer.append(OpenGLFeatureFactory.getInstance().OPENGL_MINIMUM.getName())
        return str(stringBuffer)
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.system.Memory import Memory


SpecialMessageUtil.SINGLETON = SpecialMessageUtil()

