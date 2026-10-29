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
# package org.allbinary.input.automation.actions.script.condition.processors.input

from __future__ import annotations



class ProfileActionScriptInputFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(node: Node) -> ProfileActionScriptInputInterface:
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInputData import KeyboardActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInputData import MouseActionScriptInputData
        from org.allbinary.input.automation.actions.script.condition.processors.input.MouseActionScriptInput import MouseActionScriptInput
        from org.allbinary.input.automation.actions.script.condition.processors.input.KeyboardActionScriptInput import KeyboardActionScriptInput
        profileActionScriptInputInterface: ProfileActionScriptInputInterface = None
        if DomSearchHelper.getNodeNoThrow(KeyboardActionScriptInputData.NAME, node.getChildNodes()) is not None:
            profileActionScriptInputInterface = KeyboardActionScriptInput(node)
        elif DomSearchHelper.getNodeNoThrow(MouseActionScriptInputData.NAME, node.getChildNodes()) is not None:
            profileActionScriptInputInterface = MouseActionScriptInput(node)
        else:
            raise Exception("No Such ActionScript Input")
        return profileActionScriptInputInterface
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.w3c.dom.Node import Node


