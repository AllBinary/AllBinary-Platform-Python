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
# package org.allbinary.business.init.db

from __future__ import annotations

from org.allbinary.business.init.db.DatabaseConnectionInfoInterface import DatabaseConnectionInfoInterface


class DbConnectionInfo(DatabaseConnectionInfoInterface):

    def _init_fields(self) -> None:
        self.jdbcDriver: str = None
        self.name: str = None
        self.userName: str = None
        self.password: str = None
        self.schema: str = None
        self.server: str = None
        self.port: str = None
        self.url: str = None
        self.host: str = None
        self.SCHEMA_SEP: str = "://"
        self.USER_NAME_KEY: str = "?user="
        self.PASSWORD_KEY: str = "&password="
    

    def __init__(self) -> None:
        self._init_fields()
    

    def updateUrl(self) -> None:
        self.updateHost()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.getHost())
        stringBuffer.append(self.getName())
        stringBuffer.append(self.getUserNameKey())
        stringBuffer.append(self.getUserName())
        stringBuffer.append(self.getPasswordKey())
        stringBuffer.append(self.getPassword())
        self.url = str(stringBuffer)
    

    def getUrl(self) -> str:
        return self.url
    

    def getJdbcDriver(self) -> str:
        return self.jdbcDriver
    

    def getName(self) -> str:
        return self.name
    

    def getUserName(self) -> str:
        return self.userName
    

    def getPassword(self) -> str:
        return self.password
    

    def updateHost(self) -> None:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.getSchema())
        stringBuffer.append(self.SCHEMA_SEP)
        stringBuffer.append(self.getServer())
        if self.getPort() is not None and self.getPort().length() > 1:
            stringBuffer.append(CommonSeps.getInstance().COLON)
            stringBuffer.append(self.getPort())
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        self.host = str(stringBuffer)
    

    def getHost(self) -> str:
        return self.host
    

    def getSchema(self) -> str:
        return self.schema
    

    def getServer(self) -> str:
        return self.server
    

    def getPort(self) -> str:
        return self.port
    

    def setJdbcDriver(self, value: str) -> None:
        self.jdbcDriver = value
    

    def setName(self, value: str) -> None:
        self.name = value
        self.updateUrl()
    

    def setUserName(self, value: str) -> None:
        self.userName = value
        self.updateUrl()
    

    def setPassword(self, value: str) -> None:
        self.password = value
        self.updateUrl()
    

    def setSchema(self, value: str) -> None:
        self.schema = value
        self.updateUrl()
    

    def setServer(self, value: str) -> None:
        self.server = value
        self.updateUrl()
    

    def setPort(self, value: str) -> None:
        self.port = value
        self.updateUrl()
    

    def getUserNameKey(self) -> str:
        return self.USER_NAME_KEY
    

    def getPasswordKey(self) -> str:
        return self.PASSWORD_KEY
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


