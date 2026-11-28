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
# package org.allbinary.input.automation.actions.script.condition.processors

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.automation.actions.script.ProfileActionScriptItem import ProfileActionScriptItem
from org.allbinary.input.automation.actions.script.condition.processors.ProfileActionScriptProcessorInterface import ProfileActionScriptProcessorInterface


@java_inherited_overloads
class BasicProfileActionScriptProcessor(*java_bases(ProfileActionScriptItem, ProfileActionScriptProcessorInterface)):

    def __init__(self, *args) -> None:
        if len(args) == 2:
            __class__._constructor2(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor2(self, label: str, node: Node) -> None:
        from org.w3c.dom.Node import Node
        super().__init__(label, node)
    

    def _constructor1(self, label: str) -> None:
        super().__init__(label)
    

    def actionPerformed(self, actionEvent: ActionEvent) -> None:
        from org.allbinary.input.automation.actions.script.JTreeInterfaceFactory import JTreeInterfaceFactory
        from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
        java_super_call(super(), "actionPerformed", actionEvent)
        if actionEvent.getActionCommand().compareTo(self.DELETE) == 0:
            if isinstance(self.getParent(), ProfileActionScriptConditionInterface):
                profileActionScriptConditionInterface: ProfileActionScriptConditionInterface = self.getParent()
                profileActionScriptConditionInterface.removeProcessor(self)
                JTreeInterfaceFactory.getInstance().getJTreeInterface().updateJTree()
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.actions.script.condition.processors.GenericProfileActionScriptProcessorData import GenericProfileActionScriptProcessorData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(GenericProfileActionScriptProcessorData.NAME)
        return node
# from java.awt.event.ActionEvent import ActionEvent
# from org.allbinary.input.automation.actions.script.JTreeInterfaceFactory import JTreeInterfaceFactory
# from org.allbinary.input.automation.actions.script.condition.ProfileActionScriptConditionInterface import ProfileActionScriptConditionInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


