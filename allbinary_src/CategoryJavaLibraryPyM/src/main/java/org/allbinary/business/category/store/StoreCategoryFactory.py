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
# package org.allbinary.business.category.store

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.business.category.CategoryAbstractFactory import CategoryAbstractFactory
from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface


@java_inherited_overloads
class StoreCategoryFactory(*java_bases(CategoryAbstractFactory, CategoryFactoryInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("transformInfoInterface", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "transformInfoInterface" not in vars(self): self.transformInfoInterface: TransformInfoInterface = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF(self.commonStrings.START, self, "StoreCategoryFactory(TransformInfoInterface transformInfoInterface)")
        self.transformInfoInterface = transformInfoInterface
    

    def getRootInstance_j0(self) -> CategoryInterface:
        from org.allbinary.business.category.Category import Category
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryPropertiesFactory import RootStoreCategoryPropertiesFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreCategoryPropertiesFactory(self.transformInfoInterface)
            return Category(categoryPropertiesFactoryInterface)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(String, int)", e)
            return None
    

    def getRootInstance_j1(self, categoryPath: AbPath) -> CategoryInterface:
        from org.allbinary.business.category.Category import Category
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.CategoryUtil import CategoryUtil
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryPropertiesFactory import RootStoreCategoryPropertiesFactory
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            level: int = CategoryUtil.getPathLevel(categoryPath)
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreCategoryPropertiesFactory(self.transformInfoInterface, categoryPath)
            return Category(categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(String, int)", e)
            return None

    def getRootInstance(self, *args):
        implementation = __class__.__dict__.get("getRootInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getRootInstance(*args)
    

    def getRootInstanceFromNode(self, node: Node) -> CategoryInterface:
        from org.allbinary.business.category.Category import Category
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.CategoryUtil import CategoryUtil
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryPropertiesFactory import RootStoreCategoryPropertiesFactory
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.w3c.dom.Node import Node
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreCategoryPropertiesFactory(self.transformInfoInterface, node)
            categoryPath: AbPath = AbPath(CategoryUtil.getNameFromNode(node), StringUtil.getInstance().EMPTY_STRING)
            level: int = CategoryUtil.getPathLevel(categoryPath)
            return Category(categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(String, int)", e)
            return None
# from org.allbinary.business.category.Category import Category
# from org.allbinary.business.category.CategoryInterface import CategoryInterface
# from org.allbinary.business.category.CategoryUtil import CategoryUtil
# from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
# from org.allbinary.business.category.properties.root.store.RootStoreCategoryPropertiesFactory import RootStoreCategoryPropertiesFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


