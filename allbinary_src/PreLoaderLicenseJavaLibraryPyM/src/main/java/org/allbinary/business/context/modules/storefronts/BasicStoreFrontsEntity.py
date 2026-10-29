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
# package org.allbinary.business.context.modules.storefronts

from __future__ import annotations

from org.allbinary.business.init.InitSql import InitSql


class BasicStoreFrontsEntity(InitSql):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "storefronts"
    

    def __init__(self) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTable(self.tableName)
    

    # throws Exception
    def getStoreFrontInterface(self, name: str) -> BasicStoreFrontInterface:
        from org.allbinary.business.context.modules.storefronts.BasicStoreFront import BasicStoreFront
        keysAndValues: dict = StdUtil.getInstance().createHashMap()
        keysAndValues.put(StoreFrontData.getInstance().NAME, name)
        storeHashMap: dict = super().getRow(keysAndValues)
        if storeHashMap is None:
            raise Exception("No Such Store: " + name)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().FACTORYERROR):
            self.logUtil.putF("StoreFront: " + str(storeHashMap), self, "getStore()")
        return BasicStoreFront(storeHashMap)
# from java.util.HashMap import HashMap
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil


