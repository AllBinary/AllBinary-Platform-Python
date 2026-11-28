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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from admin.tags.TableTag import TableTag


@java_inherited_overloads
class BillingAddressTag(TableTag):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("value", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "value" not in vars(self): self.value: str = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from admin.taghelpers.BillingAddressHelperFactory import BillingAddressHelperFactory
        super().__init__()
        __class__._init_fields(self)
        self.setTagHelperFactory(BillingAddressHelperFactory())
        self.setTagRequestHelperFactory(BillingAddressHelperFactory())
    

    def setValue(self, value: str) -> None:
        self.value = value
    

    # throws LicensingException
    def set(self) -> str:
        from admin.taghelpers.BillingAddressHelperFactory import BillingAddressHelperFactory
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            anyType: object = BillingAddressHelperFactory().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("set", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to set billing Address"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "set()", e)
            return error
    

    # throws LicensingException
    def setToShippingAddress(self) -> str:
        from admin.taghelpers.BillingAddressHelperFactory import BillingAddressHelperFactory
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            anyType: object = BillingAddressHelperFactory().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("setToShippingAddress", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to Set Billing address to Shipping Address"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setToShippingAddress()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        try:
            if java_predicate(self, "isEnabled"):
                if self.getCommand() is not None:
                    if self.getCommand().compareTo(BillingAddressData.SELECT) == 0:
                        self.set()
                        return self.EVAL_BODY_INCLUDE
                    elif self.getCommand().compareTo(BillingAddressData.SETTOSHIPPINGADDRESS) == 0:
                        self.setToShippingAddress()
                    else:
                        return java_super_call(super(), "doStartTag")
            return self.SKIP_BODY
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from javax.servlet.jsp.JspTagException import JspTagException
# from admin.taghelpers.BillingAddressHelperFactory import BillingAddressHelperFactory
# from org.allbinary.business.user.address.BillingAddressData import BillingAddressData
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


