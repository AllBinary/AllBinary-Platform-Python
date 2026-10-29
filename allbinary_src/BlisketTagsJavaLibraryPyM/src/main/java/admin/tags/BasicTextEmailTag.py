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
# package admin.tags

from __future__ import annotations

from tags.CustomTagSupport import CustomTagSupport


class BasicTextEmailTag(CustomTagSupport):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.subject: str = None
        self.body: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setSubject(self, value: str) -> None:
        self.subject = value
    

    def setBody(self, value: str) -> None:
        self.body = value
    

    def send(self) -> str:
        try:
            propertiesHashMap: dict = StdUtil.getInstance().createHashMap()
            propertiesHashMap.put("Subject", self.subject)
            propertiesHashMap.put("Body", self.body)
            anyType: object = BasicTextEmailHelperFactory().getInstance(propertiesHashMap, self.pageContext)
            method: Method = type(anyType).getMethod("send", None)
            method.invoke(anyType, None)
            return "Email Sent"
        except Exception as e:
            error: str = "Failed to Send Email."
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "send()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            self.pageContext.getOut().print_(self.send())
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.JspTagException import JspTagException
from admin.taghelpers.BasicTextEmailHelperFactory import BasicTextEmailHelperFactory
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil


