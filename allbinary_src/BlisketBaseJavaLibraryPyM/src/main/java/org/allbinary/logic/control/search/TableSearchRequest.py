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



class TableSearchRequest:

    def _init_fields(self) -> None:
        self.xslFile: str = None
        self.pageName: str = None
        self.contentType: str = None
        self.keywords: str = None
        self.searchParams: SearchParams = None
    

    def __init__(self, keywords: str, searchParams: SearchParams, xslFile: str, contentType: str) -> None:
        self._init_fields()
        self.keywords = keywords
        self.searchParams = searchParams
        self.xslFile = xslFile
        self.pageName = self.pageName
        self.contentType = contentType
    

    def setKeywords(self, value: str) -> None:
        self.keywords = value
    

    def setParams(self, searchParams: SearchParams) -> None:
        self.searchParams = searchParams
    

    def setXslFile(self, value: str) -> None:
        self.xslFile = value
    

    def setFileBaseName(self, value: str) -> None:
        self.pageName = value
    

    def setContentType(self, value: str) -> None:
        self.contentType = value
    

    def getKeywords(self) -> str:
        return self.keywords
    

    def getParams(self) -> SearchParams:
        return self.searchParams
    

    # throws Exception
    def getXslFile(self) -> str:
        path: str = str(self.URLGLOBALS.getMainPath() + self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH) + self.xslFile
        return path
    

    def getFileBaseName(self) -> str:
        return self.pageName
    

    def getContentType(self) -> str:
        return self.contentType
    

    # throws Exception
    def getFileBaseNameNode(self, document: Document) -> Node:
        from org.allbinary.logic.control.search.SearchData import SearchData
        return ModDomHelper.createNameValueNodes(document, SearchData.FILENAME, self.getFileBaseName())
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


