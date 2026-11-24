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
# package org.allbinary.business.category

from __future__ import annotations

from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface


class CategoryAbstractFactory(CategoryFactoryInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getRootInstance_j0(self) -> CategoryInterface:
        raise RuntimeError()
    

    def getRootInstance_j1(self, categoryAbPath: AbPath) -> CategoryInterface:
        from org.allbinary.logic.io.path.AbPath import AbPath
        raise RuntimeError()

    def getRootInstance(self, *args):
        return getattr(self, "getRootInstance_j" + str(len(args)))(*args)
    

    def getRootInstanceFromNode(self, node: Node) -> CategoryInterface:
        from org.w3c.dom.Node import Node
        raise RuntimeError()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j1_1(self, categoryName: str) -> CategoryInterface:
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF(self.commonStrings.START, self, "getInstance(String)")
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryName)
            return Category(categoryPropertiesFactoryInterface)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(String, int)", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_1(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryName: str) -> CategoryInterface:
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF(self.commonStrings.START, self, "getInstance(CategoryInterface, CategoryInterface, String)")
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryName)
            return Category(rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface , String, int)", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j1_2(self, node: Node) -> CategoryInterface:
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF(self.commonStrings.START, self, "getInstance(Node)")
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(node)
            return Category(categoryPropertiesFactoryInterface)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(Node, int)", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_2(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, node: Node) -> CategoryInterface:
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF(self.commonStrings.START, self, "getInstance(CategoryInterface, CategoryInterface, Node)")
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(node)
            return Category(rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface, Node, int)", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_3(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesHashMap: HashMap) -> CategoryInterface:
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF(self.commonStrings.START, self, "getInstance(CategoryInterface, CategoryInterface, HashMap)")
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryPropertiesHashMap)
            return Category(rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface, HashMap)", e)
            return None

    def getInstance(self, *args):
        if len(args) == 1 and True and (args[0] is None or isinstance(args[0], str)):
            return self.getInstance_j1_1(*args)
        if len(args) == 3 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and (args[2] is None or isinstance(args[2], str)):
            return self.getInstance_j3_1(*args)
        if len(args) == 1:
            return self.getInstance_j1_2(*args)
        if len(args) == 3 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and not isinstance(args[2], (str, list, int, float)):
            return self.getInstance_j3_2(*args)
        if len(args) == 3:
            return self.getInstance_j3_3(*args)
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
# from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


