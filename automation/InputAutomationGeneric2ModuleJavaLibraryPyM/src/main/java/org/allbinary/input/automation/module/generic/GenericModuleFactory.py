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
# package org.allbinary.input.automation.module.generic

from __future__ import annotations

import threading
from org.allbinary.input.automation.module.AbstractInputAutomationFactory import AbstractInputAutomationFactory
from org.allbinary.input.automation.module.InputAutomationModuleData import InputAutomationModuleData


class GenericModuleFactory(AbstractInputAutomationFactory):
    NAME: str = "Generic" + str(InputAutomationModuleData.MODULE_NAME_END)
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        super().__init__(GenericModuleFactory.NAME, GenericModuleConfigurationJPanel())
    

    # throws Exception
    def getInstance(self) -> RunnableInterface:
        with self._lock:
            return self._getInstance_unlocked()

    def _getInstance_unlocked(self) -> RunnableInterface:
        from org.allbinary.input.automation.module.generic.GenericInputAutomationAction import GenericInputAutomationAction
        from org.allbinary.input.automation.module.generic.GenericInputAutomationWorker import GenericInputAutomationWorker
        genericProfile: GenericProfile = (self.getConfigurationJPanel()).getSelectedGenericProfile()
        inputAutomationActionInterface: InputAutomationActionInterface = GenericInputAutomationAction()
        return GenericInputAutomationWorker(inputAutomationActionInterface, genericProfile, NoMotionRectangleConstraints(), NoImageComparatorConstraints())
from org.allbinary.input.automation.module.InputAutomationActionInterface import InputAutomationActionInterface
from org.allbinary.input.automation.module.generic.configuration.GenericModuleConfigurationJPanel import GenericModuleConfigurationJPanel
from org.allbinary.input.automation.module.generic.configuration.profile.GenericProfile import GenericProfile
from org.allbinary.input.automation.module.generic.constraints.NoImageComparatorConstraints import NoImageComparatorConstraints
from org.allbinary.input.automation.module.generic.constraints.NoMotionRectangleConstraints import NoMotionRectangleConstraints
from org.allbinary.thread.RunnableInterface import RunnableInterface


