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
# package org.allbinary.input.automation.actions.script

from __future__ import annotations

# from javax.swing.tree.MutableTreeNode import MutableTreeNode
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


# Java interface
class ProfileActionScriptNodeInterface(DomNodeInterface, MutableTreeNode):
    

    def addCondition(self, profileActionConditionInterface: ProfileActionScriptNodeInterface) -> None:
        raise NotImplementedError()
    

    def removeCondition(self, profileActionConditionInterface: ProfileActionScriptNodeInterface) -> None:
        raise NotImplementedError()


