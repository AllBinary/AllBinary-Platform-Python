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
# package org.allbinary.game.physics.velocity

from __future__ import annotations

from org.allbinary.game.physics.velocity.BasicVelocityInterface import BasicVelocityInterface


# Java interface
class VelocityInterface(BasicVelocityInterface):
    

    def getMaxForwardVelocity(self) -> int:
        raise NotImplementedError()
    

    def getMaxReverseVelocity(self) -> int:
        raise NotImplementedError()
    

    def limitMaxXYForwardVelocity(self) -> None:
        raise NotImplementedError()
    

    def limitMaxXYReverseVelocity(self) -> None:
        raise NotImplementedError()
    

    def limitXYToForwardAndReverseMaxVelocity(self) -> None:
        raise NotImplementedError()
    

    def limitMaxXYVelocity(self, maxVelocity: int) -> None:
        raise NotImplementedError()
    

    def setMaxForwardVelocity(self, maxForwardVelocity: int) -> None:
        raise NotImplementedError()
    

    def setMaxReverseVelocity(self, maxReverseVelocity: int) -> None:
        raise NotImplementedError()


