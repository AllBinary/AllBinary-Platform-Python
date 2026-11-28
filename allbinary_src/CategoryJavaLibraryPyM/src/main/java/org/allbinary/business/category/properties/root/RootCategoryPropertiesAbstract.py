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
# package org.allbinary.business.category.properties.root

from __future__ import annotations

from org.allbinary.business.category.properties.root.RootCategoryPropertiesInterface import RootCategoryPropertiesInterface


class RootCategoryPropertiesAbstract(RootCategoryPropertiesInterface):

    def _init_fields(self) -> None:
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        self.category: str = CategoryData.getInstance().ROOTCATEGORY
        self.fileName: str = self.category + str(AbPathData.getInstance().EXTENSION_SEP) + str(CategoryData.getInstance().UNCRYPTED_EXTENSION)
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getKey(self) -> object:
        return self.getValue()
    

    def getValue(self) -> str:
        return self.category
    

    # throws Exception
    def setValue(self, value: str) -> None:
        raise Exception("No Value Allowed")
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def setRootFilePath_j1_1(self, value: AbPath) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        raise RuntimeError()
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def setRootFilePath_j1_2(self, value: str) -> None:
        raise Exception("No Value Allowed")

    def setRootFilePath(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "AbPath" for base in type(args[0]).__mro__)):
            return __class__.__dict__["setRootFilePath_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["setRootFilePath_j1_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("setRootFilePath_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().setRootFilePath(*args)
    

    # throws Exception
    def getRootFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        raise Exception("No Value Allowed")
    

    # throws Exception
    def isRealRoot(self) -> bool:
        raise Exception("No A Real Root")
    

    # throws Exception
    def isRoot(self) -> bool:
        raise Exception("Root but not implemented")
    

    # throws Exception
    def getWebAppPath(self, categoryHierarchyInterface: CategoryHierarchyInterface) -> str:
        from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
        raise Exception("Not Root")
    

    def getPath(self, categoryHierarchyInterface: CategoryHierarchyInterface) -> AbPath:
        from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
        from org.allbinary.logic.io.path.AbPath import AbPath
        return AbPath.createAbPath()
    

    def getFileName(self) -> str:
        return self.fileName
    

    def isValid(self) -> bool:
        return True
    

    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.logic.StdUtil import StdUtil
        categoryHashMap: HashMap = StdUtil.getInstance().createHashMap()
        categoryHashMap.put(CategoryData.getInstance().NAME, self.category)
        return categoryHashMap
    

    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        categoryVector: BasicArrayList = BasicArrayListD()
        categoryVector.add(self.category)
        return categoryVector
    

    # throws Exception
    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    # throws Exception
    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    # throws Exception
    def validationInfo(self) -> str:
        return None
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.category.CategoryData import CategoryData
# from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


