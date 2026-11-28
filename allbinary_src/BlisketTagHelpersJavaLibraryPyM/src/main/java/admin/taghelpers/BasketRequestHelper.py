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
# package admin.taghelpers

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from admin.taghelpers.TagHelper import TagHelper


@java_inherited_overloads
class BasketRequestHelper(TagHelper):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("basicItemData", None)
        vars(self).setdefault("weblisketSession", None)
        vars(self).setdefault("storeFrontInterface", None)
        vars(self).setdefault("propertiesHashMap", None)
        vars(self).setdefault("pageContext", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("id", None)
        vars(self).setdefault("num", None)
        vars(self).setdefault("MAX", 0)

    def _init_fields(self) -> None:
        from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        if "weblisketSession" not in vars(self): self.weblisketSession: WeblisketSession = None
        if "storeFrontInterface" not in vars(self): self.storeFrontInterface: StoreFrontInterface = None
        if "propertiesHashMap" not in vars(self): self.propertiesHashMap: HashMap = None
        if "pageContext" not in vars(self): self.pageContext: PageContext = None
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "id" not in vars(self): self.id: str = None
        if "num" not in vars(self): self.num: str = None
        self.MAX: int = 200
    

    def __init__(self, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFront import StoreFront
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        super().__init__()
        __class__._init_fields(self)
        self.propertiesHashMap = propertiesHashMap
        self.pageContext = pageContext
        self.request = pageContext.getRequest()
        storeName: str = propertiesHashMap.get(StoreFrontData.getInstance().NAME)
        if storeName is not None:
            self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
        else:
            self.storeFrontInterface = StoreFront()
        self.weblisketSession = WeblisketSession(propertiesHashMap, pageContext)
        self.getFormData()
    

    def getFormData(self) -> None:
        from org.allbinary.business.user.commerce.inventory.basket.BasketData import BasketData
        self.id = self.request.getParameter(self.basicItemData.ID)
        self.num = self.request.getParameter(BasketData.ITEMTOTALINBASKET)
    

    def addItemToBasket(self) -> bool:
        from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if self.id is not None and self.num is not None:
                basket: BasketInterface = self.weblisketSession.getOrder().getBasket()
                if InventoryEntityFactory.getInstance().getInventoryEntityInstance().getItem(self.id) is None:
                    return False
                basket.addItem(self.id, self.num)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Successfully added item to Basket", self, "addItemToBasket()")
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "addItemToBasket()", e)
            return False
    

    def removeItemFromBasket(self) -> bool:
        from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if self.id is not None:
                basket: BasketInterface = self.weblisketSession.getOrder().getBasket()
                basket.removeItem(self.id)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Successfully removed item from Basket", self, "removeItemFromBasket()")
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "removeItemFromBasket()", e)
            return False
    

    def adjustBasket(self) -> bool:
        from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            basket: BasketInterface = self.weblisketSession.getOrder().getBasket()
            if self.id is not None and self.num is not None:
                basket.adjustItem(self.id, self.num)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Successfull Adjusted Basket", self, "adjustBasket()")
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "adjustBasket()", e)
            return False
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFront import StoreFront
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.commerce.inventory.basket.BasketData import BasketData
# from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


