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
from org.allbinary.logic.communication.sql.AbSqlBasic import AbSqlBasic


@java_inherited_overloads
class AbSqlTable(AbSqlBasic):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("tableName", None)
        vars(self).setdefault("METHOD_CREATED_TABLE", None)
        vars(self).setdefault("METHOD_DROP_TABLE", None)
        vars(self).setdefault("TABLE_CREATION_SUCCESS", None)
        vars(self).setdefault("DROPPED_SUCCESS", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "tableName" not in vars(self): self.tableName: str = None
        self.METHOD_CREATED_TABLE: str = "createTable()"
        self.METHOD_DROP_TABLE: str = "dropTable()"
        self.TABLE_CREATION_SUCCESS: str = "Table Creation Successful: "
        self.DROPPED_SUCCESS: str = " Dropped Successfully"
    

    def __init__(self, databaseConnectionInfoInterface: DbConnectionInfo) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
        super().__init__(databaseConnectionInfoInterface)
        __class__._init_fields(self)
    

    def setTableName(self, tableName: str) -> None:
        self.tableName = tableName
    

    def getTableName(self) -> str:
        return self.tableName
    

    def createTable(self, data: str) -> str:
        with self._lock:
            return __class__.__dict__["_createTable_unlocked"].__get__(self, __class__)(data)

    def _createTable_unlocked(self, data: str) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            self.executeSQLStatement(data)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.TABLE_CREATION_SUCCESS + self.tableName + " with statement: " + data, self, self.METHOD_CREATED_TABLE)
            return self.tableName + str(self.sqlStrings.CREATE_RETURN)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put("Table Creation Failed: " + self.tableName + " with statement: " + data, self, self.METHOD_CREATED_TABLE, e)
            return "Failed to Create " + self.tableName + " table."
    

    def dropTable(self) -> str:
        with self._lock:
            return __class__.__dict__["_dropTable_unlocked"].__get__(self, __class__)()

    def _dropTable_unlocked(self) -> str:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        sqlStatement: str = str(self.sqlStrings.DROP_TABLE) + self.tableName
        try:
            self.executeSQLStatement(sqlStatement)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(self.SUCCESS_SQL_STATEMENT) + sqlStatement, self, self.METHOD_DROP_TABLE)
            return self.tableName + self.DROPPED_SUCCESS
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_DROP_TABLE, e)
            return "Failed to Drop " + self.tableName + " table."
# from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


