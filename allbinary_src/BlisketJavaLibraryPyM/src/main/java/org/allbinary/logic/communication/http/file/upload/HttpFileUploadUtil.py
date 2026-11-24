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

from java.lang.JavaRuntimeStatic import lazy_static


class HttpFileUploadUtil:
    instance: HttpFileUploadUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> HttpFileUploadUtil:
        return HttpFileUploadUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def isValid(self, anyType: object) -> bool:
        from org.allbinary.logic.java.anyType.clazz.ClassUtil import ClassUtil
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.apache.commons.fileupload.FileItem import FileItem
        if anyType is not None and not isinstance(anyType, str):
            if isinstance(anyType, FileItem):
                return True
            else:
                raise Exception("Object Not Instance Of FileItem but is: " + str(ClassUtil.viewAll(anyType, CommonSeps.getInstance().NEW_LINE)))
        return False
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def log_j1_1(fileItem: FileItemStream) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.apache.commons.fileupload.FileItemStream import FileItemStream
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTP):
            logUtil.putF(str(stringBuffer), HttpFileUploadUtil.getInstance(), "log()")
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def log_j1_2(fileItem: FileItem) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.apache.commons.fileupload.FileItem import FileItem
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
            logUtil.putF(str(stringBuffer), HttpFileUploadUtil.getInstance(), "log()")

    @staticmethod
    def log(*args):
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return HttpFileUploadUtil.log_j1_1(*args)
        if len(args) == 1:
            return HttpFileUploadUtil.log_j1_2(*args)
        return getattr(HttpFileUploadUtil, "log_j" + str(len(args)))(*args)
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.anyType.clazz.ClassUtil import ClassUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.apache.commons.fileupload.FileItem import FileItem
# from org.apache.commons.fileupload.FileItemStream import FileItemStream
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _HttpFileUploadUtil_instance() -> object:
    return HttpFileUploadUtil()

lazy_static(HttpFileUploadUtil, "instance", _HttpFileUploadUtil_instance)

