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
# package org.allbinary.android.api1

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.android.ActivityFractureUtil import ActivityFractureUtil


class ActivityFractureUtilAPI1(ActivityFractureUtil):
    instance: ActivityFractureUtilAPI1 = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> ActivityFractureUtilAPI1:
        return ActivityFractureUtilAPI1.instance
    

    # throws Exception
    def process(self, activity: Activity) -> None:
        from android.app.Activity import Activity
        pass
    

    def setFullScreen(self, activity: Activity) -> None:
        from android.app.Activity import Activity
        from android.view.WindowManager import WindowManager
        activity.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN)
# from android.app.Activity import Activity
# from android.view.WindowManager import WindowManager


def _ActivityFractureUtilAPI1_instance() -> object:
    return ActivityFractureUtilAPI1()

lazy_static(ActivityFractureUtilAPI1, "instance", _ActivityFractureUtilAPI1_instance)

