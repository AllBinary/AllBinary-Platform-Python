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
class OrderItemsTag(TableTag):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("status", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "status" not in vars(self): self.status: str = None
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from admin.taghelpers.OrderItemsHelperFactory import OrderItemsHelperFactory
        from admin.taghelpers.OrderItemsRequestHelperFactory import OrderItemsRequestHelperFactory
        super().__init__()
        __class__._init_fields(self)
        self.setTagHelperFactory(OrderItemsHelperFactory())
        self.setTagRequestHelperFactory(OrderItemsRequestHelperFactory())
    

    def setStatus(self, value: str) -> None:
        self.status = value
    

    # throws LicensingException
    def setOrderStatus(self) -> str:
        from admin.taghelpers.OrderItemsRequestHelperFactory import OrderItemsRequestHelperFactory
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            anyType: object = OrderItemsRequestHelperFactory().getInstance(self.getPropertiesHashMap(), self.pageContext)
            if self.status is None:
                helperClass: type = type(anyType)
                method: Method = helperClass.getMethod("setOrderStatus", None)
                result: str = method.invoke(anyType, None)
                return result
            else:
                helperClass: type = type(anyType)
                methodParams: list[type] = [type(self.status)]
                method: Method = helperClass.getMethod("setOrderStatus", methodParams)
                methodArgs: list[object] = [self.status]
                result: str = method.invoke(anyType, methodArgs)
                return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to set Order status to: " + self.status
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setOrderStatus()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        try:
            if java_predicate(self, "isEnabled"):
                if self.getCommand() is not None:
                    self.getPropertiesHashMap().put(OrderHistoryData.STATUS, self.status)
                    if self.getCommand().compareTo(OrderHistoryData.SETSTATUS) == 0:
                        self.pageContext.getOut().print_(self.setOrderStatus())
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
# from admin.taghelpers.OrderItemsHelperFactory import OrderItemsHelperFactory
# from admin.taghelpers.OrderItemsRequestHelperFactory import OrderItemsRequestHelperFactory
# from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


