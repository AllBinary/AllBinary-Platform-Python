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
# package org.allbinary.business.user.commerce.inventory.order

from __future__ import annotations



#Retrieves a single order for a user
class OrderHistoryFactory:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance(id: str) -> OrderHistory:
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            orderHistoryEntityInterface: OrderHistoryEntity = OrderHistoryEntity()
            return orderHistoryEntityInterface.getOrder(id)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().FACTORYERROR):
                logUtil.put(commonStrings.EXCEPTION, "OrderHistoryFactory", commonStrings.GET_INSTANCE, e)
            return None
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntity import OrderHistoryEntity
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


