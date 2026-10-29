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
# package org.allbinary.logic.visual.transform.info.dom

from __future__ import annotations



class TransformInfoPropertiesDocument:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.document: Document = None
    

    def __init__(self, filePath: str) -> None:
        self._init_fields()
        xmlFile: AbFile = AbFile.createAbFile(filePath)
        self.document = DomDocumentFileHelper.createDocument(xmlFile)
    

    def toTransformInfoPropertiesHashMap(self) -> dict:
        try:
            transformInfoPropertiesHashMap: dict = StdUtil.getInstance().createHashMap()
            transformInfosNode: Node = self.document.getElementsByTagName(TransformInfosData.getInstance().NAME).item(0)
            transformInfosChildNodeList: NodeList = transformInfosNode.getChildNodes()
            transformInfoNodeVector: BasicArrayList = DomSearchHelper.getAllNodes(TransformInfoData.getInstance().NAME, transformInfosChildNodeList)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Size: " + str(transformInfoNodeVector.size()), self, "toTransformInfoPropertiesHashMap()")
            size: int = transformInfoNodeVector.size()
            node: Node = None
            transformInfoProperties: TransformInfoProperties = None
            for index in range(0, size):
                node = transformInfoNodeVector.get(index)
                transformInfoProperties = TransformInfoPropertiesFactory.getInstance().getInstance(node)
                transformInfoPropertiesHashMap.put(transformInfoProperties.getName(), transformInfoProperties)
            return transformInfoPropertiesHashMap
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "toTransformInfoPropertiesHashMap()", e)
            return None
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.document.DomDocumentFileHelper import DomDocumentFileHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from org.allbinary.logic.visual.transform.info.TransformInfoProperties import TransformInfoProperties
from org.allbinary.logic.visual.transform.info.TransformInfoPropertiesFactory import TransformInfoPropertiesFactory
from org.allbinary.logic.visual.transform.info.TransformInfosData import TransformInfosData
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


