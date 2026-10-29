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
# package org.allbinary.business.user.commerce.inventory.basket

from __future__ import annotations



class BasketReview:

    def _init_fields(self) -> None:
        self.items: BasicArrayList = BasicArrayListD()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def isValid(self) -> bool:
        return True
    

    def addItem(self, item: Item) -> None:
        self.items.add(item)
    

    def getItems(self) -> BasicArrayList:
        return self.items
    

    def removeItem(self, id: str) -> None:
        itemArray: list[object] = self.items.toArray()
        size: int = len(itemArray)
        for index in range(0, size):
            item: Item = itemArray[index]
            if item.getId().compareTo(id) == 0:
                self.items.remove(item)
    

    def adjustItem(self, id: str, num: str) -> None:
        itemArray: list[object] = self.items.toArray()
        size: int = len(itemArray)
        for index in range(0, size):
            item: Item = itemArray[index]
            if item.getId().compareTo(id) == 0:
                item.setNumber(num)
    

    def getTotalWeight(self) -> str:
        weightFloat: float = 0.0
        itemArray: list[object] = self.items.toArray()
        size: int = len(itemArray)
        for index in range(0, size):
            item: Item = itemArray[index]
            weightFloat += float(float(item.getWeight()))
        return str(float(weightFloat))
    

    def getNumberOfItems(self) -> int:
        return int(self.items.size())
    

    def getIds(self) -> Set:
        idSet: HashSet = HashSet()
        itemArray: list[object] = self.items.toArray()
        size: int = len(itemArray)
        for index in range(0, size):
            item: Item = itemArray[index]
            idSet.add(item.getId())
        return idSet
    

    def getNumberOf(self, id: str) -> int:
        itemArray: list[object] = self.items.toArray()
        size: int = len(itemArray)
        for index in range(0, size):
            item: Item = itemArray[index]
            if item.getId().compareTo(id) == 0:
                return int(item.getNumber())
        return int(0)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.commerce.inventory.basket.BasketData import BasketData
        node: Node = document.createElement(BasketData.BASKET)
        itemArray: list[object] = self.items.toArray()
        size: int = len(itemArray)
        for index in range(0, size):
            item: Item = itemArray[index]
            node.appendChild(ItemView(item, BasicArrayListD()).toXmlNode(document))
        return node
# from java.util.HashSet import HashSet
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.commerce.inventory.item.Item import Item
from org.allbinary.business.user.commerce.inventory.item.ItemView import ItemView
from org.allbinary.logic.StdUtil import StdUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


