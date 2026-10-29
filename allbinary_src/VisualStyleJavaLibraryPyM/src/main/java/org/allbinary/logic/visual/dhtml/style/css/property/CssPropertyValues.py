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


class CssPropertyValues(DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.propertyValueVector: BasicArrayList = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.propertyValueVector = BasicArrayListD()
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyValueData import CssPropertyValueData
        self._init_fields()
        indexPropertyValueHashMap: dict = StdUtil.getInstance().createHashMap()
        self.propertyValueVector = BasicArrayListD()
        cssPropertyNodeVector: BasicArrayList = DomSearchHelper.getAllNodes(CssPropertyValueData.getInstance().NAME, node.getChildNodes())
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().STYLE):
            self.logUtil.putF("Number Of Properties: " + str(cssPropertyNodeVector.size()), self, "CssProperties()")
        size: int = cssPropertyNodeVector.size()
        for index in range(0, size):
            cssPropertyValueNode: Node = cssPropertyNodeVector.get(index)
            valueNode: Node = DomSearchHelper.getNode(DomData.VALUE, cssPropertyValueNode.getChildNodes())
            propertyValue: str = DomNodeHelper.getTextNodeValue(valueNode)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().STYLE):
                self.logUtil.putF("Property Value: " + propertyValue, self, "CssProperties()")
            indexNode: Node = DomSearchHelper.getNode(DomData.INDEX, cssPropertyValueNode.getChildNodes())
            indexValue: str = DomNodeHelper.getTextNodeValue(indexNode)
            indexPropertyValueHashMap.put(indexValue, propertyValue)
        size2: int = indexPropertyValueHashMap.keySet().size()
        for index in range(0, size2):
            indexInt: int = int(index)
            propertyValue: str = indexPropertyValueHashMap.get(str(indexInt))
            self.propertyValueVector.add(propertyValue)
    

    def toHashMap(self) -> dict:
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyValueData import CssPropertyValueData
        commonSeps: CommonSeps = CommonSeps.getInstance()
        cssPropertyValueData: CssPropertyValueData = CssPropertyValueData.getInstance()
        hashMap: dict = StdUtil.getInstance().createHashMap()
        stringBuffer: StringMaker = StringMaker()
        size: int = self.propertyValueVector.size()
        index = 0
        while index < size:
            value: str = self.propertyValueVector.get(index)
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append(cssPropertyValueData.NAME)
            stringBuffer.append(commonSeps.BRACKET_OPEN)
            stringBuffer.appendint(index)
            stringBuffer.append(commonSeps.BRACKET_CLOSE)
            hashMap.put(str(stringBuffer), value)
            index += 1
            index += 1
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyData import CssPropertyData
        from org.allbinary.logic.visual.dhtml.style.css.property.CssPropertyValueData import CssPropertyValueData
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            hashMap: dict = self.toHashMap()
            self.logUtil.putF("CssPropertyValues HashMap: " + str(hashMap), self, "toXmlNode()")
        return ModDomHelper.createNameValueIndexNodes(document, CssPropertyData.getInstance().VALUES, CssPropertyValueData.getInstance().NAME, self.propertyValueVector)
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
from org.allbinary.string.CommonSeps import CommonSeps
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


