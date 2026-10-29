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
# package org.allbinary.game.ag.life

from __future__ import annotations



# Java interface
class LifeInterface:
    

    def get(self) -> int:
        raise NotImplementedError()
    

    def set(self, lives: int) -> None:
        raise NotImplementedError()
    

    def reset(self) -> None:
        raise NotImplementedError()
    

    def add(self, lives: int) -> None:
        raise NotImplementedError()
    

    def deaths(self, lives: int) -> None:
        raise NotImplementedError()
    

    def getMaxlives(self) -> int:
        raise NotImplementedError()
    

    def isAlive(self) -> bool:
        raise NotImplementedError()


