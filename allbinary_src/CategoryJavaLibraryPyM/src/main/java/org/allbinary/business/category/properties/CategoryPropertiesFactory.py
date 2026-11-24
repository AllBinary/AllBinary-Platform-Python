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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.categoryPropertiesInterface: CategoryPropertiesInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.__jconstructor1(*args)

    def __jconstructor1(self, *args) -> None:
        if True and (args[0] is None or isinstance(args[0], str)):
            self._constructor1_1(*args)
        elif True and not isinstance(args[0], (str, list, int, float)):
            self._constructor1_2(*args)
        else:
            self._constructor1_3(*args)
    

    def _constructor1_1(self, name: str) -> None:
        self._init_fields()
        self.categoryPropertiesInterface = CategoryProperties(name)
    

    def _constructor1_2(self, node: Node) -> None:
        from org.w3c.dom.Node import Node
        self._init_fields()
        self.categoryPropertiesInterface = CategoryProperties(node)
    

    def _constructor1_3(self, categoryPropertiesHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        self._init_fields()
        self.categoryPropertiesInterface = CategoryProperties(categoryPropertiesHashMap)
    

    def getInstance(self) -> CategoryPropertiesInterface:
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return self.categoryPropertiesInterface
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return None
# from java.util.HashMap import HashMap
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


