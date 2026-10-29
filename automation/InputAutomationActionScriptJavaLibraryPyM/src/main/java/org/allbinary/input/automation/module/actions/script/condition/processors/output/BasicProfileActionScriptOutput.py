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
# package org.allbinary.input.automation.module.actions.script.condition.processors.output

from __future__ import annotations

from org.allbinary.input.automation.actions.script.condition.processors.BasicProfileActionScriptProcessor import BasicProfileActionScriptProcessor
from org.allbinary.input.automation.module.actions.script.condition.processors.output.ProfileActionScriptOutputInterface import ProfileActionScriptOutputInterface


class BasicProfileActionScriptOutput(BasicProfileActionScriptProcessor, ProfileActionScriptOutputInterface):

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor2(self, label: str, node: Node) -> None:
        super().__init__(label, node)
    

    def _constructor1(self, label: str) -> None:
        super().__init__(label)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.GenericProfileActionScriptOutputData import GenericProfileActionScriptOutputData
        node: Node = document.createElement(GenericProfileActionScriptOutputData.NAME)
        return node
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


