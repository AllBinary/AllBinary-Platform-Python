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
# package org.allbinary.business.category

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class CategoriesView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.categoryInterface: CategoryInterface = None
    

    def __init__(self, categoryInterface: CategoryInterface) -> None:
        self._init_fields()
        self.categoryInterface = categoryInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.category.CategoryView import CategoryView
        node: Node = CategoryView(self.categoryInterface).toXmlNode(document)
        childArray: list[object] = self.categoryInterface.getChildNodes().toArray()
        size: int = len(childArray)
        for i in range(0, size):
            childCategoryInterface: CategoryInterface = childArray[i]
            childCategoryNode: Node = CategoriesView(childCategoryInterface).toXmlNode(document)
            node.appendChild(childCategoryNode)
        return node
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


