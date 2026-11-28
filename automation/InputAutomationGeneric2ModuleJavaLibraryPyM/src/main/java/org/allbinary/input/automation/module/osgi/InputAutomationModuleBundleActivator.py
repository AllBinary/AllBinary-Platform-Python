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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "inputAutomationModuleInterface" not in vars(self): self.inputAutomationModuleInterface: list[InputAutomationModuleFactoryInterface] = None
        if "serviceFactory" not in vars(self): self.serviceFactory: ServiceFactory = None
    

    def __init__(self) -> None:
        __class__._init_fields(self)
        self.init()
    

    # throws Exception
    def init(self) -> None:
        raise RuntimeError()
    

    # throws Exception
    def getInputAutomationConfigurationModuleChangeListener(self, context: BundleContext) -> InputAutomationConfigurationModuleChangeListener:
        from org.osgi.framework.BundleContext import BundleContext
        from org.osgi.framework.ServiceReference import ServiceReference
        from bundle.input.automation.module.configuration.InputAutomationConfigurationModuleChangeListener import InputAutomationConfigurationModuleChangeListener
        serviceReference: ServiceReference = context.getServiceReference(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(InputAutomationConfigurationModuleChangeListener))
        if serviceReference is not None:
            inputAutomationConfigurationModuleChangeListener: InputAutomationConfigurationModuleChangeListener = context.getService(serviceReference)
            if inputAutomationConfigurationModuleChangeListener is None:
                raise Exception("No Service For ServiceReference")
            return inputAutomationConfigurationModuleChangeListener
        else:
            self.logUtil.putF("No ServiceReference: " + __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(InputAutomationConfigurationModuleChangeListener), self, "addModules")
            return None
    

    def addModules(self, context: BundleContext) -> None:
        from org.osgi.framework.BundleContext import BundleContext
        from bundle.input.automation.module.configuration.InputAutomationConfigurationModuleChangeListener import InputAutomationConfigurationModuleChangeListener
        from org.allbinary.input.automation.configuration.InputAutomationConfigurationModuleChangeEvent import InputAutomationConfigurationModuleChangeEvent
        from org.allbinary.input.automation.configuration.InputAutomationConfigurationUtil import InputAutomationConfigurationUtil
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
        from org.osgi.framework.BundleContext import BundleContext
        from bundle.input.automation.module.InputAutomationModuleServiceInterface import InputAutomationModuleServiceInterface
        from org.allbinary.osgi.OSGIActivatorUtil import OSGIActivatorUtil
        OSGIActivatorUtil.registerAsService(bundleContext, self.getServiceFactory(), __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(InputAutomationModuleServiceInterface))
    

    def removeModules(self, context: BundleContext) -> None:
        from org.osgi.framework.BundleContext import BundleContext
        from bundle.input.automation.module.configuration.InputAutomationConfigurationModuleChangeListener import InputAutomationConfigurationModuleChangeListener
        from org.allbinary.input.automation.configuration.InputAutomationConfigurationModuleChangeEvent import InputAutomationConfigurationModuleChangeEvent
        from org.allbinary.input.automation.configuration.InputAutomationConfigurationUtil import InputAutomationConfigurationUtil
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
        from org.osgi.framework.BundleContext import BundleContext
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.START)
        self.addModules(context)
        self.registerAsService(context)
    

    # throws Exception
    def stop(self, context: BundleContext) -> None:
        from org.osgi.framework.BundleContext import BundleContext
        self.logUtil.putF(self.commonStrings.START, self, "stop")
        self.removeModules(context)
    

    def getInputAutomationModuleInterface(self) -> list[InputAutomationModuleFactoryInterface]:
        from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
        return self.inputAutomationModuleInterface
    

    def setInputAutomationModuleInterface(self, inputAutomationModuleInterface: list[InputAutomationModuleFactoryInterface]) -> None:
        from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
        self.inputAutomationModuleInterface = inputAutomationModuleInterface
    

    def getServiceFactory(self) -> object:
        return self.serviceFactory
    

    def setServiceFactory(self, serviceObject: ServiceFactory) -> None:
        from org.osgi.framework.ServiceFactory import ServiceFactory
        self.serviceFactory = serviceObject
# from org.osgi.framework.BundleContext import BundleContext
# from org.osgi.framework.ServiceFactory import ServiceFactory
# from org.osgi.framework.ServiceReference import ServiceReference
# from bundle.input.automation.module.InputAutomationModuleServiceInterface import InputAutomationModuleServiceInterface
# from bundle.input.automation.module.configuration.InputAutomationConfigurationModuleChangeListener import InputAutomationConfigurationModuleChangeListener
# from org.allbinary.input.automation.configuration.InputAutomationConfigurationModuleChangeEvent import InputAutomationConfigurationModuleChangeEvent
# from org.allbinary.input.automation.configuration.InputAutomationConfigurationUtil import InputAutomationConfigurationUtil
# from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.osgi.OSGIActivatorUtil import OSGIActivatorUtil
# from org.allbinary.string.CommonStrings import CommonStrings


