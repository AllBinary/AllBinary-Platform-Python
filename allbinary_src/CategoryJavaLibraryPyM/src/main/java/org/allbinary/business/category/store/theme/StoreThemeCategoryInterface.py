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

from org.allbinary.business.category.CategoryInterface import CategoryInterface
from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.allbinary.logic.visual.transform.info.CompositeTransformInfoInterface import CompositeTransformInfoInterface


# Java interface
class StoreThemeCategoryInterface(CategoryInterface, TableMappingInterface, ValidationInterface, CompositeTransformInfoInterface):
    

    def addTheme(self, themeValidation: ThemeValidation) -> None:
        raise NotImplementedError()
    

    def getThemes(self) -> BasicArrayList:
        raise NotImplementedError()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.visual.theme.ThemeValidation import ThemeValidation


