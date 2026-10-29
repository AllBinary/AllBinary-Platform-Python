#
# AllBinary Open License Version 1
# Copyright (c) 2009 AllBinary
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
# package org.allbinary.android.input.motion.api1

from __future__ import annotations

from org.allbinary.android.input.motion.GameInputMotionInfo import GameInputMotionInfo


class GameInputMotionInfoAPI1(GameInputMotionInfo):
    instance: GameInputMotionInfoAPI1 = None
    

    @staticmethod
    def getInstance() -> GameInputMotionInfoAPI1:
        return GameInputMotionInfoAPI1.instance
    

    def __init__(self) -> None:
        super().__init__(4, 1)


GameInputMotionInfoAPI1.instance = GameInputMotionInfoAPI1()

