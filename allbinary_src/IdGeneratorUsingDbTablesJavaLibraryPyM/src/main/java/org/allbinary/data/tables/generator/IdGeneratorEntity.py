# 
# AllBinary Open License Version 1 
# Copyright (c) 2002 AllBinary 
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
# package org.allbinary.data.tables.generator

from __future__ import annotations

from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.generator.IdGeneratorEntityInterface import IdGeneratorEntityInterface


class IdGeneratorEntity(AbSqlBean, IdGeneratorEntityInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "idgenerator"
        self.tableData: str = None
        self.NAME: str = "NAME"
        self.VALUE: str = "VALUE"
    

    def __init__(self) -> None:
        super().__init__(UserDbInitInfo())
        self._init_fields()
        self.tableData = str(StringMaker().append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(self.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(self.VALUE).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(self.NAME).append(self.sqlStrings.END))
        super().setTableName(self.tableName)
    

    # throws Exception
    def get(self, name: str) -> int:
        keysAndValues: dict = StdUtil.getInstance().createHashMap()
        keysAndValues.put(self.NAME, name)
        hashMap: dict = super().getRow(keysAndValues)
        if (hashMap.get(self.NAME)).compareTo(name) != 0:
            raise Exception("results do not match")
        value: str = hashMap.get(self.VALUE)
        return int(value)
    

    def insert(self, values: BasicArrayList) -> None:
        try:
            super().insert(values)
            self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    def delete(self, value: str) -> None:
        try:
            super().deleteWhere(self.NAME, value)
            self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    def update(self, name: str, value: int) -> None:
        map: dict = StdUtil.getInstance().createHashMap()
        map.put(self.NAME, name)
        map.put(self.VALUE, value)
        self.update(map)
    

    # Java overloaded method: Python keeps the last definition
    def update(self, hashMap: dict) -> None:
        super().updateWhere(self.NAME, hashMap.get(self.NAME), hashMap)
    

    def createTable(self) -> str:
        returnStr: str = super().createTable(self.tableData)
        return returnStr
    

    def dropTable(self) -> str:
        return super().dropTable()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker


