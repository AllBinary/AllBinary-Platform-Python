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

from org.allbinary.util.BasicArrayListD import BasicArrayListD


class LogConfigType:
    availableLogConfigTypes: BasicArrayList = BasicArrayListD()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.name: str = None
        self.description: str = None
    

    def __init__(self, name: str, description: str) -> None:
        self._init_fields()
        self.name = name
        self.description = description
        LogConfigType.availableLogConfigTypes.add(self)
    

    def getName(self) -> str:
        return self.name
    

    def getDescription(self) -> str:
        return self.description
    

    def setName(self, value: str) -> None:
        self.name = value
    

    def setDescription(self, value: str) -> None:
        self.description = value
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.util.BasicArrayList import BasicArrayList


