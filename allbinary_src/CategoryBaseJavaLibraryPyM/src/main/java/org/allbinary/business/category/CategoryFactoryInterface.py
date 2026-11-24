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



# Java interface
class CategoryFactoryInterface:
    

    def getRootInstance_j0(self) -> CategoryInterface:
        raise NotImplementedError()
    

    def getRootInstance_j1(self, categoryPath: AbPath) -> CategoryInterface:
        from org.allbinary.logic.io.path.AbPath import AbPath
        raise NotImplementedError()

    def getRootInstance(self, *args):
        return getattr(self, "getRootInstance_j" + str(len(args)))(*args)
    

    def getRootInstanceFromNode(self, node: Node) -> CategoryInterface:
        from org.w3c.dom.Node import Node
        raise NotImplementedError()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_1(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, name: str) -> CategoryInterface:
        raise NotImplementedError()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_2(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, node: Node) -> CategoryInterface:
        from org.w3c.dom.Node import Node
        raise NotImplementedError()
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j3_3(self, rootCategoryInterface: CategoryInterface, parentCategoryInterface: CategoryInterface, categoryPropertiesHashMap: HashMap) -> CategoryInterface:
        from java.util.HashMap import HashMap
        raise NotImplementedError()

    def getInstance(self, *args):
        if len(args) == 3 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and (args[2] is None or isinstance(args[2], str)):
            return self.getInstance_j3_1(*args)
        if len(args) == 3 and True and not isinstance(args[0], (str, list, int, float)) and not isinstance(args[1], (str, list, int, float)) and not isinstance(args[2], (str, list, int, float)):
            return self.getInstance_j3_2(*args)
        if len(args) == 3:
            return self.getInstance_j3_3(*args)
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.w3c.dom.Node import Node


