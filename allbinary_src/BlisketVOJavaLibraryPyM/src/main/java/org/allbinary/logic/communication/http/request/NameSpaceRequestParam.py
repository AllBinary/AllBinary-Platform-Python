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



class NameSpaceRequestParam:

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "nameSpaceVector" not in vars(self): self.nameSpaceVector: BasicArrayList = None
        if "nameSpacePropertiesHashMap" not in vars(self): self.nameSpacePropertiesHashMap: HashMap = None
        if "value" not in vars(self): self.value: str = None
    

    def __init__(self, nameSpace: str, value: str) -> None:
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        self.nameSpaceVector = BasicArrayListD()
        self.nameSpacePropertiesHashMap = StdUtil.getInstance().createHashMap()
        self.value = value
        beginIndex: int = nameSpace.find(NameSpaceRequestParamData.NAME)
        if beginIndex < 0:
            raise Exception("Not a NameSpaceRequest")
        packages: str = nameSpace[beginIndex + __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(NameSpaceRequestParamData.NAME) + __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(NameSpaceRequestParamData.SEP):]
        sepTokenizer: Tokenizer = Tokenizer(NameSpaceRequestParamData.SEP)
        nameSpaceWithPropertiesVector: BasicArrayList = sepTokenizer.getTokensFromString(packages, BasicArrayListD())
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("\nSep Tokens: " + str(nameSpaceWithPropertiesVector), self, "NameSpaceRequestParam()")
        nameSpaceAndPropertiesTokenizer: Tokenizer = Tokenizer(NameSpaceRequestParamData.PROPERTIES)
        packageIndex: int = 0
        list_: BasicArrayList = BasicArrayListD()
        index: int = 0
        size: int = nameSpaceWithPropertiesVector.size()
        while index < size:
            nameSpaceWithProperties: str = nameSpaceWithPropertiesVector.get(((index := index + 1) - 1))
            list_.clear()
            nameSpaceAndPropertiesVector: BasicArrayList = nameSpaceAndPropertiesTokenizer.getTokensFromString(nameSpaceWithProperties, list_)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
                self.logUtil.putF("\nPackageName and PackageName Properties Tokens: " + str(nameSpaceAndPropertiesVector), self, "NameSpaceRequestParam()")
            if nameSpaceAndPropertiesVector.size() > 0:
                packageName: str = nameSpaceAndPropertiesVector.get(0)
                if packageName is None:
                    raise Exception("Package Name Is Null")
                self.nameSpaceVector.add(packageName)
                if nameSpaceAndPropertiesVector.size() > 1:
                    properties: str = nameSpaceAndPropertiesVector.get(1)
                    packagePropertiesHashMap: HashMap = self.generatePackagePropertiesHashMap(properties)
                    self.nameSpacePropertiesHashMap.put(str(packageIndex), packagePropertiesHashMap)
                packageIndex += 1
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("NameSpace: " + str(self.nameSpaceVector), self, "NameSpaceRequestParam()")
    

    def getPackages(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("NameSpace: " + str(self.nameSpaceVector), self, "getPackages()")
        return self.nameSpaceVector
    

    def getPackageProperties(self, packageIndex: int) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        packagePropertiesHashMap: HashMap = self.nameSpacePropertiesHashMap.get(str(packageIndex))
        if packagePropertiesHashMap is None:
            packagePropertiesHashMap = StdUtil.getInstance().createHashMap()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("Package Properties: " + str(packagePropertiesHashMap), self, "getPackagesProperties()")
        return packagePropertiesHashMap
    

    def getValue(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("\nValue: " + self.value, self, "getValue()")
        return self.value
    

    # throws Exception
    def generatePackagePropertiesHashMap(self, properties: str) -> HashMap:
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
        from org.allbinary.logic.visual.dhtml.html.name.HtmlNameMathData import HtmlNameMathData
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        propertiesTokenizer: Tokenizer = Tokenizer(NameSpaceRequestParamData.PROPERTIESSEPARATOR)
        packagePropertiesHashMap: HashMap = StdUtil.getInstance().createHashMap()
        propertyVector: BasicArrayList = propertiesTokenizer.getTokensFromString(properties, BasicArrayListD())
        list_: BasicArrayList = BasicArrayListD()
        propertyTokenizer: Tokenizer = Tokenizer(HtmlNameMathData.getInstance().EQUALS)
        index: int = 0
        size: int = propertyVector.size()
        while index < size:
            property: str = propertyVector.get(index)
            list_.clear()
            propertyNameValueVector: BasicArrayList = propertyTokenizer.getTokensFromString(property, list_)
            index2: int = 0
            while index2 < propertyNameValueVector.size():
                propertyName: str = propertyNameValueVector.get(((index2 := index2 + 1) - 1))
                if propertyNameValueVector.size() > 1:
                    propertyValue: str = propertyNameValueVector.get(((index2 := index2 + 1) - 1))
                    if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
                        self.logUtil.putF("\nProperty Name: " + propertyName + "\nProperty Value: " + propertyValue, self, "generatePackagePropertiesHashMap()")
                    packagePropertiesHashMap.put(propertyName, propertyValue)
                else:
                    packagePropertiesHashMap.put(propertyName, StringUtil.getInstance().EMPTY_STRING)
        return packagePropertiesHashMap
# from java.util.HashMap import HashMap
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
# from org.allbinary.logic.visual.dhtml.html.name.HtmlNameMathData import HtmlNameMathData
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


