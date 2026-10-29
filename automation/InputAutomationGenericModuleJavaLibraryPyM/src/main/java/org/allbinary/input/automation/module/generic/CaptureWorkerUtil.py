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
# package org.allbinary.input.automation.module.generic

from __future__ import annotations



class CaptureWorkerUtil:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    @staticmethod
    def processProfileActionConditions(vector: BasicArrayList, frame: int) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        logUtil.putF(commonStrings.START, "CaptureWorkerUtil", "processProfileActionConditions")
        size: int = vector.size()
        for index in range(0, size):
            profileActionConditionInterface: ProfileActionScriptConditionInterface = vector.get(index)
            if profileActionConditionInterface.shouldProcess(frame):
                profileActionConditionInterface.process(frame)
            else:
                pass
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


