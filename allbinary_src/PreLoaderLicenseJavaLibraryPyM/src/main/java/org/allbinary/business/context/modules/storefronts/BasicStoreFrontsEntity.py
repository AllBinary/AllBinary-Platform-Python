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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "storefronts"
    

    def __init__(self) -> None:
        from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTable(self.tableName)
    

    # throws Exception
    def getStoreFrontInterface(self, name: str) -> BasicStoreFrontInterface:
        from org.allbinary.business.context.modules.storefronts.BasicStoreFront import BasicStoreFront
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        keysAndValues: HashMap = StdUtil.getInstance().createHashMap()
        keysAndValues.put(StoreFrontData.getInstance().NAME, name)
        storeHashMap: HashMap = super().getRow(keysAndValues)
        if storeHashMap is None:
            raise Exception("No Such Store: " + name)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().FACTORYERROR):
            self.logUtil.putF("StoreFront: " + str(storeHashMap), self, "getStore()")
        return BasicStoreFront(storeHashMap)
# from java.util.HashMap import HashMap
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


