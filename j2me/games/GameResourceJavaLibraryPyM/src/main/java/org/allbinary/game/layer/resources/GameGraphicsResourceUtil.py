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

from org.allbinary.logic.NullUtil import NullUtil


class GameGraphicsResourceUtil:
    instance: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.SPRITE: str = "_sprite"
        self.QUARTER: str = "_quarter"
        self.name: str = StringUtil.getInstance().EMPTY_STRING
    

    @staticmethod
    def getInstance() -> GameGraphicsResourceUtil:
        if GameGraphicsResourceUtil.instance == NullUtil.getInstance().NULL_OBJECT:
            GameGraphicsResourceUtil.instance = GameGraphicsResourceUtil()
        return GameGraphicsResourceUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
        try:
            self.name = self.getString()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CONSTRUCTOR, e)
    

    # throws Exception
    def getString(self) -> str:
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
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GraphicsFeature import GraphicsFeature
from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory
from org.allbinary.graphics.displayable.CanvasStrings import CanvasStrings
from org.allbinary.graphics.opengles.OpenGLFeatureUtil import OpenGLFeatureUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


