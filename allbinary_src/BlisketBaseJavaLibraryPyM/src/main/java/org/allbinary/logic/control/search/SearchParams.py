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



class SearchParams:

    def _init_fields(self) -> None:
        self.columnsAndSearchValues: dict = None
        self.order: str = None
        self.sortBy: str = None
        self.listLength: str = None
        self.startPage: str = None
        self.endPage: str = None
    

    def __init__(self, request: HttpServletRequest) -> None:
        from org.allbinary.logic.control.search.SearchData import SearchData
        from org.allbinary.logic.control.search.SearchData import SearchData
        from org.allbinary.logic.control.search.SearchData import SearchData
        from org.allbinary.logic.control.search.SearchData import SearchData
        from org.allbinary.logic.control.search.SearchData import SearchData
        from org.allbinary.logic.control.search.SearchData import SearchData
        from org.allbinary.logic.control.search.SearchData import SearchData
        from org.allbinary.logic.control.search.SearchData import SearchData
        self._init_fields()
        self.columnsAndSearchValues = StdUtil.getInstance().createHashMap()
        self.setLength(request.getParameter(SearchData.LENGTH))
        self.setOrder(request.getParameter(SearchData.ORDER))
        page: str = request.getParameter(SearchData.PAGE)
        self.setStartPage(page)
        self.setEndPage(page)
        self.setSortBy(request.getParameter(SearchData.SORTBY))
        index: int = 0
        columnName: str = request.getParameter(str(SearchData.COLUMNNAME) + "[0]")
        columnValue: str = request.getParameter(str(SearchData.COLUMNVALUE) + "[0]")
        while columnName is not None:
            self.add(columnName, columnValue)
            index += 1
            columnName = request.getParameter(str(SearchData.COLUMNNAME) + "[" + str(index) + "]")
            columnValue = request.getParameter(str(SearchData.COLUMNVALUE) + "[" + str(index) + "]")
    

    def add(self, column: str, value: str) -> None:
        self.columnsAndSearchValues.put(column, value)
    

    def setOrder(self, value: str) -> None:
        self.order = value
    

    def setSortBy(self, value: str) -> None:
        self.sortBy = value
    

    def setLength(self, value: str) -> None:
        self.listLength = value
    

    def setStartPage(self, value: str) -> None:
        self.startPage = value
    

    def setEndPage(self, value: str) -> None:
        self.endPage = value
    

    def get(self) -> dict:
        return self.columnsAndSearchValues
    

    def getOrder(self) -> str:
        return self.order
    

    def getSortBy(self) -> str:
        return self.sortBy
    

    def getLength(self) -> str:
        return self.listLength
    

    def getLengthInt(self) -> int:
        if self.listLength is not None:
            return int(self.listLength)
        else:
            return int(0)
    

    def getStartPage(self) -> str:
        return self.startPage
    

    def getEndPage(self) -> str:
        return self.endPage
    

    def getStartPageInt(self) -> int:
        if self.startPage is not None:
            return int(self.startPage)
        else:
            return int(0)
    

    def getEndPageInt(self) -> int:
        if self.endPage is not None:
            return int(self.endPage)
        else:
            return int(0)
    

    # throws Exception
    def getParamsNode(self, document: Document) -> Node:
        from org.allbinary.logic.control.search.SearchData import SearchData
        from org.allbinary.logic.control.search.SearchData import SearchData
        paramsNode: Node = ModDomHelper.createNameValueNodes(document, SearchData.PARAMS, SearchData.PARAMS)
        paramsNode.appendChild(self.getFieldsNode(document))
        paramsNode.appendChild(self.getOrderNode(document))
        paramsNode.appendChild(self.getSortByNode(document))
        paramsNode.appendChild(self.getLengthNode(document))
        return paramsNode
    

    # throws Exception
    def getFieldsNode(self, document: Document) -> Node:
        from org.allbinary.logic.control.search.SearchData import SearchData
        from org.allbinary.logic.control.search.SearchData import SearchData
        fieldsNode: Node = ModDomHelper.createNameValueNodes(document, SearchData.FIELDS, str(int(self.columnsAndSearchValues.size())))
        set: Set = self.columnsAndSearchValues.keySet()
        searchValueArray: list[object] = set.toArray()
        size: int = len(searchValueArray)
        for index in range(0, size):
            key: str = searchValueArray[index]
            searchValue: str = self.columnsAndSearchValues.get(key)
            fieldsNode.appendChild(ModDomHelper.createNameValueNodes(document, SearchData.FIELD, key, ToDomHelper.convertNull(searchValue)))
        return fieldsNode
    

    # throws Exception
    def getOrderNode(self, document: Document) -> Node:
        from org.allbinary.logic.control.search.SearchData import SearchData
        return ModDomHelper.createNameValueNodes(document, SearchData.ORDER, ToDomHelper.convertNull(self.getOrder()))
    

    # throws Exception
    def getSortByNode(self, document: Document) -> Node:
        from org.allbinary.logic.control.search.SearchData import SearchData
        return ModDomHelper.createNameValueNodes(document, SearchData.SORTBY, ToDomHelper.convertNull(self.getSortBy()))
    

    # throws Exception
    def getLengthNode(self, document: Document) -> Node:
        from org.allbinary.logic.control.search.SearchData import SearchData
        return ModDomHelper.createNameValueNodes(document, SearchData.LENGTH, ToDomHelper.convertNull(self.getLength()))
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.data.tree.dom.ToDomHelper import ToDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


