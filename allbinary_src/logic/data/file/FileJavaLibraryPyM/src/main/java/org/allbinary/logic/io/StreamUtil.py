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
# package org.allbinary.logic.io

from __future__ import annotations



class StreamUtil:
    instance: StreamUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> StreamUtil:
        return StreamUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def get(self, inputStream: InputStream, outputStream: OutputStream, buffer: list[int]) -> OutputStream:
        len_: int = 0
        while True:
            len_ = inputStream.read(buffer, 0, len(buffer))
            if len_ != -1:
                pass
            else:
                break
            outputStream.write(buffer, 0, len_)
        return outputStream
    

    # throws Exception
    def getByteArray(self, inputStream: InputStream, outputStream2: ByteArrayOutputStream, byteArray: list[int]) -> list[int]:
        outputStream: ByteArrayOutputStream = outputStream2
        try:
            self.get(inputStream, outputStream, byteArray)
            return outputStream.toByteArray()
        except Exception as e:
            raise e
        finally:
            self.close(outputStream)
    

    def close(self, closeable: Closeable) -> bool:
        try:
            if closeable is not None:
                closeable.close()
            return True
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.CLOSE, e)
            return False
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.Closeable import Closeable
# from java.io.InputStream import InputStream
# from java.io.OutputStream import OutputStream
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


StreamUtil.instance = StreamUtil()

