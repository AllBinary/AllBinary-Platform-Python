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
# package org.allbinary.business.category.hierarchy

from __future__ import annotations

from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface


class CategoryHierarchy(CategoryHierarchyInterface):

    def _init_fields(self) -> None:
        self.rootCategoryInterface: CategoryInterface = None
        self.parentCategoryInterface: CategoryInterface = None
        self.level: int = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self._constructor3(*args)
        elif len(args) == 3:
            self._constructor3(*args)
    

    def _constructor2(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface) -> None:
        self._init_fields()
        self.level = 0
        self.setRoot(rootCategoryInterface)
        self.setParent(parentCategoryInterface)
    

    def _constructor3(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, level: int) -> None:
        self._init_fields()
        self.level = level
        self.setRoot(rootCategoryInterface)
        self.setParent(parentCategoryInterface)
    

    def _constructor3(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesHashMap: dict) -> None:
        self._init_fields()
        levelString: str = StringUtil.getInstance().getNonNull(categoryPropertiesHashMap.get(CategoryData.getInstance().LEVEL))
        self.level = int(str(levelString))
        self.setRoot(rootCategoryInterface)
        self.setParent(parentCategoryInterface)
    

    def getLevel(self) -> int:
        return self.level
    

    def getLevelString(self) -> str:
        return str(self.level)
    

    def setLevel(self, level: int) -> None:
        self.level = level
    

    def setParent(self, categoryInterface: CategoryInterface) -> None:
        self.parentCategoryInterface = categoryInterface
    

    def setRoot(self, categoryInterface: CategoryInterface) -> None:
        self.rootCategoryInterface = categoryInterface
    

    def getRoot(self) -> CategoryInterface:
        return self.rootCategoryInterface
    

    def getParent(self) -> CategoryInterface:
        return self.parentCategoryInterface
# from java.util.HashMap import HashMap
from org.allbinary.business.category.CategoryData import CategoryData
from org.allbinary.business.category.CategoryInterface import CategoryInterface
from org.allbinary.logic.string.StringUtil import StringUtil


