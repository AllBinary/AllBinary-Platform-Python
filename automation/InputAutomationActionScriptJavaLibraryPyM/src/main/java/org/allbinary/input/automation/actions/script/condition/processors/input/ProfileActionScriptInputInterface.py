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

from org.allbinary.input.automation.actions.script.condition.processors.ProfileActionScriptProcessorInterface import ProfileActionScriptProcessorInterface


# Java interface
class ProfileActionScriptInputInterface(ProfileActionScriptProcessorInterface):
    

    def setInputRobotInterface(self, inputRobotInterface: InputRobotInterface) -> None:
        raise NotImplementedError()
    

    def getInputRobotInterface(self) -> InputRobotInterface:
        raise NotImplementedError()
    

    def getTime(self) -> int:
        raise NotImplementedError()
    

    def setTime(self, time: int) -> None:
        raise NotImplementedError()
from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface


