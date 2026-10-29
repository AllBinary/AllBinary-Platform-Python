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
# package org.allbinary.android.input.api3

from __future__ import annotations



class ShowVirtualKeyboardRunnable(object):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.activity: Activity = None
    

    def __init__(self, activity: Activity) -> None:
        self._init_fields()
        self.activity = activity
    

    def run(self) -> None:
        try:
            inputMethodManager: InputMethodManager = self.activity.getSystemService(Context.INPUT_METHOD_SERVICE)
            viewCompositeInterface: ViewCompositeInterface = self.activity
            if viewCompositeInterface is None:
                ForcedLogUtil.log("Activity Null", self)
            view: View = viewCompositeInterface.getView()
            inputMethodManager.toggleSoftInputFromWindow(view.getWindowToken(), InputMethodManager.SHOW_FORCED, 0)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
from android.app.Activity import Activity
from android.content.Context import Context
from android.view.View import View
from android.view.inputmethod.InputMethodManager import InputMethodManager
from org.allbinary.android.activity.ViewCompositeInterface import ViewCompositeInterface
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


