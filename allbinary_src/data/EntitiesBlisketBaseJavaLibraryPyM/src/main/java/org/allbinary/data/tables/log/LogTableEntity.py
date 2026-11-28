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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.log.LogTableEntityInterface import LogTableEntityInterface


@java_inherited_overloads
class LogTableEntity(*java_bases(AbSqlBean, LogTableEntityInterface)):
    def _java_defaults(self):
        vars(self).setdefault("tableName", None)

    def _init_fields(self) -> None:
        self.tableName: str = "log"
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.LogDbInitInfo import LogDbInitInfo
        super().__init__(LogDbInitInfo())
        __class__._init_fields(self)
        self.setTableName(self.tableName)
    

    def createTableStatement(self) -> str:
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.logic.communication.http.request.AbeHttpRequestInfoData import AbeHttpRequestInfoData
        from org.allbinary.logic.string.StringMaker import StringMaker
        abeHttpRequestInfoData: AbeHttpRequestInfoData = AbeHttpRequestInfoData.getInstance()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(self.sqlStrings.ID).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(abeHttpRequestInfoData.HTTP_USER_AGENT).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(abeHttpRequestInfoData.REMOTE_HOST).append(self.sqlTypeStrings.MAX_CHAR_COLUMN).append(abeHttpRequestInfoData.REMOTE_ADDRESS).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(abeHttpRequestInfoData.REQUEST_FILE_PATH).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(abeHttpRequestInfoData.REMOTE_PORT).append(self.sqlTypeStrings.MAX_INT_UNSIGNED_NOT_NULL).append(EntryData.getInstance().TIMECREATED).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(self.sqlStrings.ID).append(self.sqlStrings.END)
        return str(stringBuffer)
    

    def createTable(self) -> str:
        return java_super_call(super(), "createTable", self.createTableStatement())
    

    def deleteWhere(self, key: str, value: str) -> None:
        java_super_call(super(), "deleteWhere", key, value)
    

    def insert(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        java_super_call(super(), "insert", values)
    

    def dropTable(self) -> str:
        return java_super_call(super(), "dropTable")
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.init.db.LogDbInitInfo import LogDbInitInfo
# from org.allbinary.logic.communication.http.request.AbeHttpRequestInfoData import AbeHttpRequestInfoData
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.util.BasicArrayList import BasicArrayList


