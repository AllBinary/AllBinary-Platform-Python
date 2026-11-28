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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface


# Java interface
@java_inherited_overloads
class CategoryInterface(*java_bases(TableMappingInterface, ValidationInterface)):
    

    def getChildNodes(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()
    

    def addChildProperty(self, categoryPropertiesInterface: CategoryPropertiesInterface) -> bool:
        from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
        raise NotImplementedError()
    

    def addChild(self, categoryInterface: CategoryInterface) -> bool:
        raise NotImplementedError()
    

    def removeChild(self, categoryInterface: CategoryInterface) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def isLeaf(self) -> bool:
        raise NotImplementedError()
    

    def getProperties(self) -> CategoryPropertiesInterface:
        from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
        raise NotImplementedError()
    

    def setProperties(self, categoryPropertiesInterface: CategoryPropertiesInterface) -> None:
        from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
        raise NotImplementedError()
    

    def getHierarchy(self) -> CategoryHierarchyInterface:
        from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
        raise NotImplementedError()
    

    def setHierarchy(self, categoryHierarchyInterface: CategoryHierarchyInterface) -> None:
        from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
        raise NotImplementedError()
    

    # throws Exception
    def getPath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        raise NotImplementedError()
    

    # throws Exception
    def getFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        raise NotImplementedError()
    

    # throws Exception
    def getWebAppPath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        raise NotImplementedError()
    

    # throws Exception
    def getRootFilePath(self) -> AbPath:
        from org.allbinary.logic.io.path.AbPath import AbPath
        raise NotImplementedError()
    

    # throws Exception
    def log(self) -> None:
        raise NotImplementedError()
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
# from org.allbinary.business.category.properties.CategoryPropertiesInterface import CategoryPropertiesInterface
# from org.allbinary.logic.io.path.AbPath import AbPath


