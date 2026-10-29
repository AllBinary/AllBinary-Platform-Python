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
# package servlet.request

from __future__ import annotations

from servlet.request.HttpServlet import HttpServlet


class RequestHandler(HttpServlet):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws ServletException
    def init(self, config: ServletConfig) -> None:
        super().init(config)
    

    def destroy(self) -> None:
        pass
    

    # throws ServletException, IOException
    def processRequest(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        try:
            response.setContentType("text/html")
            out: PrintWriter = response.getWriter()
            workflowInterface: WorkFlowInterface = RequestWorkFlowFactory.getInstance(request, response, self.getServletConfig(), self.getServletContext())
            if workflowInterface is not None:
                out.print_(workflowInterface.process())
            out.flush()
            out.close()
        except LicensingException as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SERVLETERROR):
                self.logUtil.put("Servlet LicensingException", self, "processRequest()", e)
            response.sendRedirect(self.abcs.globals.URLGLOBALS.LICENSEERRORPAGE)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SERVLETERROR):
                self.logUtil.put("Servlet Exception", self, "processRequest()", e)
            response.sendRedirect(self.abcs.globals.URLGLOBALS.ERRORPAGE)
    

    # throws ServletException, IOException
    def doGet(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        self.processRequest(request, response)
    

    # throws ServletException, IOException
    def doPost(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        self.processRequest(request, response)
    

    def getServletInfo(self) -> str:
        return "WorkFlow Request Handler"
# from java.io import *
# from java.net import *
# from javax.servlet import *
# from javax.servlet.http import *
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface
from org.allbinary.logic.control.workflow.RequestWorkFlowFactory import RequestWorkFlowFactory


