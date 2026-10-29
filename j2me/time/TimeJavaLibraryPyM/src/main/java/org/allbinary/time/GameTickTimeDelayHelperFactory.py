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
# package org.allbinary.time

from __future__ import annotations

from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper


class GameTickTimeDelayHelperFactory:
    instance: GameTickTimeDelayHelper = GameTickTimeDelayHelper(-1)
    

    @staticmethod
    def getInstance() -> GameTickTimeDelayHelper:
        return GameTickTimeDelayHelperFactory.instance
    

    def __init__(self) -> None:
        pass


