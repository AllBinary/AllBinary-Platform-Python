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
# package org.allbinary.input.motion.gesture.observer

from __future__ import annotations

from org.allbinary.input.motion.gesture.observer.CompleteMotionGestureListenerInterface import CompleteMotionGestureListenerInterface


class NullCompleteMotionGestureReceiver(CompleteMotionGestureListenerInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self._init_fields()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF("Null Gesture Reciever", self, commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def onMotionGestureCompleted(self, list_: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        pass
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList


