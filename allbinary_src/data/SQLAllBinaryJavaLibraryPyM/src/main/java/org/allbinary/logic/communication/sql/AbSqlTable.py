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

import threading
from org.allbinary.logic.communication.sql.AbSqlBasic import AbSqlBasic


class AbSqlTable(AbSqlBasic):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = None
        self.METHOD_CREATED_TABLE: str = "createTable()"
        self.METHOD_DROP_TABLE: str = "dropTable()"
        self.TABLE_CREATION_SUCCESS: str = "Table Creation Successful: "
        self.DROPPED_SUCCESS: str = " Dropped Successfully"
    

    def __init__(self, databaseConnectionInfoInterface: DbConnectionInfo) -> None:
        super().__init__(databaseConnectionInfoInterface)
        self._init_fields()
    

    def setTableName(self, tableName: str) -> None:
        self.tableName = tableName
    

    def getTableName(self) -> str:
        return self.tableName
    

    def createTable(self, data: str) -> str:
        with self._lock:
            return self._createTable_unlocked(data)

    def _createTable_unlocked(self, data: str) -> str:
        try:
            self.executeSQLStatement(data)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.TABLE_CREATION_SUCCESS + self.tableName + " with statement: " + data, self, self.METHOD_CREATED_TABLE)
            return self.tableName + str(self.sqlStrings.CREATE_RETURN)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put("Table Creation Failed: " + self.tableName + " with statement: " + data, self, self.METHOD_CREATED_TABLE, e)
            return "Failed to Create " + self.tableName + " table."
    

    def dropTable(self) -> str:
        with self._lock:
            return self._dropTable_unlocked()

    def _dropTable_unlocked(self) -> str:
        sqlStatement: str = str(self.sqlStrings.DROP_TABLE) + self.tableName
        try:
            self.executeSQLStatement(sqlStatement)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(self.SUCCESS_SQL_STATEMENT) + sqlStatement, self, self.METHOD_DROP_TABLE)
            return self.tableName + self.DROPPED_SUCCESS
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(str(self.FAILED_SQL_STATEMENT) + sqlStatement, self, self.METHOD_DROP_TABLE, e)
            return "Failed to Drop " + self.tableName + " table."
from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
from org.allbinary.logic.communication.log.LogUtil import LogUtil


