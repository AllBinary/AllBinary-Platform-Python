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

from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface


class AbstractInputAutomationFactory(InputAutomationModuleFactoryInterface):

    def _init_fields(self) -> None:
        self.name: str = None
        self.jPanel: JPanel = None
        self.helpSet: HelpSet = None

    def __init__(self, *args) -> None:
        if len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor3(self, name: str, jPanel: JPanel, helpSet: HelpSet) -> None:
        super().__init__()
        self._init_fields()
        self.name = name
        self.jPanel = jPanel
        self.helpSet = helpSet
    

    def _constructor2(self, name: str, jPanel: JPanel) -> None:
        super().__init__()
        self._init_fields()
        self.name = name
        self.jPanel = jPanel
        url: URL = type(self).getResource("/help/Help.hs")
        self.helpSet = JavaHelpUtil.getInstance().getHelpSet(url)
    

    def getName(self) -> str:
        return self.name
    

    def getConfigurationJPanel(self) -> JPanel:
        return self.jPanel
    

    def getHelpSet(self) -> HelpSet:
        return self.helpSet
# from java.net.URL import URL
# from javax.help.HelpSet import HelpSet
# from javax.swing import *
from org.allbinary.logic.java.help.JavaHelpUtil import JavaHelpUtil


