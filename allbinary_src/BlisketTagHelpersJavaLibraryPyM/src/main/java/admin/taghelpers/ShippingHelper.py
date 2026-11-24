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

from admin.taghelpers.TagHelper import TagHelper


class ShippingHelper(TagHelper):

    def _init_fields(self) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.storeFrontInterface: StoreFrontInterface = None
        self.propertiesHashMap: HashMap = None
        self.pageContext: PageContext = None
        self.request: HttpServletRequest = None
        self.shippingType: str = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        super().__init__()
        self._init_fields()
        self.pageContext = pageContext
        self.request = pageContext.getRequest()
        storeName: str = hashMap.get(StoreFrontData.getInstance().NAME)
        if storeName is not None:
            self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
        self.weblisketSession = WeblisketSession(hashMap, pageContext)
        self.getFormData()
    

    def getFormData(self) -> None:
        from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
        self.shippingType = self.request.getParameter(ShippingMethodData.NAME)
    

    def setShippingType(self) -> str:
        from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successfully Set Shipping Type"
            order: OrderInterface = self.weblisketSession.getOrder()
            order.setShippingMethod(self.shippingType)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "setShippingType()")
            return success
        except Exception as e:
            error: str = "Failed to view Shipping Type"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setShippingType()", e)
            return error
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
# from org.allbinary.business.user.commerce.shipping.ShippingMethodData import ShippingMethodData
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


