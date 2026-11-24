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
# package org.allbinary.servlet

from __future__ import annotations

# from javax.servlet.http.HttpServlet import HttpServlet


class MagicalImageServlet(HttpServlet):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws ServletException, IOException
    def processRequest(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        from org.allbinary.servlet.BlisketServletUtil import BlisketServletUtil
        from java.io.InputStream import InputStream
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.CloudStreamUtil import CloudStreamUtil
        from org.allbinary.logic.io.StreamUtil import StreamUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        inputStream: InputStream = None
        try:
            BlisketServletUtil.getInstance().init(request)
            requestURI: str = request.getRequestURI()
            file: AbFile = AbFile.createAbFile(str(URLGLOBALS.getWebappPath()) + requestURI)
            inputStream = CloudStreamUtil.getInstance().getFileAnyWhere(file)
            outputStream: ByteArrayOutputStream = ByteArrayOutputStream(8000)
            byteArray: list[int] = StreamUtil.getInstance().getByteArray(inputStream, outputStream, [0] * (16384))
            response.setContentType("image/jpeg;charset=utf-8")
            response.getOutputStream().write(byteArray)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "processRequest()", e)
        finally:
            StreamUtil.getInstance().close(response.getOutputStream())
            if not StreamUtil.getInstance().close(inputStream):
                response.sendError(HttpServletResponse.SC_NOT_FOUND)
    

    # throws ServletException, IOException
    def doGet(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        self.processRequest(request, response)
    

    # throws ServletException, IOException
    def doPost(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        self.processRequest(request, response)
    

    def getServletInfo(self) -> str:
        return "Serves Up Image From Local or Cloud"
# from java.io.ByteArrayOutputStream import ByteArrayOutputStream
# from java.io.IOException import IOException
# from java.io.InputStream import InputStream
# from javax.servlet.ServletException import ServletException
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.http.HttpServletResponse import HttpServletResponse
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.CloudStreamUtil import CloudStreamUtil
# from org.allbinary.logic.io.StreamUtil import StreamUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


