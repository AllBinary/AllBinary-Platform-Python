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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from tags.TransformTag import TransformTag


@java_inherited_overloads
class ValidationTransformTag(TransformTag):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("xslFile", None)
        vars(self).setdefault("logic", False)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "xslFile" not in vars(self): self.xslFile: str = None
        if "logic" not in vars(self): self.logic: bool = False
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from taghelpers.ValidatedViewHelperFactory import ValidatedViewHelperFactory
        super().__init__(ValidatedViewHelperFactory())
        __class__._init_fields(self)
        self.logic = True
    

    def setXsl(self, value: str) -> None:
        self.xslFile = value
        self.setTemplateFile(self.xslFile)
    

    def setLogic(self, logic: bool) -> None:
        self.logic = logic
    

    # throws Exception
    def isValid(self) -> bool:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            helperClass: type = type(self.getHelper())
            method: Method = helperClass.getMethod(self.commonStrings.IS_VALID, None)
            result: bool = method.invoke(self.getHelper(), None)
            return result
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.IS_VALID, e)
            raise e
    

    # throws Exception
    def validationInfo(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            addressHelperClass: type = type(self.getHelper())
            method: Method = addressHelperClass.getMethod("validationInfo", None)
            result: str = method.invoke(self.getHelper(), None)
            return result
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "validationInfo()", e)
            raise e
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
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
            if java_predicate(self, "isValid"):
                java_super_call(super(), "doStartTag")
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
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
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
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
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
            self.logUtil.putF("Tag Ended", self, "doEndTag")
        self.logic = True
        return java_super_call(super(), "doEndTag")
# from java.lang.reflect.Method import Method
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.JspTagException import JspTagException
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from taghelpers.ValidatedViewHelperFactory import ValidatedViewHelperFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


