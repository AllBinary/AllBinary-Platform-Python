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
# package org.allbinary.business.category.properties

from __future__ import annotations

from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface


class CategoryPropertiesFactory(CategoryPropertiesFactoryInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.categoryPropertiesInterface: CategoryPropertiesInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, name: str) -> None:
        from org.allbinary.business.category.properties.CategoryProperties import CategoryProperties
        self._init_fields()
        self.categoryPropertiesInterface = CategoryProperties(name)
    

    def _constructor1(self, node: Node) -> None:
        from org.allbinary.business.category.properties.CategoryProperties import CategoryProperties
        self._init_fields()
        self.categoryPropertiesInterface = CategoryProperties(node)
    

    def _constructor1(self, categoryPropertiesHashMap: dict) -> None:
        from org.allbinary.business.category.properties.CategoryProperties import CategoryProperties
        self._init_fields()
        self.categoryPropertiesInterface = CategoryProperties(categoryPropertiesHashMap)
    

    def getInstance(self) -> CategoryPropertiesInterface:
        try:
            return self.categoryPropertiesInterface
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return None
# from java.util.HashMap import HashMap
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Node import Node


