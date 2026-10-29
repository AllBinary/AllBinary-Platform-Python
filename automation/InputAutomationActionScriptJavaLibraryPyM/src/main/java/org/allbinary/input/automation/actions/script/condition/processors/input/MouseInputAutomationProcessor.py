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
# package org.allbinary.input.automation.actions.script.condition.processors.input

from __future__ import annotations

import time
import threading


class MouseInputAutomationProcessor:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def process(mouseActionScriptInputInterface: MouseActionScriptInputInterface) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        logUtil.putF(str(StringMaker().append("Start - Processing Mouse Input at: ").append(str(mouseActionScriptInputInterface.getPoint())).append(" clicks: ").appendint(int(mouseActionScriptInputInterface.getButtonClicks()))), "MouseInputAutomationProcessor", commonStrings.PROCESS)
        inputRobotInterface: InputRobotInterface = mouseActionScriptInputInterface.getInputRobotInterface()
        if mouseActionScriptInputInterface.getPoint().x != -1 and mouseActionScriptInputInterface.getPoint().y != -1:
            inputRobotInterface.mouseMove(mouseActionScriptInputInterface.getPoint())
        time.sleep((mouseActionScriptInputInterface.getTime()) / 1000)
        if mouseActionScriptInputInterface.getButtonClicks() != 0:
            inputRobotInterface.mousePress(mouseActionScriptInputInterface.getButtonClicks())
            time.sleep((mouseActionScriptInputInterface.getTime()) / 1000)
            inputRobotInterface.mouseRelease(mouseActionScriptInputInterface.getButtonClicks())
        time.sleep((mouseActionScriptInputInterface.getTime()) / 1000)
from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings


