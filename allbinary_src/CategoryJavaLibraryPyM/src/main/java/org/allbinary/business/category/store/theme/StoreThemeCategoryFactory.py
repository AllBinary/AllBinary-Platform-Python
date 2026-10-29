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
# package org.allbinary.business.category.store.theme

from __future__ import annotations

from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface


class StoreThemeCategoryFactory(CategoryFactoryInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.transformInfoInterface: TransformInfoInterface = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF(self.commonStrings.START, self, "StoreCategoryFactory(TransformInfoInterface transformInfoInterface)")
        self.transformInfoInterface = transformInfoInterface
    

    def getRootInstance(self) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreThemeCategoryPropertiesFactory(self.transformInfoInterface)
            return StoreThemeCategory(self.transformInfoInterface, categoryPropertiesFactoryInterface, 0)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getRootInstance()", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getRootInstance(self, categoryAbPath: AbPath) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        try:
            level: int = CategoryUtil.getPathLevel(categoryAbPath)
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreThemeCategoryPropertiesFactory(self.transformInfoInterface, categoryAbPath)
            return StoreThemeCategory(self.transformInfoInterface, categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getRootInstance(String)", e)
            return None
    

    def getRootInstanceFromNode(self, node: Node) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreThemeCategoryPropertiesFactory(self.transformInfoInterface, node)
            categoryPath: AbPath = AbPath(CategoryUtil.getNameFromNode(node), StringUtil.getInstance().EMPTY_STRING)
            level: int = CategoryUtil.getPathLevel(categoryPath)
            return StoreThemeCategory(self.transformInfoInterface, node, categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getRootInstance(node)", e)
            return None
    

    def getInstance(self, categoryPath: str, level: int) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryPath)
            return StoreThemeCategory(self.transformInfoInterface, categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(String, int)", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPath: str) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryPath)
            return StoreThemeCategory(self.transformInfoInterface, rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface , String, int)", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, node: Node, level: int) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(node)
            return StoreThemeCategory(self.transformInfoInterface, categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(Node, int)", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, node: Node) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(node)
            return StoreThemeCategory(self.transformInfoInterface, rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface, Node, int)", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, categoryPropertiesHashMap: dict, level: int) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryPropertiesHashMap)
            return StoreThemeCategory(self.transformInfoInterface, categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(HashMap)", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getInstance(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesHashMap: dict) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryPropertiesHashMap)
            return StoreThemeCategory(self.transformInfoInterface, rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface, HashMap)", e)
            return None
# from java.util.HashMap import HashMap
from org.allbinary.business.category.CategoryInterface import CategoryInterface
from org.allbinary.business.category.CategoryUtil import CategoryUtil
from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
from org.allbinary.business.category.properties.root.store.theme.RootStoreThemeCategoryPropertiesFactory import RootStoreThemeCategoryPropertiesFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Node import Node


