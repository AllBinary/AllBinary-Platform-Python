# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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


class SimpleFileUtil:
    instance: SimpleFileUtil = None

    def _init_fields(self) -> None:
        from java.io.Reader import Reader
        from java.io.Writer import Writer
        from org.allbinary.logic.NullUtil import NullUtil
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.io.StreamUtil import StreamUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.NULL_WRITER: Writer = SimpleFileUtil.nullWriter()
        self.NULL_READER: Reader = SimpleFileUtil.nullReader()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.nullUtil: NullUtil = NullUtil.getInstance()
        self.streamUtil: StreamUtil = StreamUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> SimpleFileUtil:
        return SimpleFileUtil.instance
    

    @staticmethod
    def nullOutputStream() -> OutputStream:
        from java.io.OutputStream import OutputStream
        from org.allbinary.logic.io.NullOutputStream import NullOutputStream
        return NullOutputStream.NULL_OUTPUT_STREAM
    

    @staticmethod
    def nullWriter() -> Writer:
        from java.io.Writer import Writer
        from org.allbinary.logic.io.NullWriter import NullWriter
        return NullWriter.NULL_WRITER
    

    @staticmethod
    def nullReader() -> Reader:
        from java.io.Reader import Reader
        from org.allbinary.logic.io.NullReader import NullReader
        return NullReader.NULL_READER
    

    def loadFileAsList(self, inputStream: InputStream, max: int, byteArray1: list[int]) -> BasicArrayList:
        from java.io.InputStream import InputStream
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.loadFileAsListReturnLine(inputStream, max, byteArray1, 0)
    

    def loadFileAsListReturnLine(self, inputStream: InputStream, max: int, byteArray1: list[int], includeReturnLine: int) -> BasicArrayList:
        from java.io.InputStream import InputStream
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        stringList: BasicArrayList = BasicArrayListD()
        if inputStream is None:
            return stringList
        byteArray: list[int] = self.nullUtil.NULL_BYTE_ARRAY
        try:
            outputStream2: ByteArrayOutputStream = ByteArrayOutputStream(max)
            byteArray = self.streamUtil.getByteArray(inputStream, outputStream2, byteArray1)
            self.streamUtil.close(inputStream)
        except Exception as e:
            self.streamUtil.close(inputStream)
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.ADD, e)
        if byteArray is None:
            return stringList
        size: int = len(byteArray)
        index: int = 0
        startIndex: int = 0
        returnLine: int = 0
        while index < size:
            startIndex = index
            while index < size - 1 and byteArray[index] != ord('\n'):
                index += 1
            if includeReturnLine == 0:
                if index > 0 and byteArray[index - 1] == ord('\r'):
                    returnLine = 1
                else:
                    returnLine = 0
            s: str = bytes(byteArray, startIndex, (index + includeReturnLine - returnLine - startIndex)).decode()
            stringList.add(s)
            index += 1
        return stringList
    

    def createStringFromArrayOfStrings(self, stringArray: list[str]) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        stringMaker: StringMaker = StringMaker()
        size: int = len(stringArray)
        for index in range(0, size):
            stringMaker.append(stringArray[index])
        return str(stringMaker)
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.InputStream import InputStream
# from java.io.OutputStream import OutputStream
# from java.io.Reader import Reader
# from java.io.Writer import Writer
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.NullOutputStream import NullOutputStream
# from org.allbinary.logic.io.NullReader import NullReader
# from org.allbinary.logic.io.NullWriter import NullWriter
# from org.allbinary.logic.io.StreamUtil import StreamUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _SimpleFileUtil_instance() -> object:
    return SimpleFileUtil()

lazy_static(SimpleFileUtil, "instance", _SimpleFileUtil_instance)

