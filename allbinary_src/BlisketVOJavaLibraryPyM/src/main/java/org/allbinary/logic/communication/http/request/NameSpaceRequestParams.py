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

from org.allbinary.logic.communication.http.request.RequestParams import RequestParams


#containing string values and other hashmaps of the like
class NameSpaceRequestParams(RequestParams):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        super().__init__()
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("Constructing empty", self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor1(self, httpServletRequest: HttpServletRequest) -> None:
        super().__init__(httpServletRequest)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("Constructing from HttpServletRequest", self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor1(self, pageContext: PageContext) -> None:
        super().__init__(pageContext)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("Constructing from PageContext", self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def createPackageNode(self, document: Document, packageName: str, packagePropertiesHashMap: dict) -> Node:
        node: Node = document.createElement(packageName)
        propertyKeySet: Set = packagePropertiesHashMap.keySet()
        propertyKeySetArray: list[object] = propertyKeySet.toArray()
        size: int = len(propertyKeySetArray)
        for index in range(0, size):
            propertyName: str = propertyKeySetArray[index]
            propertyValue: str = packagePropertiesHashMap.get(propertyName)
            propertyNode: Node = ModDomHelper.createTextNode(document, propertyName, propertyValue)
            node.appendChild(propertyNode)
        return node
    

    # throws Exception
    def createPackageMultiNode(self, document: Document, nameSpaceRequestParam: NameSpaceRequestParam, packageName: str, packagePropertiesHashMap: dict) -> Node:
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        beginIndex: int = packageName.find('[')
        indexValue: str = packageName[beginIndex + 1:len(packageName) - 1]
        multiElementPackage: str = packageName[0:beginIndex]
        selectedValue: str = nameSpaceRequestParam.getValue()
        propertyValue: str = packagePropertiesHashMap.get(DomData.VALUE)
        if ((propertyValue > NameSpaceRequestParamData.VALUE) - (propertyValue < NameSpaceRequestParamData.VALUE)) != 0:
            selectedValue = propertyValue
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("\nAppending Multinode Element: " + multiElementPackage + "[" + indexValue + "] " + selectedValue, self, "createPackageMultiNode")
        nextNode: Node = ModDomHelper.createNameValueNodes(document, multiElementPackage, selectedValue)
        indexNode: Node = ModDomHelper.createTextNode(document, DomData.INDEX, indexValue)
        nextNode.appendChild(indexNode)
        return nextNode
    

    # throws Exception
    def getRootNode(self, rootElementPackage: str, packagePropertiesHashMap: dict, document: Document) -> Node:
        rootNode: Node = DomSearchHelper.getNodeNoThrow(rootElementPackage, document.getChildNodes())
        if rootNode is None:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                self.logUtil.putF("\nAppending Document Root: " + "\nElementName: " + rootElementPackage + "\nProperties: " + str(packagePropertiesHashMap), self, "getRootNode")
            node: Node = self.createPackageNode(document, rootElementPackage, packagePropertiesHashMap)
            document.appendChild(node)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                self.logUtil.putF("\nAppended Document Created: " + XmlDocumentHelper.toString(document), self, "getRootNode")
            return node
        else:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                self.logUtil.putF("\nUsing Existing Root Node", self, "getRootNode")
            return rootNode
    

    # throws Exception
    def addNewProperties(self, document: Document, node: Node, nextPackagePropertiesHashMap: dict) -> Node:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF(str(StringMaker().append("\nAdding Any New Properties: ").append(str(nextPackagePropertiesHashMap)).append("\nto node: ").append(node.getNodeName())), self, "addNewProperties")
        propertyNameSet: Set = nextPackagePropertiesHashMap.keySet()
        propertyNameSetArray: list[object] = propertyNameSet.toArray()
        size: int = len(propertyNameSetArray)
        for index in range(0, size):
            nextPropertyName: str = propertyNameSetArray[index]
            propertyValue: str = StringUtil.getInstance().getNonNull(nextPackagePropertiesHashMap.get(nextPropertyName))
            valueNode: Node = DomSearchHelper.getNodeNoThrow(nextPropertyName, node.getChildNodes())
            if valueNode is not None:
                existingElementNodeTextNodeValue: str = DomNodeHelper.getTextNodeValue(valueNode)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("\nIf property: \"" + nextPropertyName + " is the same as:\n" + "Node: " + str(node.getNodeName()) + " then: " + propertyValue + "==" + existingElementNodeTextNodeValue, self, "addNewProperties")
                if ((propertyValue > existingElementNodeTextNodeValue) - (propertyValue < existingElementNodeTextNodeValue)) != 0:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                        self.logUtil.putF("At least one Property from NameSpaceRequest Package was different from Node", self, "addNewProperties")
                    raise Exception("Property Modifications Should Not Occur")
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("Adding a new Property: " + nextPropertyName + "=" + propertyValue, self, "addNewProperties")
                newPropertyNode: Node = ModDomHelper.createTextNode(document, nextPropertyName, propertyValue)
                node.appendChild(newPropertyNode)
        return node
    

    # throws Exception
    def isElementValueTextNodeEqual(self, nextPackagePropertiesHashMap: dict, node: Node) -> bool:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("\nComparing the value property in: " + str(nextPackagePropertiesHashMap) + "\nto node child leaves of node: " + str(node.getNodeName()), self, "isElementValueTextNodeEqual")
        propertyValue: str = nextPackagePropertiesHashMap.get(DomData.VALUE)
        valueNode: Node = DomSearchHelper.getNodeNoThrow(DomData.VALUE, node.getChildNodes())
        if valueNode is not None:
            existingElementNodeTextNodeValue: str = DomNodeHelper.getTextNodeValue(valueNode)
            if ((propertyValue > existingElementNodeTextNodeValue) - (propertyValue < existingElementNodeTextNodeValue)) == 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("Value Node is the same", self, "isElementValueTextNodeEqual")
                return True
        else:
            return True
        return False
    

    # throws Exception
    def isElementValueTextNodeUnique(self, nextPackagePropertiesHashMap: dict, elementNodeVector: BasicArrayList) -> int:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("\nComparing Properties of: " + str(elementNodeVector.size()) + " Nodes", self, "isElementValueTextNodeUnique")
        size: int = elementNodeVector.size()
        for index in range(0, size):
            existingElementNode: Node = elementNodeVector.get(index)
            if self.isElementValueTextNodeEqual(nextPackagePropertiesHashMap, existingElementNode):
                return index
        return -1
    

    # throws Exception
    def addChildren(self, document: Document, rootNode: Node, nameSpaceRequestParam: NameSpaceRequestParam) -> Document:
        node: Node = rootNode
        packageVector: BasicArrayList = nameSpaceRequestParam.getPackages()
        size: int = packageVector.size()
        for index in range(1, size):
            nextPackageName: str = packageVector.get(index)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                self.logUtil.putF(str(StringMaker().append("\nTrying to Add Child to Node: ").append(node.getNodeName()).append("\nwith new PackageName: ").append(nextPackageName)), self, "addChildren")
            nextPackagePropertiesHashMap: dict = nameSpaceRequestParam.getPackageProperties(index)
            elementNodeVector: BasicArrayList = DomSearchHelper.getAllNodesNoThrow(nextPackageName, node.getChildNodes())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                self.logUtil.putF("\nDocument Contains " + str(elementNodeVector.size()) + " Node(s) With Same Name", self, "addChildren")
            isElementValueTextNodeUniqueIndex: int = self.isElementValueTextNodeUnique(nextPackagePropertiesHashMap, elementNodeVector)
            if (elementNodeVector.size() == 0 or isElementValueTextNodeUniqueIndex == -1) and not nextPackageName.endswith(CommonSeps.getInstance().BRACKET_CLOSE):
                nextNode: Node = self.createPackageNode(document, nextPackageName, nextPackagePropertiesHashMap)
                node.appendChild(nextNode)
                node = nextNode
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("\nAppended Package: " + str(node.getNodeName()), self, "addChildren")
                    self.logUtil.putF("\nAppended Document Created: " + XmlDocumentHelper.toString(document), self, "addChildren")
            elif nextPackageName.endswith(CommonSeps.getInstance().BRACKET_CLOSE):
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("Package is MultiNode: just append", self, "addChildren")
                nextNode: Node = self.createPackageMultiNode(document, nameSpaceRequestParam, nextPackageName, nextPackagePropertiesHashMap)
                node.appendChild(nextNode)
                node = nextNode
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("\nAppended Multinode Element: " + XmlDocumentHelper.toString(document), self, "addChildren")
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("Value Node already exists: Now compare (properties to leaf nodes)", self, "addChildren")
                nodeNameDuplicateNode: Node = elementNodeVector.get(isElementValueTextNodeUniqueIndex)
                node = self.addNewProperties(document, nodeNameDuplicateNode, nextPackagePropertiesHashMap)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("\nDuplicate Node Found: Moving to next child ^", self, "addChildre")
        return document
    

    # throws Exception
    def addNameSpace(self, key: str, value: str, document: Document) -> Document:
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParam import NameSpaceRequestParam
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF(str(StringMaker().append("NameSpace key: ").append(key).append(" Value: ").append(value)), self, "addNameSpace")
        nameSpaceRequestParam: NameSpaceRequestParam = NameSpaceRequestParam(key, value)
        packageVector: BasicArrayList = nameSpaceRequestParam.getPackages()
        size: int = packageVector.size()
        for index in range(0, size):
            packageName: str = packageVector.get(index)
            packagePropertiesHashMap: dict = nameSpaceRequestParam.getPackageProperties(packageVector.indexOf(packageName))
            rootNode: Node = self.getRootNode(packageName, packagePropertiesHashMap, document)
            if index < size - 1:
                return self.addChildren(document, rootNode, nameSpaceRequestParam)
        return document
    

    # throws Exception
    def toHashMap(self) -> dict:
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        from org.allbinary.logic.communication.http.request.NameSpaceRequestParamData import NameSpaceRequestParamData
        document: Document = DomDocumentHelper.create()
        hashMap: dict = StdUtil.getInstance().createHashMap()
        keys: Set = self.getMap().keySet()
        keyArray: list[object] = keys.toArray()
        keySize: int = len(keyArray)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("NameSpace Request Size: " + str(keys.size()), self, "toHashMap")
        for i in range(0, keySize):
            key: str = keyArray[i]
            anyType: object = self.getMap().get(key)
            className: str = type(anyType).__module__ + "." + type(anyType).__qualname__
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                self.logUtil.putF("Request Param Class: " + className, self, "toHashMap")
            if isinstance(self.getMap().get(key), str):
                value: str = self.getMap().get(key)
                if key.find(NameSpaceRequestParamData.NAME) < 0:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                        self.logUtil.putF("Not NameSpace key: " + key + " Value: " + value, self, "toHashMap()")
                    hashMap.put(str(key), str(value))
                else:
                    document = self.addNameSpace(str(key), str(value), document)
            elif isinstance(self.getMap().get(key), list):
                values: list[str] = self.getMap().get(key)
                if key.find(NameSpaceRequestParamData.NAME) < 0:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                        self.logUtil.putF("Not NameSpace key: " + key + " Value: " + str(values[0]), self, "toHashMap()")
                    hashMap.put(str(key), str(values[0]))
                else:
                    document = self.addNameSpace(str(key), str(values[0]), document)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            self.logUtil.putF("NameSpaceRequestParams: " + str(self.getMap()) + "\ntoHashMap(): " + str(hashMap) + "\nDocument Created: " + XmlDocumentHelper.toString(document), self, "toHashMap()")
        hashMap.put(NameSpaceRequestParamData.DOCUMENT, document)
        return hashMap
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.data.tree.dom.DomData import DomData
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


