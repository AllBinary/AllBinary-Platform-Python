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
# package org.allbinary.input.motion.button

from __future__ import annotations



class TouchScreenFactory:
    SINGLETON: TouchScreenFactory = None

    def _init_fields(self) -> None:
        self.multiTouch: bool = False
        self.touch: bool = False
        self.touchScreenType: TouchScreenType = TouchScreenTypesFactory.getInstance().NOTOUCH
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TouchScreenFactory:
        return TouchScreenFactory.SINGLETON
    

    def isMultiTouch(self) -> bool:
        return self.multiTouch
    

    def setTouch(self, touch: bool) -> None:
        pass
    

    def isTouch(self) -> bool:
        return self.touch
    

    def getTouchScreenType(self) -> TouchScreenType:
        return self.touchScreenType
from org.allbinary.input.motion.button.TouchScreenTypesFactory import TouchScreenTypesFactory


TouchScreenFactory.SINGLETON = TouchScreenFactory()

