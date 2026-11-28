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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.control.validate.ValidationComponentInterface import ValidationComponentInterface
from views.admin.inventory.InventoryItemView import InventoryItemView


@java_inherited_overloads
class EditValidationView(*java_bases(InventoryItemView, ValidationComponentInterface)):
    def _java_defaults(self):
        vars(self).setdefault("id", None)

    def _init_fields(self) -> None:
        if "id" not in vars(self): self.id: str = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        __class__._java_defaults(self)
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface, StringUtil.getInstance().EMPTY_STRING)
        __class__._init_fields(self)
        self.getFormData()
    

    # throws Exception
    def getFormData(self) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
        hashMap: HashMap = RequestParams(self.request).toHashMap()
        if hashMap is None:
            raise Exception("No Request Params Found")
        self.id = hashMap.get(self.basicItemData.ID)
    

    # throws Exception
    def isValid(self) -> bool:
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntity import DownloadItemsEntity
        from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntityFactory import DownloadItemsEntityFactory
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        if self.id is None or not (StringValidationUtil.getInstance().isNumber(self.id)):
            return False
        self.itemInterface = InventoryEntityFactory.getInstance().getInventoryEntityInstance().getItem(self.id)
        if self.itemInterface is None:
            return False
        downloadable: int = int(self.itemInterface.getDownloads())
        if downloadable != 0:
            downloadItemsEntity: DownloadItemsEntity = DownloadItemsEntityFactory.getInstance().getDownloadItemsEntityInstance()
            self.downloadableItemVector = downloadItemsEntity.getForItem(self.itemInterface.getId())
        return True
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    # throws MoneyException
    def validationInfo(self) -> str:
        from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        stringBuffer: StringMaker = StringMaker()
        if self.id is None or not (StringValidationUtil.getInstance().isNumber(self.id)):
            stringBuffer.append("Id is not valid.<br />")
        if InventoryEntityFactory.getInstance().getInventoryEntityInstance().getItem(self.id) is None:
            stringBuffer.append("Item does not exist.<br />")
        return str(stringBuffer)
    

    # throws Exception
    def getTransformInfoInterface(self) -> TransformInfoInterface:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        return java_super_call(super(), "getTransformInfoInterface")
# from java.util.HashMap import HashMap
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.business.user.commerce.money.MoneyException import MoneyException
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
# from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntity import DownloadItemsEntity
# from org.allbinary.data.tables.user.commerce.inventory.item.downloads.DownloadItemsEntityFactory import DownloadItemsEntityFactory
# from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node


