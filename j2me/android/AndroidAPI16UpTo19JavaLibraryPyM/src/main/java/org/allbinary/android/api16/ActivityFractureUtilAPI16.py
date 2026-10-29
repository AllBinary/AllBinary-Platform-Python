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
# package org.allbinary.android.api16

from __future__ import annotations

from org.allbinary.android.api5.ActivityFractureUtilAPI5 import ActivityFractureUtilAPI5


class ActivityFractureUtilAPI16(ActivityFractureUtilAPI5):
    instance16: ActivityFractureUtilAPI16 = None

    def __init__(self) -> None:
        super().__init__()
    

    @staticmethod
    def getInstance() -> ActivityFractureUtilAPI16:
        return ActivityFractureUtilAPI16.instance16
    

    def setFullScreen(self, activity: Activity) -> None:
        decorView: View = activity.getWindow().getDecorView()
        visibility: int = View.SYSTEM_UI_FLAG_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_FULLSCREEN
        decorView.setSystemUiVisibility(visibility)
from android.app.Activity import Activity
from android.view.View import View


ActivityFractureUtilAPI16.instance16 = ActivityFractureUtilAPI16()

