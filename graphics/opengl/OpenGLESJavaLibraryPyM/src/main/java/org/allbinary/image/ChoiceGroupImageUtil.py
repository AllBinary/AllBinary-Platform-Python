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

from java.lang.JavaRuntimeStatic import lazy_static


class ChoiceGroupImageUtil:
    instance: ChoiceGroupImageUtil = None
    

    @staticmethod
    def getInstance() -> ChoiceGroupImageUtil:
        return ChoiceGroupImageUtil.instance
    

    def init(self) -> None:
        from javax.microedition.lcdui.ChoiceGroupImageFactory import ChoiceGroupImageFactory
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.game.configuration.feature.Features import Features
        features: Features = Features.getInstance()
        choiceGroupFactory: ChoiceGroupImageFactory = ChoiceGroupImageFactory.getInstance()
        imageArray: list[Image] = choiceGroupFactory.getImageArray()
        if features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
            preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
            size: int = len(imageArray)
            for index in range(0, size):
                imageArray[index] = preResourceImageUtil.encapsulate(imageArray[index])
            choiceGroupFactory.init(imageArray)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def update_j1_1(self, gl: GL) -> None:
        from javax.microedition.khronos.opengles.GL import GL
        from javax.microedition.lcdui.ChoiceGroupImageFactory import ChoiceGroupImageFactory
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.game.configuration.feature.Features import Features
        features: Features = Features.getInstance()
        choiceGroupFactory: ChoiceGroupImageFactory = ChoiceGroupImageFactory.getInstance()
        imageArray: list[Image] = choiceGroupFactory.getImageArray()
        if features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
            preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
            size: int = len(imageArray)
            for index in range(0, size):
                preResourceImageUtil.updateGL(gl, imageArray[index])
        choiceGroupFactory.init(imageArray)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def update_j1_2(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.ChoiceGroupImageFactory import ChoiceGroupImageFactory
        from javax.microedition.lcdui.Graphics import Graphics
        from javax.microedition.lcdui.Image import Image
        from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
        from org.allbinary.game.configuration.feature.Features import Features
        features: Features = Features.getInstance()
        choiceGroupFactory: ChoiceGroupImageFactory = ChoiceGroupImageFactory.getInstance()
        imageArray: list[Image] = choiceGroupFactory.getImageArray()
        if features.isDefault(OpenGLFeatureFactory.getInstance().OPENGL):
            preResourceImageUtil: PreResourceImageUtil = PreResourceImageUtil.getInstance()
            size: int = len(imageArray)
            for index in range(0, size):
                preResourceImageUtil.update(graphics, imageArray[index])
        choiceGroupFactory.init(imageArray)

    def update(self, *args):
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return self.update_j1_1(*args)
        if len(args) == 1:
            return self.update_j1_2(*args)
        return getattr(self, "update_j" + str(len(args)))(*args)
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.ChoiceGroupImageFactory import ChoiceGroupImageFactory
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
# from org.allbinary.game.configuration.feature.Features import Features


def _ChoiceGroupImageUtil_instance() -> object:
    return ChoiceGroupImageUtil()

lazy_static(ChoiceGroupImageUtil, "instance", _ChoiceGroupImageUtil_instance)

