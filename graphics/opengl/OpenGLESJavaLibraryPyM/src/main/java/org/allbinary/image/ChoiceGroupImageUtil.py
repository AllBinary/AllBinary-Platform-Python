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
# package org.allbinary.image

from __future__ import annotations



class ChoiceGroupImageUtil:
    instance: ChoiceGroupImageUtil = None
    

    @staticmethod
    def getInstance() -> ChoiceGroupImageUtil:
        return ChoiceGroupImageUtil.instance
    

    def init(self) -> None:
        from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
        features: Features = Features.getInstance()
        choiceGroupFactory: ChoiceGroupImageFactory = ChoiceGroupImageFactory.getInstance()
        imageArray: list[Image] = choiceGroupFactory.getImageArray()
        if features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
            preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
            size: int = len(imageArray)
            for index in range(0, size):
                imageArray[index] = preResourceImageUtil.encapsulate(imageArray[index])
            choiceGroupFactory.init(imageArray)
    

    def update(self, gl: GL) -> None:
        from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
        features: Features = Features.getInstance()
        choiceGroupFactory: ChoiceGroupImageFactory = ChoiceGroupImageFactory.getInstance()
        imageArray: list[Image] = choiceGroupFactory.getImageArray()
        if features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
            preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
            size: int = len(imageArray)
            for index in range(0, size):
                preResourceImageUtil.updateGL(gl, imageArray[index])
        choiceGroupFactory.init(imageArray)
    

    # Java overloaded method: Python keeps the last definition
    def update(self, graphics: Graphics) -> None:
        from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
        features: Features = Features.getInstance()
        choiceGroupFactory: ChoiceGroupImageFactory = ChoiceGroupImageFactory.getInstance()
        imageArray: list[Image] = choiceGroupFactory.getImageArray()
        if features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
            preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
            size: int = len(imageArray)
            for index in range(0, size):
                preResourceImageUtil.update(graphics, imageArray[index])
        choiceGroupFactory.init(imageArray)
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.ChoiceGroupImageFactory import ChoiceGroupImageFactory
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
from org.allbinary.game.configuration.feature.Features import Features


ChoiceGroupImageUtil.instance = ChoiceGroupImageUtil()

