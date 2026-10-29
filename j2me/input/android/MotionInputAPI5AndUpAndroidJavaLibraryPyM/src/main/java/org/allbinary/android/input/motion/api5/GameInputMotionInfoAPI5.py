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
# package org.allbinary.android.input.motion.api5

from __future__ import annotations

from org.allbinary.android.input.motion.GameInputMotionInfo import GameInputMotionInfo


class GameInputMotionInfoAPI5(GameInputMotionInfo):
    instance: GameInputMotionInfoAPI5 = None
    

    @staticmethod
    def getInstance() -> GameInputMotionInfoAPI5:
        return GameInputMotionInfoAPI5.instance
    

    def __init__(self) -> None:
        super().__init__(2147483647, 10)


GameInputMotionInfoAPI5.instance = GameInputMotionInfoAPI5()

