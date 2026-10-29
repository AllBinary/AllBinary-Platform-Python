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


class DownloadFileServlet(HttpServlet):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.DOWNLOAD: str = "download"
        self.DEFAULT_BUFFER_SIZE: int = 16384

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws ServletException, IOException
    def processRequest(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        inputStream: InputStream = None
        try:
            BlisketServletUtil.getInstance().init(request)
            requestPath: str = request.getRequestURI()
            if requestPath is None:
                response.sendError(HttpServletResponse.SC_NOT_FOUND)
                return
            beginIndex: int = requestPath.find(self.DOWNLOAD)
            filePath: str = StringUtil.getInstance().EMPTY_STRING
            if beginIndex >= 0:
                filePath = requestPath[beginIndex + len(self.DOWNLOAD):]
            else:
                response.sendError(HttpServletResponse.SC_NOT_FOUND)
            file: AbFile = AbFile.createAbFile(str(self.URLGLOBALS.getWebappPath()) + filePath)
            if not file.exists():
                response.sendError(HttpServletResponse.SC_NOT_FOUND)
                return
            hashMap: dict = StdUtil.getInstance().createHashMap()
            authenticationHelper: AuthenticationHelper = AuthenticationHelperFactory().getInstance(hashMap, request)
            if authenticationHelper.isAuthenticated():
                if AuthenticationHelperUtil.getInstance().isAuthorized(authenticationHelper, filePath):
                    inputStream = CloudStreamUtil.getInstance().getFile(file)
                    contentType: str = self.getServletContext().getMimeType(file.getName())
                    if contentType is None:
                        contentType = "application/octet-stream"
                    response.reset()
                    response.setBufferSize(self.DEFAULT_BUFFER_SIZE)
                    response.setContentType(contentType)
                    response.setHeader("Content-Length", str(file.length()))
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("attachment; filename=\"")
                    stringBuffer.append(file.getName())
                    stringBuffer.append(CommonSeps.getInstance().QUOTE)
                    response.setHeader("Content-Disposition", str(stringBuffer))
                    StreamUtil.getInstance().get(inputStream, response.getOutputStream(), [0] * (16348))
                else:
                    response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "You are not Authorized")
            else:
                response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Please Login")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "processRequest()", e)
            response.sendError(HttpServletResponse.SC_NOT_FOUND)
        finally:
            StreamUtil.getInstance().close(response.getOutputStream())
            if not StreamUtil.getInstance().close(inputStream):
                pass
    

    # throws ServletException, IOException
    def doGet(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        self.processRequest(request, response)
    

    # throws ServletException, IOException
    def doPost(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        self.processRequest(request, response)
    

    def getServletInfo(self) -> str:
        return "Serves Up Cloud Files"
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
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.CloudStreamUtil import CloudStreamUtil
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.servlet.BlisketServletUtil import BlisketServletUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


