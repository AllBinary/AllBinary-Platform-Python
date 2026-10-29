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

from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas


class AndroidTitleProgressBar(ProgressCanvas):
    class TitleProgressBarSetProgressRunnable(object):

        def _init_fields(self) -> None:
            self.androidTitleProgressBar: AndroidTitleProgressBar = None
        

        def __init__(self, androidTitleProgressBar: AndroidTitleProgressBar) -> None:
            self._init_fields()
            self.androidTitleProgressBar = androidTitleProgressBar
        

        def run(self) -> None:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            try:
                value: int = int(self.androidTitleProgressBar.getValue())
                self.androidTitleProgressBar.progressActivity.onTitleProgressBarSetProgress(value)
            except Exception as e:
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    class TitleProgressBarPortionSetProgressRunnable(object):

        def _init_fields(self) -> None:
            self.androidTitleProgressBar: AndroidTitleProgressBar = None
        

        def __init__(self, androidTitleProgressBar: AndroidTitleProgressBar) -> None:
            self._init_fields()
            self.androidTitleProgressBar = androidTitleProgressBar
        

        def run(self) -> None:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            try:
                value: int = int((self.androidTitleProgressBar.getValue() + self.androidTitleProgressBar.getMaxValue() / self.androidTitleProgressBar.portion))
                self.androidTitleProgressBar.progressActivity.onTitleProgressBarSetProgress(value)
            except Exception as e:
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    class ShowTitleProgressBarRunnable(object):

        def _init_fields(self) -> None:
            self.androidTitleProgressBar: AndroidTitleProgressBar = None
        

        def __init__(self, androidTitleProgressBar: AndroidTitleProgressBar) -> None:
            self._init_fields()
            self.androidTitleProgressBar = androidTitleProgressBar
        

        def run(self) -> None:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            try:
                maxValue: int = int(self.androidTitleProgressBar.getMaxValue())
                self.androidTitleProgressBar.progressActivity.onShowTitleProgressBar(maxValue, False)
            except Exception as e:
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
    class DismissTitleProgressBarRunnable(object):

        def _init_fields(self) -> None:
            self.androidTitleProgressBar: AndroidTitleProgressBar = None
        

        def __init__(self, androidTitleProgressBar: AndroidTitleProgressBar) -> None:
            self._init_fields()
            self.androidTitleProgressBar = androidTitleProgressBar
        

        def run(self) -> None:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            try:
                self.androidTitleProgressBar.progressActivity.onDismissTitleProgressBar()
            except Exception as e:
                logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)

    def _init_fields(self) -> None:
        self.showTitleProgressBarRunnable: ShowTitleProgressBarRunnable = ShowTitleProgressBarRunnable(self)
        self.dismissTitleProgressBarRunnable: DismissTitleProgressBarRunnable = DismissTitleProgressBarRunnable(self)
        self.progressDialogPortionSetProgressRunnable: TitleProgressBarPortionSetProgressRunnable = TitleProgressBarPortionSetProgressRunnable(self)
        self.progressDialogSetProgressRunnable: TitleProgressBarSetProgressRunnable = TitleProgressBarSetProgressRunnable(self)
        self.progressActivity: ProgressActivityInterface = NullProgressActivity.NULL_PROGRESS_ACTIVITY
        self.portion: int = 0
    

    def __init__(self, title: str, backgroundBasicColor: BasicColor, foregroundBasicColor: BasicColor) -> None:
        super().__init__(title, backgroundBasicColor, foregroundBasicColor)
        self._init_fields()
    

    def init(self, activity: ProgressActivityInterface) -> None:
        self.progressActivity = activity
    

    def isInitialized(self) -> bool:
        if self.progressActivity != NullProgressActivity.NULL_PROGRESS_ACTIVITY:
            return True
        else:
            return False
    

    def start(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.START_METHOD_NAME)
            super().start()
            self.progressActivity.runOnUiThread(self.showTitleProgressBarRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.START_METHOD_NAME, e)
    

    def end(self) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.END_METHOD_NAME)
            self.progressActivity.runOnUiThread(self.dismissTitleProgressBarRunnable)
            super().end()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.END_METHOD_NAME, e)
    

    def addPortion(self, value: int, text: str, index: int) -> None:
        try:
            super().addPortion(value, text, index)
            self.portion = value
            self.progressActivity.runOnUiThread(self.progressDialogPortionSetProgressRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.ADD_PORTION, e)
    

    def addNormalPortion(self, value: int, text: str) -> None:
        try:
            super().addNormalPortion(value, text)
            self.portion = value
            self.progressActivity.runOnUiThread(self.progressDialogPortionSetProgressRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.ADD_PORTION, e)
    

    def setValue(self, value: int) -> None:
        try:
            super().setValue(value)
            self.progressActivity.runOnUiThread(self.progressDialogSetProgressRunnable)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "setValue", e)
    

    def waitUntilDisplayed(self) -> None:
        pass
    

    def paint(self, graphics: Graphics) -> None:
        pass
# from javax.microedition.lcdui.Graphics import Graphics
from org.allbinary.android.activity.NullProgressActivity import NullProgressActivity
from org.allbinary.android.activity.ProgressActivityInterface import ProgressActivityInterface
from org.allbinary.graphics.color.BasicColor import BasicColor
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.graphics.canvas.transition.progress.ShowTitleProgressBarRunnable import ShowTitleProgressBarRunnable
from org.allbinary.graphics.canvas.transition.progress.DismissTitleProgressBarRunnable import DismissTitleProgressBarRunnable
from org.allbinary.graphics.canvas.transition.progress.TitleProgressBarPortionSetProgressRunnable import TitleProgressBarPortionSetProgressRunnable
from org.allbinary.graphics.canvas.transition.progress.TitleProgressBarSetProgressRunnable import TitleProgressBarSetProgressRunnable


