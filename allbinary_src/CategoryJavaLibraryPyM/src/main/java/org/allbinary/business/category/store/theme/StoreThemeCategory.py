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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.business.category.Category import Category
from org.allbinary.business.category.store.theme.StoreThemeCategoryInterface import StoreThemeCategoryInterface


@java_inherited_overloads
class StoreThemeCategory(*java_bases(Category, StoreThemeCategoryInterface)):
    def _java_defaults(self):
        vars(self).setdefault("transformInfoInterface", None)
        vars(self).setdefault("themeVector", None)

    def _init_fields(self) -> None:
        if "transformInfoInterface" not in vars(self): self.transformInfoInterface: TransformInfoInterface = None
        if "themeVector" not in vars(self): self.themeVector: BasicArrayList = None

    def __init__(self, *args) -> None:
        if len(args) == 3:
            __class__._constructor3(self, *args)
        elif len(args) == 4:
            __class__.__jconstructor4(self, *args)
        elif len(args) == 5:
            __class__._constructor5(self, *args)

    def __jconstructor4(self, *args) -> None:
        if True and (args[0] is None or any(base.__name__ == "TransformInfoInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "CategoryInterface" for base in type(args[1]).__mro__)) and (args[2] is None or any(base.__name__ == "CategoryInterface" for base in type(args[2]).__mro__)) and (args[3] is None or any(base.__name__ == "CategoryPropertiesFactoryInterface" for base in type(args[3]).__mro__)):
            __class__._constructor4_1(self, *args)
        else:
            __class__._constructor4_2(self, *args)
    

    def _constructor3(self, transformInfoInterface: TransformInfoInterface, categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface, level: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(categoryPropertiesFactoryInterface, level)
        __class__._init_fields(self)
        self.transformInfoInterface = transformInfoInterface
        self.themeVector = BasicArrayListD()
    

    def _constructor4_1(self, transformInfoInterface: TransformInfoInterface, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        __class__._init_fields(self)
        self.transformInfoInterface = transformInfoInterface
        self.themeVector = BasicArrayListD()
    

    def _constructor4_2(self, transformInfoInterface: TransformInfoInterface, node: Node, categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface, level: int) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.w3c.dom.Node import Node
        super().__init__(categoryPropertiesFactoryInterface, level)
        __class__._init_fields(self)
        self.transformInfoInterface = transformInfoInterface
        self.themeVector = BasicArrayListD()
        self.addThemes(node)
    

    def _constructor5(self, transformInfoInterface: TransformInfoInterface, node: Node, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesFactoryInterface: CategoryPropertiesFactoryInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.business.category.CategoryInterface import CategoryInterface
        from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.w3c.dom.Node import Node
        super().__init__(rootCategoryInterface, parentCategoryInterface, categoryPropertiesFactoryInterface)
        __class__._init_fields(self)
        self.transformInfoInterface = transformInfoInterface
        self.themeVector = BasicArrayListD()
        self.addThemes(node)
    

    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return self.transformInfoInterface
    

    # throws Exception
    def addThemes(self, node: Node) -> None:
        from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
        from org.allbinary.logic.visual.theme.ThemeData import ThemeData
        from org.allbinary.logic.visual.theme.ThemeValidation import ThemeValidation
        from org.allbinary.logic.visual.theme.ThemesData import ThemesData
        from org.w3c.dom.Node import Node
        from org.w3c.dom.NodeList import NodeList
        themesNode: Node = DomSearchHelper.getNode(ThemesData.getInstance().NAME, node.getChildNodes())
        nodeList: NodeList = themesNode.getChildNodes()
        for index in range(0, nodeList.getLength()):
            themeNode: Node = nodeList.item(index)
            if themeNode.getNodeName().compareTo(ThemeData.getInstance().NAME) == 0:
                self.themeVector.add(ThemeValidation(self, themeNode))
    

    def addTheme(self, themeValidation: ThemeValidation) -> None:
        from org.allbinary.logic.visual.theme.ThemeValidation import ThemeValidation
        self.themeVector.add(themeValidation)
    

    def getThemes(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.themeVector
    

    # throws Exception
    def isValid(self) -> bool:
        if not (java_super_call(super(), "isValid")):
            return False
        return True
    

    # throws Exception
    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.visual.theme.ThemesData import ThemesData
        categoryHashMap: HashMap = java_super_call(super(), "toHashMap")
        categoryHashMap.put(ThemesData.getInstance().NAME, self.themeVector)
        return categoryHashMap
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        categoryVector: BasicArrayList = java_super_call(super(), "toVector")
        return categoryVector
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.category.CategoryInterface import CategoryInterface
# from org.allbinary.business.category.properties.CategoryPropertiesFactoryInterface import CategoryPropertiesFactoryInterface
# from org.allbinary.data.tree.dom.DomSearchHelper import DomSearchHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.visual.theme.ThemeData import ThemeData
# from org.allbinary.logic.visual.theme.ThemeValidation import ThemeValidation
# from org.allbinary.logic.visual.theme.ThemesData import ThemesData
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Node import Node
# from org.w3c.dom.NodeList import NodeList


