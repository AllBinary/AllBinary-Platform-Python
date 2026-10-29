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

import time
import threading


class AbSqlBasic:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.sqlConnectionPool: SqlConnectionPool = SqlConnectionPool.getInstance()
        self.databaseConnectionInfoInterface: DbConnectionInfo = None
        self.connectAttemptCounter: int = None
        self.conn: Connection = None
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.stdUtil: StdUtil = StdUtil.getInstance()
        self.sqlTypeStrings: SqlTypeStrings = SqlTypeStrings.getInstance()
        self.sqlStrings: SqlStrings = SqlStrings.getInstance()
        self.INSERT: str = "insert"
        self.UPDATE: str = "update"
        self.FAILED_SQL_STATEMENT: str = "Failed\nSQL Statement: "
        self.SUCCESS_SQL_STATEMENT: str = "Success\nSQL Statement: "
        self.METHOD_EXECUTED_SQL_STATEMENT: str = "executedSQLStatement"
        self.METHOD_CREATE: str = "create"
        self.DATABASE_CREATED_LABEL: str = "Database Created: "
        self.DATABASE_CREATION_FAILED_LABEL: str = "Database Creation Failed: "
        self.SQL_CONNECTION_FAILED: str = "SQL Connection Failed"
        self.SQL_CONNECTION_RETRYING: str = "SQL Connection Retrying"
        self.SQL_CONNECTION_RETRY: str = "SQL Connection Retry"
        self.METHOD_CREATE_CONNECTION: str = "createConnection()"
        self.METHOD_INITIALIZE: str = "initialize"
        self.LOAD_JDBC_DRIVER_FAILED_LABEL: str = "Load JDBC Driver Failed: "
    

    def __init__(self, databaseConnectionInfoInterface: DbConnectionInfo) -> None:
        self._init_fields()
        self.databaseConnectionInfoInterface = databaseConnectionInfoInterface
        self.connectAttemptCounter = 0
        self.conn = None
    

    # throws SQLException
    def executeSQLStatement(self, statement: str) -> ResultSet:
        try:
            self.initialize()
            stmt: Statement = self.conn.createStatement()
            stmt.execute(statement)
            rset: ResultSet = stmt.getResultSet()
            stmt.close()
            tempConnection: Connection = self.conn
            self.conn = None
            self.sqlConnectionPool.add(self.getDatabaseConnectionInfoInterface().getUrl(), tempConnection)
            return rset
        except SQLException as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.FAILED_SQL_STATEMENT + statement, self, self.METHOD_EXECUTED_SQL_STATEMENT, e)
            self.conn.close()
            self.conn = None
            raise e
    

    def create(self, databaseName: str) -> str:
        try:
            self.executeSQLStatement(str(self.sqlStrings.CREATE_DATABASE) + databaseName)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.DATABASE_CREATED_LABEL + databaseName, self, self.METHOD_CREATE)
            return databaseName + str(self.sqlStrings.CREATE_RETURN)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.DATABASE_CREATION_FAILED_LABEL + databaseName, self, self.METHOD_CREATE, e)
            return self.DATABASE_CREATION_FAILED_LABEL + databaseName
    

    def createConnection(self) -> None:
        try:
            self.conn = self.sqlConnectionPool.get(self.getDatabaseConnectionInfoInterface().getUrl())
        except SQLException as se:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.SQL_CONNECTION_RETRYING, self, self.METHOD_CREATE_CONNECTION, se)
            try:
                threading.current_thread().sleep(2000)
                if self.connectAttemptCounter < 10:
                    self.connectAttemptCounter += 1
                    self.initialize()
            except Exception as e:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                    self.logUtil.put(self.SQL_CONNECTION_RETRY + str(se), self, self.METHOD_CREATE_CONNECTION, e)
    

    def initialize(self) -> None:
        try:
            if True:
                try:
                    loader: ClassLoader = threading.current_thread().getContextClassLoader()
                    jdbcDriverClass: type = loader.loadClass(self.getDatabaseConnectionInfoInterface().getJdbcDriver())
                    jdbcDriverClass.newInstance()
                except Exception as e:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                        self.logUtil.put(self.LOAD_JDBC_DRIVER_FAILED_LABEL + str(self.getDatabaseConnectionInfoInterface().getJdbcDriver()), self, self.METHOD_INITIALIZE, e)
            self.createConnection()
        except Exception as se:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.SQL_CONNECTION_FAILED, self, self.METHOD_INITIALIZE, se)
    

    def getDatabaseConnectionInfoInterface(self) -> DatabaseConnectionInfoInterface:
        return self.databaseConnectionInfoInterface
    

    def setDatabaseConnectionInfoInterface(self, databaseConnectionInfoInterface: DbConnectionInfo) -> None:
        self.databaseConnectionInfoInterface = databaseConnectionInfoInterface
# from java.sql.Connection import Connection
# from java.sql.ResultSet import ResultSet
# from java.sql.SQLException import SQLException
# from java.sql.Statement import Statement
from org.allbinary.business.init.db.DatabaseConnectionInfoInterface import DatabaseConnectionInfoInterface
from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.sql.connection.pool.SqlConnectionPool import SqlConnectionPool
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.sql.SqlTypeStrings import SqlTypeStrings
from org.allbinary.logic.communication.sql.SqlStrings import SqlStrings


