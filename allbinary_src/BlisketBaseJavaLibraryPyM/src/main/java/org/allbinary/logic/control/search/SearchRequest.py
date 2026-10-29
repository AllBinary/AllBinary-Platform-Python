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
# package org.allbinary.logic.control.search

from __future__ import annotations

from org.allbinary.business.context.AbContext import AbContext


class SearchRequest(AbContext):

    def _init_fields(self) -> None:
        self.xslFile: str = None
        self.pageName: str = None
        self.contentType: str = None
        self.searchParams: SearchParams = None
        self.storeFront: StoreFrontInterface = None
    

    def __init__(self, storeFront: StoreFrontInterface, searchParams: SearchParams, xslFile: str, contentType: str, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__(propertiesHashMap, pageContext)
        self._init_fields()
        self.storeFront = storeFront
        self.searchParams = searchParams
        self.xslFile = xslFile
        self.pageName = self.pageName
        self.contentType = contentType
    

    def setStoreFront(self, storeFront: StoreFrontInterface) -> None:
        self.storeFront = storeFront
    

    def setParams(self, searchParams: SearchParams) -> None:
        self.searchParams = searchParams
    

    def setXslFile(self, value: str) -> None:
        self.xslFile = value
    

    def setFileBaseName(self, value: str) -> None:
        self.pageName = value
    

    def setContentType(self, value: str) -> None:
        self.contentType = value
    

    def getStoreFront(self) -> StoreFrontInterface:
        return self.storeFront
    

    def getParams(self) -> SearchParams:
        return self.searchParams
    

    def getXslFile(self) -> str:
        return self.xslFile
    

    def getFileBaseName(self) -> str:
        return self.pageName
    

    def getContentType(self) -> str:
        return self.contentType
    

    # throws Exception
    def getFileBaseNameNode(self, document: Document) -> Node:
        from org.allbinary.logic.control.search.SearchData import SearchData
        return ModDomHelper.createNameValueNodes(document, SearchData.FILENAME, self.getFileBaseName())
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


