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



class OnDemandLoader:

    def _init_fields(self) -> None:
        self.onDemandResourcesFactory: OnDemandResourcesFactory = None
        self.gameLayerPlacementInterfaceBasicArrayListFactoryInterfaceFactory: GameLayerPlacementInterfaceBasicArrayListFactoryInterfaceFactory = None
        self.resourceAnimationInterfaceFactoryInterfaceFactory: BaseResourceAnimationInterfaceFactoryInterfaceFactory = None
    

    def __init__(self, onDemandResourcesFactory: OnDemandResourcesFactory, gameLayerPlacementInterfaceBasicArrayListFactoryInterfaceFactory: GameLayerPlacementInterfaceBasicArrayListFactoryInterfaceFactory, resourceAnimationInterfaceFactoryInterfaceFactory: BaseResourceAnimationInterfaceFactoryInterfaceFactory) -> None:
        self._init_fields()
        self.onDemandResourcesFactory = onDemandResourcesFactory
        self.gameLayerPlacementInterfaceBasicArrayListFactoryInterfaceFactory = gameLayerPlacementInterfaceBasicArrayListFactoryInterfaceFactory
        self.resourceAnimationInterfaceFactoryInterfaceFactory = resourceAnimationInterfaceFactoryInterfaceFactory
    

    # throws Exception
    def init(self, imageCache: ImageCache, level: int, loadingString: str) -> None:
        resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
        if Features.getInstance().isFeature(MainFeatureFactory.getInstance().LOAD_ALL):
            if self.resourceAnimationInterfaceFactoryInterfaceFactory.isInitialized():
                return
            self.initAll(imageCache, loadingString)
        elif level != resourceLoadingLevelFactory.LOAD_ALL.getLevel():
            layerPlacementInterfaceBasicArrayListFactoryInterface: LayerPlacementInterfaceBasicArrayListFactoryInterface = self.gameLayerPlacementInterfaceBasicArrayListFactoryInterfaceFactory.getInstance(level)
            self.initLevel(layerPlacementInterfaceBasicArrayListFactoryInterface, imageCache, level, loadingString)
    

    # throws Exception
    def initAll(self, imageCache: ImageCache, loadingString: str) -> None:
        from org.allbinary.game.layer.resources.OnDemandResources import OnDemandResources
        index: int = 0
        portion: int = 120
        onDemandResources: OnDemandResources = None
        onDemandIndex = self.onDemandResourcesFactory.size()
        while (onDemandIndex := onDemandIndex - 1) >= 0:
            onDemandResources = self.onDemandResourcesFactory.remove(onDemandIndex)
            if onDemandResources != OnDemandResources.NULL_ON_DEMAND_RESOURCES:
                index = onDemandResources.initAt(imageCache, self.resourceAnimationInterfaceFactoryInterfaceFactory, portion, loadingString, index)
    

    # throws Exception
    def initLevel(self, layerPlacementInterfaceBasicArrayListFactoryInterface: LayerPlacementInterfaceBasicArrayListFactoryInterface, imageCache: ImageCache, level: int, loadingString: str) -> None:
        from org.allbinary.game.layer.resources.OnDemandResources import OnDemandResources
        commonStrings: CommonStrings = CommonStrings.getInstance()
        portion: int = 120
        index: int = 0
        onDemandArray: list[int] = layerPlacementInterfaceBasicArrayListFactoryInterface.getOnDemandResources()
        PreLogUtil.put(str(StringMaker().append(commonStrings.START).appendint(len(onDemandArray))), self, "initLevel")
        onDemandResources: OnDemandResources = None
        onDemandIndex = len(onDemandArray)
        while (onDemandIndex := onDemandIndex - 1) >= 0:
            onDemandResources = self.onDemandResourcesFactory.remove(onDemandArray[onDemandIndex])
            if onDemandResources != OnDemandResources.NULL_ON_DEMAND_RESOURCES:
                index = onDemandResources.initAt(imageCache, self.resourceAnimationInterfaceFactoryInterfaceFactory, portion, loadingString, index)
from org.allbinary.animation.resource.BaseResourceAnimationInterfaceFactoryInterfaceFactory import BaseResourceAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
from org.allbinary.game.layer.GameLayerPlacementInterfaceBasicArrayListFactoryInterfaceFactory import GameLayerPlacementInterfaceBasicArrayListFactoryInterfaceFactory
from org.allbinary.game.layer.LayerPlacementInterfaceBasicArrayListFactoryInterface import LayerPlacementInterfaceBasicArrayListFactoryInterface
from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory
from org.allbinary.image.ImageCache import ImageCache
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings


