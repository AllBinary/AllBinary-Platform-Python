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

from java.lang.JavaRuntimeStatic import lazy_static


class FileUtil2:
    instance: FileUtil2 = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.StreamUtil import StreamUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.streamUtil: StreamUtil = StreamUtil.getInstance()
    

    @staticmethod
    def getInstance() -> FileUtil2:
        return FileUtil2.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def loadFileAsList(self, file: AbFile, max: int, byteArray1: list[int]) -> BasicArrayList:
        from org.allbinary.logic.io.file.SimpleFileUtil import SimpleFileUtil
        from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
        from org.allbinary.util.BasicArrayList import BasicArrayList
        inputStream: AbFileInputStream = None
        try:
            inputStream = AbFileInputStream.createFromAbFile(file)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.ADD, e)
        return SimpleFileUtil.getInstance().loadFileAsList(inputStream, max, byteArray1)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
# from org.allbinary.logic.io.StreamUtil import StreamUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList


def _FileUtil2_instance() -> object:
    return FileUtil2()

lazy_static(FileUtil2, "instance", _FileUtil2_instance)

