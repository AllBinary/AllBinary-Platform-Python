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
# package org.allbinary.data.tables.user.commerce.inventory.order

from __future__ import annotations



class OrderItemsEntityFactory:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> OrderItemsEntity:
        from org.allbinary.data.tables.user.commerce.inventory.order.OrderItemsEntity import OrderItemsEntity
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            return OrderItemsEntity()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                logUtil.put(commonStrings.EXCEPTION, "OrderItemsEntityFactory", commonStrings.GET_INSTANCE, e)
            return None
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


