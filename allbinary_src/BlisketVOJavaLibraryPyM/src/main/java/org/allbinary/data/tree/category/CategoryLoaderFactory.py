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
# package org.allbinary.data.tree.category

from __future__ import annotations



class CategoryLoaderFactory:
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def getInstance(categoryFactoryInterface: CategoryFactoryInterface) -> CategoryLoaderInterface:
        from org.allbinary.data.tree.category.CategoryLoader import CategoryLoader
        from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        logUtil: LogUtil = LogUtil.getInstance()
        try:
            return CategoryLoader(categoryFactoryInterface)
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                logUtil.put(commonStrings.EXCEPTION, "CategoryNodeFactory", commonStrings.GET_INSTANCE, e)
            return None
# from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


