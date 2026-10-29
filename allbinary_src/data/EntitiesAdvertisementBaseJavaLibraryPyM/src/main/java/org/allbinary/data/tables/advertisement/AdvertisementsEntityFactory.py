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
# package org.allbinary.data.tables.advertisement

from __future__ import annotations



class AdvertisementsEntityFactory:
    CLASSNAME: str = "org.allbinary.data.tables.AdvertisementEntity"
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance() -> AdvertisementsEntityInterface:
        from org.allbinary.data.tables.advertisement.AdvertisementsEntity import AdvertisementsEntity
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            return AdvertisementsEntity()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                logUtil.put(commonStrings.EXCEPTION, "AdvertisementEntityFactory", commonStrings.GET_INSTANCE, e)
            return None
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


