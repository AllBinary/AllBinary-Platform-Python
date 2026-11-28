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

from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import lazy_static


class ChoiceGroupImageUtil:
    instance: ChoiceGroupImageUtil = None
    

    @staticmethod
    def getInstance() -> ChoiceGroupImageUtil:
        return ChoiceGroupImageUtil.instance
    

    def init(self) -> None:
        from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
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
        from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
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
        from org.allbinary.image.PreResourceImageUtil import PreResourceImageUtil
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
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "GL" for base in type(args[0]).__mro__)):
            return __class__.__dict__["update_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["update_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("update_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().update(*args)
# from javax.microedition.khronos.opengles.GL import GL
# from javax.microedition.lcdui.ChoiceGroupImageFactory import ChoiceGroupImageFactory
# from javax.microedition.lcdui.Graphics import Graphics
# from javax.microedition.lcdui.Image import Image
# from org.allbinary.graphics.opengles.OpenGLFeatureFactory import OpenGLFeatureFactory
# from org.allbinary.game.configuration.feature.Features import Features


def _ChoiceGroupImageUtil_instance() -> object:
    return ChoiceGroupImageUtil()

lazy_static(ChoiceGroupImageUtil, "instance", _ChoiceGroupImageUtil_instance)

