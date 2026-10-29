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
# package org.allbinary.game.configuration

from __future__ import annotations

from org.allbinary.init.Init import Init


class InGameFeatures(Init):

    def __init__(self) -> None:
        super().__init__()
    

    def init(self) -> None:
        LABEL: str = "Screen Buttons"
        orientationData: OrientationData = OrientationData.getInstance()
        exclusiveOrientationSensorVector: BasicArrayList = GameFeatureChoiceGroups.getExclusiveInstance().get().get(orientationData.ORIENTATION_SENSOR_INPUT)
        inGameFeatureChoiceGroups: InGameFeatureChoiceGroups = InGameFeatureChoiceGroups.getExclusiveInstance()
        if exclusiveOrientationSensorVector is not None:
            inGameExclusiveOrientationSensorVectorCanBeNull: object = inGameFeatureChoiceGroups.get().get(orientationData.ORIENTATION_SENSOR_INPUT)
            if inGameExclusiveOrientationSensorVectorCanBeNull is None:
                self.addToInGameMenu()
            else:
                inGameExclusiveOrientationSensorVector: BasicArrayList = inGameExclusiveOrientationSensorVectorCanBeNull
                if inGameExclusiveOrientationSensorVector.size() == 0:
                    self.addToInGameMenu()
        features: Features = Features.getInstance()
        if features.isFeature(TouchFeatureFactory.getInstance().SHOW_SCREEN_BUTTONS) or features.isFeature(TouchFeatureFactory.getInstance().AUTO_HIDE_SHOW_SCREEN_BUTTONS) or features.isFeature(TouchFeatureFactory.getInstance().HIDE_SCREEN_BUTTONS):
            exclusiveScreenButtonsVector: BasicArrayList = BasicArrayListD()
            touchFeatureFactory: TouchFeatureFactory = TouchFeatureFactory.getInstance()
            exclusiveScreenButtonsVector.add(touchFeatureFactory.AUTO_HIDE_SHOW_SCREEN_BUTTONS)
            exclusiveScreenButtonsVector.add(touchFeatureFactory.SHOW_SCREEN_BUTTONS)
            exclusiveScreenButtonsVector.add(touchFeatureFactory.HIDE_SCREEN_BUTTONS)
            inGameFeatureChoiceGroups.add(LABEL, exclusiveScreenButtonsVector)
    

    def addToInGameMenu(self) -> None:
        orientationData: OrientationData = OrientationData.getInstance()
        inGameExclusiveOrientationSensorVector: BasicArrayList = BasicArrayListD()
        inGameExclusiveOrientationSensorVector.add(SensorFeatureFactory.getInstance().ORIENTATION_SENSORS)
        inGameExclusiveOrientationSensorVector.add(SensorFeatureFactory.getInstance().NO_ORIENTATION)
        InGameFeatureChoiceGroups.getExclusiveInstance().add(orientationData.ORIENTATION_SENSOR_INPUT, inGameExclusiveOrientationSensorVector)
    

    def isAny(self) -> bool:
        features: Features = Features.getInstance()
        touchFeatureFactory: TouchFeatureFactory = TouchFeatureFactory.getInstance()
        if features.isFeature(touchFeatureFactory.SHOW_SCREEN_BUTTONS) or features.isFeature(touchFeatureFactory.AUTO_HIDE_SHOW_SCREEN_BUTTONS) or features.isFeature(touchFeatureFactory.HIDE_SCREEN_BUTTONS):
            return True
        exclusiveOrientationSensorVector: BasicArrayList = GameFeatureChoiceGroups.getExclusiveInstance().get().get(OrientationData.getInstance().ORIENTATION_SENSOR_INPUT)
        if exclusiveOrientationSensorVector is not None:
            return True
        return False
from org.allbinary.game.configuration.feature.Features import Features
from org.allbinary.game.configuration.feature.GameFeatureChoiceGroups import GameFeatureChoiceGroups
from org.allbinary.game.configuration.feature.InGameFeatureChoiceGroups import InGameFeatureChoiceGroups
from org.allbinary.game.configuration.feature.SensorFeatureFactory import SensorFeatureFactory
from org.allbinary.game.configuration.feature.TouchFeatureFactory import TouchFeatureFactory
from org.allbinary.input.gyro.OrientationData import OrientationData
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


