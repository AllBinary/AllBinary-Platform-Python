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
from org.allbinary.logic.communication.sql.AbSqlRow import AbSqlRow


@java_inherited_overloads
class AbSqlBean(AbSqlRow):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("METHOD_GET_FIELD", None)
        vars(self).setdefault("METHOD_IS_SUBSET_OF_ENTRY", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.METHOD_GET_FIELD: str = "getField"
        self.METHOD_IS_SUBSET_OF_ENTRY: str = "isSubsetOfEntry"
    

    def __init__(self, databaseConnectionInfoInterface: DbConnectionInfo) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
        super().__init__(databaseConnectionInfoInterface)
        __class__._init_fields(self)
    

    def getField_j3(self, key: str, value: str, requestedField: str) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append(self.sqlStrings.SQL_STATEMENT_LABEL)
                    stringBuffer.append(sqlStatement)
                    stringBuffer.append(self.sqlStrings.FIELD_VALUE)
                    stringBuffer.append(field)
                    self.logUtil.putF(str(stringBuffer), self, self.METHOD_GET_FIELD)
                return field
            return None
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_GET_FIELD, e)
            return str(self.FAILED_SQL_STATEMENT) + sqlStatement
    

    def getField_j2(self, keysAndValues: HashMap, requestedField: str) -> str:
        from java.util.HashMap import HashMap
        from java.util.Set import Set
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_GET_FIELD, e)
            return str(self.FAILED_SQL_STATEMENT) + sqlStatement

    def getField(self, *args):
        implementation = __class__.__dict__.get("getField_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getField(*args)
    

    def isSubsetOfEntry(self, key: str, value: str, columnsAndValues: HashMap) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
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
                        return GLOBALS2.NOTASUBSET
            if rset.getRow() != 1:
                return GLOBALS2.NOTASUBSET
            else:
                return GLOBALS2.ISASUBSET
        except Exception as e:
            sqlStatement: str = str(stringBuffer)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_IS_SUBSET_OF_ENTRY, e)
            return str(self.FAILED_SQL_STATEMENT) + sqlStatement
# from java.sql.ResultSet import ResultSet
# from java.util.HashMap import HashMap
# from java.util.Set import Set
# from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


