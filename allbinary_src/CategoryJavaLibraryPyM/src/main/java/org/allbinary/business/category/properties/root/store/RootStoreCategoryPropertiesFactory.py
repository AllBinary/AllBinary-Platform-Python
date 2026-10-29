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
# package org.allbinary.business.category.properties.root.store

from __future__ import annotations

from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface


class RootStoreCategoryPropertiesFactory(CategoryPropertiesFactoryInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.categoryPropertiesInterface: CategoryPropertiesInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryProperties import RootStoreCategoryProperties
        self._init_fields()
        self.categoryPropertiesInterface = RootStoreCategoryProperties(transformInfoInterface)
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, abPath: AbPath) -> None:
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryProperties import RootStoreCategoryProperties
        self._init_fields()
        self.categoryPropertiesInterface = RootStoreCategoryProperties(transformInfoInterface, abPath)
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, node: Node) -> None:
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryProperties import RootStoreCategoryProperties
        self._init_fields()
        self.categoryPropertiesInterface = RootStoreCategoryProperties(transformInfoInterface, node)
    

    def _constructor2(self, transformInfoInterface: TransformInfoInterface, categoryPropertiesHashMap: dict) -> None:
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryProperties import RootStoreCategoryProperties
        self._init_fields()
        self.categoryPropertiesInterface = RootStoreCategoryProperties(transformInfoInterface, categoryPropertiesHashMap)
    

    def getInstance(self) -> CategoryPropertiesInterface:
        try:
            return self.categoryPropertiesInterface
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().ENTITYFACTORYERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            return None
# from java.util.HashMap import HashMap
from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Node import Node


