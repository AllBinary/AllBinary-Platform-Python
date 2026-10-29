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
# package org.allbinary.game.configuration.feature

from __future__ import annotations

from org.allbinary.logic.NullUtil import NullUtil


class Features:
    SINGLETON: object = NullUtil.getInstance().NULL_OBJECT

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.list_: BasicArrayList = None
        self.defaultList: BasicArrayList = None
    

    @staticmethod
    def getInstance() -> Features:
        if Features.SINGLETON == NullUtil.getInstance().NULL_OBJECT:
            Features.SINGLETON = Features()
        return Features.SINGLETON
    

    def __init__(self) -> None:
        self._init_fields()
        self.list_ = BasicArrayListD()
        self.defaultList = BasicArrayListD()
        self.init()
    

    # throws Exception
    def addDefault(self, gameFeature: Feature) -> None:
        self.add(gameFeature)
        if not self.defaultList.contains(gameFeature):
            self.defaultList.add(gameFeature)
    

    # throws Exception
    def add(self, gameFeature: Feature) -> None:
        if not self.list_.contains(gameFeature):
            self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append(str(gameFeature))), self, self.commonStrings.ADD)
            self.list_.add(gameFeature)
            GameFeatureEventHandler.getInstance().fireEvent(GameFeatureEvent(gameFeature, str(gameFeature)))
    

    # throws Exception
    def removeDefault(self, gameFeature: Feature) -> None:
        self.logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append(str(gameFeature))), self, "removeDefault")
        self.remove(gameFeature)
        self.defaultList.remove(gameFeature)
    

    # throws Exception
    def remove(self, gameFeature: Feature) -> None:
        if self.list_.contains(gameFeature):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.REMOVE)
            self.list_.remove(gameFeature)
            GameFeatureEventHandler.getInstance().fireEvent(GameFeatureEvent(gameFeature, str(gameFeature)))
    

    def init(self) -> None:
        from org.allbinary.game.configuration.feature.GameFeatureFactory import GameFeatureFactory
        from org.allbinary.game.configuration.feature.InputFeatureFactory import InputFeatureFactory
        from org.allbinary.game.configuration.feature.SensorFeatureFactory import SensorFeatureFactory
        from org.allbinary.game.configuration.feature.TouchFeatureFactory import TouchFeatureFactory
        from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
        from org.allbinary.game.configuration.feature.MainFeatureFactory import MainFeatureFactory
        try:
            gameFeatureFactory: GameFeatureFactory = GameFeatureFactory.getInstance()
            inputFeatureFactory: InputFeatureFactory = InputFeatureFactory.getInstance()
            sensorFeatureFactory: SensorFeatureFactory = SensorFeatureFactory.getInstance()
            touchFeatureFactory: TouchFeatureFactory = TouchFeatureFactory.getInstance()
            self.addDefault(gameFeatureFactory.ARTIFICIAL_INTELLEGENCE_PROCESSOR)
            self.addDefault(gameFeatureFactory.COLLIDABLE_INTERFACE_LAYER_PROCESSOR)
            self.addDefault(gameFeatureFactory.GAME_INPUT_LAYER_PROCESSOR)
            self.addDefault(gameFeatureFactory.TICKABLE_LAYER_PROCESSOR)
            self.addDefault(inputFeatureFactory.MULTI_KEY_PRESS)
            self.addDefault(inputFeatureFactory.REMOVE_DUPLICATE_KEY_PRESSES)
            self.addDefault(gameFeatureFactory.SCREEN_SHAKE)
            self.addDefault(gameFeatureFactory.POST_IMAGE_LOADING_MODIFICATION)
            operatingSystemInterface: GenericOperatingSystem = OperatingSystemFactory.getInstance().getOperatingSystemInstance()
            if operatingSystemInterface.isOverScan():
                self.addDefault(sensorFeatureFactory.NO_ORIENTATION)
                self.addDefault(touchFeatureFactory.HIDE_SCREEN_BUTTONS)
            else:
                self.addDefault(sensorFeatureFactory.ORIENTATION_SENSORS)
                self.addDefault(touchFeatureFactory.AUTO_HIDE_SHOW_SCREEN_BUTTONS)
            self.addDefault(touchFeatureFactory.TOUCH_ENABLED)
            self.addDefault(MainFeatureFactory.getInstance().FULL_SCREEN)
            self.addDefault(MainFeatureFactory.getInstance().LOAD_ONDEMAND)
        except Exception as e:
            PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, self.commonStrings.INIT, e)
    

    def isDefault(self, gameFeature: Feature) -> bool:
        return self.defaultList.contains(gameFeature)
    

    def isFeature(self, gameFeature: Feature) -> bool:
        return self.list_.contains(gameFeature)
    

    # throws Exception
    def toggle(self, gameFeature: Feature) -> None:
        if self.isFeature(gameFeature):
            self.remove(gameFeature)
        else:
            self.add(gameFeature)
from org.allbinary.game.configuration.event.GameFeatureEvent import GameFeatureEvent
from org.allbinary.game.configuration.event.GameFeatureEventHandler import GameFeatureEventHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.os.GenericOperatingSystem import GenericOperatingSystem
from org.allbinary.logic.system.os.OperatingSystemFactory import OperatingSystemFactory
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


