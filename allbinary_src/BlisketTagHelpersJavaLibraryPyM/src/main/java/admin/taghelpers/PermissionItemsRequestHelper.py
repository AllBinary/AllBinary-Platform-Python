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

import datetime
from admin.taghelpers.ModifyTable import ModifyTable


class PermissionItemsRequestHelper(ModifyTable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.request: HttpServletRequest = None
        self.id: str = None
        self.enabled: str = None
        self.number: str = None
        self.who: str = None
        self.what: str = None
        self.type_: str = None
        self.remoteAddr: str = None
        self.startTime: str = None
        self.endTime: str = None
        self.price: str = None
        self.timeEntered: str = None
        self.lastModified: str = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.request = pageContext.getRequest()
        self.getFormData()
    

    def getFormData(self) -> None:
        self.id = self.request.getParameter(self.basicItemData.ID)
        self.number = self.request.getParameter(self.basicItemData.NUMBER)
        self.enabled = self.request.getParameter(EntryData.getInstance().ENABLE)
        self.who = self.request.getParameter(PermissionItemData.WHO)
        self.what = self.request.getParameter(PermissionItemData.WHAT)
        self.type_ = self.request.getParameter(PermissionItemData.TYPE)
        self.remoteAddr = self.request.getParameter(PermissionItemData.REMOTE_ADDR)
        self.startTime = self.request.getParameter(PermissionItemData.START_TIME)
        self.endTime = self.request.getParameter(PermissionItemData.END_TIME)
        self.price = self.request.getParameter(self.basicItemData.PRICE)
        self.timeEntered = self.request.getParameter(EntryData.getInstance().TIMECREATED)
        self.lastModified = self.request.getParameter(EntryData.getInstance().LASTMODIFIED)
    

    def getHashMap(self) -> dict:
        values: dict = StdUtil.getInstance().createHashMap()
        values.put(self.basicItemData.ID, self.id)
        values.put(self.basicItemData.NUMBER, self.number)
        values.put(EntryData.getInstance().ENABLE, self.enabled)
        values.put(PermissionItemData.WHO, self.who)
        values.put(PermissionItemData.WHAT, self.what)
        values.put(PermissionItemData.TYPE, self.type_)
        values.put(PermissionItemData.REMOTE_ADDR, self.remoteAddr)
        values.put(PermissionItemData.START_TIME, self.startTime)
        values.put(PermissionItemData.END_TIME, self.endTime)
        values.put(self.basicItemData.PRICE, self.price)
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        values.put(EntryData.getInstance().LASTMODIFIED, time)
        return values
    

    def insert(self) -> str:
        try:
            calendar: datetime.datetime = datetime.datetime.now()
            time: str = str(str(int(calendar.getTimeInMillis())))
            values: BasicArrayList = BasicArrayListD()
            values.add(self.id)
            values.add(self.number)
            values.add(self.enabled)
            values.add(self.who)
            values.add(self.what)
            values.add(self.type_)
            values.add(self.remoteAddr)
            values.add(self.startTime)
            values.add(self.endTime)
            values.add(self.price)
            values.add(time)
            values.add(time)
            PermissionItemsEntityFactory.getInstance().getPermissionItemsEntityInstance().insert(values)
            success: str = "Successfully inserted " + self.id + " into items table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert()")
            return success
        except Exception as e:
            error: str = "Failed to insert " + self.id + " into items table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "inserts()", e)
            return error
    

    def delete(self) -> str:
        try:
            PermissionItemsEntityFactory.getInstance().getPermissionItemsEntityInstance().delete(self.id)
            success: str = "Successfully deleted"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            error: str = "Failed to delete"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
    

    def update(self) -> str:
        try:
            success: str = "Update Pricing Successful"
            values: dict = self.getHashMap()
            PermissionItemsEntityFactory.getInstance().getPermissionItemsEntityInstance().update(values)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(str(StringMaker().append(self.id).append(CommonSeps.getInstance().SPACE).append(success)), self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update: " + self.id
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.business.user.commerce.inventory.item.permission.PermissionItemData import PermissionItemData
from org.allbinary.data.tables.user.commerce.inventory.item.permissions.PermissionItemsEntityFactory import PermissionItemsEntityFactory
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


