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
# package org.allbinary.logic.communication.log.config.type

from __future__ import annotations

import threading
from org.allbinary.util.BasicArrayListD import BasicArrayListD


class LogConfigTypes:
    JSP_ERROR_NO_FUNCTION: str = "in JSP Not In Function"
    LOGGING: BasicArrayList = BasicArrayListD()
    _lock = threading.RLock()
    

    @staticmethod
    def _static_init() -> None:
        LogConfigTypes.init()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def init() -> None:
        with LogConfigTypes._lock:
            return LogConfigTypes._init_unlocked()

    @staticmethod
    def _init_unlocked() -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        try:
            PreLogUtil.put("Initialize LogconfigTypes", "LogConfigTypes", "init()")
            LogConfigTypeFactory.getInstance()
            loggingInitInfo: LoggingInitInfo = LoggingInitInfo()
            logConfigTypeVector: BasicArrayList = loggingInitInfo.getTypeList()
            PreLogUtil.put("Number Of Log Configs: " + str(loggingInitInfo.getNumberOfLogConfigs()), "LogConfigTypes", "init()")
            PreLogUtil.put("Number Of Log Config Type Names: " + str(logConfigTypeVector.size()), "LogConfigTypes", "init()")
            LogConfigTypes.LOGGING.addAllList(logConfigTypeVector)
            LogConfigTypes.LOGGING.add(LogConfigTypeFactory.getInstance().NETBEANS_MODULE)
        except Exception as e:
            PreLogUtil.putSE("Unable to initialize LogConfigTypes", "LogConfigTypes", "init()", e)
    

    # throws Exception
    @staticmethod
    def getInstance(node: Node) -> LogConfigType:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeData import LogConfigTypeData
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeData import LogConfigTypeData
        from org.allbinary.logic.communication.log.config.type.LogConfigType import LogConfigType
        nameValueNode: Node = DomSearchHelper.getNode(LogConfigTypeData.getInstance().NAME, node.getChildNodes())
        name: str = DomNodeHelper.getTextNodeValue(nameValueNode)
        descriptionValueNode: Node = DomSearchHelper.getNodeNoThrow(LogConfigTypeData.getInstance().DESCRIPTION, node.getChildNodes())
        if descriptionValueNode is not None:
            description: str = DomNodeHelper.getTextNodeValue(descriptionValueNode)
        availableLogConfigTypes: BasicArrayList = LogConfigType.availableLogConfigTypes
        size: int = availableLogConfigTypes.size()
        logConfigType: LogConfigType = None
        for index in range(0, size):
            logConfigType = availableLogConfigTypes.get(index)
            if logConfigType.getName().compareTo(name) == 0:
                return logConfigType
        raise Exception("No Such LogConfigType: " + name)
from org.allbinary.data.tree.dom.DomNodeHelper import DomNodeHelper
from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.communication.log.config.LoggingInitInfo import LoggingInitInfo
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.w3c.dom.Node import Node


LogConfigTypes._static_init()

