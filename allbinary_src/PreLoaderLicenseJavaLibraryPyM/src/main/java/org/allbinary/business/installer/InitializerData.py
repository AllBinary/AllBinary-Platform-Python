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



class InitializerData:
    instance: InitializerData = None

    def _init_fields(self) -> None:
        self.DBUSER: str = "DBUSER"
        self.DBPASSWORD: str = "DBPASSWORD"
        self.ADMINJDBCDRIVER: str = "ADMIN_JDBCDRIVER"
        self.ADMINSCHEMA: str = "ADMINSCHEMA"
        self.ADMINSERVER: str = "ADMINSERVER"
        self.ADMINPORT: str = "ADMINPORT"
        self.CUSTOMERJDBCDRIVER: str = "CUSTOMER_JDBCDRIVER"
        self.CUSTOMERNAME: str = "CUSTOMERNAME"
        self.CUSTOMERUSERNAME: str = "CUSTOMERUSERNAME"
        self.CUSTOMERPASSWORD: str = "CUSTOMERPASSWORD"
        self.CUSTOMERSCHEMA: str = "CUSTOMERSCHEMA"
        self.CUSTOMERSERVER: str = "CUSTOMERSERVER"
        self.CUSTOMERPORT: str = "CUSTOMERPORT"
        self.HISTORYJDBCDRIVER: str = "HISTORY_JDBCDRIVER"
        self.HISTORYNAME: str = "HISTORYNAME"
        self.HISTORYUSERNAME: str = "HISTORYUSERNAME"
        self.HISTORYPASSWORD: str = "HISTORYPASSWORD"
        self.HISTORYSCHEMA: str = "HISTORYSCHEMA"
        self.HISTORYSERVER: str = "HISTORYSERVER"
        self.HISTORYPORT: str = "HISTORYPORT"
        self.LOGJDBCDRIVER: str = "LOG_JDBCDRIVER"
        self.LOGNAME: str = "LOGNAME"
        self.LOGUSERNAME: str = "LOGUSERNAME"
        self.LOGPASSWORD: str = "LOGPASSWORD"
        self.LOGSCHEMA: str = "LOGSCHEMA"
        self.LOGSERVER: str = "LOGSERVER"
        self.LOGPORT: str = "LOGPORT"
        self.INVENTORYJDBCDRIVER: str = "INVENTORY_JDBCDRIVER"
        self.INVENTORYNAME: str = "INVENTORYNAME"
        self.INVENTORYUSERNAME: str = "INVENTORYUSERNAME"
        self.INVENTORYPASSWORD: str = "INVENTORYPASSWORD"
        self.INVENTORYSCHEMA: str = "INVENTORYSCHEMA"
        self.INVENTORYSERVER: str = "INVENTORYSERVER"
        self.INVENTORYPORT: str = "INVENTORYPORT"
        self.STATICPAGESJDBCDRIVER: str = "STATICPAGES_JDBCDRIVER"
        self.STATICPAGESNAME: str = "STATICPAGESNAME"
        self.STATICPAGESUSERNAME: str = "STATICPAGESUSERNAME"
        self.STATICPAGESPASSWORD: str = "STATICPAGESPASSWORD"
        self.STATICPAGESSCHEMA: str = "STATICPAGESSCHEMA"
        self.STATICPAGESSERVER: str = "STATICPAGESSERVER"
        self.STATICPAGESPORT: str = "STATICPAGESPORT"

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> InitializerData:
        return InitializerData.instance
    

    def getJdbcDriverSolutionInfo(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("The following describes the possible problems and solutions regarding the Jdbc Driver error(s):<p/>")
        stringBuffer.append("1. A JDBC driver you specified is not in your classpath.<br/>")
        stringBuffer.append("Solution 1: Move the JDBC driver into any directory specified in the existing classpath. <br/>")
        stringBuffer.append("Solution 2: Add the directory that contains the JDBC driver to the classpath.<br/>")
        stringBuffer.append("Solution 3: Add the JDBC driver to the WEB-INF/lib directory where you installed this webapp.<br/>")
        stringBuffer.append("2. The JDBC driver you specified does not exit.<br/>")
        stringBuffer.append("Solution: Get a JDBC driver. <br/>")
        stringBuffer.append("3. The JDBC driver you specified is not valid.<br/>")
        stringBuffer.append("Solution: Use a valid JDBC driver.<p/>")
        return str(stringBuffer)
from org.allbinary.logic.string.StringMaker import StringMaker


InitializerData.instance = InitializerData()

