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
# package org.allbinary.data.tables.log

from __future__ import annotations

from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.log.LogTableEntityInterface import LogTableEntityInterface


class LogTableEntity(AbSqlBean, LogTableEntityInterface):

    def _init_fields(self) -> None:
        self.tableName: str = "log"
    

    def __init__(self) -> None:
        super().__init__(LogDbInitInfo())
        self._init_fields()
        self.setTableName(self.tableName)
    

    def createTableStatement(self) -> str:
        abeHttpRequestInfoData: AbeHttpRequestInfoData = AbeHttpRequestInfoData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(self.sqlStrings.ID).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(abeHttpRequestInfoData.HTTP_USER_AGENT).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(abeHttpRequestInfoData.REMOTE_HOST).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(abeHttpRequestInfoData.REMOTE_ADDRESS).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(abeHttpRequestInfoData.REQUEST_FILE_PATH).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(abeHttpRequestInfoData.REMOTE_PORT).append(self.sqlTypeStrings.MAX_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(self.sqlStrings.ID).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return super().createTable(self.createTableStatement())
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.init.db.LogDbInitInfo import LogDbInitInfo
from org.allbinary.logic.communication.http.request.AbeHttpRequestInfoData import AbeHttpRequestInfoData
from org.allbinary.logic.string.StringMaker import StringMaker


