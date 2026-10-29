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
# package org.allbinary.logic.visual.dhtml.style.css

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class CssElementView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.TITLE: str = "title"
        self.DESCRIPTION: str = "description"
        self.value: str = None
        self.title: str = None
        self.description: str = None
        self.cssElementVector: BasicArrayList = None
        self.cssPropertyVector: BasicArrayList = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.cssPropertyVector = BasicArrayListD()
        stringUtil: StringUtil = StringUtil.getInstance()
        self.title = stringUtil.EMPTY_STRING
        self.description = stringUtil.EMPTY_STRING
        self.value = stringUtil.EMPTY_STRING
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.logic.visual.dhtml.style.css.CssElementData import CssElementData
        from org.allbinary.logic.visual.dhtml.style.css.CssElementsValidationFactory import CssElementsValidationFactory
        self._init_fields()
        try:
            valueNode: Node = DomSearchHelper.getNode(DomData.VALUE, node.getChildNodes())
            self.value = DomNodeHelper.getTextNodeValue(valueNode)
            titleValueNode: Node = DomSearchHelper.getNodeNoThrow(self.TITLE, node.getChildNodes())
            if titleValueNode is not None:
                self.title = DomNodeHelper.getTextNodeValue(titleValueNode)
            else:
                stringUtil: StringUtil = StringUtil.getInstance()
                self.title = stringUtil.EMPTY_STRING
            descriptionValueNode: Node = DomSearchHelper.getNodeNoThrow(self.DESCRIPTION, node.getChildNodes())
            if descriptionValueNode is not None:
                self.description = DomNodeHelper.getTextNodeValue(descriptionValueNode)
            else:
                self.description = StringUtil.getInstance().EMPTY_STRING
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF(str(StringMaker().append("Value: ").append(self.value).append("\nTitle: ").append(self.title).append("\nDescription: ").append(self.description)), self, self.commonStrings.CONSTRUCTOR)
            cssElementStyleNodeVector: BasicArrayList = DomSearchHelper.getAllNodes(CssElementData.getInstance().NAME, node.getChildNodes())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Child Css Elements: " + str(cssElementStyleNodeVector.size()), self, "CssElementView()")
            self.cssElementVector = CssElementsValidationFactory.getInstance(cssElementStyleNodeVector)
            nodeList: NodeList = node.getChildNodes()
            self.cssPropertyVector = CssPropertiesValidationFactory.getInstance(nodeList)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(str(StringMaker().append("Value: ").append(self.value).append("\nTitle: ").append(self.title).append("\nDescription: ").append(self.description)), self, self.commonStrings.CONSTRUCTOR, e)
            raise Exception("CssElementView")
    

    def getValue(self) -> str:
        return self.value
    

    def toHashMap(self) -> dict:
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(DomData.VALUE, self.value)
        hashMap.put(self.TITLE, self.title)
        hashMap.put(self.DESCRIPTION, self.description)
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.dhtml.style.css.CssElementData import CssElementData
        hashMap: dict = self.toHashMap()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("CssView HashMap: " + str(hashMap), self, "toXmlNode")
        node: Node = ModDomHelper.createNodeWithValueNodes(document, CssElementData.getInstance().NAME, hashMap)
        size: int = self.cssPropertyVector.size()
        for index in range(0, size):
            cssPropertyDomNodeInterface: DomNodeInterface = self.cssPropertyVector.get(index)
            node.appendChild(cssPropertyDomNodeInterface.toXmlNode(document))
        size2: int = self.cssElementVector.size()
        for index in range(0, size2):
            cssElementDomNodeInterface: DomNodeInterface = self.cssElementVector.get(index)
            node.appendChild(cssElementDomNodeInterface.toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tree.dom.DomData import DomData
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertiesValidationFactory import CssPropertiesValidationFactory
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


