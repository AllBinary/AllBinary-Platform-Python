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



class InputFeatureFactory:
    instance: InputFeatureFactory = None

    def _init_fields(self) -> None:
        self.REMOVE_DUPLICATE_KEY_PRESSES: InputFeature = InputFeature("Remove Duplicate Key Presses")
        self.INPUT_MAPPING: InputFeature = InputFeature("Input Mapping")
        self.MULTI_KEY_PRESS: InputFeature = InputFeature("Multi Key Press")
        self.SINGLE_KEY_REPEAT_PRESS: InputFeature = InputFeature("Single Key Repeat Press")
        self.SINGLE_KEY_PRESS: InputFeature = InputFeature("Single Key Press")
    

    @staticmethod
    def getInstance() -> InputFeatureFactory:
        return InputFeatureFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def isSingleKeyProcessing(self) -> bool:
        from org.allbinary.game.configuration.feature.Features import Features
        features: Features = Features.getInstance()
        if features.isFeature(self.SINGLE_KEY_REPEAT_PRESS) or features.isFeature(self.SINGLE_KEY_PRESS):
            return True
        else:
            return False
from org.allbinary.game.configuration.feature.InputFeature import InputFeature


InputFeatureFactory.instance = InputFeatureFactory()

