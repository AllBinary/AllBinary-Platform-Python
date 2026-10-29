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



class HttpFileUploadUtil:
    instance: HttpFileUploadUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> HttpFileUploadUtil:
        return HttpFileUploadUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def isValid(self, anyType: object) -> bool:
        if anyType is not None and not (isinstance(anyType, str)):
            if isinstance(anyType, FileItem):
                return True
            else:
                raise Exception("Object Not Instance Of FileItem but is: " + str(ClassUtil.viewAll(anyType, CommonSeps.getInstance().NEW_LINE)))
        return False
    

    # throws Exception
    @staticmethod
    def log(fileItem: FileItemStream) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        stringBuffer: StringMaker = StringMaker()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringBuffer.append("FileItem Log:")
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append("Content Type:")
        stringBuffer.append(fileItem.getContentType())
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append("Field Name:")
        stringBuffer.append(fileItem.getFieldName())
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append("Name:")
        stringBuffer.append(fileItem.getName())
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append("Size:")
        stringBuffer.append(" Not Calculated Yet")
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTP):
            logUtil.putF(str(stringBuffer), HttpFileUploadUtil.getInstance(), "log()")
    

    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def log(fileItem: FileItem) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        stringBuffer: StringMaker = StringMaker()
        commonSeps: CommonSeps = CommonSeps.getInstance()
        stringBuffer.append("FileItem Log:")
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append("Content Type:")
        stringBuffer.append(fileItem.getContentType())
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append("Field Name:")
        stringBuffer.append(fileItem.getFieldName())
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append("Name:")
        stringBuffer.append(fileItem.getName())
        stringBuffer.append(commonSeps.NEW_LINE)
        stringBuffer.append("Size:")
        stringBuffer.appendlong(int(fileItem.getSize()))
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
            logUtil.putF(str(stringBuffer), HttpFileUploadUtil.getInstance(), "log()")
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.anyType.clazz.ClassUtil import ClassUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps
from org.apache.commons.fileupload.FileItem import FileItem
from org.apache.commons.fileupload.FileItemStream import FileItemStream


HttpFileUploadUtil.instance = HttpFileUploadUtil()

