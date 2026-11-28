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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.osgi.service.InputAutomationServiceConsumer import InputAutomationServiceConsumer


@java_inherited_overloads
class InputAutomationRobotServiceConsumer(InputAutomationServiceConsumer):
    

    def __init__(self, bundleContext: BundleContext) -> None:
        from org.allbinary.input.automation.robot.osgi.InputAutomationRobotOSGIServiceVisitor import InputAutomationRobotOSGIServiceVisitor
        from org.osgi.framework.BundleContext import BundleContext
        from bundle.input.automation.robot.InputAutomationRobotServiceInterface import InputAutomationRobotServiceInterface
        super().__init__(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(InputAutomationRobotServiceInterface), bundleContext, InputAutomationRobotOSGIServiceVisitor())
# from org.osgi.framework.BundleContext import BundleContext
# from bundle.input.automation.robot.InputAutomationRobotServiceInterface import InputAutomationRobotServiceInterface


