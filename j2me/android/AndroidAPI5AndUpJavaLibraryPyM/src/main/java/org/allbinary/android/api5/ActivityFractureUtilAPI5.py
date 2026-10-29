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
# package org.allbinary.android.api5

from __future__ import annotations

from org.allbinary.android.api1.ActivityFractureUtilAPI1 import ActivityFractureUtilAPI1


class ActivityFractureUtilAPI5(ActivityFractureUtilAPI1):
    instance5: ActivityFractureUtilAPI5 = None

    def _init_fields(self) -> None:
        self.FEATURE_TOUCHSCREEN_MULTITOUCH: str = "android.hardware.touchscreen.multitouch"
        self.FEATURE_TOUCHSCREEN: str = "android.hardware.touchscreen"
        self.FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT: str = "android.hardware.touchscreen.multitouch.distinct"

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    @staticmethod
    def getInstance() -> ActivityFractureUtilAPI5:
        return ActivityFractureUtilAPI5.instance5
    

    def process(self, activity: Activity) -> None:
        touchScreenFactory: TouchScreenFactory = TouchScreenFactory.getInstance()
        touchScreenTypeFactory: TouchScreenTypeFactory = TouchScreenTypeFactory.getInstance()
        touchScreenFactory.setTouch(self.isTouch(activity))
        touchScreenFactory.setMultiTouch(self.isMultiTouch(activity))
        touchScreenFactory.setMultiTouchDistinct(self.isMultiTouchDistinct(activity))
        touchScreenTypeFactory.update(activity)
        commonStrings: CommonStrings = CommonStrings.getInstance()
        PreLogUtil.put(str(touchScreenFactory), self, commonStrings.PROCESS)
    

    def isTouch(self, activity: Activity) -> bool:
        return self.isFeature(activity, self.FEATURE_TOUCHSCREEN)
    

    def isMultiTouch(self, activity: Activity) -> bool:
        return self.isFeature(activity, self.FEATURE_TOUCHSCREEN_MULTITOUCH)
    

    def isMultiTouchDistinct(self, activity: Activity) -> bool:
        return self.isFeature(activity, self.FEATURE_TOUCHSCREEN_MULTITOUCH_DISTINCT)
    

    def isFeature(self, activity: Activity, property: str) -> bool:
        return activity.getPackageManager().hasSystemFeature(property)
from android.app.Activity import Activity
from org.allbinary.input.motion.button.TouchScreenTypeFactory import TouchScreenTypeFactory
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.input.motion.button.TouchScreenFactory import TouchScreenFactory


ActivityFractureUtilAPI5.instance5 = ActivityFractureUtilAPI5()

