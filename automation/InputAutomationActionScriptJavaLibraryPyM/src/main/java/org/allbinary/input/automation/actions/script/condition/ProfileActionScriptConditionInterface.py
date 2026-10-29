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
# package org.allbinary.input.automation.actions.script.condition

from __future__ import annotations

from org.allbinary.input.automation.actions.script.ProfileActionScriptItemInterface import ProfileActionScriptItemInterface
from org.allbinary.input.automation.actions.script.ProfileActionScriptNodeInterface import ProfileActionScriptNodeInterface
from org.allbinary.input.automation.actions.script.condition.CustomTreeNodeInterface import CustomTreeNodeInterface


# Java interface
class ProfileActionScriptConditionInterface(ProfileActionScriptNodeInterface, CustomTreeNodeInterface, ProfileActionScriptItemInterface):
    

    def addProcessor(self, profileActionProcessorInterface: ProfileActionScriptProcessorInterface) -> None:
        raise NotImplementedError()
    

    def removeProcessor(self, profileActionProcessorInterface: ProfileActionScriptProcessorInterface) -> None:
        raise NotImplementedError()
    

    # throws Exception
    def shouldProcess(self, frame: int) -> bool:
        raise NotImplementedError()
from org.allbinary.input.automation.actions.script.condition.processors.ProfileActionScriptProcessorInterface import ProfileActionScriptProcessorInterface


