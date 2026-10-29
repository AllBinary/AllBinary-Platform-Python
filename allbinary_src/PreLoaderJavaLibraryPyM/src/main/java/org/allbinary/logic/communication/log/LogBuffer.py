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
# package org.allbinary.logic.communication.log

from __future__ import annotations



class LogBuffer:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.logEntryVector: BasicArrayList = None
    

    def __init__(self) -> None:
        self._init_fields()
        self.logEntryVector = BasicArrayListD()
    

    def add(self, log: Log) -> None:
        self.logEntryVector.add(log)
    

    def logAll(self) -> None:
        size: int = self.logEntryVector.size()
        for index in range(0, size):
            log: Log = self.logEntryVector.get(index)
            self.logUtil.putL(log)
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil


