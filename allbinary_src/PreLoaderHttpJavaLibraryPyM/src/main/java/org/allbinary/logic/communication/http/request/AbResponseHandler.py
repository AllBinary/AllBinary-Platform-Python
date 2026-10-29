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



class AbResponseHandler:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws JspTagException
    @staticmethod
    def sendJspTagRedirect(pageContext: PageContext, e: Exception) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGERROR):
                logUtil.put("Jsp Tag Exception", "AbResponseHandler", "sendJspRedirect()", e)
            AbResponseHandler.sendRedirect(pageContext, self.FREEBLISKET_PATH_GLOBALS.getInstance().ERRORPAGE)
        except Exception as e2:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LICENSINGERROR):
                logUtil.put("Exception in Redirect Handling", "AbResponseHandler", "sendJspRedirect", e)
            raise JspTagException()
    

    # throws ServletException
    @staticmethod
    def sendServletRedirect(pageContext: PageContext, e: Exception) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGERROR):
                logUtil.put("Jsp Tag Exception", "AbResponseHandler", "sendJspRedirect()", e)
            AbResponseHandler.sendRedirect(pageContext, self.FREEBLISKET_PATH_GLOBALS.getInstance().ERRORPAGE)
        except Exception as e2:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LICENSINGERROR):
                logUtil.put("Exception in Redirect Handling", "AbResponseHandler", "sendJspRedirect", e)
            raise ServletException()
    

    # throws JspTagException
    @staticmethod
    def sendJspTagLicensingRedirect(pageContext: PageContext, e: Exception) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGERROR):
                logUtil.put("Licensing Exception", "AbResponseHandler", "sendJspTagLicensingRedirect()", e)
            AbResponseHandler.sendRedirect(pageContext, self.FREEBLISKET_PATH_GLOBALS.getInstance().LICENSEERRORPAGE)
        except Exception as e2:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LICENSINGERROR):
                logUtil.put("Exception in Redirect Handling", "AbResponseHandler", "sendJspTagLicensingRedirect", e)
            raise JspTagException()
    

    # throws ServletException
    @staticmethod
    def sendServletLicensingRedirect(pageContext: PageContext, e: Exception) -> None:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGERROR):
                logUtil.put("Licensing Exception", "AbResponseHandler", "sendServletLicensingRedirect()", e)
            AbResponseHandler.sendRedirect(pageContext, self.FREEBLISKET_PATH_GLOBALS.getInstance().LICENSEERRORPAGE)
        except Exception as e2:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().LICENSINGERROR):
                logUtil.put("Exception in Redirect Handling", "AbResponseHandler", "sendServletLicensingRedirect", e)
            raise ServletException()
    

    # throws Exception
    @staticmethod
    def sendRedirect(pageContext: PageContext, page: str) -> None:
        request: HttpServletRequest = pageContext.getRequest()
        response: HttpServletResponse = pageContext.getResponse()
        requestDispatcher: RequestDispatcher = request.getRequestDispatcher(page)
        if response.isCommitted():
            response.sendRedirect(page)
        else:
            try:
                requestDispatcher.forward(request, response)
            except Exception as e:
                pageContext.getOut().print_("Error: " + page)
# from javax.servlet.RequestDispatcher import RequestDispatcher
# from javax.servlet.ServletException import ServletException
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.http.HttpServletResponse import HttpServletResponse
# from javax.servlet.jsp.JspTagException import JspTagException
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


