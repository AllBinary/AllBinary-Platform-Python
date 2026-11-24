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
# package org.allbinary.data.tables.user.address.billing

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class BillingAddressesEntityFactory:
    instance: BillingAddressesEntityFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> BillingAddressesEntityFactory:
        return BillingAddressesEntityFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getInstance_j1(self, userName: str) -> StreetAddressesEntity:
        from org.allbinary.data.tables.user.address.billing.BillingAddressesEntity import BillingAddressesEntity
        from org.allbinary.data.tables.user.address.StreetAddressesEntity import StreetAddressesEntity
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return BillingAddressesEntity(userName)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return None

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from org.allbinary.data.tables.user.address.StreetAddressesEntity import StreetAddressesEntity
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _BillingAddressesEntityFactory_instance() -> object:
    return BillingAddressesEntityFactory()

lazy_static(BillingAddressesEntityFactory, "instance", _BillingAddressesEntityFactory_instance)

