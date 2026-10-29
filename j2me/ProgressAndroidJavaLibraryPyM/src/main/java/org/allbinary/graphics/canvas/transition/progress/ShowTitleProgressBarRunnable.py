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

from org.allbinary.graphics.canvas.transition.progress.ProgressRunnable import ProgressRunnable


class ShowTitleProgressBarRunnable(ProgressRunnable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.FADE_IN_HALF: list[int] = [TransistionTypes.getInstance().FADE_IN_TO_HALF_ALPHA, TransistionTypes.getInstance().FADE_IN_FROM_HALF_ALPHA]
    

    def __init__(self, midletActivity: Activity, progressCanvas: ProgressCanvas) -> None:
        super().__init__(midletActivity, progressCanvas)
        self._init_fields()
    

    def run(self) -> None:
        try:
            self.midletActivity.onShowProgress(False, self.FADE_IN_HALF)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
from org.allbinary.animation.transition.TransistionTypes import TransistionTypes
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from android.app.Activity import Activity


