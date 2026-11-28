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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from tags.CustomTagSupport import CustomTagSupport


@java_inherited_overloads
class BasicTextEmailTag(CustomTagSupport):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("subject", None)
        vars(self).setdefault("body", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "subject" not in vars(self): self.subject: str = None
        if "body" not in vars(self): self.body: str = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def setSubject(self, value: str) -> None:
        self.subject = value
    

    def setBody(self, value: str) -> None:
        self.body = value
    

    def send(self) -> str:
        from java.util.HashMap import HashMap
        from admin.taghelpers.BasicTextEmailHelperFactory import BasicTextEmailHelperFactory
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            propertiesHashMap: HashMap = StdUtil.getInstance().createHashMap()
            propertiesHashMap.put("Subject", self.subject)
            propertiesHashMap.put("Body", self.body)
            anyType: object = BasicTextEmailHelperFactory().getInstance(propertiesHashMap, self.pageContext)
            method: Method = type(anyType).getMethod("send", None)
            method.invoke(anyType, None)
            return "Email Sent"
        except Exception as e:
            error: str = "Failed to Send Email."
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "send()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        try:
            self.pageContext.getOut().print_(self.send())
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.JspTagException import JspTagException
# from admin.taghelpers.BasicTextEmailHelperFactory import BasicTextEmailHelperFactory
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


