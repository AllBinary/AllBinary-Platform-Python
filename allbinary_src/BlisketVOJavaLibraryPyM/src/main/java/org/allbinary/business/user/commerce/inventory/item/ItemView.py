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



class ItemView:

    def _init_fields(self) -> None:
        self.itemInterface: OrderItemInterface = None
        self.vector: BasicArrayList = None
    

    def __init__(self, itemInterface: OrderItemInterface, vector: BasicArrayList) -> None:
        self._init_fields()
        self.itemInterface = itemInterface
        self.vector = vector
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.commerce.inventory.item.ItemData import ItemData
        from org.allbinary.business.user.commerce.inventory.item.BasicItemView import BasicItemView
        hashMap: dict = self.itemInterface.toHashMap()
        keySet: Set = hashMap.keySet()
        node: Node = document.createElement(ItemData.ITEM)
        basicItemView: BasicItemView = BasicItemView(self.itemInterface, self.vector)
        node.appendChild(basicItemView.toXmlNode(document))
        stringUtil: StringUtil = StringUtil.getInstance()
        nameArray: list[object] = keySet.toArray()
        size: int = len(nameArray)
        for index in range(0, size):
            name: str = nameArray[index]
            value: str = hashMap.get(name)
            value = stringUtil.getNonNull(value)
            node.appendChild(ModDomHelper.createNameValueNodes(document, name, value))
        shippingAddressNode: Node = document.createElement(StreetAddressData.NAME)
        shippingAddressNode.appendChild(self.itemInterface.getShippingAddress().toXmlNode(document))
        return node
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.address.StreetAddressData import StreetAddressData
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.string.StringUtil import StringUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


