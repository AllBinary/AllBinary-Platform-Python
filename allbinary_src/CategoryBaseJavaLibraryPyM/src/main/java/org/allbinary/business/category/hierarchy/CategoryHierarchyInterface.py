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
# package org.allbinary.business.category.hierarchy

from __future__ import annotations



# Java interface
class CategoryHierarchyInterface:
    

    def getLevel(self) -> int:
        raise NotImplementedError()
    

    def getLevelString(self) -> str:
        raise NotImplementedError()
    

    def getRoot(self) -> CategoryInterface:
        raise NotImplementedError()
    

    def getParent(self) -> CategoryInterface:
        raise NotImplementedError()
    

    def setLevel(self, level: int) -> None:
        raise NotImplementedError()
    

    def setRoot(self, categoryInterface: CategoryInterface) -> None:
        raise NotImplementedError()
    

    def setParent(self, categoryInterface: CategoryInterface) -> None:
        raise NotImplementedError()
from org.allbinary.business.category.CategoryInterface import CategoryInterface


