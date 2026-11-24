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
# package org.allbinary.logic.visual.dhtml.style.css.property

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class CssPropertyView(DomNodeInterface):

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.cssProperty: CssProperty = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.__jconstructor1(*args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or isinstance(args[0], str)):
            self._constructor1_1(*args)
        elif True and not isinstance(args[0], (str, list, int, float)):
            self._constructor1_2(*args)
        else:
            self._constructor1_3(*args)
    

    def _constructor1_1(self, name: str) -> None:
        from org.allbinary.logic.visual.dhtml.style.css.property.CssProperty import CssProperty
        self._init_fields()
        self.cssProperty = CssProperty(name)
    

    def _constructor1_2(self, node: Node) -> None:
        from org.allbinary.logic.visual.dhtml.style.css.property.CssProperty import CssProperty
        from org.w3c.dom.Node import Node
        self._init_fields()
        self.cssProperty = CssProperty(node)
    

    def _constructor1_3(self, cssProperty: CssProperty) -> None:
        self._init_fields()
        self.cssProperty = cssProperty
    

    def getProperty(self) -> CssProperty:
        return self.cssProperty
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return self.cssProperty.toXmlNode(document)
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


