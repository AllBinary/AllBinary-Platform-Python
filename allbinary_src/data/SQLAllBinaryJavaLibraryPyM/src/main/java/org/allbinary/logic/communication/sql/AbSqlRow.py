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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from org.allbinary.logic.communication.sql.AbSqlColumn import AbSqlColumn


@java_inherited_overloads
class AbSqlRow(AbSqlColumn):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("EQUAL_QUOTE", None)
        vars(self).setdefault("ESCAPE_QUOTES", None)
        vars(self).setdefault("GET_ROW", None)
        vars(self).setdefault("METHOD_GET_ROW", None)
        vars(self).setdefault("METHOD_GET_ROWS", None)
        vars(self).setdefault("METHOD_GET_ALL_ROWS", None)
        vars(self).setdefault("METHOD_UPDATE_WHERE", None)
        vars(self).setdefault("METHOD_GET_ROWS_WHERE_BETWEEN", None)
        vars(self).setdefault("METHOD_DELETE_WHERE", None)
        vars(self).setdefault("ROW_VALUE_LABEL", None)
        vars(self).setdefault("ROW_VALUES_LABEL", None)
        vars(self).setdefault("NO_RESULTS_IN_RESULT_SET", None)
        vars(self).setdefault("COLUMN_NAME_LABEL", None)
        vars(self).setdefault("INSERT_END", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.EQUAL_QUOTE: str = "=\""
        self.ESCAPE_QUOTES: str = "\\\""
        self.GET_ROW: str = "Row Value: "
        self.METHOD_GET_ROW: str = "getRow()"
        self.METHOD_GET_ROWS: str = "getRows()"
        self.METHOD_GET_ALL_ROWS: str = "getAllRows()"
        self.METHOD_UPDATE_WHERE: str = "updateWhere()"
        self.METHOD_GET_ROWS_WHERE_BETWEEN: str = "getRowsWhereBetween()"
        self.METHOD_DELETE_WHERE: str = "deleteWhere()"
        self.ROW_VALUE_LABEL: str = "Row Value: "
        self.ROW_VALUES_LABEL: str = "Row Values: "
        self.NO_RESULTS_IN_RESULT_SET: str = "No Results in ResultSet"
        self.COLUMN_NAME_LABEL: str = "columnName: "
        self.INSERT_END: str = "')"
    

    def __init__(self, databaseConnectionInfoInterface: DbConnectionInfo) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
        super().__init__(databaseConnectionInfoInterface)
        __class__._init_fields(self)
    

    def getValue(self, value: str) -> str:
        with self._lock:
            return __class__.__dict__["_getValue_unlocked"].__get__(self, __class__)(value)

    def _getValue_unlocked(self, value: str) -> str:
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        if StringValidationUtil.getInstance().isEmpty(value):
            return self.stringUtil.EMPTY_STRING
        else:
            return value
    

    def updateWhere_j3(self, key: str, value: str, updatedKeyValuePairs: HashMap) -> None:
        with self._lock:
            return __class__.__dict__["_updateWhere_j3_unlocked"].__get__(self, __class__)(key, value, updatedKeyValuePairs)

    def _updateWhere_j3_unlocked(self, key: str, value: str, updatedKeyValuePairs: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.regex.replace.Replace import Replace
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.UPDATE)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.SET)
        try:
            keyArray: list[object] = updatedKeyValuePairs.keySet().toArray()
            size: int = len(keyArray)
            for i in range(0, size):
                columnName: str = str(keyArray[i])
                stringBuffer.append(self.commonSeps.SPACE)
                stringBuffer.append(columnName)
                stringBuffer.append(self.EQUAL_QUOTE)
                columnValue: str = updatedKeyValuePairs.get(columnName)
                if columnValue is None:
                    columnValue = self.stringUtil.EMPTY_STRING
                else:
                    columnValue = Replace(self.sqlStrings.CLOSE_QUOTE, self.ESCAPE_QUOTES).all(columnValue)
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(self.SUCCESS_SQL_STATEMENT) + sqlStatement, self, self.METHOD_UPDATE_WHERE)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.FAILED_SQL_STATEMENT + stringBuffer, self, self.METHOD_UPDATE_WHERE, e)
    

    # throws Exception
    def updateWhere_j2(self, whereKeyValuePairs: HashMap, updatedKeyValuePairs: HashMap) -> None:
        with self._lock:
            return __class__.__dict__["_updateWhere_j2_unlocked"].__get__(self, __class__)(whereKeyValuePairs, updatedKeyValuePairs)

    def _updateWhere_j2_unlocked(self, whereKeyValuePairs: HashMap, updatedKeyValuePairs: HashMap) -> None:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.regex.replace.Replace import Replace
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.UPDATE)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.SET)
        try:
            keyArray: list[object] = updatedKeyValuePairs.keySet().toArray()
            size: int = len(keyArray)
            for i in range(0, size):
                columnName: str = str(keyArray[i])
                stringBuffer.append(self.commonSeps.SPACE)
                stringBuffer.append(columnName)
                stringBuffer.append(self.EQUAL_QUOTE)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.COLUMN_NAME_LABEL + columnName, self, self.METHOD_UPDATE_WHERE)
                columnValue: str = updatedKeyValuePairs.get(columnName)
                if columnValue is None:
                    columnValue = self.stringUtil.EMPTY_STRING
                else:
                    columnValue = Replace(self.sqlStrings.CLOSE_QUOTE, self.ESCAPE_QUOTES).all(columnValue)
                stringBuffer.append(self.getValue(columnValue))
                stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
                if i < size - 1:
                    stringBuffer.append(self.commonSeps.COMMA)
            stringBuffer.append(self.sqlStrings.WHERE)
            set: Set = whereKeyValuePairs.keySet()
            keyArray2: list[object] = set.toArray()
            size2: int = len(keyArray2)
            for i in range(0, size2):
                key: str = keyArray2[i]
                value: str = whereKeyValuePairs.get(key)
                if True:
                    stringBuffer.append(key)
                    stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
                    stringBuffer.append(self.getValue(value))
                    stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
                    if i < size2 - 1:
                        stringBuffer.append(self.sqlStrings.AND)
            sqlStatement: str = str(stringBuffer)
            self.executeSQLStatement(sqlStatement)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(self.SUCCESS_SQL_STATEMENT) + sqlStatement, self, self.METHOD_UPDATE_WHERE)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.FAILED_SQL_STATEMENT + stringBuffer, self, self.METHOD_UPDATE_WHERE, e)
            raise e

    def updateWhere(self, *args):
        implementation = __class__.__dict__.get("updateWhere_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().updateWhere(*args)
    

    def deleteWhere_j2(self, key: str, value: str) -> None:
        with self._lock:
            return __class__.__dict__["_deleteWhere_j2_unlocked"].__get__(self, __class__)(key, value)

    def _deleteWhere_j2_unlocked(self, key: str, value: str) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.DELETE)
        stringBuffer.append(self.sqlStrings.FROM)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.WHERE)
        stringBuffer.append(key)
        stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
        stringBuffer.append(value)
        stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
        try:
            sqlStatement: str = str(stringBuffer)
            self.executeSQLStatement(sqlStatement)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(self.SUCCESS_SQL_STATEMENT) + sqlStatement, self, self.METHOD_DELETE_WHERE)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + str(stringBuffer), self, self.METHOD_DELETE_WHERE, e)
    

    def deleteWhere_j1(self, keysAndValues: HashMap) -> None:
        with self._lock:
            return __class__.__dict__["_deleteWhere_j1_unlocked"].__get__(self, __class__)(keysAndValues)

    def _deleteWhere_j1_unlocked(self, keysAndValues: HashMap) -> None:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.DELETE)
        stringBuffer.append(self.sqlStrings.FROM)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.WHERE)
        try:
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
            self.executeSQLStatement(sqlStatement)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(self.SUCCESS_SQL_STATEMENT) + sqlStatement, self, self.METHOD_DELETE_WHERE)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + str(stringBuffer), self, self.METHOD_DELETE_WHERE, e)

    def deleteWhere(self, *args):
        implementation = __class__.__dict__.get("deleteWhere_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().deleteWhere(*args)
    

    def insert(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.regex.replace.Replace import Replace
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.INSERT_INTO)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.VALUES)
        try:
            for i in range(0, values.size() - 1):
                value: str = self.getValue(values.get(i))
                value = Replace(self.sqlStrings.ESCAPE, self.sqlStrings.DOUBLE_ESCAPE).all(value)
                stringBuffer.append(value)
                stringBuffer.append(self.sqlStrings.SINGLE_QUOTE_COMMA_SEP)
            value: str = self.getValue(values.get(values.size() - 1))
            value = Replace(self.sqlStrings.ESCAPE, self.sqlStrings.DOUBLE_ESCAPE).all(value)
            stringBuffer.append(value)
            stringBuffer.append(self.INSERT_END)
            sqlStatement: str = str(stringBuffer)
            self.executeSQLStatement(sqlStatement)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(self.SUCCESS_SQL_STATEMENT) + sqlStatement, self, self.INSERT)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + str(stringBuffer), self, self.INSERT, e)
    

    def getRow(self, keysAndValues: HashMap) -> HashMap:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT_ALL_FROM)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.WHERE)
        try:
            result: HashMap = None
            set: Set = keysAndValues.keySet()
            keyArray: list[object] = set.toArray()
            size: int = len(keyArray)
            for index in range(0, size):
                key: str = keyArray[index]
                value: str = str(keysAndValues.get(key))
                stringBuffer.append(key)
                stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
                stringBuffer.append(self.getValue(value))
                stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
                if index < size - 1:
                    stringBuffer.append(self.sqlStrings.AND)
            sqlStatement: str = str(stringBuffer)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(self.sqlStrings.SQL_STATEMENT_LABEL) + sqlStatement, self, self.METHOD_GET_ROW)
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            resultSetMetaData: ResultSetMetaData = rset.getMetaData()
            while rset.next():
                result = self.stdUtil.createHashMap()
                columnCount: int = resultSetMetaData.getColumnCount()
                for index in range(1, columnCount + 1):
                    columnName: str = resultSetMetaData.getColumnName(index)
                    field: str = rset.getString(columnName)
                    result.put(columnName, field)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.ROW_VALUE_LABEL + str(result), self, self.METHOD_GET_ROW)
                return result
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.putF(self.NO_RESULTS_IN_RESULT_SET, self, self.METHOD_GET_ROW)
            return None
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.FAILED_SQL_STATEMENT + stringBuffer, self, self.METHOD_GET_ROW, e)
            return None
    

    def getRows_j1(self, keysAndValues: HashMap) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.logic.string.StringUtil import StringUtil
        return self.getRows(keysAndValues, StringUtil.getInstance().EMPTY_STRING)
    

    def getRows_j2(self, keysAndValues: HashMap, more: str) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT_ALL_FROM)
        stringBuffer.append(self.getTableName())
        stringBuffer.append(self.sqlStrings.WHERE)
        try:
            rows: BasicArrayList = BasicArrayListD()
            set: Set = keysAndValues.keySet()
            keyArray: list[object] = set.toArray()
            size: int = len(keyArray)
            for index in range(0, size):
                key: str = keyArray[index]
                value: str = str(keysAndValues.get(key))
                stringBuffer.append(key)
                stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
                stringBuffer.append(self.getValue(value))
                stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
                if index < size - 1:
                    stringBuffer.append(self.sqlStrings.AND)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.sqlStrings.SQL_STATEMENT_LABEL + stringBuffer, self, self.METHOD_GET_ROWS)
            stringBuffer.append(more)
            sqlStatement: str = str(stringBuffer)
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            resultSetMetaData: ResultSetMetaData = rset.getMetaData()
            while rset.next():
                result: HashMap = self.stdUtil.createHashMap()
                columnCount: int = resultSetMetaData.getColumnCount()
                for index in range(1, columnCount + 1):
                    columnName: str = resultSetMetaData.getColumnName(index)
                    field: str = rset.getString(columnName)
                    result.put(columnName, field)
                resultAsString: str = str(result)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.GET_ROW + resultAsString, self, self.METHOD_GET_ROWS)
                rows.add(result)
            return rows
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.FAILED_SQL_STATEMENT + stringBuffer, self, self.METHOD_GET_ROWS, e)
            return None

    def getRows(self, *args):
        implementation = __class__.__dict__.get("getRows_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getRows(*args)
    

    def getAllRows(self) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT_ALL_FROM)
        stringBuffer.append(self.getTableName())
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.sqlStrings.SQL_STATEMENT_LABEL + stringBuffer, self, self.METHOD_GET_ALL_ROWS)
            rows: BasicArrayList = BasicArrayListD()
            sqlStatement: str = str(stringBuffer)
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            resultSetMetaData: ResultSetMetaData = rset.getMetaData()
            while rset.next():
                result: HashMap = self.stdUtil.createHashMap()
                columnCount: int = resultSetMetaData.getColumnCount()
                for index in range(1, columnCount + 1):
                    columnName: str = resultSetMetaData.getColumnName(index)
                    field: str = rset.getString(columnName)
                    result.put(columnName, field)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.ROW_VALUES_LABEL + str(result), self, self.METHOD_GET_ALL_ROWS)
                rows.add(result)
            return rows
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.FAILED_SQL_STATEMENT + stringBuffer, self, self.METHOD_GET_ALL_ROWS, e)
            return None
    

    def getRowsWhereBetween_j4(self, whereKeyValuePairs: HashMap, betweenColumn: str, smallest: str, largest: str) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT_ALL_FROM)
        stringBuffer.append(self.getTableName())
        try:
            rows: BasicArrayList = BasicArrayListD()
            stringBuffer.append(self.sqlStrings.WHERE)
            set: Set = whereKeyValuePairs.keySet()
            key: str = None
            value: str = None
            keyArray: list[object] = set.toArray()
            size: int = len(keyArray)
            for index in range(0, size):
                key = keyArray[index]
                value = whereKeyValuePairs.get(key)
                stringBuffer.append(key)
                stringBuffer.append(self.sqlStrings.EQUAL_QUOTE)
                stringBuffer.append(self.getValue(value))
                stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
                stringBuffer.append(self.sqlStrings.AND)
            stringBuffer.append(betweenColumn)
            stringBuffer.append(self.sqlStrings.MORE_THAN_QUOTE)
            stringBuffer.append(smallest)
            stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
            stringBuffer.append(self.sqlStrings.AND)
            stringBuffer.append(betweenColumn)
            stringBuffer.append(self.sqlStrings.LESS_THAN_QUOTE)
            stringBuffer.append(largest)
            stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
            sqlStatement: str = str(stringBuffer)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(self.sqlStrings.SQL_STATEMENT_LABEL) + sqlStatement, self, self.METHOD_GET_ROWS_WHERE_BETWEEN)
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            resultSetMetaData: ResultSetMetaData = rset.getMetaData()
            result: HashMap = None
            columnNames: BasicArrayList = None
            columnCount: int = 0
            columnName: str = None
            field: str = None
            while rset.next():
                result = self.stdUtil.createHashMap()
                columnNames = BasicArrayListD()
                columnCount = resultSetMetaData.getColumnCount()
                for index in range(1, columnCount + 1):
                    columnName = resultSetMetaData.getColumnName(index)
                    field = rset.getString(columnName)
                    result.put(columnName, field)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.ROW_VALUE_LABEL + str(result), self, self.METHOD_GET_ROWS_WHERE_BETWEEN)
                rows.add(result)
            return rows
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.FAILED_SQL_STATEMENT + stringBuffer, self, self.METHOD_GET_ROWS_WHERE_BETWEEN, e)
            return None
    

    def getRowsWhereBetween_j3(self, betweenColumn: str, smallest: str, largest: str) -> BasicArrayList:
        from java.util.HashMap import HashMap
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.SELECT_ALL_FROM)
        stringBuffer.append(self.getTableName())
        try:
            rows: BasicArrayList = BasicArrayListD()
            stringBuffer.append(self.sqlStrings.WHERE)
            stringBuffer.append(betweenColumn)
            stringBuffer.append(self.sqlStrings.MORE_THAN_QUOTE)
            stringBuffer.append(smallest)
            stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
            stringBuffer.append(self.sqlStrings.AND)
            stringBuffer.append(betweenColumn)
            stringBuffer.append(self.sqlStrings.LESS_THAN_QUOTE)
            stringBuffer.append(largest)
            stringBuffer.append(self.sqlStrings.CLOSE_QUOTE)
            sqlStatement: str = str(stringBuffer)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(self.sqlStrings.SQL_STATEMENT_LABEL) + sqlStatement, self, self.METHOD_GET_ROWS_WHERE_BETWEEN)
            rset: ResultSet = self.executeSQLStatement(sqlStatement)
            resultSetMetaData: ResultSetMetaData = rset.getMetaData()
            columnName: str = None
            field: str = None
            result: HashMap = None
            columnNames: BasicArrayList = None
            columnCount: int = 0
            while rset.next():
                result = self.stdUtil.createHashMap()
                columnNames = BasicArrayListD()
                columnCount = resultSetMetaData.getColumnCount()
                for index in range(1, columnCount + 1):
                    columnName = resultSetMetaData.getColumnName(index)
                    field = rset.getString(columnName)
                    result.put(columnName, field)
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.ROW_VALUE_LABEL + str(result), self, self.METHOD_GET_ROWS_WHERE_BETWEEN)
                rows.add(result)
            return rows
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.FAILED_SQL_STATEMENT + stringBuffer, self, self.METHOD_GET_ROWS_WHERE_BETWEEN, e)
            return None

    def getRowsWhereBetween(self, *args):
        implementation = __class__.__dict__.get("getRowsWhereBetween_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getRowsWhereBetween(*args)
# from java.sql.ResultSet import ResultSet
# from java.sql.ResultSetMetaData import ResultSetMetaData
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.string.regex.replace.Replace import Replace
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


