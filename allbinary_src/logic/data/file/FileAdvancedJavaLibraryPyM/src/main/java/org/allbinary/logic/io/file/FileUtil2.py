# 
# AllBinary Open License Version 1 
# Copyright (c) 2022 AllBinary 
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
# package org.allbinary.logic.io.file

from __future__ import annotations



class FileUtil2:
    instance: FileUtil2 = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.streamUtil: StreamUtil = StreamUtil.getInstance()
    

    @staticmethod
    def getInstance() -> FileUtil2:
        return FileUtil2.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def loadFileAsList(self, file: AbFile, max: int, byteArray1: list[int]) -> BasicArrayList:
        from org.allbinary.logic.io.file.SimpleFileUtil import SimpleFileUtil
        inputStream: AbFileInputStream = None
        try:
            inputStream = AbFileInputStream(file)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.ADD, e)
        return SimpleFileUtil.getInstance().loadFileAsList(inputStream, max, byteArray1)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


FileUtil2.instance = FileUtil2()

