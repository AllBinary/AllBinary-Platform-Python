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

import threading
from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS


class LoggingInitInfo:
    INITFILENAME: str = "logConfig.xml"
    PACKAGE: str = self.PATH_GLOBALS.getInstance().INIT_PATH
    logConfigInfoList: BasicArrayList = None
    hasRead: bool = False
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getDoc() -> Document:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._getDoc_unlocked()

    @staticmethod
    def _getDoc_unlocked() -> Document:
        path: str = self.URLGLOBALS.getWebappPath() + LoggingInitInfo.PACKAGE
        FILEABPATH: AbPath = AbPath(path, LoggingInitInfo.INITFILENAME)
        file: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
        document: Document = DomDocumentHelper.create(AbFileLocalInputStream(file))
        return document
    

    # throws Exception
    @staticmethod
    def write() -> None:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._write_unlocked()

    @staticmethod
    def _write_unlocked() -> None:
        try:
            LoggingInitInfo.hasRead = False
        except Exception as e:
            raise e
    

    # throws Exception
    @staticmethod
    def read() -> None:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._read_unlocked()

    @staticmethod
    def _read_unlocked() -> None:
        from org.allbinary.logic.communication.log.config.LogConfigsData import LogConfigsData
        from org.allbinary.logic.communication.log.config.LogConfigData import LogConfigData
        from org.allbinary.logic.communication.log.config.LogConfig import LogConfig
        try:
            document: Document = LoggingInitInfo.getDoc()
            logConfigsNodeList: NodeList = document.getElementsByTagName(LogConfigsData.getInstance().NAME)
            logConfigsNode: Node = logConfigsNodeList.item(0)
            logConfigNodeVector: BasicArrayList = DomSearchHelper.getAllNodes(LogConfigData.getInstance().NAME, logConfigsNode.getChildNodes())
            LoggingInitInfo.logConfigInfoList = BasicArrayListD()
            size: int = logConfigNodeVector.size()
            for i in range(0, size):
                node: Node = logConfigNodeVector.get(i)
                logConfigInfo: LogConfig = LogConfig(node)
                LoggingInitInfo.logConfigInfoList.add(logConfigInfo)
        except Exception as e:
            raise e
    

    @staticmethod
    def setHasRead(value: bool) -> None:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._setHasRead_unlocked(value)

    @staticmethod
    def _setHasRead_unlocked(value: bool) -> None:
        LoggingInitInfo.hasRead = value
    

    # throws Exception
    @staticmethod
    def updateIfNeeded() -> None:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._updateIfNeeded_unlocked()

    @staticmethod
    def _updateIfNeeded_unlocked() -> None:
        if not LoggingInitInfo.hasRead:
            LoggingInitInfo.read()
            LoggingInitInfo.hasRead = True
            if LoggingInitInfo.logConfigInfoList is None:
                raise Exception("Read Failed")
    

    def isValid(self) -> bool:
        try:
            return True
        except Exception as e:
            return False
    

    @staticmethod
    def set(logConfigInfoVector: BasicArrayList) -> None:
        with LoggingInitInfo._lock:
            return LoggingInitInfo._set_unlocked(logConfigInfoVector)

    @staticmethod
    def _set_unlocked(logConfigInfoVector: BasicArrayList) -> None:
        LoggingInitInfo.logConfigInfoList = logConfigInfoVector
    

    # throws Exception
    @staticmethod
    def get() -> BasicArrayList:
        LoggingInitInfo.updateIfNeeded()
        return LoggingInitInfo.logConfigInfoList
    

    # throws Exception
    @staticmethod
    def getTypeNameList() -> BasicArrayList:
        LoggingInitInfo.updateIfNeeded()
        allLogTypeVector: BasicArrayList = BasicArrayListD()
        size: int = LoggingInitInfo.logConfigInfoList.size()
        for index in range(0, size):
            logConfigInfo: LogConfig = LoggingInitInfo.logConfigInfoList.objectArray[index]
            logTypeVector: BasicArrayList = logConfigInfo.getTypeVector()
            if logConfigInfo.isEnabled():
                allLogTypeVector.addAllList(logTypeVector)
        return allLogTypeVector
    

    # throws Exception
    @staticmethod
    def getTypeList() -> BasicArrayList:
        LoggingInitInfo.updateIfNeeded()
        allLogTypeVector: BasicArrayList = BasicArrayListD()
        size: int = LoggingInitInfo.logConfigInfoList.size()
        for index in range(0, size):
            logConfigInfo: LogConfig = LoggingInitInfo.logConfigInfoList.objectArray[index]
            logTypeVector: BasicArrayList = logConfigInfo.getTypeVector()
            if logConfigInfo.isEnabled():
                allLogTypeVector.addAllList(logTypeVector)
        return allLogTypeVector
    

    # throws Exception
    def getNumberOfLogConfigs(self) -> int:
        return LoggingInitInfo.logConfigInfoList.size()
    

    def toString(self) -> str:
        try:
            document: Document = LoggingInitInfo.getDoc()
            return XmlDocumentHelper.toString(document)
        except Exception as e:
            return "Error"

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.data.tree.dom.document.DomDocumentHelper import DomDocumentHelper
from org.allbinary.data.tree.dom.document.XmlDocumentHelper import XmlDocumentHelper
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.io.AbFileLocalInputStream import AbFileLocalInputStream
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node
from org.w3c.dom.NodeList import NodeList


