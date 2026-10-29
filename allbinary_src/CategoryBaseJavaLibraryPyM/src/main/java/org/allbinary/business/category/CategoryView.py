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


class CategoryView(DomNodeInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.categoryInterface: CategoryInterface = None
    

    def __init__(self, categoryInterface: CategoryInterface) -> None:
        self._init_fields()
        self.categoryInterface = categoryInterface
    

    def getCategoryInterface(self) -> CategoryInterface:
        return self.categoryInterface
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.category.CategoryData import CategoryData
        node: Node = document.createElement(CategoryData.getInstance().NAME)
        childCategoryVector: BasicArrayList = self.categoryInterface.getChildNodes()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF("Number Of Children: " + str(childCategoryVector.size()), self, "toXmlNode")
        size: int = childCategoryVector.size()
        for i in range(0, size):
            anyType: object = childCategoryVector.get(i)
            categoryPropertiesInterface: CategoryPropertiesInterface = None
            if InterfaceUtil.isImplemented("CategoryPropertiesInterface", anyType):
                categoryPropertiesInterface = anyType
            elif InterfaceUtil.isImplemented("CategoryInterface", anyType):
                categoryInterface: CategoryInterface = anyType
                categoryPropertiesInterface = categoryInterface.getProperties()
            else:
                isImpl: str = InterfaceUtil.viewAll(type(anyType), CommonSeps.getInstance().NEW_LINE)
                raise Exception("CategoryView found unknown object.\n" + "Show Testing:" + isImpl)
            childCategoryNode: Node = CategoryPropertiesView(categoryPropertiesInterface).toXmlNode(document)
            node.appendChild(childCategoryNode)
        return node
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
from org.allbinary.business.category.properties.CategoryPropertiesView import CategoryPropertiesView
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.anyType.InterfaceUtil import InterfaceUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


