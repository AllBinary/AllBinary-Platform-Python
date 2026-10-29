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
# package org.allbinary.input.motion.gesture

from __future__ import annotations

from org.allbinary.game.input.Input import Input


class MotionGestureInput(Input):
    

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id, name)
        inputFactory: InputFactory = InputFactory.getInstance()
        inputFactory.add(self.getId(), self)
from org.allbinary.game.input.InputFactory import InputFactory


