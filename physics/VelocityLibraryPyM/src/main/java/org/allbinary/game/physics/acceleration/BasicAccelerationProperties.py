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
# package org.allbinary.game.physics.acceleration

from __future__ import annotations



class BasicAccelerationProperties:

    def _init_fields(self) -> None:
        self.forward: int = 0
        self.reverse: int = 0
    

    def __init__(self, forward: int, reverse: int) -> None:
        self._init_fields()
        self.setForward(forward)
        self.setReverse(reverse)
    

    def setReverse(self, reverse: int) -> None:
        self.reverse = reverse
    

    def getReverse(self) -> int:
        return self.reverse
    

    def setForward(self, forward: int) -> None:
        self.forward = forward
    

    def getForward(self) -> int:
        return self.forward


