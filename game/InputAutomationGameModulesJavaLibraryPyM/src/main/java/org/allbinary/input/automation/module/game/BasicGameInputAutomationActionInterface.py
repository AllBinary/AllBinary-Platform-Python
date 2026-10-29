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
# package org.allbinary.input.automation.module.game

from __future__ import annotations

from org.allbinary.input.automation.module.InputAutomationActionInterface import InputAutomationActionInterface


# Java interface
class BasicGameInputAutomationActionInterface(InputAutomationActionInterface):
    

    # throws Exception
    def attack(self, rectangle: Rectangle) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def target(self, rectangle: Rectangle) -> None:
        raise NotImplementedError()
# from java.awt import *


