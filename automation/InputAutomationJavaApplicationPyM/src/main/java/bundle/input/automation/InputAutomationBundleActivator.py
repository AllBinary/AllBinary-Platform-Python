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

import threading
from org.osgi.framework.BundleActivator import BundleActivator
from bundle.input.automation.InputAutomationBundleActivatorListenerInterface import InputAutomationBundleActivatorListenerInterface


class InputAutomationBundleActivator(BundleActivator, InputAutomationBundleActivatorListenerInterface):
    moduleManagementThread: threading.Thread = None
    bundleContext: BundleContext = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getBundleContext() -> BundleContext:
        return InputAutomationBundleActivator.bundleContext
    

    # throws Exception
    def start(self, bundleContext: BundleContext) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.START)
            self.bundleContext = bundleContext
            InputAutomationBundleActivator.moduleManagementThread = threading.Thread(target=InputAutomationNewBundleRunnable(self).run)
            InputAutomationBundleActivator.moduleManagementThread.start()
            InputAutomationJFrame.create(self)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.START, e)
            raise e
    

    # throws Exception
    def registerAsService(self) -> None:
        OSGIActivatorUtil.registerAsService(self.getBundleContext(), InputAutomationServiceFactory.getInstance(), InputAutomationConfigurationModuleChangeListener.getName())
        OSGIActivatorUtil.registerAsService(self.getBundleContext(), InputAutomationServiceFactory.getInstance(), InputAutomationRobotChangeListener.getName())
    

    # throws Exception
    def useServices(self) -> None:
        InputAutomationRobotServiceConsumer(self.getBundleContext()).process()
        InputAutomationModuleServiceConsumer(self.getBundleContext()).process()
    

    # throws Exception
    def stop(self, context: BundleContext) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "stop")
        if InputAutomationJFrame.getInstance() is not None:
            InputAutomationJFrame.destroy()
        else:
            self.logUtil.putF("Nothing to stop", self, "stop")
from org.osgi.framework.BundleContext import BundleContext
from bundle.input.automation.module.configuration.InputAutomationConfigurationModuleChangeListener import InputAutomationConfigurationModuleChangeListener
from bundle.input.automation.robot.InputAutomationRobotChangeListener import InputAutomationRobotChangeListener
from org.allbinary.input.automation.InputAutomationJFrame import InputAutomationJFrame
from org.allbinary.input.automation.module.osgi.InputAutomationModuleServiceConsumer import InputAutomationModuleServiceConsumer
from org.allbinary.input.automation.module.osgi.InputAutomationNewBundleRunnable import InputAutomationNewBundleRunnable
from org.allbinary.input.automation.osgi.InputAutomationServiceFactory import InputAutomationServiceFactory
from org.allbinary.input.automation.robot.osgi.InputAutomationRobotServiceConsumer import InputAutomationRobotServiceConsumer
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.osgi.OSGIActivatorUtil import OSGIActivatorUtil
from org.allbinary.string.CommonStrings import CommonStrings


