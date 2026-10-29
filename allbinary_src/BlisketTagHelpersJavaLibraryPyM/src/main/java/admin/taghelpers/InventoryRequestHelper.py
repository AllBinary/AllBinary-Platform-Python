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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.ModifyTable import ModifyTable


class InventoryRequestHelper(ModifyTable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.itemInterface: ItemInterface = None
    

    def __init__(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        from admin.taghelpers.InventoryItemViewParentTagHelper import InventoryItemViewParentTagHelper
        super().__init__()
        self._init_fields()
        inventoryTag: HelperTag = propertiesHashMap.get(AbTagData.PARENT)
        itemView: InventoryItemView = InventoryItemViewParentTagHelper.getInstance().getInventoryItemView(inventoryTag)
        self.itemInterface = itemView.getItemInterface()
    

    # throws Exception
    def insert(self) -> str:
        try:
            dataMappingInterface: TableMappingInterface = self.getItemInterface()
            values: BasicArrayList = dataMappingInterface.toVector()
            InventoryEntityFactory.getInstance().getInventoryEntityInstance().insert(values)
            success: str = "Successfully Added Product"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert()")
            return success
        except Exception as e:
            error: str = "Failed to add item to Inventory"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insert()", e)
            return error
    

    def delete(self) -> str:
        try:
            dataMappingInterface: TableMappingInterface = self.getItemInterface()
            id: str = dataMappingInterface.getKey()
            InventoryEntityFactory.getInstance().getInventoryEntityInstance().deleteWhere(self.basicItemData.ID, id)
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Successfully Removed the item with ")
            stringBuffer.append(self.basicItemData.ID)
            stringBuffer.append("=")
            stringBuffer.append(id)
            stringBuffer.append(" from to the Inventory table")
            success: str = str(stringBuffer)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, self.tagStrings.DO_START_TAG)
            return success
        except Exception as e:
            error: str = "Failed to remove item with from Inventory"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.tagStrings.DO_START_TAG, e)
            return error
    

    def update(self) -> str:
        try:
            self.delete()
            self.insert()
            success: str = "Item Successfully Updated"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed To Update Item"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    def getItemInterface(self) -> ItemInterface:
        return self.itemInterface
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
from admin.tags.AbTagData import AbTagData
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from tags.HelperTag import HelperTag
from views.admin.inventory.InventoryItemView import InventoryItemView


