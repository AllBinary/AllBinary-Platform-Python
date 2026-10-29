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
# package org.allbinary.android.api30

from __future__ import annotations

from org.allbinary.android.api5.ActivityFractureUtilAPI5 import ActivityFractureUtilAPI5


class ActivityFractureUtilAPI30(ActivityFractureUtilAPI5):
    instance30: ActivityFractureUtilAPI30 = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> ActivityFractureUtilAPI30:
        return ActivityFractureUtilAPI30.instance30
    

    def setFullScreen(self, activity: Activity) -> None:
        window: Window = activity.getWindow()
        windowInsetsController: WindowInsetsControllerCompat = WindowCompat.getInsetsController(window, window.getDecorView())
        windowInsetsController.hide(WindowInsetsCompat.Type.systemBars())
        windowInsetsController.setSystemBarsBehavior(WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE)
from android.app.Activity import Activity
from android.view.Window import Window
from androidx.core.view.WindowCompat import WindowCompat
from androidx.core.view.WindowInsetsCompat import WindowInsetsCompat
from androidx.core.view.WindowInsetsControllerCompat import WindowInsetsControllerCompat


ActivityFractureUtilAPI30.instance30 = ActivityFractureUtilAPI30()

