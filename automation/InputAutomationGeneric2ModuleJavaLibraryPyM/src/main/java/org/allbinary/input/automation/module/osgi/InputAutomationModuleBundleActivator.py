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
# package org.allbinary.input.automation.module.osgi

from __future__ import annotations

from org.osgi.framework.BundleActivator import BundleActivator


class InputAutomationModuleBundleActivator(BundleActivator):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.inputAutomationModuleInterface: list[InputAutomationModuleFactoryInterface] = None
        self.serviceFactory: ServiceFactory = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.init()
    

    # throws Exception
    def init(self) -> None:
        raise RuntimeError()
    

    # throws Exception
    def getInputAutomationConfigurationModuleChangeListener(self, context: BundleContext) -> InputAutomationConfigurationModuleChangeListener:
        serviceReference: ServiceReference = context.getServiceReference(InputAutomationConfigurationModuleChangeListener.getName())
        if serviceReference is not None:
            inputAutomationConfigurationModuleChangeListener: InputAutomationConfigurationModuleChangeListener = context.getService(serviceReference)
            if inputAutomationConfigurationModuleChangeListener is None:
                raise Exception("No Service For ServiceReference")
            return inputAutomationConfigurationModuleChangeListener
        else:
            self.logUtil.putF("No ServiceReference: " + InputAutomationConfigurationModuleChangeListener.getName(), self, "addModules")
            return None
    

    def addModules(self, context: BundleContext) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, "addModules")
            inputAutomationConfigurationModuleChangeListener: InputAutomationConfigurationModuleChangeListener = self.getInputAutomationConfigurationModuleChangeListener(context)
            if inputAutomationConfigurationModuleChangeListener is not None:
                for index in range(0, len(self.getInputAutomationModuleInterface())):
                    inputAutomationConfigurationModuleChangeEvent: InputAutomationConfigurationModuleChangeEvent = InputAutomationConfigurationUtil.getChangeEvent(self.getInputAutomationModuleInterface()[index])
                    inputAutomationConfigurationModuleChangeListener.onAdd(inputAutomationConfigurationModuleChangeEvent)
        except Exception as e:
            self.logUtil.putF(self.commonStrings.EXCEPTION, self, "addModules")
    

    # throws Exception
    def registerAsService(self, bundleContext: BundleContext) -> None:
        OSGIActivatorUtil.registerAsService(bundleContext, self.getServiceFactory(), InputAutomationModuleServiceInterface.getName())
    

    def removeModules(self, context: BundleContext) -> None:
        try:
            self.logUtil.putF(self.commonStrings.START, self, "removeModules")
            inputAutomationConfigurationModuleChangeListener: InputAutomationConfigurationModuleChangeListener = self.getInputAutomationConfigurationModuleChangeListener(context)
            if inputAutomationConfigurationModuleChangeListener is not None:
                for index in range(0, len(self.getInputAutomationModuleInterface())):
                    inputAutomationConfigurationModuleChangeEvent: InputAutomationConfigurationModuleChangeEvent = InputAutomationConfigurationUtil.getChangeEvent(self.getInputAutomationModuleInterface()[index])
                    inputAutomationConfigurationModuleChangeListener.onRemove(inputAutomationConfigurationModuleChangeEvent)
        except Exception as e:
            self.logUtil.putF(self.commonStrings.EXCEPTION, self, "removeModules")
    

    # throws Exception
    def start(self, context: BundleContext) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.START)
        self.addModules(context)
        self.registerAsService(context)
    

    # throws Exception
    def stop(self, context: BundleContext) -> None:
        self.logUtil.putF(self.commonStrings.START, self, "stop")
        self.removeModules(context)
    

    def getInputAutomationModuleInterface(self) -> list[InputAutomationModuleFactoryInterface]:
        return self.inputAutomationModuleInterface
    

    def setInputAutomationModuleInterface(self, inputAutomationModuleInterface: list[InputAutomationModuleFactoryInterface]) -> None:
        self.inputAutomationModuleInterface = inputAutomationModuleInterface
    

    def getServiceFactory(self) -> object:
        return self.serviceFactory
    

    def setServiceFactory(self, serviceObject: ServiceFactory) -> None:
        self.serviceFactory = serviceObject
from org.osgi.framework.BundleContext import BundleContext
from org.osgi.framework.ServiceFactory import ServiceFactory
from org.osgi.framework.ServiceReference import ServiceReference
from bundle.input.automation.module.InputAutomationModuleServiceInterface import InputAutomationModuleServiceInterface
from bundle.input.automation.module.configuration.InputAutomationConfigurationModuleChangeListener import InputAutomationConfigurationModuleChangeListener
from org.allbinary.input.automation.configuration.InputAutomationConfigurationModuleChangeEvent import InputAutomationConfigurationModuleChangeEvent
from org.allbinary.input.automation.configuration.InputAutomationConfigurationUtil import InputAutomationConfigurationUtil
from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.osgi.OSGIActivatorUtil import OSGIActivatorUtil
from org.allbinary.string.CommonStrings import CommonStrings


