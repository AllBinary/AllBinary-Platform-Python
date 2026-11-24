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
# package org.allbinary.data.tables.user.quoterequest

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.user.quoterequest.QuoteRequestEntityInterface import QuoteRequestEntityInterface


class QuoteRequestEntity(*java_bases(AbSqlBean, QuoteRequestEntityInterface)):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "quoterequest"
    

    def __init__(self) -> None:
        from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def insert(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            super().insert(values)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    # throws Exception
    def get(self, userName: str, id: int) -> QuoteRequest:
        from java.util.HashMap import HashMap
        from org.allbinary.business.quoterequest.QuoteRequestData import QuoteRequestData
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.quoterequest.QuoteRequest import QuoteRequest
        from org.allbinary.logic.StdUtil import StdUtil
        row: HashMap = StdUtil.getInstance().createHashMap()
        row.put(UserData.USERNAME, userName)
        row.put(QuoteRequestData.getInstance().ID, str(id))
        quoteRequestHashMap: HashMap = super().getRow(row)
        if quoteRequestHashMap is not None:
            return QuoteRequest(quoteRequestHashMap)
        else:
            return None
    

    def getIds(self, userName: str) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.business.quoterequest.QuoteRequestData import QuoteRequestData
        from org.allbinary.business.user.UserData import UserData
        return super().getColumnWhere(QuoteRequestData.getInstance().ID, UserData.USERNAME, userName)
    

    def deleteWhere(self, key: str, value: str) -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            super().deleteWhere(key, value)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.commonStrings.SUCCESS, self, "deleteWhere")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.put(self.commonStrings.FAILURE, self, "deleteWhere", e)
    

    def createTableStatement(self) -> str:
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.quoterequest.QuoteRequestData import QuoteRequestData
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.logic.string.StringMaker import StringMaker
        quoteRequestData: QuoteRequestData = QuoteRequestData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START)
        stringBuffer.append(quoteRequestData.ID).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(UserData.USERNAME)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(quoteRequestData.PROJECT_INFO)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(quoteRequestData.CUSTOMER_COMMENTS)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(quoteRequestData.BUDGET)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(quoteRequestData.TIMEFRAME)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(quoteRequestData.COMMENTS)
        stringBuffer.append(self.sqlTypeStrings.BLOB_NOT_NULL)
        stringBuffer.append(EntryData.getInstance().TIMECREATED)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(EntryData.getInstance().LASTMODIFIED)
        stringBuffer.append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL)
        stringBuffer.append(self.sqlStrings.PRIMARY_KEY)
        stringBuffer.append(quoteRequestData.ID)
        stringBuffer.append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
    

    def dropTable(self) -> str:
        result: str = str(super().dropTable())
        return result
    

    def update(self, userName: str, updatedValues: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserData import UserData
        super().updateWhere(UserData.USERNAME, userName, updatedValues)
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
# from org.allbinary.business.quoterequest.QuoteRequestData import QuoteRequestData
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.business.user.quoterequest.QuoteRequest import QuoteRequest
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


