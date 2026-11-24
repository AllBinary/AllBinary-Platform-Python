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
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        self.rootCategoryInterface: CategoryInterface = None
        self.parentCategoryInterface: CategoryInterface = None
        self.level: int = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self.__jconstructor3(*args)

    def __jconstructor3(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and isinstance(args[2], int) and not isinstance(args[2], bool):
            self._constructor3_1(*args)
        else:
            self._constructor3_2(*args)
    

    def _constructor2(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface) -> None:
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        self._init_fields()
        self.level = 0
        self.setRoot(rootCategoryInterface)
        self.setParent(parentCategoryInterface)
    

    def _constructor3_1(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, level: int) -> None:
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        self._init_fields()
        self.level = level
        self.setRoot(rootCategoryInterface)
        self.setParent(parentCategoryInterface)
    

    def _constructor3_2(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.logic.string.StringUtil import StringUtil
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
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        self.parentCategoryInterface = categoryInterface
    

    def setRoot(self, categoryInterface: CategoryInterface) -> None:
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        self.rootCategoryInterface = categoryInterface
    

    def getRoot(self) -> CategoryInterface:
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        return self.rootCategoryInterface
    

    def getParent(self) -> CategoryInterface:
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        return self.parentCategoryInterface
# from java.util.HashMap import HashMap
# from org.allbinary.business.category.CategoryData import CategoryData
# from org.allbinary.business.category.CategoryInterface import CategoryInterface
# from org.allbinary.logic.string.StringUtil import StringUtil


