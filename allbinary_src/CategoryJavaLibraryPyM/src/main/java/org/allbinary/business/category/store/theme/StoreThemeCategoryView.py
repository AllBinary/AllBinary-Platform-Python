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


class StoreThemeCategoryView(CategoryView, DomNodeInterface):
    

    def __init__(self, categoryInterface: StoreThemeCategoryInterface) -> None:
        super().__init__(categoryInterface)
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.category.store.theme.ThemeComparator import ThemeComparator
        node: Node = super().toXmlNode(document)
        storeThemeCategoryInterface: StoreThemeCategoryInterface = self.getCategoryInterface()
        themeValidationArray: list[ThemeValidation] = storeThemeCategoryInterface.getThemes().toArray()
        Arrays.sort(themeValidationArray, ThemeComparator())
        size: int = len(themeValidationArray)
        for index in range(0, size):
            themeValidation: ThemeValidation = themeValidationArray[index]
            node.appendChild(themeValidation.toXmlNode(document))
        return node
# from java.util.Arrays import Arrays
from org.allbinary.logic.visual.theme.ThemeValidation import ThemeValidation
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


