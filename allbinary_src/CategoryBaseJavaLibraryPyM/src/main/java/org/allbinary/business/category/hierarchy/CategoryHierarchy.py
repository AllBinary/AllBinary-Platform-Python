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
        if "rootCategoryInterface" not in vars(self): self.rootCategoryInterface: CategoryInterface = None
        if "parentCategoryInterface" not in vars(self): self.parentCategoryInterface: CategoryInterface = None
        if "level" not in vars(self): self.level: int = 0

    def __init__(self, *args) -> None:
        if len(args) == 2:
            __class__._constructor2(self, *args)
        elif len(args) == 3:
            __class__.__jconstructor3(self, *args)

    def __jconstructor3(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "CategoryInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "CategoryInterface" for base in type(args[1]).__mro__)) and isinstance(args[2], int) and not isinstance(args[2], bool):
            __class__._constructor3_1(self, *args)
        else:
            __class__._constructor3_2(self, *args)
    

    def _constructor2(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface) -> None:
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        __class__._init_fields(self)
        self.level = 0
        self.setRoot(rootCategoryInterface)
        self.setParent(parentCategoryInterface)
    

    def _constructor3_1(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, level: int) -> None:
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        __class__._init_fields(self)
        self.level = level
        self.setRoot(rootCategoryInterface)
        self.setParent(parentCategoryInterface)
    

    def _constructor3_2(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.logic.string.StringUtil import StringUtil
        __class__._init_fields(self)
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


