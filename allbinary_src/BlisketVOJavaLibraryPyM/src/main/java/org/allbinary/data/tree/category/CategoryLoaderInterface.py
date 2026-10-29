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
# package org.allbinary.data.tree.category

from __future__ import annotations

from org.allbinary.data.tree.category.CategoryModifierTreeInterface import CategoryModifierTreeInterface


# Java interface
class CategoryLoaderInterface(CategoryModifierTreeInterface):
    

    def getDoc(self, categoryInterface: CategoryInterface) -> Document:
        raise NotImplementedError()
    

    def get(self, categoryInterface: CategoryInterface) -> CategoryInterface:
        raise NotImplementedError()
    

    def getAll(self, categoryInterface: CategoryInterface) -> CategoryInterface:
        raise NotImplementedError()
from org.allbinary.business.category.CategoryInterface import CategoryInterface
from org.w3c.dom.Document import Document


