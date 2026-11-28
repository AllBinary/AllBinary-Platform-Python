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
# package org.allbinary.input.automation.module.game.test

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.input.automation.module.AbstractInputAutomationFactory import AbstractInputAutomationFactory


@java_inherited_overloads
class TestModuleFactory(AbstractInputAutomationFactory):
    NAME: str = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("blankModuleConfigurationJPanel", None)

    def _init_fields(self) -> None:
        if "blankModuleConfigurationJPanel" not in vars(self): self.blankModuleConfigurationJPanel: BlankModuleConfigurationJPanel = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.input.automation.module.configuration.BlankModuleConfigurationJPanel import BlankModuleConfigurationJPanel
        super().__init__(TestModuleFactory.NAME, BlankModuleConfigurationJPanel())
        __class__._init_fields(self)
    

    def getName(self) -> str:
        return TestModuleFactory.NAME
    

    def getConfigurationJPanel(self) -> JPanel:
        return self.blankModuleConfigurationJPanel
    

    # throws Exception
    def getInstance(self) -> RunnableInterface:
        with self._lock:
            return __class__.__dict__["_getInstance_unlocked"].__get__(self, __class__)()

    def _getInstance_unlocked(self) -> RunnableInterface:
        from org.allbinary.thread.RunnableInterface import RunnableInterface
        return None
# from javax.swing.JPanel import JPanel
# from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData
# from org.allbinary.input.automation.module.configuration.BlankModuleConfigurationJPanel import BlankModuleConfigurationJPanel
# from org.allbinary.thread.RunnableInterface import RunnableInterface


def _TestModuleFactory_NAME() -> object:
    from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData
    return "Test New Game" + str(InputAutomationModuleData.MODULE_NAME_END)

lazy_static(TestModuleFactory, "NAME", _TestModuleFactory_NAME)

