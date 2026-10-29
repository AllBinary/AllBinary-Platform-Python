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
# package org.allbinary.business.installer

from __future__ import annotations



#Warning you must have sql root access
class InitDb:

    def _init_fields(self) -> None:
        self.anyType: object = None
        self.METHOD_CALL_GET_HOST_NAME: str = "getHostName"
        self.METHOD_CALL_ADD_USERS: str = "addUsers"
        self.METHOD_CALL_ADD_DATABASES: str = "addDatabases"
        self.METHOD_CALL_ADD_TABLES: str = "addTables"
        self.METHOD_CALL_TEMP_MAIN_PATH: str = "useTemporaryMainPath"
        self.METHOD_CALL_MAIN_PATH: str = "useNormalMainPath"

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
    

    def _constructor1(self, dbConnectionInfo: DbConnectionInfo) -> None:
        self._init_fields()
    

    def setHelper(self, anyType: object) -> None:
        self.anyType = anyType
    

    def getHelper(self) -> object:
        return self.anyType
    

    def getHostName(self) -> str:
        try:
            dynamicClass: type = type(self.anyType)
            method: Method = dynamicClass.getMethod(self.METHOD_CALL_GET_HOST_NAME, None)
            result: str = method.invoke(self.anyType, None)
            return result
        except Exception as e:
            return None
    

    def addUsers(self) -> bool:
        try:
            dynamicClass: type = type(self.anyType)
            method: Method = dynamicClass.getMethod(self.METHOD_CALL_ADD_USERS, None)
            result: bool = method.invoke(self.anyType, None)
            return result
        except Exception as e:
            return False
    

    def addDatabases(self) -> bool:
        try:
            dynamicClass: type = type(self.anyType)
            method: Method = dynamicClass.getMethod(self.METHOD_CALL_ADD_DATABASES, None)
            result: bool = method.invoke(self.anyType, None)
            return result
        except Exception as e:
            return False
    

    def addTables(self) -> bool:
        try:
            dynamicClass: type = type(self.anyType)
            method: Method = dynamicClass.getMethod(self.METHOD_CALL_ADD_TABLES, None)
            result: bool = method.invoke(self.anyType, None)
            return result
        except Exception as e:
            return False
    

    def useTemporaryMainPath(self) -> bool:
        try:
            dynamicClass: type = type(self.anyType)
            method: Method = dynamicClass.getMethod(self.METHOD_CALL_TEMP_MAIN_PATH, None)
            result: bool = method.invoke(self.anyType, None)
            return result
        except Exception as e:
            return False
    

    def useNormalMainPath(self) -> bool:
        try:
            dynamicClass: type = type(self.anyType)
            method: Method = dynamicClass.getMethod(self.METHOD_CALL_MAIN_PATH, None)
            result: bool = method.invoke(self.anyType, None)
            return result
        except Exception as e:
            return False
# from java.lang.reflect.Method import Method
from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


