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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.input.automation.actions.script.condition.processors.BasicProfileActionScriptProcessor import BasicProfileActionScriptProcessor
from org.allbinary.input.automation.module.actions.script.condition.processors.output.ProfileActionScriptOutputInterface import ProfileActionScriptOutputInterface


@java_inherited_overloads
class BasicProfileActionScriptOutput(*java_bases(BasicProfileActionScriptProcessor, ProfileActionScriptOutputInterface)):

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
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.input.automation.module.actions.script.condition.processors.output.GenericProfileActionScriptOutputData import GenericProfileActionScriptOutputData
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        node: Node = document.createElement(GenericProfileActionScriptOutputData.NAME)
        return node
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


