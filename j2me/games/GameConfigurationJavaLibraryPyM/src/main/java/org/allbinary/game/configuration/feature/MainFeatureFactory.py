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



class MainFeatureFactory:
    instance: MainFeatureFactory = None

    def _init_fields(self) -> None:
        self.FULL_SCREEN: Feature = Feature("Full Screen")
        self.TITLE_BAR: Feature = Feature("Title Bar")
        self.STATIC: Feature = Feature("Static Dependent Feature")
        self.LOAD_ONDEMAND: Feature = Feature("Load OnDemand")
        self.LOAD_ALL: Feature = Feature("Load All")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> MainFeatureFactory:
        return MainFeatureFactory.instance
from org.allbinary.game.configuration.feature.Feature import Feature


MainFeatureFactory.instance = MainFeatureFactory()

