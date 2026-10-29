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
# package org.allbinary.game.resource

from __future__ import annotations



class FeaturedResourceFactory:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.list_: BasicArrayList = BasicArrayListD()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.ANIMATION_FEATURES: str = "Animation Features: Vector: "
        self.IMAGE_LABEL: str = " Image: "
        self.IMAGE_GRAPHICS_ARRAY: str = "Image Array: "
        self.IMAGE_GRAPHICS_ROTATION: str = "Image Rotate: "
        self.SPRITE_QUARTER: str = " Sprite Quarter: "
        self.SPRITE_FULL: str = " Sprite Full: "
        self.IS_LOADING_LEVEL_LABEL: str = " isLoadingLevel "
        self.IS_FEATURE: str = " isFeature: "
        self.GAME_FEATURE_CONTROLLED: str = "GameFeatureControlledInterface: "
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def init(self, level: int) -> None:
        from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory
        size: int = self.list_.size()
        for index in range(0, size):
            featureInterface: GameFeatureControlledInterface = self.list_.objectArray[index]
            isLoadingLevel: bool = featureInterface.isLoadingLevel(level)
            isFeature: bool = featureInterface.isFeature()
            self.logUtil.putF(str(StringMaker().append(self.GAME_FEATURE_CONTROLLED).append(str(featureInterface)).append(self.IS_LOADING_LEVEL_LABEL).append(ResourceLoadingLevelFactory.getInstance().getLevelString(level)).append(CommonSeps.getInstance().COLON_SEP).appendboolean(isLoadingLevel).append(self.IS_FEATURE).appendboolean(isFeature)), self, self.commonStrings.INIT)
            if isLoadingLevel and isFeature:
                featureInterface.init(level)
        features: Features = Features.getInstance()
        graphicsFeatureFactory: GraphicsFeatureFactory = GraphicsFeatureFactory.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.ANIMATION_FEATURES)
        stringBuffer.appendboolean(features.isFeature(graphicsFeatureFactory.VECTOR_GRAPHICS))
        stringBuffer.append(self.IMAGE_LABEL)
        stringBuffer.appendboolean(features.isFeature(graphicsFeatureFactory.IMAGE_GRAPHICS))
        self.logUtil.putF(str(stringBuffer), self, self.commonStrings.INIT)
        if features.isFeature(graphicsFeatureFactory.IMAGE_GRAPHICS):
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(self.IMAGE_GRAPHICS_ARRAY)
            stringBuffer.appendboolean(features.isFeature(graphicsFeatureFactory.IMAGE_TO_ARRAY_GRAPHICS))
            stringBuffer.append(self.IMAGE_GRAPHICS_ROTATION)
            stringBuffer.appendboolean(features.isFeature(graphicsFeatureFactory.IMAGE_TO_ARRAY_GRAPHICS))
            stringBuffer.append(self.SPRITE_QUARTER)
            stringBuffer.appendboolean(features.isFeature(graphicsFeatureFactory.SPRITE_QUARTER_ROTATION_GRAPHICS))
            stringBuffer.append(self.SPRITE_FULL)
            stringBuffer.appendboolean(features.isFeature(graphicsFeatureFactory.SPRITE_FULL_GRAPHICS))
            self.logUtil.putF(str(stringBuffer), self, self.commonStrings.INIT)
    

    def clear(self) -> None:
        self.list_.clear()
    

    def add(self, featureInterface: GameFeatureControlledInterface) -> None:
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append(StringUtil.getInstance().toString(featureInterface))), self, self.commonStrings.ADD)
        self.list_.add(featureInterface)
    

    def getList(self) -> BasicArrayList:
        return self.list_
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureControlledInterface import GameFeatureControlledInterface
from org.allbinary.game.configuration.feature.GraphicsFeatureFactory import GraphicsFeatureFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


