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

from org.allbinary.osgi.OSGIServiceVisitorInterface import OSGIServiceVisitorInterface


class InputAutomationRobotOSGIServiceVisitor(OSGIServiceVisitorInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def visit_j1_1(self, anyType: object) -> object:
        from org.allbinary.osgi.OSGIServiceInterface import OSGIServiceInterface
        return self.visit(anyType)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def visit_j1_2(self, osgiServiceInterface: OSGIServiceInterface) -> bool:
        from bundle.input.automation.robot.InputAutomationRobotServiceInterface import InputAutomationRobotServiceInterface
        from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
        from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
        from org.allbinary.osgi.OSGIServiceInterface import OSGIServiceInterface
        try:
            self.logUtil.putF(self.commonStrings.START, self, "visit")
            inputAutomationRobotServiceInterface: InputAutomationRobotServiceInterface = osgiServiceInterface
            inputRobotInterfaceArray: list[InputRobotInterface] = inputAutomationRobotServiceInterface.getInputRobotInterfaceArray()
            for index in range(0, len(inputRobotInterfaceArray)):
                self.logUtil.putF("Adding: " + inputRobotInterfaceArray[index].getName(), self, "visit")
                InputRobotFactory.getInstance().add(inputRobotInterfaceArray[index])
            return True
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "visit", e)
            return False

    def visit(self, *args):
        if len(args) == 1 and True:
            return __class__.__dict__["visit_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["visit_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("visit_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().visit(*args)
# from bundle.input.automation.robot.InputAutomationRobotServiceInterface import InputAutomationRobotServiceInterface
# from org.allbinary.input.automation.robot.InputRobotFactory import InputRobotFactory
# from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.osgi.OSGIServiceInterface import OSGIServiceInterface
# from org.allbinary.string.CommonStrings import CommonStrings


