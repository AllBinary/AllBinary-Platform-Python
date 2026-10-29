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
# package org.allbinary.logic.control.workflow

from __future__ import annotations



class RequestWorkFlowFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception, LicensingException
    @staticmethod
    def getInstance(request: ServletRequest, response: ServletResponse, servletConfig: ServletConfig, servletContext: ServletContext) -> WorkFlowInterface:
        httpRequest: HttpServletRequest = request
        requestCommand: str = httpRequest.getPathInfo()
        index: int = requestCommand.find(AbPathData.getInstance().SEPARATOR)
        storeName: str = requestCommand[0:index]
        requestName: str = requestCommand[index:len(requestCommand)]
        return WorkFlowEntityFactory.getInstance().create2().get(requestName, storeName)
    

    # throws Exception, LicensingException
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getInstance(hashMap: dict, pageContext: PageContext) -> WorkFlowInterface:
        from org.allbinary.logic.control.workflow.WorkFlowData import WorkFlowData
        workFlowName: str = pageContext.getRequest().getParameter(WorkFlowData.getInstance().NAME)
        weblisketSession: WeblisketSession = WeblisketSession(hashMap, pageContext)
        storeName: str = weblisketSession.getStoreName()
        return WorkFlowEntityFactory.getInstance().create2().get(workFlowName, storeName)
# from java.util.HashMap import HashMap
# from javax.servlet.ServletConfig import ServletConfig
# from javax.servlet.ServletContext import ServletContext
# from javax.servlet.ServletRequest import ServletRequest
# from javax.servlet.ServletResponse import ServletResponse
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.data.tables.workflow.WorkFlowEntityFactory import WorkFlowEntityFactory
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


