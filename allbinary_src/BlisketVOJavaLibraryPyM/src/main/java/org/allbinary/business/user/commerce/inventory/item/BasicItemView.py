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
# package org.allbinary.business.user.commerce.inventory.item

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class BasicItemView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.itemInterface: ItemInterface = None
        self.vector: BasicArrayList = None
    

    def __init__(self, itemInterface: ItemInterface, vector: BasicArrayList) -> None:
        self._init_fields()
        self.itemInterface = itemInterface
        self.vector = vector
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PRODUCTSEARCHLOGGING):
            self.logUtil.putF(self.commonStrings.START, self, "toXmlNode")
        hashMap: dict = self.itemInterface.toHashMap()
        EMPTY_STRING: str = StringUtil.getInstance().EMPTY_STRING
        hashMap.put(self.basicItemData.IMAGE, EMPTY_STRING)
        stringUtil: StringUtil = StringUtil.getInstance()
        keySet: Set = hashMap.keySet()
        node: Node = document.createElement(self.basicItemData.ITEM)
        nameArray: list[object] = keySet.toArray()
        size2: int = len(nameArray)
        for index in range(0, size2):
            name: str = nameArray[index]
            value: str = hashMap.get(name)
            value = stringUtil.getNonNull(value)
            node.appendChild(ModDomHelper.createNameValueNodes(document, name, value))
        totalNode: Node = ModDomHelper.createNameValueNodes(document, self.basicItemData.TOTAL, str(self.itemInterface.getTotal()))
        node.appendChild(totalNode)
        size: int = self.vector.size()
        for index in range(0, size):
            domNodeInterface: DomNodeInterface = self.vector.get(index)
            customNode: Node = domNodeInterface.toXmlNode(document)
            node.appendChild(customNode)
        return node
    

    def toXmlDoc(self) -> Document:
        return None
    

    def view(self) -> str:
        return None
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData


