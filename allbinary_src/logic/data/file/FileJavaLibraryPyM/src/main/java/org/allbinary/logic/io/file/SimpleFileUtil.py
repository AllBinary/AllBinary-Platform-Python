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



class SimpleFileUtil:
    instance: SimpleFileUtil = None

    def _init_fields(self) -> None:
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
        return (OutputStream()  # Java anonymous class body:
#             
# 
#             # throws IOException
#             def write(self, b: int) -> None:
#                 pass
#             
# 
#             # throws IOException
#             def write(self, b: list[int], off: int, len_: int) -> None:
#                 pass
#             
# 
#             def close(self) -> None:
#                 pass
)
    

    @staticmethod
    def nullWriter() -> Writer:
        return (Writer()  # Java anonymous class body:
#             self.closed: bool = False
#             
# 
#             # throws IOException
#             def append(self, c: str) -> Writer:
#                 return self
#             
# 
#             # throws IOException
#             def append(self, csq: CharSequence) -> Writer:
#                 return self
#             
# 
#             # throws IOException
#             def append(self, csq: CharSequence, start: int, end: int) -> Writer:
#                 return self
#             
# 
#             # throws IOException
#             def write(self, c: int) -> None:
#                 pass
#             
# 
#             # throws IOException
#             def write(self, cbuf: list[str], off: int, len_: int) -> None:
#                 pass
#             
# 
#             # throws IOException
#             def write(self, str_: str) -> None:
#                 pass
#             
# 
#             # throws IOException
#             def write(self, str_: str, off: int, len_: int) -> None:
#                 pass
#             
# 
#             # throws IOException
#             def flush(self) -> None:
#                 pass
#             
# 
#             # throws IOException
#             def close(self) -> None:
#                 pass
)
    

    @staticmethod
    def nullReader() -> Reader:
        return (Reader()  # Java anonymous class body:
#             
# 
#             # throws IOException
#             def read(self) -> int:
#                 return -1
#             
# 
#             # throws IOException
#             def read(self, cbuf: list[str], off: int, len_: int) -> int:
#                 return -1
#             
# 
#             # throws IOException
#             def read(self, target: CharBuffer) -> int:
#                 return -1
#             
# 
#             # throws IOException
#             def ready(self) -> bool:
#                 return False
#             
# 
#             # throws IOException
#             def skip(self, n: int) -> int:
#                 return 0
#             
# 
#             def close(self) -> None:
#                 pass
)
    

    def loadFileAsList(self, inputStream: InputStream, max: int, byteArray1: list[int]) -> BasicArrayList:
        return self.loadFileAsListReturnLine(inputStream, max, byteArray1, 0)
    

    def loadFileAsListReturnLine(self, inputStream: InputStream, max: int, byteArray1: list[int], includeReturnLine: int) -> BasicArrayList:
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
        stringMaker: StringMaker = StringMaker()
        size: int = len(stringArray)
        for index in range(0, size):
            stringMaker.append(stringArray[index])
        return str(stringMaker)
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.IOException import IOException
# from java.io.InputStream import InputStream
# from java.io.OutputStream import OutputStream
# from java.io.Reader import Reader
# from java.io.Writer import Writer
# from java.nio.CharBuffer import CharBuffer
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


SimpleFileUtil.instance = SimpleFileUtil()

