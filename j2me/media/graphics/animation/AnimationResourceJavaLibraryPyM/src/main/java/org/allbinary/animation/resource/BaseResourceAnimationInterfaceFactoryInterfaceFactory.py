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
# package org.allbinary.animation.resource

from __future__ import annotations

from org.allbinary.animation.resource.FeatureResourceAnimationInterfaceFactoryInterface import FeatureResourceAnimationInterfaceFactoryInterface


class BaseResourceAnimationInterfaceFactoryInterfaceFactory(FeatureResourceAnimationInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.hashtable: ABHashtable[object, object] = None
        self.rectangleHashtable: ABHashtable[object, object] = None
        self.rectangleArrayOfArraysHashtable: ABHashtable[object, object] = None
        self.name: str = None
        self.initialized: bool = False
    

    def __init__(self, name: str, hashtable: ABHashtable[object, object], rectangleHashtable: ABHashtable[object, object], rectangleArrayHashtable: ABHashtable[object, object]) -> None:
        self._init_fields()
        self.hashtable = hashtable
        self.rectangleHashtable = rectangleHashtable
        self.rectangleArrayOfArraysHashtable = rectangleArrayHashtable
        self.name = name
    

    def getName(self) -> str:
        return self.name
    

    # throws Exception
    def init(self, level: int) -> None:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF(str(StringMaker().append("Available List of Animations: ").append(str(self.hashtable))), self, commonStrings.INIT)
        self.setInitialized(True)
    

    # throws Exception
    def initImageCache(self, imageCache: ImageCache, level: int) -> None:
        pass
    

    # throws Exception
    def add(self, resource: str, animationInterfaceFactoryInterface: BasicAnimationInterfaceFactoryInterface) -> None:
        if self.hashtable.containsKey(resource):
            raise Exception(str(StringMaker().append("Resource Already Created: ").append(resource)))
        self.hashtable.put(resource, animationInterfaceFactoryInterface)
    

    # throws Exception
    def getBasicAnimationInterfaceFactoryInstance(self, resource: str) -> BasicAnimationInterfaceFactoryInterface:
        basicAnimationInterfaceFactoryInterfaceCanBeNull: object = self.hashtable.get(resource)
        if basicAnimationInterfaceFactoryInterfaceCanBeNull is None:
            return NullAnimationFactory.NULL_NOT_FOR_USE_ANIMATION_FACTORY
        return basicAnimationInterfaceFactoryInterfaceCanBeNull
    

    # throws Exception
    def getRectangle(self, resource: str) -> Rectangle:
        rectangleCanBeNull: object = self.rectangleHashtable.get(resource)
        if rectangleCanBeNull is None:
            return RectangleFactory.SINGLETON
        return rectangleCanBeNull
    

    # throws Exception
    def addRectangle(self, resource: str, rectangle: Rectangle) -> None:
        self.rectangleHashtable.put(resource, rectangle)
    

    # throws Exception
    def getRectangleArrayOfArrays(self, resource: str) -> list[list[Rectangle]]:
        return self.rectangleArrayOfArraysHashtable.get(resource)
    

    # throws Exception
    def addRectangleArrayOfArrays(self, resource: str, rectangleArrayOfArrays: list[list[Rectangle]]) -> None:
        self.rectangleArrayOfArraysHashtable.put(resource, rectangleArrayOfArrays)
    

    def isFeature(self) -> bool:
        return False
    

    def isLoadingLevel(self, level: int) -> bool:
        resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
        if level == resourceLoadingLevelFactory.LOAD_ALL.getLevel():
            return True
        else:
            return False
    

    def toString(self) -> str:
        return str(StringMaker().append(type(self).__module__ + "." + type(self).__qualname__).append(CommonSeps.getInstance().SEMICOLON).append(CommonSeps.getInstance().SPACE).append(self.name))

    def __str__(self) -> str:
        return self.toString()
    

    def getHashtable(self) -> ABHashtable[object, object]:
        return self.hashtable
    

    def getRectangleHashtable(self) -> ABHashtable[object, object]:
        return self.rectangleHashtable
    

    def getRectangleArrayOfArraysHashtable(self) -> ABHashtable[object, object]:
        return self.rectangleArrayOfArraysHashtable
    

    def setInitialized(self, initialized: bool) -> None:
        self.initialized = initialized
    

    def isInitialized(self) -> bool:
        return self.initialized
from org.allbinary.animation.BasicAnimationInterfaceFactoryInterface import BasicAnimationInterfaceFactoryInterface
from org.allbinary.animation.NullAnimationFactory import NullAnimationFactory
from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory
from org.allbinary.graphics.Rectangle import Rectangle
from org.allbinary.graphics.RectangleFactory import RectangleFactory
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable


