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



class BasicStoreFrontFactory:
    instance: BasicStoreFrontFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> BasicStoreFrontFactory:
        return BasicStoreFrontFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, storeName: str) -> BasicStoreFrontInterface:
        from org.allbinary.business.context.modules.storefronts.BasicStoreFrontsEntity import BasicStoreFrontsEntity
        try:
            storeFronts: BasicStoreFrontsEntity = BasicStoreFrontsEntity()
            return storeFronts.getStoreFrontInterface(storeName)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().FACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return None
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


BasicStoreFrontFactory.instance = BasicStoreFrontFactory()

