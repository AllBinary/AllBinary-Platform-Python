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



class InputAutomationModuleFactoryInterface:
    

    def getName(self) -> str:
        return None
    

    def getConfigurationJPanel(self) -> JPanel:
        return None
    

    def getHelpSet(self) -> HelpSet:
        return None
    

    # throws Exception
    def getInstance(self) -> RunnableInterface:
        return None
# from javax.help.HelpSet import HelpSet
# from javax.swing import *
from org.allbinary.thread.RunnableInterface import RunnableInterface


