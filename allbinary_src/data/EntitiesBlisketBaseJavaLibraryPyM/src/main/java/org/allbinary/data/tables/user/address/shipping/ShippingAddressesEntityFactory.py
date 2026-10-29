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
# package org.allbinary.data.tables.user.address.shipping

from __future__ import annotations



class ShippingAddressesEntityFactory:
    instance: ShippingAddressesEntityFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> ShippingAddressesEntityFactory:
        return ShippingAddressesEntityFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, userName: str) -> StreetAddressesEntity:
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
        try:
            return ShippingAddressesEntity(userName)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, "getShippingAddressesEntityInstance()", e)
            return None
from org.allbinary.data.tables.user.address.StreetAddressesEntity import StreetAddressesEntity
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


ShippingAddressesEntityFactory.instance = ShippingAddressesEntityFactory()

