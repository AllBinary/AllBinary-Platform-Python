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

import threading
from org.allbinary.business.category.CategoryInterface import CategoryInterface


class Category(CategoryInterface):
    NOT_ROOT: str = "This is not the root so it has no file path."
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.categoryHierarchyInterface: CategoryHierarchyInterface = None
        self.categoryPropertiesInterface: CategoryPropertiesInterface = None
        self.childCategoryVector: BasicArrayList = BasicArrayListD()
        self.typeVector: BasicArrayList = BasicArrayListD()
        self.PROPERTIES: int = int(1)
        self.CATEGORY: int = int(0)

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 3:
            self._constructor3(*args)
    

    def _constructor1(self, categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF(self.commonStrings.CONSTRUCTOR, self, "Category(CategoryPropertiesFactoryInterface)")
        self.categoryPropertiesInterface = categoryPropertiesFactoryInterface.getInstance()
        self.categoryHierarchyInterface = CategoryHierarchy(self, self)
        self.log()
    

    def _constructor2(self, categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface, level: int) -> None:
        self._init_fields()
        self.categoryPropertiesInterface = categoryPropertiesFactoryInterface.getInstance()
        self.categoryHierarchyInterface = CategoryHierarchy(self, self, level)
        self.log()
    

    def _constructor3(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface) -> None:
        self._init_fields()
        self.categoryPropertiesInterface = categoryPropertiesFactoryInterface.getInstance()
        self.categoryHierarchyInterface = CategoryHierarchy(rootCategoryInterface, parentCategoryInterface)
        self.log()
    

    # throws Exception
    def getKey(self) -> object:
        return self.categoryPropertiesInterface.getKey()
    

    # throws Exception
    def getRootFilePath(self) -> AbPath:
        rootAbPath: AbPath = AbPath(Category.NOT_ROOT, StringUtil.getInstance().EMPTY_STRING)
        categoryInterface: CategoryInterface = self.categoryHierarchyInterface.getRoot()
        if categoryInterface.getProperties().isRoot():
            rootCategoryPropertiesInterface: RootCategoryPropertiesInterface = categoryInterface.getProperties()
            rootAbPath = rootCategoryPropertiesInterface.getRootFilePath()
        return rootAbPath
    

    # throws Exception
    def getFilePath(self) -> AbPath:
        return AbPath(str(self.getRootFilePath()) + str(self.getProperties().getPath(self.getHierarchy())), self.getProperties().getFileName())
    

    # throws Exception
    def getWebAppPath(self) -> AbPath:
        categoryInterface: CategoryInterface = self.categoryHierarchyInterface.getRoot()
        return categoryInterface.getProperties().getWebAppPath()
    

    # throws Exception
    def getPath(self) -> AbPath:
        return self.categoryPropertiesInterface.getPath(self.categoryHierarchyInterface)
    

    def addChildProperty(self, categoryPropertiesInterface: CategoryPropertiesInterface) -> bool:
        with self._lock:
            return self._addChildProperty_unlocked(categoryPropertiesInterface)

    def _addChildProperty_unlocked(self, categoryPropertiesInterface: CategoryPropertiesInterface) -> bool:
        self.typeVector.add(self.PROPERTIES)
        return self.childCategoryVector.add(categoryPropertiesInterface)
    

    def addChild(self, categoryInterface: CategoryInterface) -> bool:
        with self._lock:
            return self._addChild_unlocked(categoryInterface)

    def _addChild_unlocked(self, categoryInterface: CategoryInterface) -> bool:
        self.removeDuplicateChild(categoryInterface)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF("adding", self, "addChild")
        childCategoryHierarchyInterface: CategoryHierarchyInterface = categoryInterface.getHierarchy()
        childCategoryHierarchyInterface.setParent(self)
        childCategoryHierarchyInterface.setRoot(self.getHierarchy().getRoot())
        categoryInterface.setHierarchy(childCategoryHierarchyInterface)
        self.typeVector.add(self.CATEGORY)
        return self.childCategoryVector.add(categoryInterface)
    

    def getChildNodes(self) -> BasicArrayList:
        return self.childCategoryVector
    

    def removeChild(self, categoryInterface: CategoryInterface) -> bool:
        with self._lock:
            return self._removeChild_unlocked(categoryInterface)

    def _removeChild_unlocked(self, categoryInterface: CategoryInterface) -> bool:
        removalVector: BasicArrayList = BasicArrayListD()
        bool_return: bool = False
        size: int = self.childCategoryVector.size()
        for index in range(0, size):
            if self.CATEGORY == self.typeVector.get(index):
                anyType: object = self.childCategoryVector.get(index)
                currentCategoryInterface: CategoryInterface = anyType
                if currentCategoryInterface.getProperties().getValue().compareTo(categoryInterface.getProperties().getValue()) == 0:
                    removalVector.add(currentCategoryInterface)
                    bool_return = True
        self.removal(removalVector)
        return bool_return
    

    def removal(self, removalVector: BasicArrayList) -> None:
        removalSize: int = removalVector.size()
        for index in range(0, removalSize):
            anyType: object = removalVector.get(index)
            objectIndex: int = self.childCategoryVector.indexOf(anyType)
            self.typeVector.remove(objectIndex)
            self.childCategoryVector.remove(objectIndex)
    

    def removeDuplicateChild(self, categoryInterface: CategoryInterface) -> bool:
        with self._lock:
            return self._removeDuplicateChild_unlocked(categoryInterface)

    def _removeDuplicateChild_unlocked(self, categoryInterface: CategoryInterface) -> bool:
        removalVector: BasicArrayList = BasicArrayListD()
        bool_return: bool = False
        size: int = self.childCategoryVector.size()
        for index in range(0, size):
            anyType: object = self.childCategoryVector.get(index)
            if self.PROPERTIES == self.typeVector.get(index):
                categoryPropertiesInterface: CategoryPropertiesInterface = anyType
                if categoryInterface.getProperties().getValue().compareTo(categoryPropertiesInterface.getValue()) == 0:
                    removalVector.add(categoryPropertiesInterface)
                    bool_return = True
                    break
            elif self.CATEGORY == self.typeVector.get(index):
                existingCategoryInterface: CategoryInterface = anyType
                categoryPropertiesInterface: CategoryPropertiesInterface = existingCategoryInterface.getProperties()
                if categoryInterface.getProperties().getValue().compareTo(categoryPropertiesInterface.getValue()) == 0:
                    removalVector.add(existingCategoryInterface)
                    bool_return = True
                    break
        self.removal(removalVector)
        return bool_return
    

    # throws Exception
    def isLeaf(self) -> bool:
        if self.childCategoryVector is None:
            raise Exception("Category Error")
        if self.childCategoryVector.size() == 0:
            return True
        else:
            return False
    

    def getProperties(self) -> CategoryPropertiesInterface:
        return self.categoryPropertiesInterface
    

    def setProperties(self, categoryPropertiesInterface: CategoryPropertiesInterface) -> None:
        self.categoryPropertiesInterface = categoryPropertiesInterface
    

    def getHierarchy(self) -> CategoryHierarchyInterface:
        return self.categoryHierarchyInterface
    

    def setHierarchy(self, categoryHierarchyInterface: CategoryHierarchyInterface) -> None:
        self.categoryHierarchyInterface = categoryHierarchyInterface
    

    # throws Exception
    def isValid(self) -> bool:
        with self._lock:
            return self._isValid_unlocked()

    def _isValid_unlocked(self) -> bool:
        if not self.categoryPropertiesInterface.isValid():
            return False
        size: int = self.childCategoryVector.size()
        for index in range(0, size):
            anyType: object = self.childCategoryVector.get(index)
            if self.PROPERTIES == self.typeVector.get(index):
                categoryPropertiesInterface: CategoryPropertiesInterface = anyType
                if not categoryPropertiesInterface.isValid():
                    return False
            elif self.CATEGORY == self.typeVector.get(index):
                categoryInterface: CategoryInterface = anyType
                if not categoryInterface.isValid():
                    return False
        return True
    

    # throws Exception
    def toValidationInfoDoc(self) -> Document:
        return None
    

    # throws Exception
    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def validationInfo(self) -> str:
        return None
    

    # throws Exception
    def toHashMap(self) -> dict:
        categoryHashMap: dict = self.categoryPropertiesInterface.toHashMap()
        return categoryHashMap
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        categoryVector: BasicArrayList = self.categoryPropertiesInterface.toVector()
        categoryVector.add(self.childCategoryVector)
        return categoryVector
    

    # throws Exception
    def log(self) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Category Name: ")
            stringBuffer.append(self.categoryPropertiesInterface.getValue())
            stringBuffer.append("\nPath = ")
            stringBuffer.append(str(self.getPath()))
            stringBuffer.append("\nFile Path: ")
            stringBuffer.append(str(self.getFilePath()))
            self.logUtil.putF(str(stringBuffer), self, "log()")
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.category.hierarchy.CategoryHierarchy import CategoryHierarchy
from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
from org.allbinary.business.category.properties.root.RootCategoryPropertiesInterface import RootCategoryPropertiesInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


