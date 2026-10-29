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

import datetime
import threading


class AbSqlTableUtil:
    instance: AbSqlTableUtil = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.EXTENSION: str = ".adb"
        self.END: str = "')\n"
        self.SAVING_BACKUP_PATH: str = "Saving Backup: Path: "
        self.FILE_LABEL: str = " File: "
        self.METHOD_RESTORE_TABLE: str = "restoreTable()"
        self.METHOD_BACKUP_TABLE: str = "backupTable()"
        self.METHOD_BACKUP_FILE: str = "backupFile()"
        self.METHOD_GET_OUTPUT_STREAM: str = "getOutputStream()"
        self.TABLE_CREATION_SUCCESS: str = "Table Creation Successful: "
        self.DROPPED_SUCCESS: str = " Dropped Successfully"
        self.SAVING: str = "Saving: "
        self.APPENDING: str = "Appending: "
        self.TABLE_LABEL: str = "Table: "
        self.BACKUP_SUCCESS: str = " Backup Success"
        self.ERROR_CREATING: str = "Error Creating: "
        self.TOTAL_LABEL: str = " Total: "
        self.SECTION_LABEL: str = " Section: "
        self.DASH: str = " - "
        self.PORTION_RESTORED: str = " Portion Restored"
        self.specialCharArray: list[str] = ['\n', '\f', '\r']
        self.NEW_LINE: str = "\\n"
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.sqlStrings: SqlStrings = SqlStrings.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> AbSqlTableUtil:
        return AbSqlTableUtil.instance
    

    def getOutputStream(self, backupPath: str, tableName: str) -> OutputStream:
        with self._lock:
            return self._getOutputStream_unlocked(backupPath, tableName)

    def _getOutputStream_unlocked(self, backupPath: str, tableName: str) -> OutputStream:
        try:
            fileName: str = tableName + self.EXTENSION
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(self.SAVING + tableName, self, self.METHOD_GET_OUTPUT_STREAM)
            backupFilePath: AbPath = AbPath(backupPath, fileName)
            backupFile: AbFile = AbFile.createAbFile(backupFilePath)
            if backupFile.exists():
                self.backupFile(backupFilePath, backupPath, tableName)
                backupFile.delete()
            backupFile.createNewFile()
            outputStream: OutputStream = AbFileOutputStream(backupFile)
            return outputStream
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put("Create File", self, self.METHOD_GET_OUTPUT_STREAM, e)
            return None
    

    def backupFile(self, path: AbPath, backupPath: str, tableName: str) -> bool:
        with self._lock:
            return self._backupFile_unlocked(path, backupPath, tableName)

    def _backupFile_unlocked(self, path: AbPath, backupPath: str, tableName: str) -> bool:
        try:
            calendar: datetime.datetime = datetime.datetime.now()
            timeLong: int = int(calendar.getTimeInMillis())
            time: str = str(timeLong)
            stringBuffer: StringMaker = StringMaker()
            fileName: str = tableName + self.EXTENSION
            stringBuffer.append(backupPath)
            stringBuffer.append(AbPathData.getInstance().SEPARATOR)
            stringBuffer.append(time)
            backupAbPath: AbPath = AbPath(str(stringBuffer))
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(self.SAVING_BACKUP_PATH)
                stringBuffer.append(backupAbPath.toFileSystemString())
                stringBuffer.append(self.FILE_LABEL)
                stringBuffer.append(fileName)
                self.logUtil.putF(str(stringBuffer), self, self.METHOD_BACKUP_FILE)
            Directory.create(backupAbPath)
            backupFileBak: AbFile = AbFile.createAbFile(backupAbPath.toFileSystemString())
            backupFileBak.createNewFile()
            FileUtil.getInstance().copy(path, backupAbPath)
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.METHOD_BACKUP_FILE, e)
            return False
    

    def convertNewLines(self, value: str) -> str:
        stringBuffer: StringMaker = StringMaker()
        index: int = 0
        lastIndex: int = 0
        while index < len(value):
            index = value.find(self.specialCharArray[0], lastIndex)
            if index != -1:
                nextLine: str = value[lastIndex:index - 1]
                stringBuffer.append(nextLine)
                stringBuffer.append(self.NEW_LINE)
                lastIndex = index + 1
            else:
                break
        if lastIndex < len(value):
            stringBuffer.append(value[lastIndex:len(value)])
        return str(stringBuffer)
    

    def backupTable(self, abSqlTable: AbSqlTable) -> str:
        with self._lock:
            return self._backupTable_unlocked(abSqlTable)

    def _backupTable_unlocked(self, abSqlTable: AbSqlTable) -> str:
        from org.allbinary.logic.communication.sql.StringBuilder import StringBuilder
        tableName: str = abSqlTable.getTableName()
        try:
            count: int = 0
            sqlStatement: str = str(self.sqlStrings.SELECT_ALL_FROM) + tableName
            path: str = org.allbinary.globals.URLGLOBALS.getMainPath() + self.PATH_GLOBALS.getInstance().BACKUP_PATH
            if not Directory.create(AbPath(path)):
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.ERROR_CREATING + str(path), self, self.METHOD_BACKUP_TABLE)
            rset: ResultSet = abSqlTable.executeSQLStatement(sqlStatement)
            rsmd: ResultSetMetaData = rset.getMetaData()
            colNum: int = rsmd.getColumnCount()
            QUERY_START: str = str(StringBuilder().append(self.sqlStrings.INSERT_INTO).append(tableName).append(self.sqlStrings.VALUES))
            stringBuffer: StringMaker = StringMaker()
            outputStream: OutputStream = self.getOutputStream(path, tableName)
            while rset.next():
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(QUERY_START)
                for i in range(1, colNum):
                    value: str = rset.getString(i)
                    stringBuffer.append(self.convertNewLines(value))
                    stringBuffer.append(self.sqlStrings.SINGLE_QUOTE_COMMA_SEP)
                stringBuffer.append(rset.getString(colNum))
                stringBuffer.append(self.END)
                sqlStatementLine: str = str(stringBuffer)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                    self.logUtil.putF(self.APPENDING + sqlStatementLine, self, self.METHOD_BACKUP_TABLE)
                outputStream.write(list(sqlStatementLine.encode()))
            StreamUtil.getInstance().close(outputStream)
            return self.TABLE_LABEL + tableName + self.BACKUP_SUCCESS
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put("Backup Table Failed\nSQL Statement", self, self.METHOD_BACKUP_TABLE, e)
            return self.TABLE_LABEL + tableName + " Backup Failed"
    

    def restoreTable(self, abSqlTable: AbSqlTable, portion: Portion) -> str:
        with self._lock:
            return self._restoreTable_unlocked(abSqlTable, portion)

    def _restoreTable_unlocked(self, abSqlTable: AbSqlTable, portion: Portion) -> str:
        tableName: str = abSqlTable.getTableName()
        try:
            path: str = org.allbinary.globals.URLGLOBALS.getMainPath() + self.PATH_GLOBALS.getInstance().BACKUP_PATH
            current: int = int(portion.getCurrent())
            if current == 0:
                if Directory.create(AbPath(path)):
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                        self.logUtil.putF(self.ERROR_CREATING + str(path), self, self.METHOD_RESTORE_TABLE)
            backupFile: AbFile = AbFile.createAbFile(path, tableName + self.EXTENSION)
            bufferedLineReader: BufferedLineReader = BufferedLineReader(backupFile)
            size: int = bufferedLineReader.getSize()
            section: int = size / int(portion.getTotal()) + 1
            start: int = section * current
            end: int = start + section
            if end > size:
                end = size
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.TOTAL_LABEL)
            stringBuffer.append(size)
            stringBuffer.append(self.SECTION_LABEL)
            stringBuffer.append(start)
            stringBuffer.append(self.DASH)
            stringBuffer.append(end)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGING):
                self.logUtil.putF(str(stringBuffer), self, self.METHOD_RESTORE_TABLE)
            bufferedLineReader.readUpToLines(start)
            line: str = self.stringUtil.EMPTY_STRING
            while bufferedLineReader.getCurrent() < end and ((line := bufferedLineReader.readLine())) is not None:
                if len(line) > 1:
                    abSqlTable.executeSQLStatement(line)
            stringBuffer.append(self.commonSeps.SPACE)
            stringBuffer.append(self.TABLE_LABEL)
            stringBuffer.append(tableName)
            stringBuffer.append(self.PORTION_RESTORED)
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLLOGGINGERROR):
                self.logUtil.put("Restore Table Failed\nSQL Statement", self, self.METHOD_RESTORE_TABLE, e)
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(self.TABLE_LABEL)
            stringBuffer.append(tableName)
            stringBuffer.append(" Restoration Failed")
            return str(stringBuffer)
from org.allbinary.logic.string.StringMaker import StringMaker
# from java.sql.ResultSet import ResultSet
# from java.sql.ResultSetMetaData import ResultSetMetaData
# from java.util.Calendar import Calendar
from org.allbinary.business.installer.Portion import Portion
from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
from org.allbinary.logic.io.BufferedLineReader import BufferedLineReader
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.FileUtil import FileUtil
from org.allbinary.logic.io.file.directory.Directory import Directory
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
# from java.io.OutputStream import OutputStream
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.communication.sql.SqlStrings import SqlStrings


AbSqlTableUtil.instance = AbSqlTableUtil()

