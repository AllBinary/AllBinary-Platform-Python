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
# package org.allbinary.business.category.properties

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface


# Java interface
class CategoryPropertiesInterface(TableMappingInterface, ValidationInterface):
    

    def setValue(self, value: str) -> None:
        raise NotImplementedError()
    

    def getValue(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def getWebAppPath(self) -> AbPath:
        raise NotImplementedError()
    

    # throws Exception
    def getPath(self, categoryHierarchyInterface: CategoryHierarchyInterface) -> AbPath:
        raise NotImplementedError()
    

    # throws Exception
    def getFileName(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def isRoot(self) -> bool:
        raise NotImplementedError()
    

    # throws Exception
    def isRealRoot(self) -> bool:
        raise NotImplementedError()
from org.allbinary.business.category.hierarchy.CategoryHierarchyInterface import CategoryHierarchyInterface
from org.allbinary.logic.io.path.AbPath import AbPath


