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
        self.category: str = CategoryData.getInstance().ROOTCATEGORY
        self.fileName: str = self.category + str(AbPathData.getInstance().EXTENSION_SEP) + str(CategoryData.getInstance().UNCRYPTED_EXTENSION)
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getKey(self) -> object:
        return self.getValue()
    

    def getValue(self) -> str:
        return self.category
    

    # throws Exception
    def setValue(self, value: str) -> None:
        raise Exception("No Value Allowed")
    

    # throws Exception
    def setRootFilePath(self, value: AbPath) -> None:
        raise RuntimeError()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def setRootFilePath(self, value: str) -> None:
        raise Exception("No Value Allowed")
    

    # throws Exception
    def getRootFilePath(self) -> AbPath:
        raise Exception("No Value Allowed")
    

    # throws Exception
    def isRealRoot(self) -> bool:
        raise Exception("No A Real Root")
    

    # throws Exception
    def isRoot(self) -> bool:
        raise Exception("Root but not implemented")
    

    # throws Exception
    def getWebAppPath(self, categoryHierarchyInterface: CategoryHierarchyInterface) -> str:
        raise Exception("Not Root")
    

    def getPath(self, categoryHierarchyInterface: CategoryHierarchyInterface) -> AbPath:
        return AbPath.createAbPath()
    

    def getFileName(self) -> str:
        return self.fileName
    

    def isValid(self) -> bool:
        return True
    

    def toHashMap(self) -> dict:
        categoryHashMap: dict = StdUtil.getInstance().createHashMap()
        categoryHashMap.put(CategoryData.getInstance().NAME, self.category)
        return categoryHashMap
    

    def toVector(self) -> BasicArrayList:
        categoryVector: BasicArrayList = BasicArrayListD()
        categoryVector.add(self.category)
        return categoryVector
    

    # throws Exception
    def toValidationInfoDoc(self) -> Document:
        return None
    

    # throws Exception
    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def validationInfo(self) -> str:
        return None
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.category.CategoryData import CategoryData
from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


