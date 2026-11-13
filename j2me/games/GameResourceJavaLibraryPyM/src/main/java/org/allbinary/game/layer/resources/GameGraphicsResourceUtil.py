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
# package org.allbinary.game.layer.resources

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class GameGraphicsResourceUtil:
    instance: object = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.SPRITE: str = "_sprite"
        self.QUARTER: str = "_quarter"
        self.name: str = StringUtil.getInstance().EMPTY_STRING
    

    @staticmethod
    def getInstance() -> GameGraphicsResourceUtil:
        from org.allbinary.logic.NullUtil import NullUtil
        if GameGraphicsResourceUtil.instance == NullUtil.getInstance().NULL_OBJECT:
            GameGraphicsResourceUtil.instance = GameGraphicsResourceUtil()
        return GameGraphicsResourceUtil.instance
    

    def __init__(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self._init_fields()
        try:
            self.name = self.getString()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
    

    # throws Exception
    def getString(self) -> str:
        from org.allbinary.game.configuration.feature.Features import Features
        from org.allbinary.game.configuration.feature.GraphicsFeature import GraphicsFeature
        from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory
        graphicsFeatureFactory: GraphicsFeatureFactory = GraphicsFeatureFactory.getInstance()
        graphicsFeature: GraphicsFeature = graphicsFeatureFactory.NONE
        features: Features = Features.getInstance()
        if features.isFeature(graphicsFeatureFactory.IMAGE_TO_ARRAY_GRAPHICS):
            graphicsFeature = graphicsFeatureFactory.IMAGE_TO_ARRAY_GRAPHICS
        elif features.isFeature(graphicsFeatureFactory.SPRITE_FULL_GRAPHICS):
            graphicsFeature = graphicsFeatureFactory.SPRITE_FULL_GRAPHICS
        elif features.isFeature(graphicsFeatureFactory.SPRITE_QUARTER_ROTATION_GRAPHICS):
            graphicsFeature = graphicsFeatureFactory.SPRITE_QUARTER_ROTATION_GRAPHICS
        elif features.isFeature(graphicsFeatureFactory.IMAGE_ROTATION_ON_THE_FLY):
            graphicsFeature = graphicsFeatureFactory.IMAGE_ROTATION_ON_THE_FLY
        return self.getStringForFeature(graphicsFeature)
    

    # throws Exception
    def getStringForFeature(self, graphicsFeature: GraphicsFeature) -> str:
        from org.allbinary.game.configuration.feature.Features import Features
        from org.allbinary.game.configuration.feature.GraphicsFeature import GraphicsFeature
        from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory
        from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
        from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringBuffer: StringMaker = StringMaker()
        graphicsFeatureFactory: GraphicsFeatureFactory = GraphicsFeatureFactory.getInstance()
        stringBuffer.delete(0, stringBuffer.length())
        features: Features = Features.getInstance()
        if features.isFeature(graphicsFeatureFactory.VECTOR_GRAPHICS):
            pass
        elif features.isFeature(graphicsFeatureFactory.IMAGE_GRAPHICS):
            if graphicsFeature == graphicsFeatureFactory.IMAGE_TO_ARRAY_GRAPHICS or graphicsFeature == graphicsFeatureFactory.IMAGE_ROTATION_ON_THE_FLY:
                pass
            elif graphicsFeature == graphicsFeatureFactory.SPRITE_FULL_GRAPHICS:
                stringBuffer.append(self.SPRITE)
            elif graphicsFeature == graphicsFeatureFactory.SPRITE_QUARTER_ROTATION_GRAPHICS:
                stringBuffer.append(self.QUARTER)
                stringBuffer.append(self.SPRITE)
            else:
                raise Exception("None/Unknown Sub Image Resource Type Specified")
        elif OpenGLFeatureUtil.getInstance().isAnyThreed():
            stringBuffer.append(CanvasStrings.getInstance().OBJ_MODEL)
        else:
            raise Exception("None/Unknown Main Image Resource Type Specified")
        return str(stringBuffer)
    

    def getName(self) -> str:
        return self.name
# from org.allbinary.game.configuration.feature.Features import Features
# from org.allbinary.game.configuration.feature.GraphicsFeature import GraphicsFeature
# from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory
# from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
# from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonStrings import CommonStrings


def _GameGraphicsResourceUtil_instance() -> object:
    from org.allbinary.logic.NullUtil import NullUtil
    return NullUtil.getInstance().NULL_OBJECT

lazy_static(GameGraphicsResourceUtil, "instance", _GameGraphicsResourceUtil_instance)

