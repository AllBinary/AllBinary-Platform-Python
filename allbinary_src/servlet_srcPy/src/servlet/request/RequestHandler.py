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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from servlet.request.HttpServlet import HttpServlet


@java_inherited_overloads
class RequestHandler(HttpServlet):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    # throws ServletException
    def init(self, config: ServletConfig) -> None:
        java_super_call(super(), "init", config)
    

    def destroy(self) -> None:
        pass
    

    # throws ServletException, IOException
    def processRequest(self, request: HttpServletRequest, response: HttpServletResponse) -> None:
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface
        from org.allbinary.logic.control.workflow.RequestWorkFlowFactory import RequestWorkFlowFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            response.setContentType("text/html")
            out: PrintWriter = response.getWriter()
            workflowInterface: WorkFlowInterface = RequestWorkFlowFactory.getInstance(request, response, self.getServletConfig(), self.getServletContext())
            if workflowInterface is not None:
                out.print_(workflowInterface.process())
            out.flush()
            out.close()
        except LicensingException as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SERVLETERROR):
                self.logUtil.put("Servlet LicensingException", self, "processRequest()", e)
            response.sendRedirect(self.abcs.globals.URLGLOBALS.LICENSEERRORPAGE)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SERVLETERROR):
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
# from java.io.PrintWriter import PrintWriter
# from java.io.IOException import IOException
# from java.net import *
# from javax.servlet import *
# from javax.servlet.http import *
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.control.workflow.WorkFlowInterface import WorkFlowInterface
# from org.allbinary.logic.control.workflow.RequestWorkFlowFactory import RequestWorkFlowFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


