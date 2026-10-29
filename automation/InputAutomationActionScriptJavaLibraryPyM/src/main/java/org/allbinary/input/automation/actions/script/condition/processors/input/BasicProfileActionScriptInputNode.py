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



class BasicProfileActionScriptInputNode:

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.input.automation.actions.script.condition.processors.input.GenericProfileActionScriptInputData import GenericProfileActionScriptInputData
        actionNode: Node = DomSearchHelper.getNode(GenericProfileActionScriptInputData.NAME, node.getChildNodes())
    

    def _constructor0(self) -> None:
        pass
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.actions.script.condition.processors.input.GenericProfileActionScriptInputData import GenericProfileActionScriptInputData
        node: Node = document.createElement(GenericProfileActionScriptInputData.NAME)
        return node
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


