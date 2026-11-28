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

from java.lang.JavaRuntimeStatic import java_predicate


class AbeHttpRequestInfo:

    def _init_fields(self) -> None:
        from org.allbinary.string.CommonSeps import CommonSeps
        self.NAME: str = "AbeHttpRequestInfo"
        self.abeHttpRequestInfoData: AbeHttpRequestInfoData = AbeHttpRequestInfoData.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        if "httpUserAgent" not in vars(self): self.httpUserAgent: str = None
        if "remoteAddress" not in vars(self): self.remoteAddress: str = None
        if "remoteHost" not in vars(self): self.remoteHost: str = None
        if "remoteHostByAddr" not in vars(self): self.remoteHostByAddr: str = None
        if "remotePort" not in vars(self): self.remotePort: str = None
        if "requestedFilePath" not in vars(self): self.requestedFilePath: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor1_1(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.string.StringUtil import StringUtil
        __class__._init_fields(self)
        stringUtil: StringUtil = StringUtil.getInstance()
        self.httpUserAgent = stringUtil.getNonNull(hashMap.get(self.abeHttpRequestInfoData.HTTP_USER_AGENT))
        self.remoteAddress = stringUtil.getNonNull(hashMap.get(self.abeHttpRequestInfoData.REMOTE_ADDRESS))
        self.remoteHost = stringUtil.getNonNull(hashMap.get(self.abeHttpRequestInfoData.REMOTE_HOST))
        self.remoteHostByAddr = stringUtil.getNonNull(hashMap.get(self.abeHttpRequestInfoData.REMOTE_HOST_BY_ADDRESS))
        self.remotePort = stringUtil.getNonNull(hashMap.get(self.abeHttpRequestInfoData.REMOTE_PORT))
        self.requestedFilePath = stringUtil.getNonNull(hashMap.get(self.abeHttpRequestInfoData.REQUEST_FILE_PATH))
    

    def _constructor1_2(self, httpServletRequest: HttpServletRequest) -> None:
        from java.util.Enumeration import Enumeration
        from org.allbinary.logic.string.StringUtil import StringUtil
        __class__._init_fields(self)
        stringUtil: StringUtil = StringUtil.getInstance()
        self.httpUserAgent = stringUtil.EMPTY_STRING
        enumuration: Enumeration = httpServletRequest.getHeaderNames()
        while java_predicate(enumuration, "hasMoreElements"):
            key: str = enumuration.nextElement()
            value: str = httpServletRequest.getHeader(key)
            if key.find("user") >= 0:
                self.httpUserAgent = "key: " + key + " value: " + value
        self.remoteHostByAddr = stringUtil.EMPTY_STRING
        self.remoteAddress = httpServletRequest.getRemoteAddr()
        self.remoteHost = httpServletRequest.getRemoteHost()
        self.requestedFilePath = httpServletRequest.getServletPath()
        self.remotePort = str(httpServletRequest.getRemotePort())
    

    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(self.abeHttpRequestInfoData.HTTP_USER_AGENT, self.httpUserAgent)
        hashMap.put(self.abeHttpRequestInfoData.REMOTE_ADDRESS, self.remoteAddress)
        hashMap.put(self.abeHttpRequestInfoData.REMOTE_HOST, self.remoteHost)
        hashMap.put(self.abeHttpRequestInfoData.REMOTE_HOST_BY_ADDRESS, self.remoteHostByAddr)
        hashMap.put(self.abeHttpRequestInfoData.REMOTE_PORT, self.remotePort)
        hashMap.put(self.abeHttpRequestInfoData.REQUEST_FILE_PATH, self.requestedFilePath)
        return hashMap
    

    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        vector: BasicArrayList = BasicArrayListD()
        vector.add(self.httpUserAgent)
        vector.add(self.remoteAddress)
        vector.add(self.remoteHost)
        vector.add(self.remoteHostByAddr)
        vector.add(self.remotePort)
        vector.add(self.requestedFilePath)
        return vector
    

    def toString(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        return str(StringMaker().append(self.NAME).append(self.commonSeps.COLON_SEP).append(self.abeHttpRequestInfoData.HTTP_USER_AGENT).append(self.commonSeps.COLON_SEP).append(self.httpUserAgent).append(self.commonSeps.SPACE).append(self.abeHttpRequestInfoData.REMOTE_ADDRESS).append(self.commonSeps.COLON_SEP).append(self.remoteAddress).append(self.commonSeps.SPACE).append(self.abeHttpRequestInfoData.REMOTE_HOST).append(self.commonSeps.COLON_SEP).append(self.remoteHost).append(self.commonSeps.SPACE).append(self.abeHttpRequestInfoData.REMOTE_HOST_BY_ADDRESS).append(self.commonSeps.COLON_SEP).append(self.remoteHostByAddr).append(self.commonSeps.SPACE).append(self.abeHttpRequestInfoData.REMOTE_PORT).append(self.commonSeps.COLON_SEP).append(self.remotePort).append(self.commonSeps.SPACE).append(self.abeHttpRequestInfoData.REQUEST_FILE_PATH).append(self.commonSeps.COLON_SEP).append(self.requestedFilePath))

    def __str__(self) -> str:
        return self.toString()
# from java.util.Enumeration import Enumeration
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.communication.http.request.AbeHttpRequestInfoData import AbeHttpRequestInfoData


