# 
# To change this license header, choose License Headers in Project Properties. 
# To change this template file, choose Tools | Templates 
# and open the template in the editor.  
# Generated Code Do Not Modify
# package org.allbinary.logic.communication.sql

from __future__ import annotations

from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean


class AbDatabaseManagement(AbSqlBean):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.sqlCommandLog: StringMaker = StringMaker()
        self.GRANT_ALL: str = "GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER ON "
        self.DOT_STAR: str = ".*"
        self.TO: str = " TO "
        self.AT_LOCALHOST: str = "@localhost"
        self.IDENTIFIED_BY: str = " IDENTIFIED BY '"
        self.WITH_GRANT_OPTION: str = "' WITH GRANT OPTION"
        self.FAILED: str = "Failed"
        self.GET_HOST_NAME: str = "getHostName()"
        self.METHOD_ADD_USER: str = "addUser()"
        self.METHOD_ADD_USERS: str = "addUsers()"
        self.METHOD_ADD_DB: str = "addDb()"
        self.METHOD_ADD_DATABASES: str = "addDatabases()"
        self.METHOD_ADD_TABLES: str = "addTables()"
        self.UNABLE_TO_CREATE_USER: str = "Unable to Create User: "
        self.UNABLE_TO_CREATE_DATABASE: str = "Unable to Create Database: "
        self.UNABLE_TO_CREATE_TABLES: str = "Unable to Create Tables"
        self.ADD_TABLES_RESULTS_LABEL: str = "Add Table Results: "

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, databaseConnectionInfoInterface: DatabaseConnectionInfoInterface) -> None:
        super().__init__(databaseConnectionInfoInterface)
        self._init_fields()
    

    def _constructor1(self, connectionInfo: DbConnectionInfo) -> None:
        super().__init__(connectionInfo)
        self._init_fields()
    

    def getHostName(self) -> str:
        try:
            addr: InetAddress = InetAddress.getLocalHost()
            return addr.getHostName()
        except Exception as e:
            self.logUtil.put(self.FAILED, self, self.GET_HOST_NAME, e)
            return None
    

    # throws Exception
    def addDbUser(self, hostName: str, db: str, userName: str, password: str) -> bool:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.GRANT_ALL)
        stringBuffer.append(db)
        stringBuffer.append(self.DOT_STAR)
        stringBuffer.append(self.TO)
        stringBuffer.append(userName)
        stringBuffer.append(hostName)
        stringBuffer.append(self.IDENTIFIED_BY)
        stringBuffer.append(password)
        stringBuffer.append(self.WITH_GRANT_OPTION)
        sqlStatement: str = str(stringBuffer)
        self.sqlCommandLog.append(sqlStatement)
        self.sqlCommandLog.append(self.commonSeps.NEW_LINE)
        super().executeSQLStatement(sqlStatement)
        return True
    

    # Java overloaded method: Python keeps the last definition
    def addDbUser(self, db: str, userName: str, password: str) -> bool:
        try:
            self.addDbUser(self.AT_LOCALHOST, db, userName, password)
            hostName: str = self.getHostName()
            if hostName is not None:
                self.addDbUser(hostName, db, userName, password)
            return True
        except Exception as e:
            self.logUtil.put(self.UNABLE_TO_CREATE_USER + userName, self, self.METHOD_ADD_USER, e)
            return False
    

    def addDb(self, db: str) -> bool:
        try:
            sqlStatement: str = str(self.sqlStrings.CREATE_DATABASE) + db
            self.sqlCommandLog.append(sqlStatement)
            self.sqlCommandLog.append(self.commonSeps.NEW_LINE)
            super().executeSQLStatement(sqlStatement)
            return True
        except Exception as e:
            self.logUtil.put(self.UNABLE_TO_CREATE_DATABASE + db, self, self.METHOD_ADD_DB, e)
            return False
# from java.net.InetAddress import InetAddress
from org.allbinary.business.init.db.DatabaseConnectionInfoInterface import DatabaseConnectionInfoInterface
from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings


