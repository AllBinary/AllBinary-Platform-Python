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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.logic.communication.sql.AbSqlBean import AbSqlBean
from org.allbinary.data.tables.generator.IdGeneratorEntityInterface import IdGeneratorEntityInterface


@java_inherited_overloads
class IdGeneratorEntity(*java_bases(AbSqlBean, IdGeneratorEntityInterface)):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("tableName", None)
        vars(self).setdefault("tableData", None)
        vars(self).setdefault("NAME", None)
        vars(self).setdefault("VALUE", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.tableName: str = "idgenerator"
        if "tableData" not in vars(self): self.tableData: str = None
        self.NAME: str = "NAME"
        self.VALUE: str = "VALUE"
    

    def __init__(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
        from org.allbinary.logic.string.StringMaker import StringMaker
        super().__init__(UserDbInitInfo())
        __class__._init_fields(self)
        self.tableData = str(StringMaker().append(self.sqlStrings.CREATE_TABLE).append(self.tableName).append(self.sqlStrings.START).append(self.NAME).append(self.sqlTypeStrings.MAX_CHAR_COLUMN_NOT_NULL).append(self.VALUE).append(self.sqlTypeStrings.MAX_BIG_INT_UNSIGNED_NOT_NULL).append(self.sqlStrings.PRIMARY_KEY).append(self.NAME).append(self.sqlStrings.END))
        java_super_call(super(), "setTableName", self.tableName)
    

    # throws Exception
    def get(self, name: str) -> int:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        keysAndValues: HashMap = StdUtil.getInstance().createHashMap()
        keysAndValues.put(self.NAME, name)
        hashMap: HashMap = java_super_call(super(), "getRow", keysAndValues)
        if (hashMap.get(self.NAME)).compareTo(name) != 0:
            raise Exception("results do not match")
        value: str = hashMap.get(self.VALUE)
        return int(value)
    

    def insert(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        try:
            java_super_call(super(), "insert", values)
            self.logUtil.putF(self.commonStrings.SUCCESS, self, self.INSERT)
        except Exception as e:
            self.logUtil.put(self.commonStrings.FAILURE, self, self.INSERT, e)
    

    def delete(self, value: str) -> None:
        try:
            java_super_call(super(), "deleteWhere", self.NAME, value)
            self.logUtil.putF(self.commonStrings.SUCCESS, self, self.commonStrings.delete)
        except Exception as e:
            self.logUtil.put(self.commonStrings.FAILURE, self, self.commonStrings.delete, e)
    

    def update_j2(self, name: str, value: int) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.StdUtil import StdUtil
        map: HashMap = StdUtil.getInstance().createHashMap()
        map.put(self.NAME, name)
        map.put(self.VALUE, value)
        self.update(map)
    

    def update_j1(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        java_super_call(super(), "updateWhere", self.NAME, hashMap.get(self.NAME), hashMap)

    def update(self, *args):
        implementation = __class__.__dict__.get("update_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().update(*args)
    

    def createTable(self) -> str:
        returnStr: str = java_super_call(super(), "createTable", self.tableData)
        return returnStr
    

    def dropTable(self) -> str:
        return java_super_call(super(), "dropTable")
    

    def deleteWhere(self, key: str, value: str) -> None:
        java_super_call(super(), "deleteWhere", key, value)
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.init.db.UserDbInitInfo import UserDbInitInfo
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker


