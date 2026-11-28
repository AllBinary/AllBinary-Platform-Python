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
# package org.allbinary.data.tables.user.quoterequest

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class QuoteRequestEntityFactory:
    instance: QuoteRequestEntityFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> QuoteRequestEntityFactory:
        return QuoteRequestEntityFactory.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    def getQuoteRequestEntityInstance(self) -> QuoteRequestEntity:
        from org.allbinary.data.tables.user.quoterequest.QuoteRequestEntity import QuoteRequestEntity
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return QuoteRequestEntity()
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return None
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _QuoteRequestEntityFactory_instance() -> object:
    return QuoteRequestEntityFactory()

lazy_static(QuoteRequestEntityFactory, "instance", _QuoteRequestEntityFactory_instance)

