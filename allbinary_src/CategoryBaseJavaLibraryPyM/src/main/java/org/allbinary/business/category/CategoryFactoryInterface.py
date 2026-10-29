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



# Java interface
class CategoryFactoryInterface:
    

    def getRootInstance(self) -> CategoryInterface:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def getRootInstance(self, categoryPath: AbPath) -> CategoryInterface:
        raise NotImplementedError()
    

    def getRootInstanceFromNode(self, node: Node) -> CategoryInterface:
        raise NotImplementedError()
    

    def getInstance(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, name: str) -> CategoryInterface:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, node: Node) -> CategoryInterface:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesHashMap: dict) -> CategoryInterface:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.logic.io.path.AbPath import AbPath
from org.w3c.dom.Node import Node


