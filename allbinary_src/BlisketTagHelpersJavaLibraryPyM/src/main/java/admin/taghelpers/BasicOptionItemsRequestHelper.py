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


class BasicOptionItemsRequestHelper(ModifyTable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.request: HttpServletRequest = None
        self.id: str = None
        self.optionOneTitle: str = None
        self.defaultOptionItem: str = None
        self.defaultOptionValue: str = None
        self.optionItem: BasicArrayList = None
        self.optionValue: BasicArrayList = None
        self.timeEntered: str = None
        self.lastModified: str = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.request = pageContext.getRequest()
        self.getFormData()
    

    def getFormData(self) -> None:
        self.optionItem = BasicArrayListD()
        self.optionValue = BasicArrayListD()
        self.id = self.request.getParameter(self.basicItemData.ID)
        self.optionOneTitle = self.request.getParameter(BasicOptionItemData.OPTION_ONE_TITLE)
        self.defaultOptionItem = self.request.getParameter(BasicOptionItemData.DEFAULT_OPTION_ITEM)
        self.defaultOptionValue = self.request.getParameter(BasicOptionItemData.DEFAULT_OPTION_VALUE)
        self.optionItem.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_ONE_ITEM))
        self.optionValue.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_ONE_VALUE))
        self.optionItem.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_TWO_ITEM))
        self.optionValue.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_TWO_VALUE))
        self.optionItem.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_THREE_ITEM))
        self.optionValue.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_THREE_VALUE))
        self.optionItem.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_FOUR_ITEM))
        self.optionValue.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_FOUR_VALUE))
        self.optionItem.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_FIVE_ITEM))
        self.optionValue.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_FIVE_VALUE))
        self.optionItem.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_SIX_ITEM))
        self.optionValue.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_SIX_VALUE))
        self.optionItem.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_SEVEN_ITEM))
        self.optionValue.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_SEVEN_VALUE))
        self.optionItem.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_EIGHT_ITEM))
        self.optionValue.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_EIGHT_VALUE))
        self.optionItem.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_NINE_ITEM))
        self.optionValue.add(self.request.getParameter(BasicOptionItemData.OPTION_ONE_NINE_VALUE))
        self.timeEntered = self.request.getParameter(EntryData.getInstance().TIMECREATED)
        self.lastModified = self.request.getParameter(EntryData.getInstance().LASTMODIFIED)
    

    def getHashMap(self) -> dict:
        values: dict = StdUtil.getInstance().createHashMap()
        values.put(self.basicItemData.ID, self.id)
        values.put(BasicOptionItemData.OPTION_ONE_ONE_ITEM, self.optionItem.get(0))
        values.put(BasicOptionItemData.OPTION_ONE_ONE_VALUE, self.optionValue.get(0))
        values.put(BasicOptionItemData.OPTION_ONE_TWO_ITEM, self.optionItem.get(1))
        values.put(BasicOptionItemData.OPTION_ONE_TWO_VALUE, self.optionValue.get(1))
        values.put(BasicOptionItemData.OPTION_ONE_THREE_ITEM, self.optionItem.get(2))
        values.put(BasicOptionItemData.OPTION_ONE_THREE_VALUE, self.optionValue.get(2))
        values.put(BasicOptionItemData.OPTION_ONE_FOUR_ITEM, self.optionItem.get(3))
        values.put(BasicOptionItemData.OPTION_ONE_FOUR_VALUE, self.optionValue.get(3))
        values.put(BasicOptionItemData.OPTION_ONE_FIVE_ITEM, self.optionItem.get(4))
        values.put(BasicOptionItemData.OPTION_ONE_FIVE_VALUE, self.optionValue.get(4))
        values.put(BasicOptionItemData.OPTION_ONE_SIX_ITEM, self.optionItem.get(5))
        values.put(BasicOptionItemData.OPTION_ONE_SIX_VALUE, self.optionValue.get(5))
        values.put(BasicOptionItemData.OPTION_ONE_SEVEN_ITEM, self.optionItem.get(6))
        values.put(BasicOptionItemData.OPTION_ONE_SEVEN_VALUE, self.optionValue.get(6))
        values.put(BasicOptionItemData.OPTION_ONE_EIGHT_ITEM, self.optionItem.get(7))
        values.put(BasicOptionItemData.OPTION_ONE_EIGHT_VALUE, self.optionValue.get(7))
        values.put(BasicOptionItemData.OPTION_ONE_NINE_ITEM, self.optionItem.get(8))
        values.put(BasicOptionItemData.OPTION_ONE_NINE_VALUE, self.optionValue.get(8))
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
            size: int = self.optionValue.size()
            for index in range(0, size):
                values.add(self.optionValue.get(index))
                values.add(self.optionItem.get(index))
            values.add(time)
            values.add(time)
            BasicOptionItemsEntityFactory.getInstance().getBasicOptionItemsEntityInstance().insert(values)
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
            BasicOptionItemsEntityFactory.getInstance().getBasicOptionItemsEntityInstance().delete(self.id)
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
            BasicOptionItemsEntityFactory.getInstance().getBasicOptionItemsEntityInstance().update(values)
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
from org.allbinary.business.user.commerce.inventory.item.option.BasicOptionItemData import BasicOptionItemData
from org.allbinary.data.tables.user.commerce.inventory.item.options.BasicOptionItemsEntityFactory import BasicOptionItemsEntityFactory
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


