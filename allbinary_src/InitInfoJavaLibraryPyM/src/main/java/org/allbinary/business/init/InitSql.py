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
# package org.allbinary.business.init

from __future__ import annotations

import threading


class InitSql:
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.sqlTypeStrings: SqlTypeStrings = SqlTypeStrings.getInstance()
        self.sqlStrings: SqlStrings = SqlStrings.getInstance()
        self.stdUtil: StdUtil = StdUtil.getInstance()
        self.INSERT: str = "insert"
        self.UPDATE: str = "update"
        self.databaseConnectionInfoInterface: DbConnectionInfo = None
        self.userid: str = None
        self.password: str = None
        self.tableName: str = None
        self.conn: Connection = None
        self.useridAndPassword: bool = False
        self.SUCCESS_SQL_STATEMENT: str = "Success\nSQL Statement: "
        self.FAILED_SQL_STATEMENT: str = "Failed\nSQL Statement: "
        self.INIT_SQL: str = "InitSql"
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.EQUAL_QUOTE: str = "=\""
        self.METHOD_GET_ROW: str = "getRow()"
        self.METHOD_UPDATE_WHERE: str = "updateWhere()"
        self.ROW_VALUE_LABEL: str = "Row Value: "
        self.NO_RESULTS_IN_RESULT_SET: str = "No Results in ResultSet"
        self.INSERT_END: str = "')"
    

    def __init__(self, databaseConnectionInfoInterface: DbConnectionInfo) -> None:
        self._init_fields()
        self.setDatabaseConnectionInfoInterface(databaseConnectionInfoInterface)
    

    def setTable(self, tableName: str) -> None:
        self.tableName = tableName
    

    def setDatabaseConnectionInfoInterface(self, databaseConnectionInfoInterface: DbConnectionInfo) -> None:
        self.databaseConnectionInfoInterface = databaseConnectionInfoInterface
    

    def createTable(self, tableData: str) -> bool:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Creating Table: ")
            stringBuffer.append(tableData)
            PreLogUtil.put(str(stringBuffer), self.INIT_SQL, "createTable()")
            self.executeSQLStatement(tableData)
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                PreLogUtil.putOE(self.commonStrings.EXCEPTION, self.INIT_SQL, "createTable()", e)
            return False
    

    def dropTable(self) -> bool:
        sqlStatement: str = str(self.sqlStrings.DROP_TABLE) + self.tableName
        try:
            self.executeSQLStatement(sqlStatement)
            return True
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                PreLogUtil.putOE(self.commonStrings.EXCEPTION, self.INIT_SQL, "dropTables()", e)
            return False
    

    def getRow(self, keysAndValues: dict) -> dict:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT_ALL_FROM)
        stringBuffer.append(self.tableName)
        stringBuffer.append(self.sqlStrings.WHERE)
        try:
            result: dict = None
            set: Set = keysAndValues.keySet()
            keyArray: list[object] = set.toArray()
            size: int = len(keyArray)
            for i in range(0, size):
                key: str = keyArray[i]
                value: str = str(keysAndValues.get(key))
                stringBuffer.append(key)
                stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
                stringBuffer.append(self.getValue(value))
                stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
                if i < size - 1:
                    stringBuffer.append(self.sqlStrings.AND)
            sqlStatement: str = str(stringBuffer)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                PreLogUtil.put(str(self.sqlStrings.SQL_STATEMENT_LABEL) + sqlStatement, self.INIT_SQL, self.METHOD_GET_ROW)
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            resultSetMetaData: ResultSetMetaData = rset.getMetaData()
            while rset.next():
                result = self.stdUtil.createHashMap()
                columnCount: int = resultSetMetaData.getColumnCount()
                for index in range(1, columnCount + 1):
                    columnName: str = resultSetMetaData.getColumnName(index)
                    field: str = rset.getString(columnName)
                    result.put(columnName, field)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    PreLogUtil.put(self.ROW_VALUE_LABEL + str(result), self.INIT_SQL, self.METHOD_GET_ROW)
                return result
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                PreLogUtil.put(self.NO_RESULTS_IN_RESULT_SET, self.INIT_SQL, self.METHOD_GET_ROW)
            return None
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                PreLogUtil.putOE(self.FAILED_SQL_STATEMENT + str(stringBuffer), self.INIT_SQL, self.METHOD_GET_ROW, e)
            return None
    

    def updateWhere(self, key: str, value: str, updatedKeyValuePairs: dict) -> None:
        with self._lock:
            return self._updateWhere_unlocked(key, value, updatedKeyValuePairs)

    def _updateWhere_unlocked(self, key: str, value: str, updatedKeyValuePairs: dict) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.UPDATE)
        stringBuffer.append(self.tableName)
        stringBuffer.append(self.sqlStrings.SET)
        try:
            columnArray: list[object] = updatedKeyValuePairs.keySet().toArray()
            size: int = len(columnArray)
            for i in range(0, size):
                columnName: str = str(columnArray[i])
                stringBuffer.append(self.commonSeps.SPACE)
                stringBuffer.append(columnName)
                stringBuffer.append(self.EQUAL_QUOTE)
                columnValue: str = updatedKeyValuePairs.get(columnName)
                if columnValue is None:
                    columnValue = self.stringUtil.EMPTY_STRING
                else:
                    pass
                stringBuffer.append(self.getValue(columnValue))
                stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
                if i < size - 1:
                    stringBuffer.append(self.commonSeps.COMMA)
            stringBuffer.append(self.sqlStrings.WHERE)
            stringBuffer.append(key)
            stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
            stringBuffer.append(self.getValue(value))
            stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
            sqlStatement: str = str(stringBuffer)
            self.executeSQLStatement(sqlStatement)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                PreLogUtil.put(self.SUCCESS_SQL_STATEMENT + sqlStatement, self.INIT_SQL, self.METHOD_UPDATE_WHERE)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                PreLogUtil.putOE(self.FAILED_SQL_STATEMENT + str(stringBuffer), self.INIT_SQL, self.METHOD_UPDATE_WHERE, e)
    

    def insert(self, values: BasicArrayList) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.INSERT_INTO)
        stringBuffer.append(self.tableName)
        stringBuffer.append(self.sqlStrings.VALUES)
        try:
            size: int = values.size()
            for i in range(0, size - 1):
                value: str = self.getValue(values.get(i))
                stringBuffer.append(value)
                stringBuffer.append(self.sqlStrings.SINGLE_QUOTE_COMMA_SEP)
            value: str = self.getValue(values.get(values.size() - 1))
            stringBuffer.append(value)
            stringBuffer.append(self.INSERT_END)
            sqlStatement: str = str(stringBuffer)
            self.executeSQLStatement(sqlStatement)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                PreLogUtil.put(self.SUCCESS_SQL_STATEMENT + sqlStatement, self.INIT_SQL, self.INSERT)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                PreLogUtil.putOE(self.FAILED_SQL_STATEMENT + str(stringBuffer), self.INIT_SQL, self.INSERT, e)
    

    def getValue(self, value: str) -> str:
        with self._lock:
            return self._getValue_unlocked(value)

    def _getValue_unlocked(self, value: str) -> str:
        if StringValidationUtil.getInstance().isEmpty(value):
            return self.stringUtil.EMPTY_STRING
        else:
            return value
    

    # throws Exception, SQLException
    def executeSQLStatement(self, statement: str) -> ResultSet:
        try:
            if self.conn is None:
                self.initialize()
            stmt: Statement = self.conn.createStatement()
            stmt.execute(statement)
            rset: ResultSet = stmt.getResultSet()
            stmt.close()
            return rset
        except SQLException as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                PreLogUtil.putOE(self.commonStrings.EXCEPTION, self.INIT_SQL, "executeSQLStatement()", e)
            raise e
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                PreLogUtil.putOE(self.commonStrings.EXCEPTION, self.INIT_SQL, "executeSQLStatement()", e)
            raise e
    

    # throws SQLException
    def createConnection(self) -> None:
        try:
            if self.useridAndPassword == True:
                self.conn = DriverManager.getConnection(self.databaseConnectionInfoInterface.getUrl(), self.userid, self.password)
            else:
                self.conn = DriverManager.getConnection(self.databaseConnectionInfoInterface.getUrl())
        except SQLException as se:
            PreLogUtil.putOE(self.commonStrings.EXCEPTION, self.INIT_SQL, "createConnection()", se)
            raise se
    

    # throws Exception
    def initialize(self) -> None:
        try:
            try:
                jdbcDriver: str = self.databaseConnectionInfoInterface.getJdbcDriver()
                PreLogUtil.put(str(StringMaker().append("Loading DbConnnectionInfo: ").append(type(self.databaseConnectionInfoInterface).__module__ + "." + type(self.databaseConnectionInfoInterface).__qualname__).append(" Driver: ").append(jdbcDriver)), self.INIT_SQL, "initialize()")
                Class.forName(jdbcDriver).newInstance()
            except Exception as e:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                    PreLogUtil.putOE("LoadDriver Failed: " + str(self.databaseConnectionInfoInterface.getJdbcDriver()), self.INIT_SQL, "initialize()", e)
                raise e
            if self.userid is None and self.password is None:
                self.useridAndPassword = True
            self.createConnection()
        except Exception as se:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                PreLogUtil.putOE(self.commonStrings.EXCEPTION, self.INIT_SQL, "initialize()", se)
            raise se
    

    def getDatabaseConnectionInfoInterface(self) -> DatabaseConnectionInfoInterface:
        return self.databaseConnectionInfoInterface
# from java.sql.Connection import Connection
# from java.sql.DriverManager import DriverManager
# from java.sql.ResultSet import ResultSet
# from java.sql.ResultSetMetaData import ResultSetMetaData
# from java.sql.SQLException import SQLException
# from java.sql.Statement import Statement
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.init.db.DatabaseConnectionInfoInterface import DatabaseConnectionInfoInterface
from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.communication.sql.SqlStrings import SqlStrings
from org.allbinary.logic.communication.sql.SqlTypeStrings import SqlTypeStrings
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


