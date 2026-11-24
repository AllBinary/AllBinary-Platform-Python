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

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
from org.allbinary.business.category.properties.root.RootCategoryPropertiesInterface import RootCategoryPropertiesInterface


class RootStoreCategoryProperties(*java_bases(RootCategoryPropertiesInterface, CategoryPropertiesInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
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
            self.__jconstructor2(*args)

    def __jconstructor2(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)):
            self._constructor2_1(*args)
        elif True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)):
            self._constructor2_2(*args)
        else:
            self._constructor2_3(*args)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
        self.abPath = AbPath.createAbPath()
        self.category = CategoryData.getInstance().ROOTCATEGORY
        self.isRealRoot = True
        self.initPath()
        self.log()
    

    def _constructor2_1(self, transformInfoInterface: TransformInfoInterface, categoryAbPath: AbPath) -> None:
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
        self.abPath = categoryAbPath
        self.category = self.pathData.getNameFromPath(str(categoryAbPath))
        if StringValidationUtil.getInstance().isEmpty(self.category):
            self.isRealRoot = True
            self.category = CategoryData.getInstance().ROOTCATEGORY
        self.initPath()
        self.log()
    

    def _constructor2_2(self, transformInfoInterface: TransformInfoInterface, node: Node) -> None:
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.business.category.CategoryUtil import CategoryUtil
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.w3c.dom.Node import Node
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
    

    def _constructor2_3(self, transformInfoInterface: TransformInfoInterface, categoryPropertiesHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
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
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
        transformInfoHttpStoreInterface: TransformInfoHttpInterface = self.transformInfoInterface
        storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(transformInfoHttpStoreInterface.getStoreName())
        postPath: str = storeFrontInterface.getCurrentHostNamePath() + storeFrontInterface.getCategoryPath()
        httpServletRequest: HttpServletRequest = transformInfoHttpStoreInterface.getPageContext().getRequest()
        self.webAppAbPath = AbPath(str(httpServletRequest.getContextPath()) + postPath, StringUtil.getInstance().EMPTY_STRING)
        self.setRootFilePath(AbPath(str(URLGLOBALS.getMainPath()) + postPath, StringUtil.getInstance().EMPTY_STRING))
    

    def isRealRoot(self) -> bool:
        return self.isRealRoot
    

    def isRoot(self) -> bool:
        return True
    

    def getKey(self) -> object:
        return self.getValue()
    

    def setPath(self, path: AbPath) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        self.abPath = path
    

    def setRootFilePath(self, value: AbPath) -> None:
        from org.allbinary.logic.io.path.AbPath import AbPath
        self.fileAbPath = value
    

    def getRootFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return self.fileAbPath
    

    def getValue(self) -> str:
        return self.category
    

    # throws Exception
    def getWebAppPath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        return self.webAppAbPath
    

    def getPath(self, categoryHierarchyInterface: CategoryHierarchyInterface) -> AbPath:
        from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
        from org.allbinary.logic.io.path.AbPath import AbPath
        return self.abPath
    

    def getFileName(self) -> str:
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.logic.io.path.AbPathData import AbPathData
        return self.getValue() + AbPathData.getInstance().EXTENSION_SEP + CategoryData.getInstance().UNCRYPTED_EXTENSION
    

    def setValue(self, value: str) -> None:
        self.category = value
    

    def isValid(self) -> bool:
        return True
    

    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.logic.StdUtil import StdUtil
        categoryHashMap: HashMap = StdUtil.getInstance().createHashMap()
        categoryHashMap.put(CategoryData.getInstance().NAME, self.getValue())
        return categoryHashMap
    

    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        categoryVector: BasicArrayList = BasicArrayListD()
        categoryVector.add(self.getValue())
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
    

    def log(self) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF(str(StringMaker().append("filePath = ").append(str(self.fileAbPath)).append("\npath = ").append(str(self.abPath)).append("\ncategory = ").append(self.category)), self, "log()")
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.business.category.CategoryData import CategoryData
# from org.allbinary.business.category.CategoryUtil import CategoryUtil
# from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.io.path.AbPathData import AbPathData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


