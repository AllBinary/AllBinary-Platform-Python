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
# package org.allbinary.business.init

from __future__ import annotations

from org.allbinary.business.init.InitSql import InitSql


class InitInfoEntity(InitSql):

    def _init_fields(self) -> None:
        self.NAME: str = "InitInfoEntity"
        self.NOTHING: str = "NOTHING"
        self.tableName: str = "initdata"
        self.tableData: str = None
        self.NOT_IN_DB: str = "Not In DB"
        self.METHOD_GET: str = "get()"
        self.METHOD_IS: str = "is()"
        self.METHOD_ADD: str = "add()"
        self.CREATED_SUCCESS: str = " Created Successfully"
        self.FAILED_TO_CREATE: str = "Failed to create "
    

    def __init__(self) -> None:
        from org.allbinary.business.init.InitInfo import InitInfo
        from org.allbinary.business.init.InitInfo import InitInfo
        from org.allbinary.business.init.InitInfo import InitInfo
        super().__init__(UserDbInitInfo())
        self._init_fields()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.sqlStrings.CREATE_TABLE)
        stringBuffer.append(self.tableName)
        stringBuffer.append(self.sqlStrings.START)
        stringBuffer.append(self.NOTHING)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(InitInfo.getInstance().TESTING)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(InitInfo.getInstance().TESTHTMLPATH)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(InitInfo.getInstance().MAINPATH)
        stringBuffer.append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL)
        stringBuffer.append(self.sqlStrings.PRIMARY_KEY)
        stringBuffer.append(self.NOTHING)
        stringBuffer.append(self.sqlStrings.END)
        self.tableData = str(stringBuffer)
        self.setTable(self.tableName)
    

    def get(self) -> bool:
        from org.allbinary.business.init.InitInfo import InitInfo
        try:
            keyAndValue: dict = StdUtil.getInstance().createHashMap()
            keyAndValue.put(self.NOTHING, self.NOTHING)
            hashMap: dict = self.getRow(keyAndValue)
            if hashMap is not None:
                InitInfo.getInstance().set(hashMap)
                return True
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
                    PreLogUtil.put(self.NOT_IN_DB, self.NAME, self.METHOD_GET)
                return False
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE(self.commonStrings.EXCEPTION, self.NAME, self.METHOD_GET, e)
            return False
    

    def is_(self) -> bool:
        try:
            keyAndValue: dict = StdUtil.getInstance().createHashMap()
            keyAndValue.put(self.NOTHING, self.NOTHING)
            hashMap: dict = self.getRow(keyAndValue)
            if hashMap is not None:
                return True
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
                    PreLogUtil.put(self.NOT_IN_DB, self.NAME, self.METHOD_IS)
                return False
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE(self.commonStrings.EXCEPTION, self.NAME, self.METHOD_IS, e)
            return False
    

    def update(self) -> None:
        from org.allbinary.business.init.InitInfo import InitInfo
        self.updateWhere(self.NOTHING, self.NOTHING, InitInfo.getInstance().toHashMap())
    

    def add(self) -> None:
        from org.allbinary.business.init.InitInfo import InitInfo
        from org.allbinary.business.init.InitInfo import InitInfo
        from org.allbinary.business.init.InitInfo import InitInfo
        try:
            values: BasicArrayList = BasicArrayListD()
            values.add(self.NOTHING)
            values.add(InitInfo.getInstance().getTesting())
            values.add(InitInfo.getInstance().getTestHtmlPath())
            values.add(InitInfo.getInstance().getMainPath())
            self.insert(values)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE(self.commonStrings.EXCEPTION, self.NAME, self.METHOD_ADD, e)
    

    def createTable(self) -> str:
        if super().createTable(self.tableData):
            return self.tableName + self.CREATED_SUCCESS
        else:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.FAILED_TO_CREATE)
            stringBuffer.append(self.tableData)
            stringBuffer.append(AbPathData.getInstance().EXTENSION_SEP)
            return str(stringBuffer)
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker


