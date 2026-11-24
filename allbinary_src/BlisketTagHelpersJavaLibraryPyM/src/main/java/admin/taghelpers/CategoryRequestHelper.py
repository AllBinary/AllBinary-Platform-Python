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
# package admin.taghelpers

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static
from admin.taghelpers.ModifyTable import ModifyTable


class CategoryRequestHelper(ModifyTable):
    categoryRequest: str = None

    def _init_fields(self) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.data.tree.category.CategoryLoaderInterface import CategoryLoaderInterface
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.pageContext: PageContext = None
        self.hashMap: HashMap = None
        self.request: HttpServletRequest = None
        self.categoryLoaderInterface: CategoryLoaderInterface = None
        self.categoryInterface: CategoryInterface = None
        self.childCategoryInterface: CategoryInterface = None
        self.transformInfoInterface: TransformInfoInterface = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        self._init_fields()
        try:
            self.request = pageContext.getRequest()
            self.pageContext = pageContext
            self.hashMap = hashMap
            self.getXmlData()
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "CategoryRequestHelper()", e)
    

    def getXmlData(self) -> None:
        from java.util.Map import Map
        from java.util.Set import Set
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.store.StoreCategoryFactory import StoreCategoryFactory
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            map: Map = self.request.getParameterMap()
            categoryData: CategoryData = CategoryData.getInstance()
            keys: Set = map.keySet()
            keyArray: list[object] = keys.toArray()
            size: int = len(keyArray)
            if size > 0:
                xmlRequest: str = keyArray[0]
                index: int = 1
                while index < size and not xmlRequest.startswith(CategoryRequestHelper.categoryRequest):
                    xmlRequest = keyArray[index]
                    if xmlRequest.startswith(CategoryRequestHelper.categoryRequest):
                        break
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPER):
                    self.logUtil.putF(xmlRequest, self, "getXmlData()")
                document: Document = DomDocumentHelper.create(xmlRequest)
                requestNode: Node = DomSearchHelper.getNode(categoryData.REQUEST, document.getChildNodes())
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPER):
                    self.logUtil.putF(XmlDocumentHelper.toString(document), self, "getXmlData()")
                self.setCategoryLoader(requestNode)
                parentCategoryNode: Node = DomSearchHelper.getNode(categoryData.PARENT, requestNode.getChildNodes())
                categoryNode: Node = DomSearchHelper.getNode(categoryData.NAME, parentCategoryNode.getChildNodes())
                self.categoryInterface = StoreCategoryFactory(self.transformInfoInterface).getRootInstanceFromNode(categoryNode)
                self.categoryInterface = self.categoryLoaderInterface.get(self.categoryInterface)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPER):
                    self.categoryInterface.log()
                    self.logUtil.putF("Loaded Parent Category", self, "getXmlData()")
                childCategoryNode: Node = DomSearchHelper.getNodeNoThrow(categoryData.NAME, requestNode.getChildNodes())
                if childCategoryNode is not None:
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPER):
                        self.logUtil.putF("Loading Child Category", self, "getXmlData()")
                    self.childCategoryInterface = StoreCategoryFactory(self.transformInfoInterface).getInstance(childCategoryNode)
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPER):
                        self.childCategoryInterface.log()
                        self.logUtil.putF("Loaded Child Category", self, "getXmlData()")
                else:
                    self.childCategoryInterface = self.categoryInterface
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getXmlData()", e)
    

    # throws Exception
    def setCategoryLoader(self, requestNode: Node) -> None:
        from org.allbinary.business.category.store.StoreCategoryFactory import StoreCategoryFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.data.tree.category.CategoryLoaderFactory import CategoryLoaderFactory
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.logic.visual.transform.info.TransformInfoBasic import TransformInfoBasic
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.w3c.dom.Node import Node
        storeNameNode: Node = DomSearchHelper.getNode(StoreFrontData.getInstance().NAME, requestNode.getChildNodes())
        if storeNameNode is not None:
            storeName: str = DomNodeHelper.getTextNodeValue(storeNameNode)
            if storeName is not None:
                storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(storeName)
                self.transformInfoInterface = TransformInfoBasic(storeFrontInterface, self.hashMap, self.pageContext)
                if self.transformInfoInterface is None:
                    raise Exception("TransformInfo null")
                storeCategoryFactory: StoreCategoryFactory = StoreCategoryFactory(self.transformInfoInterface)
                self.categoryLoaderInterface = CategoryLoaderFactory.getInstance(storeCategoryFactory)
            else:
                raise Exception("Store Name Error: " + storeName)
    

    def insert(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successfully Added the following to the Category table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("inserting", self, "insert()")
            self.categoryLoaderInterface.insert(self.categoryInterface, self.childCategoryInterface)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert()")
            return success
        except Exception as e:
            error: str = "Failed to add item to Category"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insert()", e)
            return error
    

    def delete(self) -> str:
        from org.allbinary.business.category.CategoryData import CategoryData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successfully Removed " + str(CategoryData.getInstance().NAME) + "=" + str(self.childCategoryInterface.getPath())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Deleting", self, "delete()")
            self.categoryLoaderInterface.delete(self.categoryInterface, self.childCategoryInterface)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            try:
                error: str = "Failed to remove category: " + str(self.childCategoryInterface.getPath())
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                    self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
                return error
            except Exception as e2:
                error: str = "Failed to remove category and show the path of the failed category"
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                    self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e2)
                return error
    

    def viewCategory(self) -> str:
        from org.allbinary.business.category.CategoryComponent import CategoryComponent
        from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
        from org.w3c.dom.Document import Document
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            document: Document = CategoryComponent(self.childCategoryInterface).toXmlDoc()
            xmlString: str = XmlDocumentHelper.toString(document)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(xmlString, self, "viewCategory()")
            return xmlString
        except Exception as e:
            error: str = "Failed to get Category"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "viewCategory()", e)
            return error
    

    def viewCategories(self) -> str:
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = StringUtil.getInstance().EMPTY_STRING
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "viewCategories()")
            return success
        except Exception as e:
            error: str = "Failed to view Categories table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "viewCategories()", e)
            return error
    

    def update(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "New Item Successfully added"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to add Item"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
# from java.util.HashMap import HashMap
# from java.util.Map import Map
# from java.util.Set import Set
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.category.CategoryComponent import CategoryComponent
# from org.allbinary.business.category.CategoryData import CategoryData
# from org.allbinary.business.category.CategoryInterface import CategoryInterface
# from org.allbinary.business.category.store.StoreCategoryFactory import StoreCategoryFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.data.tree.category.CategoryLoaderFactory import CategoryLoaderFactory
# from org.allbinary.data.tree.category.CategoryLoaderInterface import CategoryLoaderInterface
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
# from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoBasic import TransformInfoBasic
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _CategoryRequestHelper_categoryRequest() -> object:
    from org.allbinary.business.category.CategoryData import CategoryData
    from org.allbinary.logic.string.StringMaker import StringMaker
    return str(StringMaker().append("<").append(CategoryData.getInstance().REQUEST).append(">"))

lazy_static(CategoryRequestHelper, "categoryRequest", _CategoryRequestHelper_categoryRequest)

