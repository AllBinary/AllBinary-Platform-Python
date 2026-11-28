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
# package org.allbinary.graphics.canvas.transition.progress

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_new_inner
from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_divide
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas


@java_inherited_overloads
class AndroidTitleProgressBar(ProgressCanvas):
    class TitleProgressBarSetProgressRunnable(object):

        def _init_fields(self) -> None:
            if "androidTitleProgressBar" not in vars(self): self.androidTitleProgressBar: AndroidTitleProgressBar = None
        

        def __init__(self, androidTitleProgressBar: AndroidTitleProgressBar) -> None:
            __class__._init_fields(self)
            self.androidTitleProgressBar = androidTitleProgressBar
        

        def run(self) -> None:
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.string.CommonStrings import CommonStrings
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            try:
                value: int = int(self.androidTitleProgressBar.getValue())
                self.androidTitleProgressBar.progressActivity.onTitleProgressBarSetProgress(value)
            except Exception as e:
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    class TitleProgressBarPortionSetProgressRunnable(object):

        def _init_fields(self) -> None:
            if "androidTitleProgressBar" not in vars(self): self.androidTitleProgressBar: AndroidTitleProgressBar = None
        

        def __init__(self, androidTitleProgressBar: AndroidTitleProgressBar) -> None:
            __class__._init_fields(self)
            self.androidTitleProgressBar = androidTitleProgressBar
        

        def run(self) -> None:
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.string.CommonStrings import CommonStrings
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            try:
                value: int = int((self.androidTitleProgressBar.getValue() + java_divide(self.androidTitleProgressBar.getMaxValue(), self.androidTitleProgressBar.portion)))
                self.androidTitleProgressBar.progressActivity.onTitleProgressBarSetProgress(value)
            except Exception as e:
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    class ShowTitleProgressBarRunnable(object):

        def _init_fields(self) -> None:
            if "androidTitleProgressBar" not in vars(self): self.androidTitleProgressBar: AndroidTitleProgressBar = None
        

        def __init__(self, androidTitleProgressBar: AndroidTitleProgressBar) -> None:
            __class__._init_fields(self)
            self.androidTitleProgressBar = androidTitleProgressBar
        

        def run(self) -> None:
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.string.CommonStrings import CommonStrings
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            try:
                maxValue: int = int(self.androidTitleProgressBar.getMaxValue())
                self.androidTitleProgressBar.progressActivity.onShowTitleProgressBar(maxValue, False)
            except Exception as e:
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    class DismissTitleProgressBarRunnable(object):

        def _init_fields(self) -> None:
            if "androidTitleProgressBar" not in vars(self): self.androidTitleProgressBar: AndroidTitleProgressBar = None
        

        def __init__(self, androidTitleProgressBar: AndroidTitleProgressBar) -> None:
            __class__._init_fields(self)
            self.androidTitleProgressBar = androidTitleProgressBar
        

        def run(self) -> None:
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.string.CommonStrings import CommonStrings
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            try:
                self.androidTitleProgressBar.progressActivity.onDismissTitleProgressBar()
            except Exception as e:
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    def _java_defaults(self):
        vars(self).setdefault("showTitleProgressBarRunnable", None)
        vars(self).setdefault("dismissTitleProgressBarRunnable", None)
        vars(self).setdefault("progressDialogPortionSetProgressRunnable", None)
        vars(self).setdefault("progressDialogSetProgressRunnable", None)
        vars(self).setdefault("progressActivity", None)
        vars(self).setdefault("portion", 0)

    def _init_fields(self) -> None:
        from org.allbinary.android.activity.NullProgressActivity import NullProgressActivity
        self.showTitleProgressBarRunnable: ShowTitleProgressBarRunnable = java_new_inner(self, ShowTitleProgressBarRunnable, self)
        self.dismissTitleProgressBarRunnable: DismissTitleProgressBarRunnable = java_new_inner(self, DismissTitleProgressBarRunnable, self)
        self.progressDialogPortionSetProgressRunnable: TitleProgressBarPortionSetProgressRunnable = java_new_inner(self, TitleProgressBarPortionSetProgressRunnable, self)
        self.progressDialogSetProgressRunnable: TitleProgressBarSetProgressRunnable = java_new_inner(self, TitleProgressBarSetProgressRunnable, self)
        self.progressActivity: ProgressActivityInterface = NullProgressActivity.NULL_PROGRESS_ACTIVITY
        self.portion: int = 0
    

    def __init__(self, title: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        __class__._java_defaults(self)
        from org.allbinary.graphics.color.BasicColor import BasicColor
        super().__init__(title, backgroundBasicColor, foregroundBasicColor)
        __class__._init_fields(self)
    

    def init(self, activity: ProgressActivityInterface) -> None:
        from org.allbinary.android.activity.ProgressActivityInterface import ProgressActivityInterface
        self.progressActivity = activity
    

    def isInitialized(self) -> bool:
        from org.allbinary.android.activity.NullProgressActivity import NullProgressActivity
        if self.progressActivity != NullProgressActivity.NULL_PROGRESS_ACTIVITY:
            return True
        else:
            return False
    

    def start(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.START_METHOD_NAME)
            java_super_call(super(), "start")
            self.progressActivity.runOnUiThread(self.showTitleProgressBarRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.START_METHOD_NAME, e)
    

    def end(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.END_METHOD_NAME)
            self.progressActivity.runOnUiThread(self.dismissTitleProgressBarRunnable)
            java_super_call(super(), "end")
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.END_METHOD_NAME, e)
    

    def addPortion(self, value: int, text: str, index: int) -> None:
        try:
            java_super_call(super(), "addPortion", value, text, index)
            self.portion = value
            self.progressActivity.runOnUiThread(self.progressDialogPortionSetProgressRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.ADD_PORTION, e)
    

    def addNormalPortion(self, value: int, text: str) -> None:
        try:
            java_super_call(super(), "addNormalPortion", value, text)
            self.portion = value
            self.progressActivity.runOnUiThread(self.progressDialogPortionSetProgressRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.ADD_PORTION, e)
    

    def setValue(self, value: int) -> None:
        try:
            java_super_call(super(), "setValue", value)
            self.progressActivity.runOnUiThread(self.progressDialogSetProgressRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "setValue", e)
    

    def waitUntilDisplayed(self) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        from javax.microedition.lcdui.Graphics import Graphics
        pass
# from javax.microedition.lcdui.Graphics import Graphics
# from org.allbinary.android.activity.NullProgressActivity import NullProgressActivity
# from org.allbinary.android.activity.ProgressActivityInterface import ProgressActivityInterface
# from org.allbinary.graphics.color.BasicColor import BasicColor
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings


