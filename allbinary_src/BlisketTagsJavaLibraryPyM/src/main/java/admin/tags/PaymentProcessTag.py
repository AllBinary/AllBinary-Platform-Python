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

from tags.StoreValidationTransformTag import StoreValidationTransformTag


class PaymentProcessTag(StoreValidationTransformTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    # throws LicensingException, Exception
    def process(self) -> str:
        try:
            anyType: object = PaymentProcessHelperFactory().getInstance(self.getPropertiesHashMap(), self.pageContext)
            helperClass: type = type(anyType)
            method: Method = helperClass.getMethod(self.commonStrings.PROCESS, None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().LICENSINGERROR):
                self.logUtil.put("LicensingException", self, self.commonStrings.PROCESS, e)
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
            raise e
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.AUTHORIZEORDEREVALBODYONERROR) == 0 or self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.AUTHORIZEORDERANDEVALBODY) == 0 or self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.AUTHORIZEFORMEVALBODYONERROR) == 0:
                self.pageContext.getOut().print_(str(self.process()) + "<br />")
                if self.getCommand().compareTo(org.allbinary.globals.GLOBALS2.AUTHORIZEORDEREVALBODYONERROR) == 0:
                    return self.SKIP_BODY
                else:
                    return self.EVAL_BODY_INCLUDE
            else:
                raise Exception("No Such Payment Processing Command")
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from javax.servlet.jsp.JspTagException import JspTagException
from admin.taghelpers.PaymentProcessHelperFactory import PaymentProcessHelperFactory
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


