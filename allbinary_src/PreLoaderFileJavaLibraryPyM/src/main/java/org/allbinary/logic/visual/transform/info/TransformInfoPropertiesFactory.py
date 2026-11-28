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

from java.lang.JavaRuntimeStatic import lazy_static


class TransformInfoPropertiesFactory:
    instance: TransformInfoPropertiesFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> TransformInfoPropertiesFactory:
        return TransformInfoPropertiesFactory.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def getInstance_j1(self, node: Node) -> TransformInfoProperties:
        from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
        from org.allbinary.logic.visual.transform.info.TransformInfoProperties import TransformInfoProperties
        from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.string.CommonLabels import CommonLabels
        from org.w3c.dom.Attr import Attr
        from org.w3c.dom.NamedNodeMap import NamedNodeMap
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        transformInfoChildNodeList: NodeList = node.getChildNodes()
        transformInfoData: TransformInfoData = TransformInfoData.getInstance()
        attributes: NamedNodeMap = node.getAttributes()
        attrNode: Attr = attributes.getNamedItem(transformInfoData.NAME)
        name: str = attrNode.getValue()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
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

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.w3c.dom.Attr import Attr
# from org.w3c.dom.NamedNodeMap import NamedNodeMap
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _TransformInfoPropertiesFactory_instance() -> object:
    return TransformInfoPropertiesFactory()

lazy_static(TransformInfoPropertiesFactory, "instance", _TransformInfoPropertiesFactory_instance)

