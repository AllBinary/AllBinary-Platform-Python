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

from tags.TransformTag import TransformTag


class ValidationTransformTag(TransformTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.xslFile: str = None
        self.logic: bool = None
    

    def __init__(self) -> None:
        super().__init__(ValidatedViewHelperFactory())
        self._init_fields()
        self.logic = True
    

    def setXsl(self, value: str) -> None:
        self.xslFile = value
        self.setTemplateFile(self.xslFile)
    

    def setLogic(self, logic: bool) -> None:
        self.logic = logic
    

    # throws Exception
    def isValid(self) -> bool:
        try:
            helperClass: type = type(self.getHelper())
            method: Method = helperClass.getMethod(self.commonStrings.IS_VALID, None)
            result: bool = method.invoke(self.getHelper(), None)
            return result
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.IS_VALID, e)
            raise e
    

    # throws Exception
    def validationInfo(self) -> str:
        try:
            addressHelperClass: type = type(self.getHelper())
            method: Method = addressHelperClass.getMethod("validationInfo", None)
            result: str = method.invoke(self.getHelper(), None)
            return result
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "validationInfo()", e)
            raise e
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                stringBuffer: StringMaker = StringMaker()
                request: HttpServletRequest = self.pageContext.getRequest()
                stringBuffer.append("ValidationViewTag Start For: ")
                stringBuffer.append(self.getName())
                stringBuffer.append("\nView FIle: ")
                stringBuffer.append(self.getObjectFile())
                stringBuffer.append("\nRequest URI: ")
                stringBuffer.append(request.getRequestURI())
                self.logUtil.putF(str(stringBuffer), self, self.tagStrings.DO_START_TAG)
            self.setHelper()
            if self.isValid():
                super().doStartTag()
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("View File: ")
                    stringBuffer.append(self.getObjectFile())
                    stringBuffer.append("\nLogic includes body if true=")
                    stringBuffer.appendboolean(self.logic)
                    self.logUtil.putF(str(stringBuffer), self, self.tagStrings.DO_START_TAG)
                if self.logic:
                    return self.EVAL_BODY_INCLUDE
                else:
                    return self.SKIP_BODY
            else:
                self.pageContext.getOut().print_(self.validationInfo())
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("View File: ")
                    stringBuffer.append(self.getObjectFile())
                    stringBuffer.append("\nisValid()=false")
                    stringBuffer.append("\nLogic skips body if true=")
                    stringBuffer.appendboolean(self.logic)
                    self.logUtil.putF(str(stringBuffer), self, self.tagStrings.DO_START_TAG)
                if self.logic:
                    return self.SKIP_BODY
                else:
                    return self.EVAL_BODY_INCLUDE
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
    

    def doEndTag(self) -> int:
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF("Tag Ended", self, "doEndTag")
        self.logic = True
        return super().doEndTag()
# from java.lang.reflect.Method import Method
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.JspTagException import JspTagException
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
from taghelpers.ValidatedViewHelperFactory import ValidatedViewHelperFactory


