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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.graphics.canvas.transition.progress.ProgressRunnable import ProgressRunnable


@java_inherited_overloads
class DismissTitleProgressBarRunnable(ProgressRunnable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("ZOOM_OUT_AND_IN", None)

    def _init_fields(self) -> None:
        from org.allbinary.animation.transition.TransistionTypes import TransistionTypes
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.ZOOM_OUT_AND_IN: list[int] = [TransistionTypes.getInstance().ZOOM_OUT, TransistionTypes.getInstance().ZOOM_IN]
    

    def __init__(self, midletActivity: Activity, progressCanvas: ProgressCanvas) -> None:
        __class__._java_defaults(self)
        from android.app.Activity import Activity
        super().__init__(midletActivity, progressCanvas)
        __class__._init_fields(self)
    

    def run(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        try:
            self.midletActivity.onDismissProgress(self.ZOOM_OUT_AND_IN)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.RUN, e)
# from org.allbinary.animation.transition.TransistionTypes import TransistionTypes
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from android.app.Activity import Activity


