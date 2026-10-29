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


class BasketHelper(TagHelper):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.storeFrontInterface: StoreFrontInterface = None
        self.propertiesHashMap: dict = None
        self.pageContext: PageContext = None
        self.MAX: int = 200
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.propertiesHashMap = hashMap
        self.pageContext = pageContext
        storeName: str = self.propertiesHashMap.get(StoreFrontData.getInstance().NAME)
        if storeName is not None:
            self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
        self.weblisketSession = WeblisketSession(hashMap, pageContext)
    

    def isBasketEmpty(self) -> bool:
        try:
            basket: BasketInterface = self.weblisketSession.getOrder().getBasket()
            if int(basket.getNumberOfItems()) <= 0:
                return True
            else:
                return False
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isBasketEmpty()", e)
            return True
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.basket.BasketInterface import BasketInterface
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.log.LogUtil import LogUtil


