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
# package org.allbinary.data.generator

from __future__ import annotations

import threading
from org.allbinary.data.generator.IdGeneratorInterface import IdGeneratorInterface


class UniqueIdGenerator(IdGeneratorInterface):
    EXT: str = ".unq"
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "idGeneratorEntity" not in vars(self): self.idGeneratorEntity: IdGeneratorEntity = None
        if "name" not in vars(self): self.name: str = None
    

    def __init__(self) -> None:
        from org.allbinary.data.tables.generator.IdGeneratorEntity import IdGeneratorEntity
        from org.allbinary.data.tables.generator.IdGeneratorEntityFactory import IdGeneratorEntityFactory
        __class__._init_fields(self)
        self.idGeneratorEntity = IdGeneratorEntityFactory.getInstance()
    

    def initialize(self, value: int) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            vector: BasicArrayList = BasicArrayListD()
            vector.add(self.name)
            vector.add(str(str(value)))
            self.idGeneratorEntity.insert(vector)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().IDLOGGING):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "initialize", e)
    

    # throws Exception
    def setFile(self, filePathName: str, name: str) -> None:
        with self._lock:
            return __class__.__dict__["_setFile_unlocked"].__get__(self, __class__)(filePathName, name)

    def _setFile_unlocked(self, filePathName: str, name: str) -> None:
        self.name = name
    

    # throws IOException
    def getNext(self) -> str:
        with self._lock:
            return __class__.__dict__["_getNext_unlocked"].__get__(self, __class__)()

    def _getNext_unlocked(self) -> str:
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            idLong: int = self.idGeneratorEntity.get(self.name)
            newValue: int = str(int(idLong) + 1)
            self.idGeneratorEntity.update(self.name, newValue)
            return str(idLong)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().IDLOGGING):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "getNext", e)
            return "Error"
# from java.io.IOException import IOException
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.data.tables.generator.IdGeneratorEntity import IdGeneratorEntity
# from org.allbinary.data.tables.generator.IdGeneratorEntityFactory import IdGeneratorEntityFactory
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


