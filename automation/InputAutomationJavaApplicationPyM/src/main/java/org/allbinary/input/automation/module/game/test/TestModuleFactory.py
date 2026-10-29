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

import threading
from org.allbinary.input.automation.module.AbstractInputAutomationFactory import AbstractInputAutomationFactory
from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData


class TestModuleFactory(AbstractInputAutomationFactory):
    NAME: str = "Test New Game" + str(InputAutomationModuleData.MODULE_NAME_END)
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.blankModuleConfigurationJPanel: BlankModuleConfigurationJPanel = None
    

    def __init__(self) -> None:
        super().__init__(TestModuleFactory.NAME, BlankModuleConfigurationJPanel())
        self._init_fields()
    

    def getName(self) -> str:
        return TestModuleFactory.NAME
    

    def getConfigurationJPanel(self) -> JPanel:
        return self.blankModuleConfigurationJPanel
    

    # throws Exception
    def getInstance(self) -> RunnableInterface:
        with self._lock:
            return self._getInstance_unlocked()

    def _getInstance_unlocked(self) -> RunnableInterface:
        return None
# from javax.swing import *
from org.allbinary.input.automation.module.configuration.BlankModuleConfigurationJPanel import BlankModuleConfigurationJPanel
from org.allbinary.thread.RunnableInterface import RunnableInterface


