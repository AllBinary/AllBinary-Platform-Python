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
class SpecialItemsRequestHelper(ModifyTable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("basicItemData", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("id", None)
        vars(self).setdefault("enabled", None)
        vars(self).setdefault("number", None)
        vars(self).setdefault("startTime", None)
        vars(self).setdefault("endTime", None)
        vars(self).setdefault("price", None)
        vars(self).setdefault("timeEntered", None)
        vars(self).setdefault("lastModified", None)

    def _init_fields(self) -> None:
        from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "id" not in vars(self): self.id: str = None
        if "enabled" not in vars(self): self.enabled: str = None
        if "number" not in vars(self): self.number: str = None
        if "startTime" not in vars(self): self.startTime: str = None
        if "endTime" not in vars(self): self.endTime: str = None
        if "price" not in vars(self): self.price: str = None
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
        from org.allbinary.business.user.commerce.inventory.item.special.SpecialItemData import SpecialItemData
        self.id = self.request.getParameter(self.basicItemData.ID)
        self.number = self.request.getParameter(self.basicItemData.NUMBER)
        self.enabled = self.request.getParameter(EntryData.getInstance().ENABLE)
        self.startTime = self.request.getParameter(SpecialItemData.START_TIME)
        self.endTime = self.request.getParameter(SpecialItemData.END_TIME)
        self.price = self.request.getParameter(self.basicItemData.PRICE)
        self.timeEntered = self.request.getParameter(EntryData.getInstance().TIMECREATED)
        self.lastModified = self.request.getParameter(EntryData.getInstance().LASTMODIFIED)
    

    def getHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.commerce.inventory.item.special.SpecialItemData import SpecialItemData
        from org.allbinary.logic.StdUtil import StdUtil
        values: HashMap = StdUtil.getInstance().createHashMap()
        values.put(self.basicItemData.ID, self.id)
        values.put(self.basicItemData.NUMBER, self.number)
        values.put(EntryData.getInstance().ENABLE, self.enabled)
        values.put(SpecialItemData.START_TIME, self.startTime)
        values.put(SpecialItemData.END_TIME, self.endTime)
        values.put(self.basicItemData.PRICE, self.price)
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        values.put(EntryData.getInstance().LASTMODIFIED, time)
        return values
    

    def insert(self) -> str:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.data.tables.user.commerce.inventory.item.special.SpecialItemsEntityFactory import SpecialItemsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            values: BasicArrayList = BasicArrayListD()
            values.add(self.id)
            values.add(self.number)
            values.add(self.enabled)
            values.add(self.startTime)
            values.add(self.endTime)
            values.add(self.price)
            values.add(time)
            values.add(time)
            SpecialItemsEntityFactory.getInstance().getSpecialItemsEntityInstance().insert(values)
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
        from org.allbinary.data.tables.user.commerce.inventory.item.special.SpecialItemsEntityFactory import SpecialItemsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            SpecialItemsEntityFactory.getInstance().getSpecialItemsEntityInstance().delete(self.id)
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
        from org.allbinary.data.tables.user.commerce.inventory.item.special.SpecialItemsEntityFactory import SpecialItemsEntityFactory
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Update Successful"
            values: HashMap = self.getHashMap()
            SpecialItemsEntityFactory.getInstance().getSpecialItemsEntityInstance().update(values)
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
# from org.allbinary.business.user.commerce.inventory.item.special.SpecialItemData import SpecialItemData
# from org.allbinary.data.tables.user.commerce.inventory.item.special.SpecialItemsEntityFactory import SpecialItemsEntityFactory
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


