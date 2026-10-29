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
# package org.allbinary.logic.communication.sql

from __future__ import annotations

from org.allbinary.logic.communication.sql.AbSqlRow import AbSqlRow


class AbSqlBean(AbSqlRow):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.METHOD_GET_FIELD: str = "getField"
        self.METHOD_IS_SUBSET_OF_ENTRY: str = "isSubsetOfEntry"
    

    def __init__(self, databaseConnectionInfoInterface: DbConnectionInfo) -> None:
        super().__init__(databaseConnectionInfoInterface)
        self._init_fields()
    

    def getField(self, key: str, value: str, requestedField: str) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT)
        stringBuffer.append(requestedField)
        stringBuffer.append(self.sqlStrings.FROM)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.WHERE)
        stringBuffer.append(key)
        stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
        stringBuffer.append(value)
        stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
        sqlStatement: str = str(stringBuffer)
        try:
            field: str = self.stringUtil.EMPTY_STRING
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            while rset.next():
                field = rset.getString(requestedField)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append(self.sqlStrings.SQL_STATEMENT_LABEL)
                    stringBuffer.append(sqlStatement)
                    stringBuffer.append(self.sqlStrings.FIELD_VALUE)
                    stringBuffer.append(field)
                    self.logUtil.putF(str(stringBuffer), self, self.METHOD_GET_FIELD)
                return field
            return None
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_GET_FIELD, e)
            return str(self.FAILED_SQL_STATEMENT) + sqlStatement
    

    # Java overloaded method: Python keeps the last definition
    def getField(self, keysAndValues: dict, requestedField: str) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT)
        stringBuffer.append(requestedField)
        stringBuffer.append(self.sqlStrings.FROM)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.WHERE)
        try:
            field: str = self.stringUtil.EMPTY_STRING
            set: Set = keysAndValues.keySet()
            keyArray: list[object] = set.toArray()
            size: int = len(keyArray)
            key: str = None
            value: str = None
            for i in range(0, size):
                key = keyArray[i]
                value = str(keysAndValues.get(key))
                stringBuffer.append(key)
                stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
                stringBuffer.append(value)
                stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
                if i < size - 1:
                    stringBuffer.append(self.sqlStrings.AND)
            sqlStatement: str = str(stringBuffer)
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            while rset.next():
                field = rset.getString(requestedField)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append(self.sqlStrings.SQL_STATEMENT_LABEL)
                    stringBuffer.append(sqlStatement)
                    stringBuffer.append(self.sqlStrings.FIELD_VALUE)
                    stringBuffer.append(field)
                    self.logUtil.putF(str(stringBuffer), self, self.METHOD_GET_FIELD)
                return field
            return None
        except Exception as e:
            sqlStatement: str = str(stringBuffer)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_GET_FIELD, e)
            return str(self.FAILED_SQL_STATEMENT) + sqlStatement
    

    def isSubsetOfEntry(self, key: str, value: str, columnsAndValues: dict) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT)
        try:
            keyArray: list[object] = columnsAndValues.keySet().toArray()
            size: int = len(keyArray)
            stringBuffer.append(self.commonSeps.SPACE)
            stringBuffer.append(key)
            for i in range(0, size):
                stringBuffer.append(self.commonSeps.SPACE)
                stringBuffer.append(str(keyArray[i]))
            stringBuffer.append(self.sqlStrings.FROM)
            stringBuffer.append(self.getTableName())
            stringBuffer.append(self.sqlStrings.WHERE)
            stringBuffer.append(key)
            stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
            stringBuffer.append(value)
            stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
            sqlStatement: str = str(stringBuffer)
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            columnName: str = None
            field: str = None
            while rset.next():
                keyArray2: list[object] = columnsAndValues.keySet().toArray()
                size2: int = len(keyArray2)
                for i in range(0, size2):
                    columnName = str(keyArray2[i])
                    field = str(rset.getObject(columnName))
                    if ((field > columnsAndValues.get(columnName)) - (field < columnsAndValues.get(columnName))) != 0:
                        return org.allbinary.globals.GLOBALS2.NOTASUBSET
            if rset.getRow() != 1:
                return org.allbinary.globals.GLOBALS2.NOTASUBSET
            else:
                return org.allbinary.globals.GLOBALS2.ISASUBSET
        except Exception as e:
            sqlStatement: str = str(stringBuffer)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_IS_SUBSET_OF_ENTRY, e)
            return str(self.FAILED_SQL_STATEMENT) + sqlStatement
# from java.sql.ResultSet import ResultSet
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


