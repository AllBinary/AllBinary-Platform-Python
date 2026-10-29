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
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.nameSpaceVector: BasicArrayList = None
        self.nameSpacePropertiesHashMap: dict = None
        self.value: str = None
    

    def __init__(self, nameSpace: str, value: str) -> None:
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        self._init_fields()
        self.nameSpaceVector = BasicArrayListD()
        self.nameSpacePropertiesHashMap = StdUtil.getInstance().createHashMap()
        self.value = value
        beginIndex: int = nameSpace.find(NameSpaceRequestParamData.NAME)
        if beginIndex < 0:
            raise Exception("Not a NameSpaceRequest")
        packages: str = nameSpace[beginIndex + NameSpaceRequestParamData.NAME.length() + NameSpaceRequestParamData.SEP.length():]
        sepTokenizer: Tokenizer = Tokenizer(NameSpaceRequestParamData.SEP)
        nameSpaceWithPropertiesVector: BasicArrayList = sepTokenizer.getTokensFromString(packages, BasicArrayListD())
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
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
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                self.logUtil.putF("\nPackageName and PackageName Properties Tokens: " + str(nameSpaceAndPropertiesVector), self, "NameSpaceRequestParam()")
            if nameSpaceAndPropertiesVector.size() > 0:
                packageName: str = nameSpaceAndPropertiesVector.get(0)
                if packageName is None:
                    raise Exception("Package Name Is Null")
                self.nameSpaceVector.add(packageName)
                if nameSpaceAndPropertiesVector.size() > 1:
                    properties: str = nameSpaceAndPropertiesVector.get(1)
                    packagePropertiesHashMap: dict = self.generatePackagePropertiesHashMap(properties)
                    self.nameSpacePropertiesHashMap.put(str(packageIndex), packagePropertiesHashMap)
                packageIndex += 1
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("NameSpace: " + str(self.nameSpaceVector), self, "NameSpaceRequestParam()")
    

    def getPackages(self) -> BasicArrayList:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("NameSpace: " + str(self.nameSpaceVector), self, "getPackages()")
        return self.nameSpaceVector
    

    def getPackageProperties(self, packageIndex: int) -> dict:
        packagePropertiesHashMap: dict = self.nameSpacePropertiesHashMap.get(str(packageIndex))
        if packagePropertiesHashMap is None:
            packagePropertiesHashMap = StdUtil.getInstance().createHashMap()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("Package Properties: " + str(packagePropertiesHashMap), self, "getPackagesProperties()")
        return packagePropertiesHashMap
    

    def getValue(self) -> str:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("\nValue: " + self.value, self, "getValue()")
        return self.value
    

    # throws Exception
    def generatePackagePropertiesHashMap(self, properties: str) -> dict:
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        propertiesTokenizer: Tokenizer = Tokenizer(NameSpaceRequestParamData.PROPERTIESSEPARATOR)
        packagePropertiesHashMap: dict = StdUtil.getInstance().createHashMap()
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
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                        self.logUtil.putF("\nProperty Name: " + propertyName + "\nProperty Value: " + propertyValue, self, "generatePackagePropertiesHashMap()")
                    packagePropertiesHashMap.put(propertyName, propertyValue)
                else:
                    packagePropertiesHashMap.put(propertyName, StringUtil.getInstance().EMPTY_STRING)
        return packagePropertiesHashMap
# from java.util.HashMap import HashMap
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
from org.allbinary.logic.visual.dhtml.html.name.HtmlNameMathData import HtmlNameMathData
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


