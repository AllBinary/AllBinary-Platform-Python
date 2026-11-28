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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        if "transformInfoInterface" not in vars(self): self.transformInfoInterface: TransformInfoInterface = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF(self.commonStrings.START, self, "StoreCategoryFactory(TransformInfoInterface transformInfoInterface)")
        self.transformInfoInterface = transformInfoInterface
    

    def getRootInstance_j0(self) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.business.category.properties.root.store.theme.RootStoreThemeCategoryPropertiesFactory import RootStoreThemeCategoryPropertiesFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreThemeCategoryPropertiesFactory(self.transformInfoInterface)
            return StoreThemeCategory(self.transformInfoInterface, categoryPropertiesFactoryInterface, 0)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getRootInstance()", e)
            return None
    

    def getRootInstance_j1(self, categoryAbPath: AbPath) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.CategoryUtil import CategoryUtil
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.business.category.properties.root.store.theme.RootStoreThemeCategoryPropertiesFactory import RootStoreThemeCategoryPropertiesFactory
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            level: int = CategoryUtil.getPathLevel(categoryAbPath)
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreThemeCategoryPropertiesFactory(self.transformInfoInterface, categoryAbPath)
            return StoreThemeCategory(self.transformInfoInterface, categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getRootInstance(String)", e)
            return None

    def getRootInstance(self, *args):
        implementation = __class__.__dict__.get("getRootInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getRootInstance(*args)
    

    def getRootInstanceFromNode(self, node: Node) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.CategoryUtil import CategoryUtil
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.business.category.properties.root.store.theme.RootStoreThemeCategoryPropertiesFactory import RootStoreThemeCategoryPropertiesFactory
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreThemeCategoryPropertiesFactory(self.transformInfoInterface, node)
            categoryPath: AbPath = AbPath(CategoryUtil.getNameFromNode(node), StringUtil.getInstance().EMPTY_STRING)
            level: int = CategoryUtil.getPathLevel(categoryPath)
            return StoreThemeCategory(self.transformInfoInterface, node, categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getRootInstance(node)", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j2_1(self, categoryPath: str, level: int) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryPath)
            return StoreThemeCategory(self.transformInfoInterface, categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(String, int)", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_1(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPath: str) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryPath)
            return StoreThemeCategory(self.transformInfoInterface, rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface , String, int)", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j2_2(self, node: Node, level: int) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(node)
            return StoreThemeCategory(self.transformInfoInterface, categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(Node, int)", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_2(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, node: Node) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(node)
            return StoreThemeCategory(self.transformInfoInterface, rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface, Node, int)", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j2_3(self, categoryPropertiesHashMap: HashMap, level: int) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryPropertiesHashMap)
            return StoreThemeCategory(self.transformInfoInterface, categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(HashMap)", e)
            return None
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_3(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesHashMap: HashMap) -> CategoryInterface:
        from org.allbinary.business.category.store.theme.StoreThemeCategory import StoreThemeCategory
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = CategoryPropertiesFactory(categoryPropertiesHashMap)
            return StoreThemeCategory(self.transformInfoInterface, rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(CategoryInterface, CategoryInterface, HashMap)", e)
            return None

    def getInstance(self, *args):
        if len(args) == 2 and True and (args[0] is None or isinstance(args[0], str)) and isinstance(args[1], int) and not isinstance(args[1], bool):
            return __class__.__dict__["getInstance_j2_1"].__get__(self, __class__)(*args)
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "CategoryInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "CategoryInterface" for base in type(args[1]).__mro__)) and (args[2] is None or isinstance(args[2], str)):
            return __class__.__dict__["getInstance_j3_1"].__get__(self, __class__)(*args)
        if len(args) == 2 and True and (args[0] is None or any(base.__name__ == "Node" for base in type(args[0]).__mro__)) and isinstance(args[1], int) and not isinstance(args[1], bool):
            return __class__.__dict__["getInstance_j2_2"].__get__(self, __class__)(*args)
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "CategoryInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "CategoryInterface" for base in type(args[1]).__mro__)) and (args[2] is None or any(base.__name__ == "Node" for base in type(args[2]).__mro__)):
            return __class__.__dict__["getInstance_j3_2"].__get__(self, __class__)(*args)
        if len(args) == 2:
            return __class__.__dict__["getInstance_j2_3"].__get__(self, __class__)(*args)
        if len(args) == 3:
            return __class__.__dict__["getInstance_j3_3"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.business.category.CategoryInterface import CategoryInterface
# from org.allbinary.business.category.CategoryUtil import CategoryUtil
# from org.allbinary.business.category.properties.CategoryPropertiesFactory import CategoryPropertiesFactory
# from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
# from org.allbinary.business.category.properties.root.store.theme.RootStoreThemeCategoryPropertiesFactory import RootStoreThemeCategoryPropertiesFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


