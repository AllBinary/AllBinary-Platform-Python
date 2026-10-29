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



class GameInitializationUtil:
    instance: GameInitializationUtil = None

    def _init_fields(self) -> None:
        self.EVENT: GameInitializedEvent = GameInitializedEvent(self)

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def initDemo(self, abeClientInformation: AbeClientInformationInterface, canvas: MyCanvas, gameInitializationInterfaceFactoryInterface: BasicBuildGameInitializerFactory) -> None:
        mainFeatureFactory: MainFeatureFactory = MainFeatureFactory.getInstance()
        if ChangedGameFeatureListener.getInstance().isChangedFeature(mainFeatureFactory.STATIC):
            gameInitializationInterface: GameInitializationInterface = gameInitializationInterfaceFactoryInterface.getInstance()
            features: Features = Features.getInstance()
            if features.isFeature(mainFeatureFactory.LOAD_ALL):
                self.initGame(abeClientInformation, canvas, gameInitializationInterfaceFactoryInterface)
            elif features.isFeature(mainFeatureFactory.LOAD_ONDEMAND):
                resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
                gameInitializationInterface.init(abeClientInformation, canvas.getCustomCommandListener(), resourceLoadingLevelFactory.LOAD_EARLY.getLevel())
                self.EVENT.setResourceLoadingLevel(resourceLoadingLevelFactory.LOAD_EARLY)
            else:
                raise Exception("No Loading Feature Available")
            GameInitializedEventHandler.getInstance().fireEvent(self.EVENT)
    

    # throws Exception
    def initGame(self, abeClientInformation: AbeClientInformationInterface, canvas: MyCanvas, gameInitializationInterfaceFactoryInterface: BasicBuildGameInitializerFactory) -> None:
        if ChangedGameFeatureListener.getInstance().isChangedFeature(MainFeatureFactory.getInstance().STATIC):
            gameInitializationInterface: GameInitializationInterface = gameInitializationInterfaceFactoryInterface.getInstance()
            resourceLoadingLevelFactory: ResourceLoadingLevelFactory = ResourceLoadingLevelFactory.getInstance()
            gameInitializationInterface.init(abeClientInformation, canvas.getCustomCommandListener(), resourceLoadingLevelFactory.LOAD_ALL.getLevel())
            self.EVENT.setResourceLoadingLevel(resourceLoadingLevelFactory.LOAD_ALL)
            GameInitializedEventHandler.getInstance().fireEvent(self.EVENT)
            ChangedGameFeatureListener.getInstance().remove(MainFeatureFactory.getInstance().STATIC)
    

    @staticmethod
    def getInstance() -> GameInitializationUtil:
        return GameInitializationUtil.instance
from org.allbinary.game.configuration.event.ChangedGameFeatureListener import ChangedGameFeatureListener
from org.allbinary.game.configuration.event.GameInitializedEvent import GameInitializedEvent
from org.allbinary.game.configuration.event.GameInitializedEventHandler import GameInitializedEventHandler
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
from org.allbinary.game.resource.ResourceLoadingLevelFactory import ResourceLoadingLevelFactory
from org.allbinary.graphics.displayable.MyCanvas import MyCanvas
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface


GameInitializationUtil.instance = GameInitializationUtil()

