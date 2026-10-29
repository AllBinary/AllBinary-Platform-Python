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
# package org.allbinary.business.category.properties.root.store

from __future__ import annotations

from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
from org.allbinary.business.category.properties.root.RootCategoryPropertiesInterface import RootCategoryPropertiesInterface


class RootStoreCategoryProperties(RootCategoryPropertiesInterface, CategoryPropertiesInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.pathData: AbPathData = AbPathData.getInstance()
        self.fileAbPath: AbPath = None
        self.abPath: AbPath = None
        self.category: str = None
        self.isRealRoot: bool = None
        self.webAppAbPath: AbPath = None
        self.transformInfoInterface: TransformInfoInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
        self.abPath = AbPath.createAbPath()
        self.category = CategoryData.getInstance().ROOTCATEGORY
        self.isRealRoot = True
        self.initPath()
        self.log()
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, categoryAbPath: AbPath) -> None:
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
        self.abPath = categoryAbPath
        self.category = self.pathData.getNameFromPath(str(categoryAbPath))
        if StringValidationUtil.getInstance().isEmpty(self.category):
            self.isRealRoot = True
            self.category = CategoryData.getInstance().ROOTCATEGORY
        self.initPath()
        self.log()
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, node: Node) -> None:
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
        categoryPath: str = CategoryUtil.getNameFromNode(node)
        self.abPath = AbPath(categoryPath, StringUtil.getInstance().EMPTY_STRING)
        self.category = self.pathData.getNameFromPath(categoryPath)
        if StringValidationUtil.getInstance().isEmpty(self.category):
            self.isRealRoot = True
            self.category = CategoryData.getInstance().ROOTCATEGORY
        self.initPath()
        self.log()
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, categoryPropertiesHashMap: dict) -> None:
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
        categoryPath: str = str(categoryPropertiesHashMap.get(CategoryData.getInstance().NAME))
        self.abPath = AbPath(categoryPath, StringUtil.getInstance().EMPTY_STRING)
        self.category = self.pathData.getNameFromPath(categoryPath)
        if StringValidationUtil.getInstance().isEmpty(self.category):
            self.isRealRoot = True
            self.category = CategoryData.getInstance().ROOTCATEGORY
        self.initPath()
        self.log()
    

    # throws Exception
    def initPath(self) -> None:
        transformInfoHttpStoreInterface: TransformInfoHttpInterface = self.transformInfoInterface
        storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(transformInfoHttpStoreInterface.getStoreName())
        postPath: str = storeFrontInterface.getCurrentHostNamePath() + storeFrontInterface.getCategoryPath()
        httpServletRequest: HttpServletRequest = transformInfoHttpStoreInterface.getPageContext().getRequest()
        self.webAppAbPath = AbPath(str(httpServletRequest.getContextPath()) + postPath, StringUtil.getInstance().EMPTY_STRING)
        self.setRootFilePath(AbPath(str(self.URLGLOBALS.getMainPath()) + postPath, StringUtil.getInstance().EMPTY_STRING))
    

    def isRealRoot(self) -> bool:
        return self.isRealRoot
    

    def isRoot(self) -> bool:
        return True
    

    def getKey(self) -> object:
        return self.getValue()
    

    def setPath(self, path: AbPath) -> None:
        self.abPath = path
    

    def setRootFilePath(self, value: AbPath) -> None:
        self.fileAbPath = value
    

    def getRootFilePath(self) -> AbPath:
        return self.fileAbPath
    

    def getValue(self) -> str:
        return self.category
    

    # throws Exception
    def getWebAppPath(self) -> AbPath:
        return self.webAppAbPath
    

    def getPath(self, categoryHierarchyInterface: CategoryHierarchyInterface) -> AbPath:
        return self.abPath
    

    def getFileName(self) -> str:
        return self.getValue() + AbPathData.getInstance().EXTENSION_SEP + CategoryData.getInstance().UNCRYPTED_EXTENSION
    

    def setValue(self, value: str) -> None:
        self.category = value
    

    def isValid(self) -> bool:
        return True
    

    def toHashMap(self) -> dict:
        categoryHashMap: dict = StdUtil.getInstance().createHashMap()
        categoryHashMap.put(CategoryData.getInstance().NAME, self.getValue())
        return categoryHashMap
    

    def toVector(self) -> BasicArrayList:
        categoryVector: BasicArrayList = BasicArrayListD()
        categoryVector.add(self.getValue())
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
    

    def log(self) -> None:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF(str(StringMaker().append("filePath = ").append(str(self.fileAbPath)).append("\npath = ").append(str(self.abPath)).append("\ncategory = ").append(self.category)), self, "log()")
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.category.CategoryData import CategoryData
from org.allbinary.business.category.CategoryUtil import CategoryUtil
from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


