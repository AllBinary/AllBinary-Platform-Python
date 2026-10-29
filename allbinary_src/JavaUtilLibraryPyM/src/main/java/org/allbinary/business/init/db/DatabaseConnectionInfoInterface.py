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



# Java interface
class DatabaseConnectionInfoInterface:
    

    def getUrl(self) -> str:
        raise NotImplementedError()
    

    def getJdbcDriver(self) -> str:
        raise NotImplementedError()
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def getUserName(self) -> str:
        raise NotImplementedError()
    

    def getPassword(self) -> str:
        raise NotImplementedError()
    

    def getHost(self) -> str:
        raise NotImplementedError()
    

    def getSchema(self) -> str:
        raise NotImplementedError()
    

    def getServer(self) -> str:
        raise NotImplementedError()
    

    def getPort(self) -> str:
        raise NotImplementedError()
    

    def setJdbcDriver(self, value: str) -> None:
        raise NotImplementedError()
    

    def setName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setUserName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPassword(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSchema(self, value: str) -> None:
        raise NotImplementedError()
    

    def setServer(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPort(self, value: str) -> None:
        raise NotImplementedError()
    

    def getUserNameKey(self) -> str:
        raise NotImplementedError()
    

    def getPasswordKey(self) -> str:
        raise NotImplementedError()


