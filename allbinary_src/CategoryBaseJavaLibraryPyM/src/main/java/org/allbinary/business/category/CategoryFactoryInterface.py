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
        implementation = __class__.__dict__.get("getRootInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getRootInstance(*args)
    

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
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "CategoryInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "CategoryInterface" for base in type(args[1]).__mro__)) and (args[2] is None or isinstance(args[2], str)):
            return __class__.__dict__["getInstance_j3_1"].__get__(self, __class__)(*args)
        if len(args) == 3 and True and (args[0] is None or any(base.__name__ == "CategoryInterface" for base in type(args[0]).__mro__)) and (args[1] is None or any(base.__name__ == "CategoryInterface" for base in type(args[1]).__mro__)) and (args[2] is None or any(base.__name__ == "Node" for base in type(args[2]).__mro__)):
            return __class__.__dict__["getInstance_j3_2"].__get__(self, __class__)(*args)
        if len(args) == 3:
            return __class__.__dict__["getInstance_j3_3"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.w3c.dom.Node import Node


