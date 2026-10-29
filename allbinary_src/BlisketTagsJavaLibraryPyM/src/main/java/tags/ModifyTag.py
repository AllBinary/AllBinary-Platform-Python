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
# package tags

from __future__ import annotations

from tags.HelperTag import HelperTag


class ModifyTag(HelperTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, tagHelperFactoryInterface: TagHelperFactoryInterface) -> None:
        super().__init__(tagHelperFactoryInterface)
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
    

    # throws LicensingException
    def insert(self) -> str:
        try:
            helperClass: type = type(self.getHelper())
            method: Method = helperClass.getMethod("insert", None)
            result: str = method.invoke(self.getHelper(), None)
            return result
        except Exception as e:
            error: str = "Failed to insert"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insert()", e)
            return error
    

    # throws LicensingException
    def delete(self) -> str:
        try:
            helperClass: type = type(self.getHelper())
            method: Method = helperClass.getMethod(self.commonStrings.delete, None)
            result: str = method.invoke(self.getHelper(), None)
            return result
        except Exception as e:
            error: str = "Failed to delete"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
    

    # throws LicensingException
    def update(self) -> str:
        try:
            helperClass: type = type(self.getHelper())
            method: Method = helperClass.getMethod("update", None)
            result: str = method.invoke(self.getHelper(), None)
            return result
        except Exception as e:
            error: str = "Failed to update"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                request: HttpServletRequest = self.pageContext.getRequest()
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Command: ")
                stringBuffer.append(self.getCommand())
                stringBuffer.append(" Request URI: ")
                stringBuffer.append(request.getRequestURI())
                self.logUtil.putF(str(stringBuffer), self, self.tagStrings.DO_START_TAG)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                pass
            if self.getCommand() is not None:
                self.setHelper()
                commonStrings: CommonStrings = CommonStrings.getInstance()
                if self.getCommand().compareTo(commonStrings.INSERT) == 0:
                    output: str = self.insert()
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                        self.pageContext.getOut().print_(output + "<br />")
                elif self.getCommand().compareTo(commonStrings.DELETE) == 0:
                    output: str = self.delete()
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                        self.pageContext.getOut().print_(output + "<br />")
                elif self.getCommand().compareTo(commonStrings.UPDATE) == 0:
                    output: str = self.update()
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGEXTRAOUTPUT):
                        self.pageContext.getOut().print_(output + "<br />")
            return self.EVAL_BODY_INCLUDE
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.JspTagException import JspTagException
from admin.taghelpers.TagHelperFactoryInterface import TagHelperFactoryInterface
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from org.allbinary.string.CommonStrings import CommonStrings


