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
# package org.allbinary.logic.visual.theme

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class ThemePropertiesView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.themeInterface: ThemeInterface = None
    

    def __init__(self, themeInterface: ThemeInterface) -> None:
        self._init_fields()
        self.themeInterface = themeInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        node: Node = ModDomHelper.createNameValueNodes(document, ThemeData.getInstance().NAME, self.themeInterface.toHashMap())
        return node
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


