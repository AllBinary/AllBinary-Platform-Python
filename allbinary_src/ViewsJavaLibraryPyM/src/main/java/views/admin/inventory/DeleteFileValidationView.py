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


class DeleteFileValidationView(InventoryItemView, ValidationComponentInterface):

    def _init_fields(self) -> None:
        self.id: str = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface, StringUtil.getInstance().EMPTY_STRING)
        self._init_fields()
        self.getFormData()
    

    # throws Exception
    def getFormData(self) -> None:
        hashMap: dict = RequestParams(self.request).toHashMap()
        if hashMap is None:
            raise Exception("No Request Params Found")
        self.id = hashMap.get(self.basicItemData.ID)
    

    def isValid(self) -> bool:
        try:
            if self.id is None or not StringValidationUtil.getInstance().isNumber(self.id):
                return False
            self.itemInterface = InventoryEntityFactory.getInstance().getInventoryEntityInstance().getItem(self.id)
            if self.itemInterface is None:
                return False
            return True
        except Exception as e:
            return False
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            if self.id is None or not StringValidationUtil.getInstance().isNumber(self.id):
                stringBuffer.append("Id is not valid.<br />")
            if InventoryEntityFactory.getInstance().getInventoryEntityInstance().getItem(self.id) is None:
                stringBuffer.append("Item does not exist.<br />")
            return str(stringBuffer)
        except Exception as e:
            return "Unkown Validation Error.<br />"
# from java.util.HashMap import HashMap
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


