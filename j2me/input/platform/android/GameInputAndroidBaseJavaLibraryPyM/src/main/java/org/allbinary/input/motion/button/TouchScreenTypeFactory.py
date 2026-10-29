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
# package org.allbinary.input.motion.button

from __future__ import annotations



class TouchScreenTypeFactory:
    instance: TouchScreenTypeFactory = None
    

    @staticmethod
    def getInstance() -> TouchScreenTypeFactory:
        return TouchScreenTypeFactory.instance
    

    def update(self, activity: Activity) -> None:
        from org.allbinary.input.motion.button.TouchScreenFactory import TouchScreenFactory
        from org.allbinary.input.motion.button.TouchScreenTypesFactory import TouchScreenTypesFactory
        commonStrings: CommonStrings = CommonStrings.getInstance()
        touchScreenFactory: TouchScreenFactory = TouchScreenFactory.getInstance()
        touchScreenTypesFactory: TouchScreenTypesFactory = TouchScreenTypesFactory.getInstance()
        configuration: Configuration = activity.getResources().getConfiguration()
        touchScreen: int = configuration.touchscreen
        if touchScreen == Configuration.TOUCHSCREEN_FINGER:
            touchScreenFactory.setTouchScreenType(touchScreenTypesFactory.FINGER)
            if not touchScreenFactory.isTouch():
                PreLogUtil.put("Not Really Exception: This indicates that a touch screen does exist but is not API8 so we will try it", self, commonStrings.PROCESS)
                touchScreenFactory.setTouch(True)
        elif touchScreen == Configuration.TOUCHSCREEN_STYLUS:
            touchScreenFactory.setTouchScreenType(touchScreenTypesFactory.STYLUS)
            if not touchScreenFactory.isTouch():
                PreLogUtil.put("Not Really Exception: This indicates that a touch screen does exist but is not API8 so we will try it", self, commonStrings.PROCESS)
                touchScreenFactory.setTouch(True)
        elif touchScreen == Configuration.TOUCHSCREEN_NOTOUCH:
            touchScreenFactory.setTouchScreenType(touchScreenTypesFactory.NOTOUCH)
        elif touchScreen == Configuration.TOUCHSCREEN_UNDEFINED:
            touchScreenFactory.setTouchScreenType(touchScreenTypesFactory.UNDEFINED)
from android.app.Activity import Activity
from android.content.res.Configuration import Configuration
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil


TouchScreenTypeFactory.instance = TouchScreenTypeFactory()

