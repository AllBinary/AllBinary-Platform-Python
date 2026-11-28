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
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "categoryPropertiesInterface" not in vars(self): self.categoryPropertiesInterface: CategoryPropertiesInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 2:
            __class__.__jconstructor2(self, *args)

    def __jconstructor2(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "AbPath" for base in type(args[1]).__mro__)):
            __class__._constructor2_1(self, *args)
        elif True and (args[0] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "Node" for base in type(args[1]).__mro__)):
            __class__._constructor2_2(self, *args)
        else:
            __class__._constructor2_3(self, *args)
    

    def _constructor1(self, transformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryProperties import RootStoreCategoryProperties
        from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        __class__._init_fields(self)
        self.categoryPropertiesInterface = RootStoreCategoryProperties(transformInfoInterface)
    

    def _constructor2_1(self, transformInfoInterface: TransformInfoInterface, abPath: AbPath) -> None:
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryProperties import RootStoreCategoryProperties
        from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        __class__._init_fields(self)
        self.categoryPropertiesInterface = RootStoreCategoryProperties(transformInfoInterface, abPath)
    

    def _constructor2_2(self, transformInfoInterface: TransformInfoInterface, node: Node) -> None:
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryProperties import RootStoreCategoryProperties
        from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.w3c.dom.Node import Node
        __class__._init_fields(self)
        self.categoryPropertiesInterface = RootStoreCategoryProperties(transformInfoInterface, node)
    

    def _constructor2_3(self, transformInfoInterface: TransformInfoInterface, categoryPropertiesHashMap: HashMap) -> None:
        from org.allbinary.business.category.properties.root.store.RootStoreCategoryProperties import RootStoreCategoryProperties
        from java.util.HashMap import HashMap
        from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        __class__._init_fields(self)
        self.categoryPropertiesInterface = RootStoreCategoryProperties(transformInfoInterface, categoryPropertiesHashMap)
    

    def getInstance(self) -> CategoryPropertiesInterface:
        from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
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
# from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.w3c.dom.Node import Node
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


