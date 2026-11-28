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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "map" not in vars(self): self.map: Map = None
        self.KEY: str = "Key: "
        self.VALUE: str = " Value: "

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "HttpServletRequest" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor0(self) -> None:
        __class__._init_fields(self)
        self.logUtil.putF("New RequestParams Size: 0", self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor1_1(self, request: HttpServletRequest) -> None:
        __class__._init_fields(self)
        self.map = request.getParameterMap()
        self.logUtil.putF("RequestParams Size: " + str(self.getMap().keySet().size()), self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor1_2(self, pageContext: PageContext) -> None:
        __class__._init_fields(self)
        self.map = pageContext.getRequest().getParameterMap()
        self.logUtil.putF("Request Params Size: " + str(self.getMap().keySet().size()), self, self.commonStrings.CONSTRUCTOR)
    

    def setMap(self, map: Map) -> None:
        from java.util.Map import Map
        self.map = map
    

    def getMap(self) -> Map:
        from java.util.Map import Map
        return self.map
    

    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.logic.communication.http.request.RequestData import RequestData
        from org.allbinary.logic.communication.http.request.RequestData import RequestData
        from java.util.Set import Set
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
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
    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
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
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


