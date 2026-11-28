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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.input.automation.module.InputAutomationModuleFactoryInterface import InputAutomationModuleFactoryInterface


@java_inherited_overloads
class AbstractInputAutomationFactory(InputAutomationModuleFactoryInterface):
    def _java_defaults(self):
        vars(self).setdefault("name", None)
        vars(self).setdefault("jPanel", None)
        vars(self).setdefault("helpSet", None)

    def _init_fields(self) -> None:
        if "name" not in vars(self): self.name: str = None
        if "jPanel" not in vars(self): self.jPanel: JPanel = None
        if "helpSet" not in vars(self): self.helpSet: HelpSet = None

    def __init__(self, *args) -> None:
        if len(args) == 3:
            __class__._constructor3(self, *args)
        elif len(args) == 2:
            __class__._constructor2(self, *args)
    

    def _constructor3(self, name: str, jPanel: JPanel, helpSet: HelpSet) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.name = name
        self.jPanel = jPanel
        self.helpSet = helpSet
    

    def _constructor2(self, name: str, jPanel: JPanel) -> None:
        __class__._java_defaults(self)
        from java.net.URL import URL
        from org.allbinary.logic.java.help.JavaHelpUtil import JavaHelpUtil
        super().__init__()
        __class__._init_fields(self)
        self.name = name
        self.jPanel = jPanel
        url: URL = __import__("java.lang.ClassLoader", fromlist=["ClassLoader"]).ClassLoader.classResource(type(self), "/help/Help.hs", False)
        self.helpSet = JavaHelpUtil.getInstance().getHelpSet(url)
    

    def getName(self) -> str:
        return self.name
    

    def getConfigurationJPanel(self) -> JPanel:
        return self.jPanel
    

    def getHelpSet(self) -> HelpSet:
        return self.helpSet
# from java.net.URL import URL
# from javax.help.HelpSet import HelpSet
# from javax.swing.JPanel import JPanel
# from org.allbinary.logic.java.help.JavaHelpUtil import JavaHelpUtil


