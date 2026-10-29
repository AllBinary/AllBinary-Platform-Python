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
# package org.allbinary.business.category.properties

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class CategoryPropertiesView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.categoryPropertiesInterface: CategoryPropertiesInterface = None
    

    def __init__(self, categoryPropertiesInterface: CategoryPropertiesInterface) -> None:
        self._init_fields()
        self.categoryPropertiesInterface = categoryPropertiesInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        categoryNode: Node = document.createElement(CategoryData.getInstance().NAME)
        newCategoryNode: Element = categoryNode
        newCategoryNode.setAttribute(CategoryData.getInstance().LABEL, self.categoryPropertiesInterface.getValue())
        return categoryNode
from org.allbinary.business.category.CategoryData import CategoryData
from org.w3c.dom.Document import Document
from org.w3c.dom.Element import Element
from org.w3c.dom.Node import Node


