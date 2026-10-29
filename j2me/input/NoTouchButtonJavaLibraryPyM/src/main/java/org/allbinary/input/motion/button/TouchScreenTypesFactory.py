# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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
# package org.allbinary.input.motion.button

from __future__ import annotations



class TouchScreenTypesFactory:
    instance: TouchScreenTypesFactory = None

    def _init_fields(self) -> None:
        self.FINGER: TouchScreenType = TouchScreenType("Finger")
        self.NOTOUCH: TouchScreenType = TouchScreenType("No Touch")
        self.STYLUS: TouchScreenType = TouchScreenType("Stylus")
        self.UNDEFINED: TouchScreenType = TouchScreenType("Undefined")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TouchScreenTypesFactory:
        return TouchScreenTypesFactory.instance
from org.allbinary.input.motion.button.TouchScreenType import TouchScreenType


TouchScreenTypesFactory.instance = TouchScreenTypesFactory()

