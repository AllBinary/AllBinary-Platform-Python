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
# package org.allbinary.logic.visual.transform.info

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.visual.transform.info.TransformInfoDomNode import TransformInfoDomNode


@java_inherited_overloads
class TransformInfoDomNodeView(*java_bases(TransformInfoDomNode, DomNodeInterface)):

    def __init__(self, *args) -> None:
        if len(args) == 2:
            __class__.__jconstructor2(self, *args)
        elif len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor2(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[0]).__mro__)) and (args[1] is None or isinstance(args[1], str)):
            __class__._constructor2_1(self, *args)
        else:
            __class__._constructor2_2(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor2_1(self, transformInfoInterface: TransformInfoInterface, mapping: str) -> None:
        super().__init__(transformInfoInterface, mapping)
    

    def _constructor1_1(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
    

    def _constructor2_2(self, name: str, mappedName: str) -> None:
        super().__init__(name, mappedName)
    

    def _constructor1_2(self, name: str) -> None:
        super().__init__(name, None)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        from org.w3c.dom.Attr import Attr
        from org.w3c.dom.Document import Document
        from org.w3c.dom.NamedNodeMap import NamedNodeMap
        from org.w3c.dom.Node import Node
        transformInfoData: TransformInfoData = TransformInfoData.getInstance()
        subViewNode: Node = document.createElement(transformInfoData.NAME)
        viewNameAttr: Attr = document.createAttribute(transformInfoData.NAME)
        viewNameAttr.setValue(self.getTransformInfoInterface().getName())
        componentNodeAttributes: NamedNodeMap = subViewNode.getAttributes()
        componentNodeAttributes.setNamedItem(viewNameAttr)
        if self.getMappedName() is not None:
            mappedNameAttr: Attr = document.createAttribute(transformInfoData.MAPPED)
            mappedNameAttr.setValue(self.getMappedName())
            componentNodeAttributes.setNamedItem(mappedNameAttr)
        return subViewNode
# from org.w3c.dom.Attr import Attr
# from org.w3c.dom.Document import Document
# from org.w3c.dom.NamedNodeMap import NamedNodeMap
# from org.w3c.dom.Node import Node


