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



class ProfileActionScriptConditionFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(node: Node) -> ProfileActionScriptConditionInterface:
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptConditionData import ColorAtActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptConditionData import TimeIntervalActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptConditionData import AlwaysActionScriptConditionData
        from org.allbinary.input.automation.actions.script.condition.AlwaysActionScriptCondition import AlwaysActionScriptCondition
        from org.allbinary.input.automation.actions.script.condition.TimeIntervalActionScriptCondition import TimeIntervalActionScriptCondition
        from org.allbinary.input.automation.actions.script.condition.ColorAtActionScriptCondition import ColorAtActionScriptCondition
        profileActionScriptConditionInterface: ProfileActionScriptConditionInterface = None
        if DomSearchHelper.getNodeNoThrow(ColorAtActionScriptConditionData.NAME, node.getChildNodes()) is not None:
            profileActionScriptConditionInterface = ColorAtActionScriptCondition(node)
        elif DomSearchHelper.getNodeNoThrow(TimeIntervalActionScriptConditionData.NAME, node.getChildNodes()) is not None:
            profileActionScriptConditionInterface = TimeIntervalActionScriptCondition(node)
        elif DomSearchHelper.getNodeNoThrow(AlwaysActionScriptConditionData.NAME, node.getChildNodes()) is not None:
            profileActionScriptConditionInterface = AlwaysActionScriptCondition(node)
        return profileActionScriptConditionInterface
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.w3c.dom.Node import Node


