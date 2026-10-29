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
# package org.allbinary.data.tables.context.module.storefronts

from __future__ import annotations



class StoreFrontsEntityFactory:
    instance: StoreFrontsEntityFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> StoreFrontsEntityFactory:
        return StoreFrontsEntityFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getStoreFrontsEntityInstance(self) -> StoreFrontsEntity:
        from org.allbinary.data.tables.context.module.storefronts.StoreFrontsEntity import StoreFrontsEntity
        try:
            return StoreFrontsEntity()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return None
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


StoreFrontsEntityFactory.instance = StoreFrontsEntityFactory()

