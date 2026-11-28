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

import threading
from java.lang.JavaRuntimeStatic import lazy_static


class AbSqlTableUtil:
    instance: AbSqlTableUtil = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.string.CommonStrings import CommonStrings
        self.TABLE_LABEL: str = "Table: "
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.sqlStrings: SqlStrings = SqlStrings.getInstance()

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    @staticmethod
    def getInstance() -> AbSqlTableUtil:
        return AbSqlTableUtil.instance
    

    def backupTable(self, abSqlTable: AbSqlTable) -> str:
        with self._lock:
            return __class__.__dict__["_backupTable_unlocked"].__get__(self, __class__)(abSqlTable)

    def _backupTable_unlocked(self, abSqlTable: AbSqlTable) -> str:
        tableName: str = abSqlTable.getTableName()
        return self.TABLE_LABEL + tableName + " Backup Failed"
    

    def restoreTable(self, abSqlTable: AbSqlTable, portion: Portion) -> str:
        with self._lock:
            return __class__.__dict__["_restoreTable_unlocked"].__get__(self, __class__)(abSqlTable, portion)

    def _restoreTable_unlocked(self, abSqlTable: AbSqlTable, portion: Portion) -> str:
        from org.allbinary.business.installer.Portion import Portion
        from org.allbinary.logic.string.StringMaker import StringMaker
        tableName: str = abSqlTable.getTableName()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(self.TABLE_LABEL)
        stringBuffer.append(tableName)
        stringBuffer.append(" Restoration Failed")
        return str(stringBuffer)
# from org.allbinary.business.installer.Portion import Portion
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.communication.sql.SqlStrings import SqlStrings


def _AbSqlTableUtil_instance() -> object:
    return AbSqlTableUtil()

lazy_static(AbSqlTableUtil, "instance", _AbSqlTableUtil_instance)

