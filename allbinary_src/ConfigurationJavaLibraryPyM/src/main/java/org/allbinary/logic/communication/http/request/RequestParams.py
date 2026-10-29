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
# package org.allbinary.logic.communication.http.request

from __future__ import annotations



#Note: if request is destroyed or messed up this will not work. Use fileRequestParams
class RequestParams:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.map: Map = None
        self.KEY: str = "Key: "
        self.VALUE: str = " Value: "

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.logUtil.putF("New RequestParams Size: 0", self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor1(self, request: HttpServletRequest) -> None:
        self._init_fields()
        self.map = request.getParameterMap()
        self.logUtil.putF("RequestParams Size: " + str(self.getMap().keySet().size()), self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor1(self, pageContext: PageContext) -> None:
        self._init_fields()
        self.map = pageContext.getRequest().getParameterMap()
        self.logUtil.putF("Request Params Size: " + str(self.getMap().keySet().size()), self, self.commonStrings.CONSTRUCTOR)
    

    def setMap(self, map: Map) -> None:
        self.map = map
    

    def getMap(self) -> Map:
        return self.map
    

    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.http.request.RequestData import RequestData
        from org.allbinary.logic.communication.http.request.RequestData import RequestData
        try:
            node: Node = document.createElement(RequestData.REQUEST)
            stringBuffer: StringMaker = StringMaker()
            keys: Set = self.map.keySet()
            keyArray: list[object] = keys.toArray()
            size: int = len(keyArray)
            for i in range(0, size):
                key: str = keyArray[i]
                values: list[str] = self.map.get(key)
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(self.KEY)
                stringBuffer.append(key)
                stringBuffer.append(self.VALUE)
                stringBuffer.append(values[0])
                self.logUtil.putF(str(stringBuffer), self, "toXmlNode(document)")
                node.appendChild(ModDomHelper.createNameValueNodes(document, RequestData.PARAMETER, str(key), str(values[0])))
            return node
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "toXmlNode(document)", e)
            return None
    

    # throws Exception
    def toHashMap(self) -> dict:
        hashMap: dict = StdUtil.getInstance().createHashMap()
        keys: Set = self.map.keySet()
        keyArray: list[object] = keys.toArray()
        size: int = len(keyArray)
        stringBuffer: StringMaker = StringMaker()
        for i in range(0, size):
            key: str = keyArray[i]
            values: list[str] = self.map.get(key)
            hashMap.put(str(key), str(values[0]))
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append("RequestParams: ")
        stringBuffer.append(str(self.map))
        stringBuffer.append("\ntoHashMap: ")
        stringBuffer.append(str(hashMap))
        self.logUtil.putF(str(stringBuffer), self, "toHashMap()")
        return hashMap
# from java.util.HashMap import HashMap
# from java.util.Map import Map
# from java.util.Set import Set
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


