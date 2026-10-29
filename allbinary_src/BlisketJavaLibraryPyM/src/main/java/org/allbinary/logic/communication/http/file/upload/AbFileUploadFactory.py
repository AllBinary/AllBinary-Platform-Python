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



class AbFileUploadFactory:
    instance: AbFileUploadFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> AbFileUploadFactory:
        return AbFileUploadFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getFileItemStreamList(self, httpServletRequest: HttpServletRequest) -> List:
        from org.allbinary.logic.communication.http.file.upload.AbFileUpload import AbFileUpload
        from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
        from org.allbinary.logic.communication.http.file.upload.AbFileItem import AbFileItem
        try:
            fileUpload: AbFileUpload = AbFileUpload(AbFileItemFactory())
            iterator: FileItemIterator = fileUpload.getItemIterator(httpServletRequest)
            items: List = ArrayList()
            while iterator.hasNext():
                fileItemStream: FileItemStream = iterator.next()
                HttpFileUploadUtil.log(fileItemStream)
                fileItem: AbFileItem = AbFileItem(fileItemStream.getName(), fileItemStream.getFieldName(), FileItemUtil.getInstance().getBytes(fileItemStream))
                items.add(fileItem)
            return items
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, "get()", e)
            raise e
    

    # throws Exception
    def getFileItemList(self, httpServletRequest: HttpServletRequest) -> List:
        from org.allbinary.logic.communication.http.file.upload.AbFileUpload import AbFileUpload
        try:
            abFileUpload: AbFileUpload = AbFileUpload(AbFileItemFactory())
            return abFileUpload.parseRequest(httpServletRequest)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, "get()", e)
            raise e
# from java.util.ArrayList import ArrayList
# from java.util.List import List
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.logic.communication.http.AbFileItemFactory import AbFileItemFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.apache.commons.fileupload.FileItemIterator import FileItemIterator
from org.apache.commons.fileupload.FileItemStream import FileItemStream
from org.apache.commons.fileupload.FileItemUtil import FileItemUtil


AbFileUploadFactory.instance = AbFileUploadFactory()

