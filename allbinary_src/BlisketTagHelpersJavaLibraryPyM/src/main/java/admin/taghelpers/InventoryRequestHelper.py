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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from admin.taghelpers.ModifyTable import ModifyTable


@java_inherited_overloads
class InventoryRequestHelper(ModifyTable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("basicItemData", None)
        vars(self).setdefault("itemInterface", None)

    def _init_fields(self) -> None:
        from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        if "itemInterface" not in vars(self): self.itemInterface: ItemInterface = None
    

    def __init__(self, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from admin.taghelpers.InventoryItemViewParentTagHelper import InventoryItemViewParentTagHelper
        from java.util.HashMap import HashMap
        from admin.tags.AbTagData import AbTagData
        from tags.HelperTag import HelperTag
        from views.admin.inventory.InventoryItemView import InventoryItemView
        super().__init__()
        __class__._init_fields(self)
        inventoryTag: HelperTag = propertiesHashMap.get(AbTagData.PARENT)
        itemView: InventoryItemView = InventoryItemViewParentTagHelper.getInstance().getInventoryItemView(inventoryTag)
        self.itemInterface = itemView.getItemInterface()
    

    # throws Exception
    def insert(self) -> str:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            dataMappingInterface: TableMappingInterface = self.getItemInterface()
            values: BasicArrayList = dataMappingInterface.toVector()
            InventoryEntityFactory.getInstance().getInventoryEntityInstance().insert(values)
            success: str = "Successfully Added Product"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert()")
            return success
        except Exception as e:
            error: str = "Failed to add item to Inventory"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insert()", e)
            return error
    

    def delete(self) -> str:
        from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
        from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, self.tagStrings.DO_START_TAG)
            return success
        except Exception as e:
            error: str = "Failed to remove item with from Inventory"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.tagStrings.DO_START_TAG, e)
            return error
    

    def update(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            self.delete()
            self.insert()
            success: str = "Item Successfully Updated"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed To Update Item"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    def getItemInterface(self) -> ItemInterface:
        from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
        return self.itemInterface
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
# from admin.tags.AbTagData import AbTagData
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.business.user.commerce.inventory.item.ItemInterface import ItemInterface
# from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
# from org.allbinary.data.tables.user.commerce.inventory.item.InventoryEntityFactory import InventoryEntityFactory
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from tags.HelperTag import HelperTag
# from views.admin.inventory.InventoryItemView import InventoryItemView
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


