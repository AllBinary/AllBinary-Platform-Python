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

from org.allbinary.osgi.service.InputAutomationServiceConsumer import InputAutomationServiceConsumer


class InputAutomationRobotServiceConsumer(InputAutomationServiceConsumer):
    

    def __init__(self, bundleContext: BundleContext) -> None:
        from org.allbinary.input.automation.robot.osgi.InputAutomationRobotOSGIServiceVisitor import InputAutomationRobotOSGIServiceVisitor
        super().__init__(InputAutomationRobotServiceInterface.getName(), bundleContext, InputAutomationRobotOSGIServiceVisitor())
from org.osgi.framework.BundleContext import BundleContext
from bundle.input.automation.robot.InputAutomationRobotServiceInterface import InputAutomationRobotServiceInterface


