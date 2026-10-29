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
# package views.admin.inventory

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.admin.inventory.InventoryItemView import InventoryItemView


class NewValidationView(InventoryItemView, ValidationComponentInterface):
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface, StringUtil.getInstance().EMPTY_STRING)
        self.itemInterface = BasicItem()
    

    def isValid(self) -> bool:
        try:
            return True
        except Exception as e:
            return False
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    def validationInfo(self) -> str:
        return "Error Creating New Item"
from org.allbinary.business.user.commerce.inventory.item.BasicItem import BasicItem
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


