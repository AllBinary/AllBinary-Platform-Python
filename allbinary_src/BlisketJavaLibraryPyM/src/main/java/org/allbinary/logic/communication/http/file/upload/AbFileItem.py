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
# package org.allbinary.logic.communication.http.file.upload

from __future__ import annotations

from org.apache.commons.fileupload.FileItem import FileItem


class AbFileItem(FileItem):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.name: str = None
        self.fieldName: str = None
        self.byteArray: list[int] = None
    

    def __init__(self, name: str, fieldName: str, byteArray: list[int]) -> None:
        self._init_fields()
        self.name = name
        self.fieldName = fieldName
        self.byteArray = byteArray
    

    # throws IOException
    def getInputStream(self) -> InputStream:
        raise OSError(self.commonStrings.NOT_IMPLEMENTED)
    

    def getContentType(self) -> str:
        return None
    

    def getName(self) -> str:
        return self.name
    

    def isInMemory(self) -> bool:
        return True
    

    def getSize(self) -> int:
        return len(self.byteArray)
    

    def get(self) -> list[int]:
        return self.byteArray
    

    # throws UnsupportedEncodingException
    def getString(self, encoding: str) -> str:
        return bytes(self.byteArray, encoding).decode()
    

    # Java overloaded method: Python keeps the last definition
    def getString(self) -> str:
        try:
            return FileItemUtil.getInstance().getString(self.byteArray)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getString", e)
            return StringUtil.getInstance().EMPTY_STRING
    

    # throws Exception
    def write(self, file: File) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def write(self, file: AbFile) -> None:
        raise Exception(self.commonStrings.NOT_IMPLEMENTED)
    

    def delete(self) -> None:
        ForcedLogUtil.log(self.commonStrings.NOT_IMPLEMENTED, "delete()")
    

    def getFieldName(self) -> str:
        return self.fieldName
    

    def setFieldName(self, name: str) -> None:
        self.fieldName = name
    

    def isFormField(self) -> bool:
        if StringValidationUtil.getInstance().isEmpty(self.fieldName):
            return False
        else:
            return True
    

    def setFormField(self, state: bool) -> None:
        pass
    

    # throws IOException
    def getOutputStream(self) -> OutputStream:
        raise OSError(self.commonStrings.NOT_IMPLEMENTED)
    

    def getHeaders(self) -> FileItemHeaders:
        raise RuntimeError(self.commonStrings.NOT_IMPLEMENTED)
    

    def setHeaders(self, fih: FileItemHeaders) -> None:
        raise RuntimeError(self.commonStrings.NOT_IMPLEMENTED)
# from java.io.File import File
# from java.io.IOException import IOException
# from java.io.InputStream import InputStream
# from java.io.OutputStream import OutputStream
# from java.io.UnsupportedEncodingException import UnsupportedEncodingException
from org.allbinary.logic.communication.log.ForcedLogUtil import ForcedLogUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.apache.commons.fileupload.FileItemHeaders import FileItemHeaders
from org.apache.commons.fileupload.FileItemUtil import FileItemUtil


