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


class KeyboardInputAutomationProcessor:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def process(keyActionScriptInputInterface: KeyboardActionScriptInputInterface) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        commonStrings: CommonStrings = CommonStrings.getInstance()
        logUtil.putF(str(CommonLabels.getInstance().START) + str(keyActionScriptInputInterface), "KeyInputAutomationProcessor", commonStrings.PROCESS)
        inputRobotInterface: InputRobotInterface = keyActionScriptInputInterface.getInputRobotInterface()
        integer: list[int] = keyActionScriptInputInterface.getKeyArray()
        if keyActionScriptInputInterface.getDelayBetweenKeys() == 0:
            for index in range(0, len(keyActionScriptInputInterface.getKeyArray())):
                if keyActionScriptInputInterface.isPress():
                    inputRobotInterface.keyPress(integer[index])
            time.sleep((keyActionScriptInputInterface.getTime()) / 1000)
            for index in range(len(keyActionScriptInputInterface.getKeyArray()) - 1, 0 - 1, -1):
                if keyActionScriptInputInterface.isRelease():
                    inputRobotInterface.keyRelease(integer[index])
        else:
            for index in range(0, len(keyActionScriptInputInterface.getKeyArray())):
                if keyActionScriptInputInterface.isPress():
                    inputRobotInterface.keyPress(integer[index])
                time.sleep((keyActionScriptInputInterface.getTime()) / 1000)
                if keyActionScriptInputInterface.isRelease():
                    inputRobotInterface.keyRelease(integer[index])
                timeHelper: TimeDelayHelper = TimeDelayHelper(keyActionScriptInputInterface.getDelayBetweenKeys())
                toLong: int = 0
                while not timeHelper.isTimeTNT() or toLong > 6000:
                    toLong += 1
                    time.sleep((50) / 1000)
from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper


