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
# package org.allbinary.animation.transition.shake

from __future__ import annotations



class ShakeEventFactory:
    instance: ShakeEventFactory = None

    def _init_fields(self) -> None:
        self.MICRO: ShakeEvent = ShakeEvent()
        self.SMALL: ShakeEvent = ShakeEvent()
        self.MEDIUM: ShakeEvent = ShakeEvent()
        self.LARGE: ShakeEvent = ShakeEvent()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ShakeEventFactory:
        return ShakeEventFactory.instance
    

    def init(self) -> None:
        pass
from org.allbinary.animation.transition.shake.ShakeEvent import ShakeEvent


ShakeEventFactory.instance = ShakeEventFactory()

