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

from org.osgi.framework.BundleActivator import BundleActivator


class InputAutomationRobotBundleActivator(BundleActivator):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.inputRobotInterface: list[InputRobotInterface] = None
        self.serviceFactory: ServiceFactory = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.init()
    

    # throws Exception
    def init(self) -> None:
        raise RuntimeError()
    

    # throws Exception
    def registerAsService(self, bundleContext: BundleContext) -> None:
        OSGIActivatorUtil.registerAsService(bundleContext, self.getServiceFactory(), InputAutomationRobotServiceInterface.getName())
    

    # throws Exception
    def getInputAutomationRobotChangeListener(self, context: BundleContext) -> InputAutomationRobotChangeListener:
        serviceReference: ServiceReference = context.getServiceReference(InputAutomationRobotChangeListener.getName())
        if serviceReference is not None:
            inputAutomationRobotChangeListener: InputAutomationRobotChangeListener = context.getService(serviceReference)
            if inputAutomationRobotChangeListener is None:
                raise Exception("No Service For ServiceReference")
            return inputAutomationRobotChangeListener
        else:
            self.logUtil.putF("No ServiceReference: " + InputAutomationRobotChangeListener.getName(), self, "getInputAutomationRobotChangeListener")
            return None
    

    def addRobots(self, context: BundleContext) -> None:
        from org.allbinary.input.automation.robot.osgi.InputAutomationRobotUtil import InputAutomationRobotUtil
        try:
            self.logUtil.putF(self.commonStrings.START, self, "addRobots")
            inputAutomationRobotChangeListener: InputAutomationRobotChangeListener = self.getInputAutomationRobotChangeListener(context)
            if inputAutomationRobotChangeListener is not None:
                for index in range(0, len(self.getInputRobotInterface())):
                    inputAutomationRobotChangeEvent: InputAutomationRobotChangeEvent = InputAutomationRobotUtil.getChangeEvent(self.getInputRobotInterface()[index])
                    inputAutomationRobotChangeListener.onAdd(inputAutomationRobotChangeEvent)
        except Exception as e:
            self.logUtil.putF(self.commonStrings.EXCEPTION, self, "addModules")
    

    def removeRobots(self, context: BundleContext) -> None:
        from org.allbinary.input.automation.robot.osgi.InputAutomationRobotUtil import InputAutomationRobotUtil
        try:
            self.logUtil.putF(self.commonStrings.START, self, "removeRobots")
            inputAutomationRobotChangeListener: InputAutomationRobotChangeListener = self.getInputAutomationRobotChangeListener(context)
            if inputAutomationRobotChangeListener is not None:
                for index in range(0, len(self.getInputRobotInterface())):
                    inputAutomationRobotChangeEvent: InputAutomationRobotChangeEvent = InputAutomationRobotUtil.getChangeEvent(self.getInputRobotInterface()[index])
                    inputAutomationRobotChangeListener.onRemove(inputAutomationRobotChangeEvent)
        except Exception as e:
            self.logUtil.putF(self.commonStrings.EXCEPTION, self, "removeRobots")
    

    # throws Exception
    def start(self, context: BundleContext) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.START)
        self.addRobots(context)
        self.registerAsService(context)
    

    # throws Exception
    def stop(self, context: BundleContext) -> None:
        self.logUtil.putF("Stop", self, self.commonStrings.START)
        self.removeRobots(context)
    

    def getServiceFactory(self) -> object:
        return self.serviceFactory
    

    def setServiceFactory(self, serviceObject: ServiceFactory) -> None:
        self.serviceFactory = serviceObject
    

    def getInputRobotInterface(self) -> list[InputRobotInterface]:
        return self.inputRobotInterface
    

    def setInputRobotInterface(self, inputRobotInterface: list[InputRobotInterface]) -> None:
        self.inputRobotInterface = inputRobotInterface
from org.osgi.framework.BundleContext import BundleContext
from org.osgi.framework.ServiceFactory import ServiceFactory
from org.osgi.framework.ServiceReference import ServiceReference
from bundle.input.automation.robot.InputAutomationRobotChangeListener import InputAutomationRobotChangeListener
from bundle.input.automation.robot.InputAutomationRobotServiceInterface import InputAutomationRobotServiceInterface
from org.allbinary.input.automation.robot.InputRobotInterface import InputRobotInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.osgi.OSGIActivatorUtil import OSGIActivatorUtil
from org.allbinary.string.CommonStrings import CommonStrings


