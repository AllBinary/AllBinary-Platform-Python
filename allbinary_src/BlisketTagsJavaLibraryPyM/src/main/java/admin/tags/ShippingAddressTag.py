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

from admin.tags.TableTag import TableTag


class ShippingAddressTag(TableTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.value: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.setTagHelperFactory(ShippingAddressHelperFactory())
        self.setTagRequestHelperFactory(ShippingAddressHelperFactory())
    

    def setValue(self, value: str) -> None:
        self.value = value
    

    # throws LicensingException
    def set(self) -> str:
        try:
            anyType: object = ShippingAddressHelperFactory().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("set", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to set Shipping Address"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "set()", e)
            return error
    

    # throws LicensingException
    def setToBillingAddress(self) -> str:
        try:
            anyType: object = ShippingAddressHelperFactory().getInstance(self.getPropertiesHashMap(), self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("setToBillingAddress", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed Setting Shipping address to Billing Address"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setShippingAddressToBillingAddress()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.isEnabled():
                if self.getCommand() is not None:
                    if self.getCommand().compareTo(ShippingAddressData.SELECT) == 0:
                        self.set()
                        return self.EVAL_BODY_INCLUDE
                    elif self.getCommand().compareTo(ShippingAddressData.SETTOBILLINGADDRESS) == 0:
                        self.setToBillingAddress()
                    else:
                        return super().doStartTag()
            return self.SKIP_BODY
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from javax.servlet.jsp.JspTagException import JspTagException
from admin.taghelpers.ShippingAddressHelperFactory import ShippingAddressHelperFactory
from org.allbinary.business.user.address.ShippingAddressData import ShippingAddressData
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


