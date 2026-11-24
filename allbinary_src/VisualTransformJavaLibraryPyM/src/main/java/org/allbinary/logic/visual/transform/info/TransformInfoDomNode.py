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
# package org.allbinary.logic.visual.transform.info

from __future__ import annotations



class TransformInfoDomNode:

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.transformInfoInterface: TransformInfoInterface = None
        self.mappedName: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.__jconstructor1(*args)
        elif len(args) == 2:
            self.__jconstructor2(*args)

    def __jconstructor1(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)):
            self._constructor1_1(*args)
        else:
            self._constructor1_2(*args)

    def __jconstructor2(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)) and (args[1] is None or isinstance(args[1], str)):
            self._constructor2_1(*args)
        else:
            self._constructor2_2(*args)
    

    def _constructor1_1(self, node: Node) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
        from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.w3c.dom.Attr import Attr
        from org.w3c.dom.NamedNodeMap import NamedNodeMap
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        self._init_fields()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Constructing TransformInfo From TransformInfoDomNode: " + str(node.getNodeName()), self, "TransformInfoDomNode(Node node)")
        transformInfoData: TransformInfoData = TransformInfoData.getInstance()
        attributes: NamedNodeMap = node.getAttributes()
        attrNode: Attr = attributes.getNamedItem(transformInfoData.NAME)
        name: str = attrNode.getValue()
        nodeList: NodeList = node.getChildNodes()
        if nodeList.getLength() > 1:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Constructing Complete TransformInfo Node For: ")
                stringBuffer.append(name)
                stringBuffer.append(" with ")
                stringBuffer.appendint(int(nodeList.getLength()))
                stringBuffer.append(" children")
                self.logUtil.putF(str(stringBuffer), self, "TransformInfoObjectConfigComponent(Node node)")
            objectFileNameNode: Node = DomSearchHelper.getNode(transformInfoData.OBJECTFILENAME, nodeList)
            objectFileName: str = DomNodeHelper.getTextNodeValue(objectFileNameNode)
            objectConfigFileNameNode: Node = DomSearchHelper.getNode(transformInfoData.OBJECTCONFIGFILENAME, nodeList)
            objectConfigFileName: str = DomNodeHelper.getTextNodeValue(objectConfigFileNameNode)
            templateFileNameNode: Node = DomSearchHelper.getNode(transformInfoData.TEMPLATEFILENAME, nodeList)
            templateFileName: str = DomNodeHelper.getTextNodeValue(templateFileNameNode)
            dataFileNameNode: Node = DomSearchHelper.getNode(transformInfoData.DATAFILENAME, nodeList)
            dataFileName: str = DomNodeHelper.getTextNodeValue(dataFileNameNode)
            self.transformInfoInterface = TransformInfo(name, objectFileName, objectConfigFileName, templateFileName, dataFileName)
        else:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Constructing Partial TransformInfo Node For: ")
                stringBuffer.append(name)
                stringBuffer.append(" with ")
                stringBuffer.appendint(int(nodeList.getLength()))
                stringBuffer.append(" children")
                self.logUtil.putF(str(stringBuffer), self, "TransformInfoObjectConfigComponent(Node node)")
            self.transformInfoInterface = TransformInfo(name)
        templateAttrNode: Attr = attributes.getNamedItem(transformInfoData.MAPPED)
        if templateAttrNode is not None:
            self.mappedName = templateAttrNode.getValue()
        else:
            self.mappedName = self.getTransformInfoInterface().getName()
    

    def _constructor1_2(self, transformInfoInterface: TransformInfoInterface) -> None:
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
        self.mappedName = transformInfoInterface.getName()
    

    def _constructor2_1(self, transformInfoInterface: TransformInfoInterface, mappedName: str) -> None:
        self._init_fields()
        self.transformInfoInterface = transformInfoInterface
        self.mappedName = mappedName
    

    def _constructor2_2(self, name: str, mappedName: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
        self._init_fields()
        self.transformInfoInterface = TransformInfo(name)
        self.mappedName = mappedName
    

    def getTransformInfoInterface(self) -> TransformInfoInterface:
        return self.transformInfoInterface
    

    def getMappedName(self) -> str:
        return self.mappedName
    

    def getReplaceKey(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("<transform:component name=\"")
        stringBuffer.append("body")
        stringBuffer.append("\"/>")
        key: str = str(stringBuffer)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Component Key: " + key, self, "getReplaceKey()")
        return key
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.w3c.dom.Attr import Attr
# from org.w3c.dom.NamedNodeMap import NamedNodeMap
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


