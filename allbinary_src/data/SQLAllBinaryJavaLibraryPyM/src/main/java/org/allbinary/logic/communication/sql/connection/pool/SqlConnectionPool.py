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
# package org.allbinary.logic.communication.sql.connection.pool

from __future__ import annotations

import threading


class SqlConnectionPool:
    instance: SqlConnectionPool = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.stdUtil: StdUtil = StdUtil.getInstance()
        self.connectionHashMap: dict = None
        self.FIRST_NEW_CONNECTION_CREATED: str = "First New Connection Created: "
        self.FIRST: str = "First "
        self.NEW_CONNECTION_FOR: str = "New Connection For "
        self.CREATED: str = " Created"
        self.NUMBER_OF_SQL_CONNECTIONS_FOR: str = "Number Of Sql Connections for: "
        self.NUMBER_OF_SQL_CONNECTION_VECTORS: str = "Number Of Sql Connection Vectors: "
        self.IS: str = " is "
        self.CONNECTION_ALLREADY_CLOSED: str = "Connection AllReady Closed"
        self.METHOD_GET: str = "get()"
        self.METHOD_ADD: str = "add()"
    

    @staticmethod
    def getInstance() -> SqlConnectionPool:
        return SqlConnectionPool.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws SQLException
    def get(self, url: str) -> Connection:
        with self._lock:
            return self._get_unlocked(url)

    def _get_unlocked(self, url: str) -> Connection:
        if self.connectionHashMap is None:
            self.connectionHashMap = self.stdUtil.createHashMap()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGPOOL):
                self.logUtil.putF(self.FIRST_NEW_CONNECTION_CREATED + url, self, self.METHOD_GET)
            return DriverManager.getConnection(url)
        else:
            connectionVector: BasicArrayList = self.connectionHashMap.get(url)
            if connectionVector is None:
                connectionVector = BasicArrayListD()
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGPOOL):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append(self.FIRST)
                    stringBuffer.append(self.NEW_CONNECTION_FOR)
                    stringBuffer.append(url)
                    stringBuffer.append(self.CREATED)
                    self.logUtil.putF(str(stringBuffer), self, self.METHOD_GET)
                return DriverManager.getConnection(url)
            elif connectionVector.size() == 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGPOOL):
                    self.logUtil.putF(str(StringMaker().append(self.NEW_CONNECTION_FOR).append(url).append(self.CREATED)), self, self.METHOD_GET)
                return DriverManager.getConnection(url)
            else:
                stringBuffer: StringMaker = StringMaker()
                size: int = connectionVector.size()
                for i in range(0, size):
                    sqlConnection: Connection = connectionVector.get(i)
                    if not sqlConnection.isClosed():
                        connectionVector.remove(sqlConnection)
                        self.connectionHashMap.put(url, connectionVector)
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGPOOL):
                            stringBuffer.delete(0, stringBuffer.length())
                            stringBuffer.append(self.NUMBER_OF_SQL_CONNECTIONS_FOR)
                            stringBuffer.append(url)
                            stringBuffer.append(self.IS)
                            stringBuffer.appendint(connectionVector.size())
                            self.logUtil.putF(self.NUMBER_OF_SQL_CONNECTION_VECTORS + str(self.connectionHashMap.size()), self, self.METHOD_GET)
                            self.logUtil.putF(str(stringBuffer), self, self.METHOD_GET)
                        return sqlConnection
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGPOOL):
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.NEW_CONNECTION_FOR)
            stringBuffer.append(url)
            stringBuffer.append(self.CREATED)
            self.logUtil.putF(str(stringBuffer), self, self.METHOD_GET)
        return DriverManager.getConnection(url)
    

    # throws SQLException
    def add(self, url: str, sqlConnection: Connection) -> None:
        with self._lock:
            return self._add_unlocked(url, sqlConnection)

    def _add_unlocked(self, url: str, sqlConnection: Connection) -> None:
        if not sqlConnection.isClosed():
            connectionVector: BasicArrayList = None
            if self.connectionHashMap is None:
                self.connectionHashMap = self.stdUtil.createHashMap()
                connectionVector = BasicArrayListD()
                connectionVector.add(sqlConnection)
            else:
                connectionVector = self.connectionHashMap.get(url)
                if connectionVector is None:
                    connectionVector = BasicArrayListD()
                connectionVector.add(sqlConnection)
                self.connectionHashMap.put(url, connectionVector)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGPOOL):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append(self.NUMBER_OF_SQL_CONNECTIONS_FOR)
                stringBuffer.append(url)
                stringBuffer.append(self.IS)
                stringBuffer.appendint(connectionVector.size())
                self.logUtil.putF(self.NUMBER_OF_SQL_CONNECTION_VECTORS + str(self.connectionHashMap.size()), self, self.METHOD_ADD)
                self.logUtil.putF(str(stringBuffer), self, self.METHOD_ADD)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGPOOL):
            self.logUtil.putF(self.CONNECTION_ALLREADY_CLOSED, self, self.METHOD_ADD)
# from java.sql.Connection import Connection
# from java.sql.DriverManager import DriverManager
# from java.sql.SQLException import SQLException
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


SqlConnectionPool.instance = SqlConnectionPool()

