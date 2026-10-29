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
# package org.allbinary.input.automation.module

from __future__ import annotations



class InputAutomationModuleFactoryFactory:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.hashMap: dict = None
        self.defaultListModelHelper: DefaultListModelHelper = None
        self.helpSetListenerInterface: HelpSetListener = None
    

    def __init__(self, inputAutomationModuleConfigurations: InputAutomationModuleConfigurations, helpSetListenerInterface: HelpSetListener) -> None:
        from org.allbinary.input.automation.module.DefaultListModelHelper import DefaultListModelHelper
        self._init_fields()
        self.helpSetListenerInterface = helpSetListenerInterface
        self.defaultListModelHelper = DefaultListModelHelper()
        self.hashMap = StdUtil.getInstance().createHashMap()
        collection: Collection = inputAutomationModuleConfigurations.getHashMap().values()
        iterator: Iterator = collection.iterator()
        inputAutomationModuleConfiguration: InputAutomationModuleConfiguration = None
        while iterator.hasNext():
            inputAutomationModuleConfiguration = iterator.next()
            self.add(inputAutomationModuleConfiguration)
        self.defaultListModelHelper.initDefaultModelList()
        self.logUtil.putF("Loaded " + str(self.hashMap.size()) + "/" + str(self.defaultListModelHelper.getListModel().getSize()) + " Input Automation Modules", self, "Contructor")
    

    def add(self, inputAutomationModuleConfiguration: InputAutomationModuleConfiguration) -> None:
        inputAutomationModuleInterface: InputAutomationModuleFactoryInterface = inputAutomationModuleConfiguration.getInputAutomationModuleInterface()
        self.hashMap.put(inputAutomationModuleConfiguration.getName(), inputAutomationModuleInterface)
        self.defaultListModelHelper.add(inputAutomationModuleConfiguration.getName())
        helpSet: HelpSet = inputAutomationModuleInterface.getHelpSet()
        if not JavaHelpSetNotifier.isNotified(helpSet):
            helpSetEvent: HelpSetEvent = HelpSetEvent(self, helpSet, HelpSetEvent.HELPSET_ADDED)
            self.helpSetListenerInterface.helpSetAdded(helpSetEvent)
    

    def getListModel(self) -> ListModel:
        return self.defaultListModelHelper.getListModel()
    

    def getInstance(self, moduleName: str) -> InputAutomationModuleFactoryInterface:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        self.logUtil.putF("Getting Module: " + moduleName, self, commonStrings.GET_INSTANCE)
        inputAutomationModuleFactoryInterface: InputAutomationModuleFactoryInterface = self.hashMap.get(moduleName)
        if inputAutomationModuleFactoryInterface is None:
            self.logUtil.putF("Module: " + moduleName + " was null", self, commonStrings.GET_INSTANCE)
        return inputAutomationModuleFactoryInterface
# from java.util.Collection import Collection
# from java.util.HashMap import HashMap
# from java.util.Iterator import Iterator
# from javax.help.HelpSet import HelpSet
# from javax.help.event.HelpSetEvent import HelpSetEvent
# from javax.help.event.HelpSetListener import HelpSetListener
# from javax.swing.ListModel import ListModel
from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfiguration import InputAutomationModuleConfiguration
from org.allbinary.input.automation.module.configuration.InputAutomationModuleConfigurations import InputAutomationModuleConfigurations
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.help.JavaHelpSetNotifier import JavaHelpSetNotifier
from org.allbinary.string.CommonStrings import CommonStrings


