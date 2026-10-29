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
# package org.allbinary.data.tree.category

from __future__ import annotations

import threading
from org.allbinary.data.tree.category.CategoryModifierTree import CategoryModifierTree
from org.allbinary.data.tree.category.CategoryLoaderInterface import CategoryLoaderInterface


class CategoryLoader(CategoryModifierTree, CategoryLoaderInterface):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, categoryFactoryInterface: CategoryFactoryInterface) -> None:
        super().__init__(categoryFactoryInterface)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF(self.commonStrings.START, self, "CategoryLoader(CategoryFactoryInterface categoryFactoryInterface)")
    

    def getDoc(self, categoryInterface: CategoryInterface) -> Document:
        with self._lock:
            return self._getDoc_unlocked(categoryInterface)

    def _getDoc_unlocked(self, categoryInterface: CategoryInterface) -> Document:
        try:
            if categoryInterface.getProperties().getPath(categoryInterface.getHierarchy()) is not None:
                if categoryInterface.getHierarchy().getLevel() == 1:
                    rootAbFile: AbFile = AbFile.createAbFileFromAbPath(categoryInterface.getRootFilePath())
                    if not rootAbFile.isDirectory():
                        rootAbFile.mkdirs()
                        if not rootAbFile.isDirectory():
                            raise Exception("Could Not Create Directory")
                        self.save(categoryInterface)
                fileAbPath: AbPath = categoryInterface.getFilePath()
                cryptFileReader: CryptFileReader = CryptFileReader(CategoryData.getInstance().UNCRYPTED_EXTENSION, CategoryData.getInstance().ENCRYPTED_EXTENSION)
                document: Document = DomDocumentHelper.create(cryptFileReader.get(fileAbPath))
                return document
            else:
                raise Exception("Null Category")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                try:
                    categoryInterface.log()
                except Exception as e2:
                    self.logUtil.put("Could Not Log Category", self, "getDoc", e)
                self.logUtil.put(self.commonStrings.FAILURE, self, "getDoc", e)
            return None
    

    def get(self, categoryInterface: CategoryInterface) -> CategoryInterface:
        with self._lock:
            return self._get_unlocked(categoryInterface)

    def _get_unlocked(self, categoryInterface: CategoryInterface) -> CategoryInterface:
        try:
            document: Document = self.getDoc(categoryInterface)
            categoryNode: Node = DomSearchHelper.getNode(CategoryData.getInstance().NAME, document.getChildNodes())
            return self.addProperties(categoryInterface, categoryNode.getChildNodes())
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def get(self, document: Document) -> CategoryInterface:
        with self._lock:
            return self._get_unlocked(document)

    def _get_unlocked(self, document: Document) -> CategoryInterface:
        try:
            categoryNode: Node = DomSearchHelper.getNode(CategoryData.getInstance().NAME, document.getChildNodes())
            loadedCategoryInterface: CategoryInterface = self.categoryFactoryInterface.getRootInstanceFromNode(categoryNode)
            return self.addProperties(loadedCategoryInterface, categoryNode.getChildNodes())
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None
    

    def getAll(self, categoryInterface: CategoryInterface) -> CategoryInterface:
        with self._lock:
            return self._getAll_unlocked(categoryInterface)

    def _getAll_unlocked(self, categoryInterface: CategoryInterface) -> CategoryInterface:
        try:
            document: Document = self.getDoc(categoryInterface)
            return self.getAll(document)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getAll(self, document: Document) -> CategoryInterface:
        with self._lock:
            return self._getAll_unlocked(document)

    def _getAll_unlocked(self, document: Document) -> CategoryInterface:
        try:
            categoryNode: Node = DomSearchHelper.getNode(CategoryData.getInstance().NAME, document.getChildNodes())
            loadedCategoryInterface: CategoryInterface = self.categoryFactoryInterface.getRootInstanceFromNode(categoryNode)
            return self.addProperties(loadedCategoryInterface, categoryNode.getChildNodes())
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getAll(self, parentCategoryInterface: CategoryInterface, categoryNodeList: NodeList) -> CategoryInterface:
        with self._lock:
            return self._getAll_unlocked(parentCategoryInterface, categoryNodeList)

    def _getAll_unlocked(self, parentCategoryInterface: CategoryInterface, categoryNodeList: NodeList) -> CategoryInterface:
        try:
            if categoryNodeList is not None:
                for index in range(0, categoryNodeList.getLength()):
                    categoryNode: Node = categoryNodeList.item(index)
                    if categoryNode is not None and categoryNode.getNodeName().compareTo(CategoryData.getInstance().NAME) == 0:
                        categoryInterface: CategoryInterface = self.categoryFactoryInterface.getInstance(parentCategoryInterface.getHierarchy().getRoot(), parentCategoryInterface, categoryNode)
                        parentCategoryInterface.addChild(categoryInterface)
            return parentCategoryInterface
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None
    

    def addProperties(self, loadedCategoryInterface: CategoryInterface, categoryNodeList: NodeList) -> CategoryInterface:
        with self._lock:
            return self._addProperties_unlocked(loadedCategoryInterface, categoryNodeList)

    def _addProperties_unlocked(self, loadedCategoryInterface: CategoryInterface, categoryNodeList: NodeList) -> CategoryInterface:
        try:
            if categoryNodeList is not None:
                for index in range(0, categoryNodeList.getLength()):
                    categoryNode: Node = categoryNodeList.item(index)
                    if categoryNode is not None and categoryNode.getNodeName().compareTo(CategoryData.getInstance().NAME) == 0:
                        categoryPropertiesInterface: CategoryPropertiesInterface = CategoryProperties(categoryNode)
                        loadedCategoryInterface.addChildProperty(categoryPropertiesInterface)
            return loadedCategoryInterface
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.GET, e)
            return None
from org.allbinary.business.category.CategoryData import CategoryData
from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
from org.allbinary.business.category.CategoryInterface import CategoryInterface
from org.allbinary.business.category.properties.CategoryProperties import CategoryProperties
from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.crypt.file.CryptFileReader import CryptFileReader
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.path.AbPath import AbPath
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


