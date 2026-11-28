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
import datetime
from admin.taghelpers.ModifyTable import ModifyTable


@java_inherited_overloads
class BasicGroupItemsRequestHelper(ModifyTable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("basicItemData", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("id", None)
        vars(self).setdefault("itemOne", None)
        vars(self).setdefault("itemTwo", None)
        vars(self).setdefault("itemThree", None)
        vars(self).setdefault("itemFour", None)
        vars(self).setdefault("itemFive", None)
        vars(self).setdefault("itemSix", None)
        vars(self).setdefault("itemSeven", None)
        vars(self).setdefault("itemEight", None)
        vars(self).setdefault("itemNine", None)
        vars(self).setdefault("itemTen", None)
        vars(self).setdefault("timeEntered", None)
        vars(self).setdefault("lastModified", None)

    def _init_fields(self) -> None:
        from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "id" not in vars(self): self.id: str = None
        if "itemOne" not in vars(self): self.itemOne: str = None
        if "itemTwo" not in vars(self): self.itemTwo: str = None
        if "itemThree" not in vars(self): self.itemThree: str = None
        if "itemFour" not in vars(self): self.itemFour: str = None
        if "itemFive" not in vars(self): self.itemFive: str = None
        if "itemSix" not in vars(self): self.itemSix: str = None
        if "itemSeven" not in vars(self): self.itemSeven: str = None
        if "itemEight" not in vars(self): self.itemEight: str = None
        if "itemNine" not in vars(self): self.itemNine: str = None
        if "itemTen" not in vars(self): self.itemTen: str = None
        if "timeEntered" not in vars(self): self.timeEntered: str = None
        if "lastModified" not in vars(self): self.lastModified: str = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        super().__init__()
        __class__._init_fields(self)
        self.request = pageContext.getRequest()
        self.getFormData()
    

    def getFormData(self) -> None:
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.commerce.inventory.item.group.BasicGroupItemData import BasicGroupItemData
        self.id = self.request.getParameter(self.basicItemData.ID)
        self.itemOne = self.request.getParameter(BasicGroupItemData.ITEM_ONE)
        self.itemTwo = self.request.getParameter(BasicGroupItemData.ITEM_TWO)
        self.itemThree = self.request.getParameter(BasicGroupItemData.ITEM_THREE)
        self.itemFour = self.request.getParameter(BasicGroupItemData.ITEM_FOUR)
        self.itemFive = self.request.getParameter(BasicGroupItemData.ITEM_FIVE)
        self.itemSix = self.request.getParameter(BasicGroupItemData.ITEM_SIX)
        self.itemSeven = self.request.getParameter(BasicGroupItemData.ITEM_SEVEN)
        self.itemEight = self.request.getParameter(BasicGroupItemData.ITEM_EIGHT)
        self.itemNine = self.request.getParameter(BasicGroupItemData.ITEM_NINE)
        self.itemTen = self.request.getParameter(BasicGroupItemData.ITEM_TEN)
        self.timeEntered = self.request.getParameter(EntryData.getInstance().TIMECREATED)
        self.lastModified = self.request.getParameter(EntryData.getInstance().LASTMODIFIED)
    

    def getHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.commerce.inventory.item.group.BasicGroupItemData import BasicGroupItemData
        from org.allbinary.logic.StdUtil import StdUtil
        values: HashMap = StdUtil.getInstance().createHashMap()
        values.put(self.basicItemData.ID, self.id)
        values.put(BasicGroupItemData.ITEM_ONE, self.itemOne)
        values.put(BasicGroupItemData.ITEM_TWO, self.itemTwo)
        values.put(BasicGroupItemData.ITEM_THREE, self.itemThree)
        values.put(BasicGroupItemData.ITEM_FOUR, self.itemFour)
        values.put(BasicGroupItemData.ITEM_FIVE, self.itemFive)
        values.put(BasicGroupItemData.ITEM_SIX, self.itemSix)
        values.put(BasicGroupItemData.ITEM_SEVEN, self.itemSeven)
        values.put(BasicGroupItemData.ITEM_EIGHT, self.itemEight)
        values.put(BasicGroupItemData.ITEM_NINE, self.itemNine)
        values.put(BasicGroupItemData.ITEM_TEN, self.itemTen)
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        values.put(EntryData.getInstance().LASTMODIFIED, time)
        return values
    

    def insert(self) -> str:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.data.tables.user.commerce.inventory.item.groups.BasicGroupItemsEntityFactory import BasicGroupItemsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            values: BasicArrayList = BasicArrayListD()
            values.add(self.id)
            values.add(self.itemOne)
            values.add(self.itemTwo)
            values.add(self.itemThree)
            values.add(self.itemFour)
            values.add(self.itemFive)
            values.add(self.itemSix)
            values.add(self.itemSeven)
            values.add(self.itemEight)
            values.add(self.itemNine)
            values.add(self.itemTen)
            values.add(time)
            values.add(time)
            BasicGroupItemsEntityFactory.getInstance().getBasicGroupItemsEntityInstance().insert(values)
            success: str = "Successfully inserted " + self.id + " into items table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert()")
            return success
        except Exception as e:
            error: str = "Failed to insert " + self.id + " into items table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "inserts()", e)
            return error
    

    def delete(self) -> str:
        from org.allbinary.data.tables.user.commerce.inventory.item.groups.BasicGroupItemsEntityFactory import BasicGroupItemsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            BasicGroupItemsEntityFactory.getInstance().getBasicGroupItemsEntityInstance().delete(self.id)
            success: str = "Successfully deleted"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            error: str = "Failed to delete"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
    

    def update(self) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.data.tables.user.commerce.inventory.item.groups.BasicGroupItemsEntityFactory import BasicGroupItemsEntityFactory
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Update Pricing Successful"
            values: HashMap = self.getHashMap()
            BasicGroupItemsEntityFactory.getInstance().getBasicGroupItemsEntityInstance().update(values)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(str(StringMaker().append(self.id).append(CommonSeps.getInstance().SPACE).append(success)), self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update: " + self.id
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
# from org.allbinary.business.user.commerce.inventory.item.group.BasicGroupItemData import BasicGroupItemData
# from org.allbinary.data.tables.user.commerce.inventory.item.groups.BasicGroupItemsEntityFactory import BasicGroupItemsEntityFactory
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


