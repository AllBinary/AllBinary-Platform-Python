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
# package views.generic.inventory

from __future__ import annotations

from views.generic.inventory.InventorySearch import InventorySearch


class AutoSearchValidationInventoryView(InventorySearch):
    

    def __init__(self, searchRequest: SearchRequest) -> None:
        super().__init__(searchRequest)
    

    def isValid(self) -> bool:
        return True
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    def validationInfo(self) -> str:
        return None
from org.allbinary.logic.control.search.SearchRequest import SearchRequest
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


