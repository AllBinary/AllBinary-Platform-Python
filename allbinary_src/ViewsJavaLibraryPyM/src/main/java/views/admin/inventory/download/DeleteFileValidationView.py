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
# package views.admin.inventory.download

from __future__ import annotations

from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.admin.inventory.download.DownloadableInventoryItemView import DownloadableInventoryItemView


class DeleteFileValidationView(DownloadableInventoryItemView, ValidationComponentInterface):

    def _init_fields(self) -> None:
        self.downloadItemId: str = None
    

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
        self.downloadItemId = hashMap.get(DownloadItemData.ID)
    

    def isValid(self) -> bool:
        try:
            if self.id is None or not StringValidationUtil.getInstance().isNumber(self.id):
                return False
            inventoryEntity: InventoryEntity = InventoryEntityFactory.getInstance().getInventoryEntityInstance()
            self.itemInterface = inventoryEntity.getItem(self.id)
            if self.itemInterface is None:
                return False
            downloadItemsEntity: DownloadItemsEntity = DownloadItemsEntityFactory.getInstance().getDownloadItemsEntityInstance()
            vector: BasicArrayList = downloadItemsEntity.getForItem(self.id, self.downloadItemId)
            if vector.size() != 1:
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
            downloadItemsEntity: DownloadItemsEntity = DownloadItemsEntityFactory.getInstance().getDownloadItemsEntityInstance()
            vector: BasicArrayList = downloadItemsEntity.getForItem(self.id, self.downloadItemId)
            if vector.size() == 0:
                stringBuffer.append("DownloadItem does not exist.<br />")
            if vector.size() > 1:
                stringBuffer.append("To Many DownloadItems exist.<br />")
            return str(stringBuffer)
        except Exception as e:
            return "Unkown Validation Error.<br />"
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.business.user.commerce.inventory.item.download.DownloadItemData import DownloadItemData
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntity import InventoryEntity
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntity import DownloadItemsEntity
from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntityFactory import DownloadItemsEntityFactory
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


