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
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    def getRootInstance(self) -> CategoryInterface:
        raise RuntimeError()
    

    # Java overloaded method: Python keeps the last definition
    def getRootInstance(self, categoryAbPath: AbPath) -> CategoryInterface:
        raise RuntimeError()
    

    def getRootInstanceFromNode(self, node: Node) -> CategoryInterface:
        raise RuntimeError()
    

    def getInstance(self, categoryName: str) -> CategoryInterface:
        from org.allbinary.business.category.Category import Category
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF(self.commonStrings.START, self, "getInstance(String)")
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryName)
            return Category(categoryPropertiesFactoryInterface)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(String, int)", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryName: str) -> CategoryInterface:
        from org.allbinary.business.category.Category import Category
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF(self.commonStrings.START, self, "getInstance(CategoryInterface, CategoryInterface, String)")
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryName)
            return Category(rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface , String, int)", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, node: Node) -> CategoryInterface:
        from org.allbinary.business.category.Category import Category
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF(self.commonStrings.START, self, "getInstance(Node)")
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(node)
            return Category(categoryPropertiesFactoryInterface)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(Node, int)", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, node: Node) -> CategoryInterface:
        from org.allbinary.business.category.Category import Category
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF(self.commonStrings.START, self, "getInstance(CategoryInterface, CategoryInterface, Node)")
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(node)
            return Category(rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface, Node, int)", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesHashMap: dict) -> CategoryInterface:
        from org.allbinary.business.category.Category import Category
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
                self.logUtil.putF(self.commonStrings.START, self, "getInstance(CategoryInterface, CategoryInterface, HashMap)")
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryPropertiesHashMap)
            return Category(rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface, HashMap)", e)
            return None
# from java.util.HashMap import HashMap
from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Node import Node


