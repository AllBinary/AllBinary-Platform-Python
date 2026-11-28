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
        if "transformInfoInterface" not in vars(self): self.transformInfoInterface: TransformInfoInterface = None
        if "mappedName" not in vars(self): self.mappedName: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)
        elif len(args) == 2:
            __class__.__jconstructor2(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "Node" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)

    def __jconstructor2(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[0]).__mro__)) and (args[1] is None or isinstance(args[1], str)):
            __class__._constructor2_1(self, *args)
        else:
            __class__._constructor2_2(self, *args)
    

    def _constructor1_1(self, node: Node) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
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
        __class__._init_fields(self)
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
        __class__._init_fields(self)
        self.transformInfoInterface = transformInfoInterface
        self.mappedName = transformInfoInterface.getName()
    

    def _constructor2_1(self, transformInfoInterface: TransformInfoInterface, mappedName: str) -> None:
        __class__._init_fields(self)
        self.transformInfoInterface = transformInfoInterface
        self.mappedName = mappedName
    

    def _constructor2_2(self, name: str, mappedName: str) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfo import TransformInfo
        __class__._init_fields(self)
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


