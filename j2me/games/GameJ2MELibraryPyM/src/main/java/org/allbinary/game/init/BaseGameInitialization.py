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
# package org.allbinary.game.init

from __future__ import annotations

from org.allbinary.game.resource.ResourceInitialization import ResourceInitialization
from org.allbinary.game.init.GameInitializationInterface import GameInitializationInterface


class BaseGameInitialization(GameInitializationInterface):
    NULL_BASE_GAME_INITIALIZATION: BaseGameInitialization = None

    def _init_fields(self) -> None:
        self.resourceInitializationArray: list[ResourceInitialization] = None
        self.portion: int = None
        self.initialized: bool = False
        self.EARLY_RESOURCES: int = 0
        self.GAME_RESOURCES: int = 1
        self.EARLY_CHANGABLE_RESOURCES: int = 2
        self.GAME_CHANGABLE_RESOURCES: int = 3
        self.gameInitialized: bool = False
        self.allLoaded: bool = False
    

    def __init__(self, resourceInitializationArray: list[ResourceInitialization], portion: int) -> None:
        self._init_fields()
        self.resourceInitializationArray = resourceInitializationArray
        self.portion = portion
    

    # throws Exception
    def initKey(self, portion: int) -> None:
        pass
    

    # throws Exception
    def initKeyMapping(self, abeClientInformation: AbeClientInformationInterface, portion: int) -> None:
        if ChangedGameFeatureListener.getInstance().isChangedFeature(InputFeatureFactory.getInstance().INPUT_MAPPING):
            PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance().init(abeClientInformation)
            ProgressCanvasFactory.getInstance().addNormalPortion(50, "Game Keys")
            ChangedGameFeatureListener.getInstance().remove(InputFeatureFactory.getInstance().INPUT_MAPPING)
    

    # throws Exception
    def init(self, abeClientInformation: AbeClientInformationInterface, commandListener: CommandListener, level: int) -> None:
        resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
        if not self.isInitialized() and (level == resourceLoadingLevelFactory.LOAD_ALL.getLevel() or level == resourceLoadingLevelFactory.LOAD_EARLY.getLevel()):
            localPortion: int = 40
            if level == resourceLoadingLevelFactory.LOAD_EARLY.getLevel():
                localPortion = 8
            self.setInitialized(True)
            self.initKey(self.getPortion())
            self.initKeyMapping(abeClientInformation, self.getPortion())
            GameKeyEventFactory.getInstance().init()
            progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
            progressCanvas.addNormalPortion(localPortion, "Game Key Events")
            BasicTouchInputFactory.getInstance().init(PlatformInputMappingFactory.getInstance().getPersistentInputMappingInstance().getInputMapping())
            CancelTouchButtonInputFactory.getInstance()
            progressCanvas.addNormalPortion(localPortion, "Touch Input")
            CompleteMotionGestureInputToGameMotionGestureInput.getInstance().init()
            progressCanvas.addNormalPortion(localPortion, "Motion Input")
            GameFeatureImageCacheFactory.init()
            progressCanvas.addNormalPortion(localPortion, "Image Cache")
            self.resourceInitializationArray[self.EARLY_RESOURCES].init()
    

    # throws Exception
    def resourceInitialization(self, level: int) -> None:
        resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
        if self.resourceAnimationChange() and level == resourceLoadingLevelFactory.LOAD_EARLY.getLevel():
            self.clearResources()
            self.resourceInitializationArray[self.EARLY_CHANGABLE_RESOURCES].init()
        if self.resourceAnimationChange() and level == resourceLoadingLevelFactory.LOAD_ALL.getLevel():
            if self.allLoaded:
                self.clearResources()
            if FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance().getList().size() == 0:
                self.resourceInitializationArray[self.EARLY_CHANGABLE_RESOURCES].init()
            self.resourceInitializationArray[self.GAME_CHANGABLE_RESOURCES].init()
            self.allLoaded = True
    

    def resourceAnimationChange(self) -> bool:
        changedGameFeatureListener: ChangedGameFeatureListener = ChangedGameFeatureListener.getInstance()
        gameConfigurationCentral: GameConfigurationCentral = GameConfigurationCentral.getInstance()
        if changedGameFeatureListener.isChangedGameConfiguration(gameConfigurationCentral.SCALE):
            return True
        if ChangedGameFeatureListener.getInstance().isChangedFeature(MainFeatureFactory.getInstance().STATIC):
            return True
        return False
    

    def clearResources(self) -> None:
        self.allLoaded = False
        GameFeatureImageCacheFactory.releaseAll()
        featuredAnimationInterfaceFactoryInterfaceFactory: FeaturedAnimationInterfaceFactoryInterfaceFactory = FeaturedAnimationInterfaceFactoryInterfaceFactory.getInstance()
        featuredAnimationInterfaceFactoryInterfaceFactory.clear()
        FeaturedResourceRelativeRelationshipFactory.getInstance().clear()
    

    def setGameInitialized(self, gameInitialized: bool) -> None:
        self.gameInitialized = gameInitialized
    

    def isGameInitialized(self) -> bool:
        return self.gameInitialized
    

    def getPortion(self) -> int:
        return self.portion
    

    def setInitialized(self, initialized: bool) -> None:
        self.initialized = initialized
    

    def isInitialized(self) -> bool:
        return self.initialized
# from javax.microedition.lcdui.CommandListener import CommandListener
from org.allbinary.animation.FeaturedAnimationInterfaceFactoryInterfaceFactory import FeaturedAnimationInterfaceFactoryInterfaceFactory
from org.allbinary.game.configuration.GameConfigurationCentral import GameConfigurationCentral
from org.allbinary.game.configuration.event.ChangedGameFeatureListener import ChangedGameFeatureListener
from org.allbinary.game.configuration.feature.InputFeatureFactory import InputFeatureFactory
from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
from org.allbinary.game.input.PlatformInputMappingFactory import PlatformInputMappingFactory
from org.allbinary.game.input.event.GameKeyEventFactory import GameKeyEventFactory
from org.allbinary.game.resource.FeaturedResourceRelativeRelationshipFactory import FeaturedResourceRelativeRelationshipFactory
from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.image.GameFeatureImageCacheFactory import GameFeatureImageCacheFactory
from org.allbinary.input.motion.CompleteMotionGestureInputToGameMotionGestureInput import CompleteMotionGestureInputToGameMotionGestureInput
from org.allbinary.input.motion.button.BasicTouchInputFactory import BasicTouchInputFactory
from org.allbinary.input.motion.button.CancelTouchButtonInputFactory import CancelTouchButtonInputFactory
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


BaseGameInitialization.NULL_BASE_GAME_INITIALIZATION = BaseGameInitialization([None] * (0), 0)

