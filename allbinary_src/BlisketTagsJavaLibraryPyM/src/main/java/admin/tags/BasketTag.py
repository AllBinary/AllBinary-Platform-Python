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


class BasketTag(CustomTagSupport):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.command: str = None
        self.storeName: str = None
        self.propertiesHashMap: dict = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setCommand(self, command: str) -> None:
        self.command = command
    

    def setStoreName(self, value: str) -> None:
        self.storeName = value
    

    # throws LicensingException
    def isBasketEmpty(self) -> bool:
        try:
            anyType: object = BasketHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            method: Method = type(anyType).getMethod("isBasketEmpty", None)
            emptyBoolean: bool = method.invoke(anyType, None)
            return emptyBoolean
        except LicensingException as e:
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isBasketEmpty()", e)
            return True
    

    # throws LicensingException
    def addItemToBasket(self) -> bool:
        try:
            anyType: object = BasketRequestHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            method: Method = type(anyType).getMethod("addItemToBasket", None)
            emptyBoolean: bool = method.invoke(anyType, None)
            return emptyBoolean
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to add item from Basket"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "addItemToBasket()", e)
            return False
    

    # throws LicensingException
    def removeItemFromBasket(self) -> bool:
        try:
            anyType: object = BasketRequestHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            method: Method = type(anyType).getMethod("removeItemFromBasket", None)
            emptyBoolean: bool = method.invoke(anyType, None)
            return emptyBoolean
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to remove item from Basket"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "removeItemFromBasket()", e)
            return False
    

    # throws LicensingException
    def adjustBasket(self) -> bool:
        try:
            anyType: object = BasketRequestHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            method: Method = type(anyType).getMethod("adjustBasket", None)
            emptyBoolean: bool = method.invoke(anyType, None)
            return emptyBoolean
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to Adjust Basket"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "adjustBasket()", e)
            return False
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.command is not None:
                self.propertiesHashMap = StdUtil.getInstance().createHashMap()
                self.propertiesHashMap.put(StoreFrontData.getInstance().NAME, self.storeName)
                if ((self.command > BasketData.INSERT) - (self.command < BasketData.INSERT)) == 0:
                    if not self.addItemToBasket():
                        self.pageContext.getOut().println("Item is not currently being sold.<p/>")
                elif ((self.command > BasketData.DELETE) - (self.command < BasketData.DELETE)) == 0:
                    self.removeItemFromBasket()
                elif ((self.command > BasketData.ADJUST) - (self.command < BasketData.ADJUST)) == 0:
                    self.adjustBasket()
                elif ((self.command > BasketData.ISEMPTY) - (self.command < BasketData.ISEMPTY)) == 0:
                    if self.isBasketEmpty():
                        return self.EVAL_BODY_INCLUDE
                    else:
                        return self.SKIP_BODY
            return self.SKIP_BODY
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.JspTagException import JspTagException
from admin.taghelpers.BasketHelperFactory import BasketHelperFactory
from admin.taghelpers.BasketRequestHelperFactory import BasketRequestHelperFactory
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.user.commerce.inventory.basket.BasketData import BasketData
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


