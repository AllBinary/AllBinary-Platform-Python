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
# package org.allbinary.data.tables.user.commerce.inventory.item.downloads

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class DownloadItemsEntityFactory:
    instance: DownloadItemsEntityFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> DownloadItemsEntityFactory:
        return DownloadItemsEntityFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getDownloadItemsEntityInstance(self) -> DownloadItemsEntity:
        from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntity import DownloadItemsEntity
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return DownloadItemsEntity()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return None
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _DownloadItemsEntityFactory_instance() -> object:
    return DownloadItemsEntityFactory()

lazy_static(DownloadItemsEntityFactory, "instance", _DownloadItemsEntityFactory_instance)

