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
# package org.allbinary.logic.communication.http.request

from __future__ import annotations

from org.allbinary.logic.communication.http.request.RequestParams import RequestParams


class MultipartRequestParams(RequestParams):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.special: bool = False

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, request: HttpServletRequest) -> None:
        super().__init__()
        self._init_fields()
        self.processMultipartRequest(request)
    

    def _constructor1(self, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.processMultipartRequest(pageContext.getRequest())
    

    def setSpecial(self) -> None:
        self.special = True
    

    def processMultipartRequest(self, request: HttpServletRequest) -> None:
        try:
            specialRequest: dict = StdUtil.getInstance().createHashMap()
            multipartRequestList: List = AbFileUploadFactory.getInstance().getFileItemStreamList(request)
            if multipartRequestList is not None:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("FileItem List Size: " + str(multipartRequestList.size()), self, "processMultipartRequest()")
                fileItemArray: list[object] = multipartRequestList.toArray()
                size: int = len(fileItemArray)
                for index in range(0, size):
                    fileItem: FileItem = fileItemArray[index]
                    name: str = fileItem.getName()
                    if StringValidationUtil.getInstance().isEmpty(name):
                        specialRequest.put(fileItem.getFieldName(), fileItem.getString())
                    else:
                        specialRequest.put(fileItem.getFieldName(), fileItem)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("Special Request Data: " + str(specialRequest), self, "processMultipartRequest()")
                self.setSpecial()
                self.setMap(specialRequest)
        except InvalidContentTypeException as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                self.logUtil.putF("Using Normal RequestParams", self, "processMultipartRequest()")
            super().setMap(request.getParameterMap())
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUESTERROR):
                self.logUtil.putF("Should Not Occur", self, "processMultipartRequest()")
            super().setMap(request.getParameterMap())
    

    # throws Exception
    def toHashMap(self) -> dict:
        if self.special:
            return self.getMap()
        else:
            return super().toHashMap()
# from java.util.HashMap import HashMap
# from java.util.List import List
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.file.upload.AbFileUploadFactory import AbFileUploadFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.apache.commons.fileupload.FileItem import FileItem
from org.apache.commons.fileupload.FileUploadBase.InvalidContentTypeException import InvalidContentTypeException


