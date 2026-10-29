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



class ActivityFractureInputUtilFactory:
    

    @staticmethod
    def getInstance() -> ActivityFractureUtil:
        SDK_VERSION: int = AndroidInfoFactory.getInstance().getVersion()
        if SDK_VERSION <= 4:
            return ActivityFractureUtilAPI1.getInstance()
        elif SDK_VERSION <= 15:
            return ActivityFractureUtilAPI5.getInstance()
        elif SDK_VERSION <= 16:
            return ActivityFractureUtilAPI16.getInstance()
        else:
            return ActivityFractureUtilAPI19.getInstance()
from org.allbinary.android.ActivityFractureUtil import ActivityFractureUtil
from org.allbinary.android.AndroidInfoFactory import AndroidInfoFactory
from org.allbinary.android.api1.ActivityFractureUtilAPI1 import ActivityFractureUtilAPI1
from org.allbinary.android.api16.ActivityFractureUtilAPI16 import ActivityFractureUtilAPI16
from org.allbinary.android.api19.ActivityFractureUtilAPI19 import ActivityFractureUtilAPI19
from org.allbinary.android.api5.ActivityFractureUtilAPI5 import ActivityFractureUtilAPI5


