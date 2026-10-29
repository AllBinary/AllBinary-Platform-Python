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
# package org.allbinary.animation

from __future__ import annotations

from org.allbinary.game.resource.FeaturedResourceFactory import FeaturedResourceFactory


class FeaturedAnimationInterfaceFactoryInterfaceFactory(FeaturedResourceFactory):
    INSTANCE: FeaturedAnimationInterfaceFactoryInterfaceFactory = None
    

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> FeaturedAnimationInterfaceFactoryInterfaceFactory:
        return FeaturedAnimationInterfaceFactoryInterfaceFactory.INSTANCE
    

    # throws Exception
    def getRectangle(self, resource: str) -> Rectangle:
        return self.getRectangleXY(resource, 0, 0)
    

    # throws Exception
    def getRectangleXY(self, resource: str, x: int, y: int) -> Rectangle:
        pointFactory: PointFactory = PointFactory.getInstance()
        list_: BasicArrayList = self.getList()
        scale: int = int(GameConfigurationCentral.getInstance().SCALE.getValue())
        size: int = self.getList().size()
        for index in range(0, size):
            featureInterface: FeatureResourceAnimationInterfaceFactoryInterface = list_.objectArray[index]
            if featureInterface.isFeature():
                rectangle: Rectangle = featureInterface.getRectangle(resource)
                if rectangle != RectangleFactory.SINGLETON:
                    return Rectangle(pointFactory.createXY(x, y), ((rectangle.getWidth() * scale) >> 1), ((rectangle.getHeight() * scale) >> 1))
        raise Exception(str(StringMaker().append("No rectangle available for current feature selection or Resource: ").append(resource)))
    

    # throws Exception
    def getProcedural(self, resource: str) -> ProceduralAnimationInterfaceFactoryInterface:
        return self.getBasicAnimationInterfaceFactoryInstance(resource)
    

    # throws Exception
    def get(self, resource: str) -> AnimationInterfaceFactoryInterface:
        return self.getBasicAnimationInterfaceFactoryInstance(resource)
    

    # throws Exception
    def getBasicAnimationInterfaceFactoryInstance(self, resource: str) -> BasicAnimationInterfaceFactoryInterface:
        from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
        list_: BasicArrayList = self.getList()
        resourceTypeAvailableList: BasicArrayList = BasicArrayListD()
        size: int = self.getList().size()
        featureInterface: FeatureResourceAnimationInterfaceFactoryInterface = None
        animationInterfaceFactoryInterface: BasicAnimationInterfaceFactoryInterface = None
        for index in range(0, size):
            featureInterface = list_.objectArray[index]
            if featureInterface.isFeature():
                resourceTypeAvailableList.add(featureInterface)
                animationInterfaceFactoryInterface = featureInterface.getBasicAnimationInterfaceFactoryInstance(resource)
                if animationInterfaceFactoryInterface != NullAnimationFactory.NULL_NOT_FOR_USE_ANIMATION_FACTORY:
                    return animationInterfaceFactoryInterface
        if resourceTypeAvailableList.size() > 0:
            NO_ANIMATION_AVAILABLE_FROM: str = "No animation available from: "
            FOR_FACTORIES: str = " factories: "
            FOR_RESOURCE: str = " for Resource: "
            HAS_KEY: str = " has: "
            RESOURCES_LABEL: str = " resources "
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(NO_ANIMATION_AVAILABLE_FROM)
            stringBuffer.appendint(resourceTypeAvailableList.size())
            stringBuffer.append(CommonSeps.getInstance().FORWARD_SLASH)
            stringBuffer.appendint(size)
            stringBuffer.append(FOR_FACTORIES)
            size2: int = resourceTypeAvailableList.size()
            for index in range(0, size2):
                stringBuffer.append(str(resourceTypeAvailableList.get(index)))
                stringBuffer.append(CommonSeps.getInstance().COMMA_SEP)
            stringBuffer.append(FOR_RESOURCE)
            stringBuffer.append(resource)
            for index in range(0, size):
                stringBuffer.append(CommonSeps.getInstance().NEW_LINE)
                featureInterface = list_.objectArray[index]
                if featureInterface.isFeature():
                    stringBuffer.append(StringUtil.getInstance().toString(featureInterface))
                    stringBuffer.append(HAS_KEY)
                    stringBuffer.appendint(featureInterface.getHashtable().size())
                    stringBuffer.append(RESOURCES_LABEL)
            raise Exception(str(stringBuffer))
        else:
            stringBuffer: StringMaker = StringMaker()
            for index in range(0, size):
                featureInterface = list_.objectArray[index]
                stringBuffer.append(str(featureInterface))
                stringBuffer.append(CommonSeps.getInstance().SPACE)
            result: str = str(stringBuffer)
            stringBuffer.delete(0, stringBuffer.length())
            raise Exception(str(stringBuffer.append("No feature resource type available for Resource: ").append(resource).append(" Resource Factories Available: ").append(result)))
from org.allbinary.animation.resource.FeatureResourceAnimationInterfaceFactoryInterface import FeatureResourceAnimationInterfaceFactoryInterface
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
from org.allbinary.graphics.PointFactory import PointFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


FeaturedAnimationInterfaceFactoryInterfaceFactory.INSTANCE = FeaturedAnimationInterfaceFactoryInterfaceFactory()

