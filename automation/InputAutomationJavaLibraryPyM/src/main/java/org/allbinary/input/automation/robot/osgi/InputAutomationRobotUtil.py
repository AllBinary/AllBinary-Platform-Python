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
# package org.allbinary.input.automation.robot.osgi

from __future__ import annotations



class InputAutomationRobotUtil:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getChangeEvent(inputRobotInterface: InputRobotInterface) -> InputAutomationRobotChangeEvent:
        from org.allbinary.input.automation.robot.osgi.InputAutomationRobotInterfaceWrapper import InputAutomationRobotInterfaceWrapper
        from org.allbinary.input.automation.robot.osgi.InputAutomationRobotChangeEvent import InputAutomationRobotChangeEvent
        inputAutomationRobotInterfaceWrapper: InputAutomationRobotInterfaceWrapper = InputAutomationRobotInterfaceWrapper(inputRobotInterface)
        inputAutomationRobotChangeEvent: InputAutomationRobotChangeEvent = InputAutomationRobotChangeEvent(inputAutomationRobotInterfaceWrapper)
        return inputAutomationRobotChangeEvent
from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface


