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



class TransformInfoPropertiesFactory:
    instance: TransformInfoPropertiesFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> TransformInfoPropertiesFactory:
        return TransformInfoPropertiesFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, node: Node) -> TransformInfoProperties:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        from org.allbinary.logic.visual.transform.info.TransformInfoProperties import TransformInfoProperties
        transformInfoChildNodeList: NodeList = node.getChildNodes()
        transformInfoData: TransformInfoData = TransformInfoData.getInstance()
        attributes: NamedNodeMap = node.getAttributes()
        attrNode: Attr = attributes.getNamedItem(transformInfoData.NAME)
        name: str = attrNode.getValue()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF(str(CommonLabels.getInstance().NEXT) + " View Name: " + name, self, "toTransformInfoPropertiesHashMap()")
        labelNode: Node = DomSearchHelper.getNodeNoThrow(transformInfoData.LABEL, transformInfoChildNodeList)
        label: str = DomNodeHelper.getTextNodesValue(labelNode)
        if label is None:
            label = name
        descriptionNode: Node = DomSearchHelper.getNode(transformInfoData.DESCRIPTION, transformInfoChildNodeList)
        description: str = DomNodeHelper.getTextNodesValue(descriptionNode)
        objectFileNode: Node = DomSearchHelper.getNode(transformInfoData.OBJECTFILENAME, transformInfoChildNodeList)
        objectFileName: str = DomNodeHelper.getTextNodeValue(objectFileNode)
        objectConfigFileNode: Node = DomSearchHelper.getNode(transformInfoData.OBJECTCONFIGFILENAME, transformInfoChildNodeList)
        objectConfigFileName: str = DomNodeHelper.getTextNodeValue(objectConfigFileNode)
        templateFileNode: Node = DomSearchHelper.getNode(transformInfoData.TEMPLATEFILENAME, transformInfoChildNodeList)
        templateFileName: str = DomNodeHelper.getTextNodeValue(templateFileNode)
        transformInfoProperties: TransformInfoProperties = TransformInfoProperties(name, label, description, objectFileName, objectConfigFileName, templateFileName)
        return transformInfoProperties
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.w3c.dom.Attr import Attr
from org.w3c.dom.NamedNodeMap import NamedNodeMap
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


TransformInfoPropertiesFactory.instance = TransformInfoPropertiesFactory()

