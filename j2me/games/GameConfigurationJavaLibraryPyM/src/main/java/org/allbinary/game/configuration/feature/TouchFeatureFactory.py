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



class TouchFeatureFactory:
    instance: TouchFeatureFactory = None

    def _init_fields(self) -> None:
        self.TOUCH_ENABLED: TouchFeature = TouchFeature("Touch Enabled")
        self.SHOW_SCREEN_BUTTONS: TouchFeature = TouchFeature("Show")
        self.AUTO_HIDE_SHOW_SCREEN_BUTTONS: TouchFeature = TouchFeature("Auto Hide (One Level)")
        self.HIDE_SCREEN_BUTTONS: TouchFeature = TouchFeature("Hide")
    

    @staticmethod
    def getInstance() -> TouchFeatureFactory:
        return TouchFeatureFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.game.configuration.feature.TouchFeature import TouchFeature


TouchFeatureFactory.instance = TouchFeatureFactory()

