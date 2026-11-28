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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams


@java_inherited_overloads
class MultipartRequestParams(RequestParams):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("special", False)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.special: bool = False

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "HttpServletRequest" for base in type(args[0]).__mro__)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor1_1(self, request: HttpServletRequest) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.processMultipartRequest(request)
    

    def _constructor1_2(self, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.processMultipartRequest(pageContext.getRequest())
    

    def setSpecial(self) -> None:
        self.special = True
    

    def processMultipartRequest(self, request: HttpServletRequest) -> None:
        from java.util.HashMap import HashMap
        from java.util.List import List
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.http.file.upload.AbFileUploadFactory import AbFileUploadFactory
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.apache.commons.fileupload.FileItem import FileItem
        from org.apache.commons.fileupload.FileUploadBase.InvalidContentTypeException import InvalidContentTypeException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            specialRequest: HashMap = StdUtil.getInstance().createHashMap()
            multipartRequestList: List = AbFileUploadFactory.getInstance().getFileItemStreamList(request)
            if multipartRequestList is not None:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
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
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    self.logUtil.putF("Special Request Data: " + str(specialRequest), self, "processMultipartRequest()")
                self.setSpecial()
                self.setMap(specialRequest)
        except InvalidContentTypeException as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUEST):
                self.logUtil.putF("Using Normal RequestParams", self, "processMultipartRequest()")
            java_super_call(super(), "setMap", request.getParameterMap())
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().HTTPREQUESTERROR):
                self.logUtil.putF("Should Not Occur", self, "processMultipartRequest()")
            java_super_call(super(), "setMap", request.getParameterMap())
    

    # throws Exception
    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        if self.special:
            return self.getMap()
        else:
            return java_super_call(super(), "toHashMap")
# from java.util.HashMap import HashMap
# from java.util.List import List
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.http.file.upload.AbFileUploadFactory import AbFileUploadFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.apache.commons.fileupload.FileItem import FileItem
# from org.apache.commons.fileupload.FileUploadBase.InvalidContentTypeException import InvalidContentTypeException
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


