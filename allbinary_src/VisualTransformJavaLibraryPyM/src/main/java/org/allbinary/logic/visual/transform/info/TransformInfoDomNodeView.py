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

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.visual.transform.info.TransformInfoDomNode import TransformInfoDomNode


class TransformInfoDomNodeView(TransformInfoDomNode, DomNodeInterface):

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, mapping: str) -> None:
        super().__init__(transformInfoInterface, mapping)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
    

    def _constructor2(self, name: str, mappedName: str) -> None:
        super().__init__(name, mappedName)
    

    def _constructor1(self, name: str) -> None:
        super().__init__(name, None)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
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
from org.w3c.dom.Attr import Attr
from org.w3c.dom.Document import Document
from org.w3c.dom.NamedNodeMap import NamedNodeMap
from org.w3c.dom.Node import Node


