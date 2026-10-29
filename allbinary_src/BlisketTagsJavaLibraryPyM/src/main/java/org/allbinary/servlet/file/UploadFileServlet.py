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
# package org.allbinary.servlet.file

from __future__ import annotations

# from javax.servlet.http.HttpServlet import HttpServlet


class UploadFileServlet(HttpServlet):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.requestHashMap: dict = None
        self.fileName: str = None

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws ServletException, IOException
    def processRequest(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        isError: bool = False
        inputStream: InputStream = None
        try:
            BlisketServletUtil.getInstance().init(request)
            self.requestHashMap = MultipartRequestParams(request).toHashMap()
            filePath: str = self.requestHashMap.get(FileUploadData.getInstance().UPLOAD_TO_FILE_PATH)
            if filePath is None:
                isError = True
                response.sendError(HttpServletResponse.SC_NOT_FOUND)
                return
            hashMap: dict = StdUtil.getInstance().createHashMap()
            authenticationHelper: AuthenticationHelper = AuthenticationHelperFactory().getInstance(hashMap, request)
            if authenticationHelper.isAuthenticated():
                if AuthenticationHelperUtil.getInstance().isAuthorized(authenticationHelper, filePath):
                    self.saveFile(filePath)
                    response.setContentType("text/plain")
                    response.getOutputStream().write(list("OK!".encode()))
                else:
                    isError = True
                    response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "You are not Authorized")
            else:
                isError = True
                response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Please Login")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "processRequest()", e)
            isError = True
            response.sendError(HttpServletResponse.SC_NOT_FOUND)
        finally:
            if not isError:
                StreamUtil.getInstance().close(response.getOutputStream())
            if not StreamUtil.getInstance().close(inputStream):
                pass
    

    # throws Exception
    def saveFile(self, filePath: str) -> None:
        fileOutputStream: AbFileOutputStream = None
        try:
            fileItem: FileItem = self.requestHashMap.get(FileUploadData.getInstance().FILE_DATA)
            if fileItem is not None and fileItem.getSize() > 1:
                self.fileName = HttpRequestUtil.getInstance().generateFileName(fileItem.getName())
                if filePath.endswith("/") or filePath.endswith("\\"):
                    filePath = filePath + self.fileName
                file: AbFile = AbFile.createAbFile(str(self.URLGLOBALS.getWebappPath()) + filePath)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().HTTPREQUEST):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("Uploaded File: ")
                    stringBuffer.append(self.fileName)
                    stringBuffer.append(" New File: ")
                    stringBuffer.append(file.getPath())
                    self.logUtil.putF(str(stringBuffer), self, "saveFile()")
                HttpFileUploadUtil.log(fileItem)
                byteArray: list[int] = fileItem.get()
                if file.isFile():
                    file.delete()
                    file.createNewFile()
                fileOutputStream = AbFileOutputStream.createFromAbFile(file)
                fileOutputStream.write(byteArray)
        finally:
            if fileOutputStream is not None:
                fileOutputStream.close()
    

    # throws ServletException, IOException
    def doGet(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        self.processRequest(request, response)
    

    # throws ServletException, IOException
    def doPost(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        self.processRequest(request, response)
    

    def getServletInfo(self) -> str:
        return "Upload Cloud Files"
# from java.io.IOException import IOException
# from java.io.InputStream import InputStream
# from java.util.HashMap import HashMap
# from javax.servlet.ServletException import ServletException
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.http.HttpServletResponse import HttpServletResponse
from admin.taghelpers.AuthenticationHelper import AuthenticationHelper
from admin.taghelpers.AuthenticationHelperFactory import AuthenticationHelperFactory
from admin.taghelpers.AuthenticationHelperUtil import AuthenticationHelperUtil
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.file.upload.FileUploadData import FileUploadData
from org.allbinary.logic.communication.http.file.upload.HttpFileUploadUtil import HttpFileUploadUtil
from org.allbinary.logic.communication.http.request.HttpRequestUtil import HttpRequestUtil
from org.allbinary.logic.communication.http.request.MultipartRequestParams import MultipartRequestParams
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.servlet.BlisketServletUtil import BlisketServletUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.apache.commons.fileupload.FileItem import FileItem


