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


class OrderItemsTag(TableTag):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.status: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        self.setTagHelperFactory(OrderItemsHelperFactory())
        self.setTagRequestHelperFactory(OrderItemsRequestHelperFactory())
    

    def setStatus(self, value: str) -> None:
        self.status = value
    

    # throws LicensingException
    def setOrderStatus(self) -> str:
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
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setOrderStatus()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.isEnabled():
                if self.getCommand() is not None:
                    self.getPropertiesHashMap().put(OrderHistoryData.STATUS, self.status)
                    if self.getCommand().compareTo(OrderHistoryData.SETSTATUS) == 0:
                        self.pageContext.getOut().print_(self.setOrderStatus())
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
from admin.taghelpers.OrderItemsHelperFactory import OrderItemsHelperFactory
from admin.taghelpers.OrderItemsRequestHelperFactory import OrderItemsRequestHelperFactory
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


