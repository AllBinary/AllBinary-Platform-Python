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

from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface


class CategoryProperties(CategoryPropertiesInterface):
    MAXDEPTH: int = 100

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.category: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, name: str) -> None:
        self._init_fields()
        self.category = name
    

    def _constructor1(self, node: Node) -> None:
        self._init_fields()
        self.category = CategoryUtil.getNameFromNode(node)
    

    def _constructor1(self, categoryPropertiesHashMap: dict) -> None:
        self._init_fields()
        self.category = str(categoryPropertiesHashMap.get(CategoryData.getInstance().NAME))
    

    def isRealRoot(self) -> bool:
        return False
    

    def isRoot(self) -> bool:
        return False
    

    def getKey(self) -> object:
        return self.getValue()
    

    def getValue(self) -> str:
        return self.category
    

    # throws Exception
    def getPath(self, categoryHierarchyInterface: CategoryHierarchyInterface) -> AbPath:
        abPathData: AbPathData = AbPathData.getInstance()
        pathStringBuffer: StringMaker = StringMaker()
        list_: BasicArrayList = BasicArrayListD()
        nextParentCategoryInterface: CategoryInterface = categoryHierarchyInterface.getParent()
        if self != nextParentCategoryInterface.getProperties():
            depthIndex: int = 0
            while nextParentCategoryInterface is not None:
                if nextParentCategoryInterface.getProperties().isRealRoot():
                    break
                if nextParentCategoryInterface.getProperties().isRoot():
                    list_.addAt(0, str(nextParentCategoryInterface.getPath()))
                else:
                    pathStringBuffer.delete(0, pathStringBuffer.length())
                    list_.addAt(0, str(pathStringBuffer.append(abPathData.SEPARATOR).append(nextParentCategoryInterface.getProperties().getValue())))
                if nextParentCategoryInterface == nextParentCategoryInterface.getHierarchy().getParent():
                    break
                nextParentCategoryInterface = nextParentCategoryInterface.getHierarchy().getParent()
                depthIndex += 1
                if depthIndex > CategoryProperties.MAXDEPTH:
                    raise Exception("Probably Major Error")
        pathStringBuffer.delete(0, pathStringBuffer.length())
        pathStringBuffer.append(abPathData.SEPARATOR).append(self.getValue())
        size: int = list_.size()
        for index in range(0, size):
            pathStringBuffer.append(list_.get(index))
        pathStringBuffer.append(abPathData.SEPARATOR)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF("path = " + str(pathStringBuffer), self, "getPath")
        return AbPath(str(pathStringBuffer), StringUtil.getInstance().EMPTY_STRING)
    

    def getFileName(self) -> str:
        return self.getValue() + AbPathData.getInstance().EXTENSION_SEP + CategoryData.getInstance().UNCRYPTED_EXTENSION
    

    # throws Exception
    def getWebAppPath(self) -> AbPath:
        raise Exception("Not Root")
    

    def setValue(self, value: str) -> None:
        self.category = value
    

    def isValid(self) -> bool:
        returnBoolean: bool = False
        if StringValidationUtil.getInstance().isValidRequired(self.category, 1, AbSqlData.MAXSTRING):
            returnBoolean = True
        return returnBoolean
    

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
from org.allbinary.business.category.CategoryData import CategoryData
from org.allbinary.business.category.CategoryInterface import CategoryInterface
from org.allbinary.business.category.CategoryUtil import CategoryUtil
from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


