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
# package org.allbinary.direction

from __future__ import annotations



# Java interface
class DirectionalInterface:
    

    def setFrameByDirection(self, direction: Direction) -> None:
        raise NotImplementedError()
    

    def setFrameToAngle(self, angle: Angle) -> None:
        raise NotImplementedError()
    

    def adjustFrameToAngle(self, newAngle: Angle) -> None:
        raise NotImplementedError()
    

    def adjustFrame(self, angle: int) -> None:
        raise NotImplementedError()
from org.allbinary.math.Angle import Angle


