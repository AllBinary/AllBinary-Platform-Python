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

from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface
from org.allbinary.business.category.store.theme.StoreThemeCategoryPathView import StoreThemeCategoryPathView


class StoreThemeCategoryPathValidationView(StoreThemeCategoryPathView, ValidationInterface):
    

    def __init__(self, categoryInterface: StoreThemeCategoryInterface) -> None:
        super().__init__(categoryInterface)
    

    # throws Exception
    def isValid(self) -> bool:
        return True
    

    # throws Exception
    def toValidationInfoDoc(self) -> Document:
        return None
    

    # throws Exception
    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    # throws Exception
    def validationInfo(self) -> str:
        return "Error"
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


