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

from org.allbinary.logic.communication.sql.AbSqlTable import AbSqlTable


class AbSqlColumn(AbSqlTable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.LARGEST_INT_VALUE_IN_COLUMN: str = "\nLargest Int Value in column: "
        self.METHOD_GET_LARGETS_INTEGER_IN_COLUMN: str = "getLargestIntegerInColumn"
        self.METHOD_GET_COLUMN: str = "getColumn"
        self.METHOD_GET_COLUMN_WHERE: str = "getColumnWhere"
        self.INVALID_RESULT: str = "-1"
    

    def __init__(self, databaseConnectionInfoInterface: DbConnectionInfo) -> None:
        super().__init__(databaseConnectionInfoInterface)
        self._init_fields()
    

    def getLargestIntegerInColumnWhere(self, columnName: str, key: str, value: str) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT)
        stringBuffer.append(columnName)
        stringBuffer.append(self.sqlStrings.FROM)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.WHERE)
        stringBuffer.append(key)
        stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
        stringBuffer.append(value)
        stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
        sqlStatement: str = str(stringBuffer)
        try:
            largest: int = 0
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            while rset.next():
                intValue: int = rset.getInt(columnName)
                if intValue > largest:
                    largest = intValue
            largestAsString: str = str(int(largest))
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(self.sqlStrings.SQL_STATEMENT_LABEL)
                stringBuffer.append(sqlStatement)
                stringBuffer.append(self.LARGEST_INT_VALUE_IN_COLUMN)
                stringBuffer.append(largestAsString)
                self.logUtil.putF(str(stringBuffer), self, self.METHOD_GET_LARGETS_INTEGER_IN_COLUMN)
            return largestAsString
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_GET_LARGETS_INTEGER_IN_COLUMN, e)
            return self.INVALID_RESULT
    

    def getColumn(self, columnName: str) -> BasicArrayList:
        column: BasicArrayList = BasicArrayListD()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT)
        stringBuffer.append(columnName)
        stringBuffer.append(self.sqlStrings.FROM)
        stringBuffer.append(self.getTableName())
        sqlStatement: str = str(stringBuffer)
        try:
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            while rset.next():
                field: str = str(rset.getObject(columnName))
                column.add(field)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(self.sqlStrings.SQL_STATEMENT_LABEL)
                stringBuffer.append(sqlStatement)
                stringBuffer.append(self.sqlStrings.COLUMN_VALUE)
                stringBuffer.append(str(column))
                self.logUtil.putF(str(stringBuffer), self, self.METHOD_GET_COLUMN)
            return column
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_GET_COLUMN, e)
            return column
    

    def getColumnWhere(self, columnName: str, key: str, value: str) -> BasicArrayList:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT)
        stringBuffer.append(columnName)
        stringBuffer.append(self.sqlStrings.FROM)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.WHERE)
        stringBuffer.append(key)
        stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
        stringBuffer.append(value)
        stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
        sqlStatement: str = str(stringBuffer)
        column: BasicArrayList = BasicArrayListD()
        rset: ResultSet = None
        field: str = None
        try:
            rset = self.executeSQLStatement(sqlStatement)
            while rset.next():
                field = str(rset.getObject(columnName))
                column.add(field)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(self.sqlStrings.SQL_STATEMENT_LABEL)
                stringBuffer.append(sqlStatement)
                stringBuffer.append(self.sqlStrings.COLUMN_VALUE)
                stringBuffer.append(str(column))
                self.logUtil.putF(str(stringBuffer), self, self.METHOD_GET_COLUMN_WHERE)
            return column
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_GET_COLUMN_WHERE, e)
            return column
# from java.sql.ResultSet import ResultSet
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


