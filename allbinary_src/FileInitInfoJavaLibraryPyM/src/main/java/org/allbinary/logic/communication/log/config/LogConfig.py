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
# package org.allbinary.logic.communication.log.config

from __future__ import annotations



class LogConfig:

    def _init_fields(self) -> None:
        self.isEnabled: bool = None
        self.name: str = None
        self.description: str = None
        self.path: str = None
        self.fileName: str = None

    def __init__(self, *args) -> None:
        if len(args) == 4:
            self._constructor4(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor4(self, aName: str, aDescription: str, aPath: str, aFileName: str) -> None:
        self._init_fields()
        self.isEnabled = False
        self.name = aName
        self.description = aDescription
        self.path = aPath
        self.fileName = aFileName
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.logic.communication.log.config.LogConfigData import LogConfigData
        self._init_fields()
        enabledValueNode: Node = DomSearchHelper.getNode(EntryData.getInstance().ENABLE, node.getChildNodes())
        isEnabledString: str = DomNodeHelper.getTextNodeValue(enabledValueNode)
        self.isEnabled = BooleanUtil.getInstance().getFromString(isEnabledString)
        logConfigData: LogConfigData = LogConfigData.getInstance()
        nameValueNode: Node = DomSearchHelper.getNode(logConfigData.NAME, node.getChildNodes())
        self.name = DomNodeHelper.getTextNodeValue(nameValueNode)
        descriptionValueNode: Node = DomSearchHelper.getNode(logConfigData.DESCRIPTION, node.getChildNodes())
        self.description = DomNodeHelper.getTextNodeValue(descriptionValueNode)
        fileValueNode: Node = DomSearchHelper.getNode(logConfigData.FILE, node.getChildNodes())
        self.fileName = DomNodeHelper.getTextNodeValue(fileValueNode)
    

    def getName(self) -> str:
        return self.name
    

    def isEnabled(self) -> bool:
        return self.isEnabled
    

    def enable(self) -> None:
        self.isEnabled = True
    

    def disable(self) -> None:
        self.isEnabled = False
    

    def getDescription(self) -> str:
        return self.description
    

    def getFileName(self) -> str:
        return self.fileName
    

    def setName(self, value: str) -> None:
        self.name = value
    

    def setDescription(self, value: str) -> None:
        self.description = value
    

    def setPath(self, value: str) -> None:
        self.path = value
    

    def setFileName(self, value: str) -> None:
        self.fileName = value
    

    # throws Exception
    def getDoc(self) -> Document:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.URLGLOBALS.getWebappPath())
        stringBuffer.append(self.PATH_GLOBALS.getInstance().INIT_PATH)
        stringBuffer.append(self.getFileName())
        file: AbFile = AbFile.createAbFile(str(stringBuffer))
        document: Document = DomDocumentHelper.create(AbFileLocalInputStream(file))
        return document
    

    # throws Exception
    def getTypeVector(self) -> BasicArrayList:
        logKeyVector: BasicArrayList = BasicArrayListD()
        document: Document = self.getDoc()
        logConfigTypesNodeList: NodeList = document.getElementsByTagName(LogConfigTypesData.getInstance().NAME)
        logConfigTypesNode: Node = logConfigTypesNodeList.item(0)
        logConfigTypeNodeVector: BasicArrayList = DomSearchHelper.getAllNodes(LogConfigTypeData.getInstance().NAME, logConfigTypesNode.getChildNodes())
        size: int = logConfigTypeNodeVector.size()
        for i in range(0, size):
            node: Node = logConfigTypeNodeVector.get(i)
            logType: LogConfigType = LogConfigTypes.getInstance(node)
            logKeyVector.add(logType)
        return logKeyVector
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.log.config.type.LogConfigType import LogConfigType
from org.allbinary.logic.communication.log.config.type.LogConfigTypeData import LogConfigTypeData
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.communication.log.config.type.LogConfigTypesData import LogConfigTypesData
from org.allbinary.logic.io.AbFileLocalInputStream import AbFileLocalInputStream
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


