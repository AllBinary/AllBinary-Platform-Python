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
# package bundle.input.automation

from __future__ import annotations

from java.lang.JavaThread import JavaThread
import threading
from java.lang.JavaRuntimeStatic import java_bases
from org.osgi.framework.BundleActivator import BundleActivator
from bundle.input.automation.InputAutomationBundleActivatorListenerInterface import InputAutomationBundleActivatorListenerInterface


class InputAutomationBundleActivator(*java_bases(BundleActivator, InputAutomationBundleActivatorListenerInterface)):
    moduleManagementThread: JavaThread = None
    bundleContext: BundleContext = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getBundleContext() -> BundleContext:
        from org.osgi.framework.BundleContext import BundleContext
        return InputAutomationBundleActivator.bundleContext
    

    # throws Exception
    def start(self, bundleContext: BundleContext) -> None:
        from org.osgi.framework.BundleContext import BundleContext
        from org.allbinary.input.automation.InputAutomationJFrame import InputAutomationJFrame
        from org.allbinary.input.automation.module.osgi.InputAutomationNewBundleRunnable import InputAutomationNewBundleRunnable
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.START)
            InputAutomationBundleActivator.bundleContext = bundleContext
            InputAutomationBundleActivator.moduleManagementThread = JavaThread(target=InputAutomationNewBundleRunnable(self).run)
            InputAutomationBundleActivator.moduleManagementThread.start()
            InputAutomationJFrame.create(self)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.START, e)
            raise e
    

    # throws Exception
    def registerAsService(self) -> None:
        from bundle.input.automation.module.configuration.InputAutomationConfigurationModuleChangeListener import InputAutomationConfigurationModuleChangeListener
        from bundle.input.automation.robot.InputAutomationRobotChangeListener import InputAutomationRobotChangeListener
        from org.allbinary.input.automation.osgi.InputAutomationServiceFactory import InputAutomationServiceFactory
        from org.allbinary.osgi.OSGIActivatorUtil import OSGIActivatorUtil
        OSGIActivatorUtil.registerAsService(self.getBundleContext(), InputAutomationServiceFactory.getInstance(), __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(InputAutomationConfigurationModuleChangeListener))
        OSGIActivatorUtil.registerAsService(self.getBundleContext(), InputAutomationServiceFactory.getInstance(), __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(InputAutomationRobotChangeListener))
    

    # throws Exception
    def useServices(self) -> None:
        from org.allbinary.input.automation.module.osgi.InputAutomationModuleServiceConsumer import InputAutomationModuleServiceConsumer
        from org.allbinary.input.automation.robot.osgi.InputAutomationRobotServiceConsumer import InputAutomationRobotServiceConsumer
        InputAutomationRobotServiceConsumer(self.getBundleContext()).process()
        InputAutomationModuleServiceConsumer(self.getBundleContext()).process()
    

    # throws Exception
    def stop(self, context: BundleContext) -> None:
        from org.osgi.framework.BundleContext import BundleContext
        from org.allbinary.input.automation.InputAutomationJFrame import InputAutomationJFrame
        self.logUtil.putF(self.commonStrings.START, self, "stop")
        if InputAutomationJFrame.getInstance() is not None:
            InputAutomationJFrame.destroy()
        else:
            self.logUtil.putF("Nothing to stop", self, "stop")
# from org.osgi.framework.BundleContext import BundleContext
# from bundle.input.automation.module.configuration.InputAutomationConfigurationModuleChangeListener import InputAutomationConfigurationModuleChangeListener
# from bundle.input.automation.robot.InputAutomationRobotChangeListener import InputAutomationRobotChangeListener
# from org.allbinary.input.automation.InputAutomationJFrame import InputAutomationJFrame
# from org.allbinary.input.automation.module.osgi.InputAutomationModuleServiceConsumer import InputAutomationModuleServiceConsumer
# from org.allbinary.input.automation.module.osgi.InputAutomationNewBundleRunnable import InputAutomationNewBundleRunnable
# from org.allbinary.input.automation.osgi.InputAutomationServiceFactory import InputAutomationServiceFactory
# from org.allbinary.input.automation.robot.osgi.InputAutomationRobotServiceConsumer import InputAutomationRobotServiceConsumer
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.osgi.OSGIActivatorUtil import OSGIActivatorUtil
# from org.allbinary.string.CommonStrings import CommonStrings


