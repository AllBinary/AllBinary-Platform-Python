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
# package org.allbinary.business.category.store.theme

from __future__ import annotations

from org.allbinary.business.category.CategoryView import CategoryView
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface


class StoreThemeCategoryPathView(CategoryView, DomNodeInterface):
    

    def __init__(self, categoryInterface: StoreThemeCategoryInterface) -> None:
        super().__init__(categoryInterface)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        node: Node = super().toXmlNode(document)
        storeThemeCategoryInterface: StoreThemeCategoryInterface = self.getCategoryInterface()
        themeArray: list[object] = storeThemeCategoryInterface.getThemes().toArray()
        size: int = len(themeArray)
        for i in range(0, size):
            themeValidation: ThemeValidation = themeArray[i]
            domNodeInterface: DomNodeInterface = ThemePropertiesView(themeValidation)
            node.appendChild(domNodeInterface.toXmlNode(document))
        return node
from org.allbinary.logic.visual.theme.ThemeInterface import ThemeInterface
from org.allbinary.logic.visual.theme.ThemePropertiesView import ThemePropertiesView
from org.allbinary.logic.visual.theme.ThemeValidation import ThemeValidation
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


