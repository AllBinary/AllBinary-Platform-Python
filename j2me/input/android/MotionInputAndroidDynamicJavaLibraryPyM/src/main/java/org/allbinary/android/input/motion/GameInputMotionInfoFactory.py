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
# package org.allbinary.android.input.motion

from __future__ import annotations



class GameInputMotionInfoFactory:
    

    @staticmethod
    def getInstance() -> GameInputMotionInfo:
        SDK_VERSION: int = AndroidInfoFactory.getInstance().getVersion()
        if SDK_VERSION <= 4:
            return GameInputMotionInfoAPI1.getInstance()
        else:
            return GameInputMotionInfoAPI5.getInstance()
from org.allbinary.android.AndroidInfoFactory import AndroidInfoFactory
from org.allbinary.android.input.motion.api1.GameInputMotionInfoAPI1 import GameInputMotionInfoAPI1
from org.allbinary.android.input.motion.api5.GameInputMotionInfoAPI5 import GameInputMotionInfoAPI5


