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

from org.allbinary.business.category.CategoryAbstractFactory import CategoryAbstractFactory
from org.allbinary.business.category.CategoryFactoryInterface import CategoryFactoryInterface


class StoreCategoryFactory(CategoryAbstractFactory, CategoryFactoryInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.transformInfoInterface: TransformInfoInterface = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__()
        self._init_fields()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().CATEGORY):
            self.logUtil.putF(self.commonStrings.START, self, "StoreCategoryFactory(TransformInfoInterface transformInfoInterface)")
        self.transformInfoInterface = transformInfoInterface
    

    def getRootInstance(self) -> CategoryInterface:
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreCategoryPropertiesFactory(self.transformInfoInterface)
            return Category(categoryPropertiesFactoryInterface)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(String, int)", e)
            return None
    

    # Java overloaded method: Python keeps the last definition
    def getRootInstance(self, categoryPath: AbPath) -> CategoryInterface:
        try:
            level: int = CategoryUtil.getPathLevel(categoryPath)
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreCategoryPropertiesFactory(self.transformInfoInterface, categoryPath)
            return Category(categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(String, int)", e)
            return None
    

    def getRootInstanceFromNode(self, node: Node) -> CategoryInterface:
        try:
            categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface = RootStoreCategoryPropertiesFactory(self.transformInfoInterface, node)
            categoryPath: AbPath = AbPath(CategoryUtil.getNameFromNode(node), StringUtil.getInstance().EMPTY_STRING)
            level: int = CategoryUtil.getPathLevel(categoryPath)
            return Category(categoryPropertiesFactoryInterface, level)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getInstance(String, int)", e)
            return None
from org.allbinary.business.category.Category import Category
from org.allbinary.business.category.CategoryInterface import CategoryInterface
from org.allbinary.business.category.CategoryUtil import CategoryUtil
from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
from org.allbinary.business.category.properties.root.store.RootStoreCategoryPropertiesFactory import RootStoreCategoryPropertiesFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Node import Node


