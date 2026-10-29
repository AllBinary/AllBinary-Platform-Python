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
# package org.allbinary.log

from __future__ import annotations

import threading
# from java.io.File import File
from org.allbinary.logic.string.StringUtil import StringUtil


class FileLog:
    stringUtil: StringUtil = StringUtil.getInstance()
    logLength: int = 33000000
    logPath: str = "g:\\log\\"
    extension: str = str("dat")
    fileName: str = None
    backupFileName: str = None
    ORG_ALLBINARY: str = "org.allbinary: "
    firstTime: bool = True
    logFile: File = None
    logFileBak: File = None
    fileOut: BufferedWriter = None
    backupIndex: int = 0
    _lock = threading.RLock()
    

    def __init__(self) -> None:
        pass
    

    @staticmethod
    def createLogFile() -> bool:
        with FileLog._lock:
            return FileLog._createLogFile_unlocked()

    @staticmethod
    def _createLogFile_unlocked() -> bool:
        try:
            FileLog.logFile = File(FileLog.logPath, FileLog.fileName)
            if not FileLog.firstTime:
                FileLog.fileOut = BufferedWriter(FileWriter(FileLog.logFile))
            else:
                FileLog.firstTime = False
                raFile: RandomAccessFile = RandomAccessFile(FileLog.logFile, "rw")
                raFile.seek(raFile.length())
                FileLog.fileOut = BufferedWriter(FileWriter(raFile.getFD()))
            canWrite: bool = FileLog.logFile.canWrite()
            return canWrite
        except Exception as e:
            print("Error Creating Log: " + str(e))
            return False
    

    @staticmethod
    def createLogFileBackup() -> bool:
        with FileLog._lock:
            return FileLog._createLogFileBackup_unlocked()

    @staticmethod
    def _createLogFileBackup_unlocked() -> bool:
        try:
            stringMaker: StringMaker = StringMaker()
            FileLog.logFileBak = File(FileLog.logPath, str(stringMaker.append(FileLog.backupFileName).append(CommonSeps.getInstance().PERIOD).appendint(FileLog.backupIndex)))
            while FileLog.logFileBak.isFile():
                FileLog.backupIndex += 1
                stringMaker.delete(0, stringMaker.length())
                FileLog.logFileBak = File(FileLog.logPath, str(stringMaker.append(FileLog.backupFileName).append(CommonSeps.getInstance().PERIOD).appendint(FileLog.backupIndex)))
            line: str = ""
            tmpOut: BufferedWriter = BufferedWriter(FileWriter(FileLog.logFileBak))
            tmpIn: BufferedReader = BufferedReader(FileReader(FileLog.logFile))
            while ((line := tmpIn.readLine())) is not None:
                tmpOut.write(line, 0, len(line))
                tmpOut.newLine()
            tmpOut.flush()
            tmpOut.close()
            tmpIn.close()
            FileLog.logFile.delete()
            return True
        except Exception as e:
            print("Error Creating Backup: " + str(e))
            return False
    

    @staticmethod
    def put(specialMessage: str, anyType: object, functionName: str) -> str:
        with FileLog._lock:
            return FileLog._put_unlocked(specialMessage, anyType, functionName)

    @staticmethod
    def _put_unlocked(specialMessage: str, anyType: object, functionName: str) -> str:
        return FileLog.put(specialMessage, anyType, functionName, None)
    

    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def put(specialMessage: str, anyType: object, functionName: str, exception: BaseException) -> str:
        with FileLog._lock:
            return FileLog._put_unlocked(specialMessage, anyType, functionName, exception)

    @staticmethod
    def _put_unlocked(specialMessage: str, anyType: object, functionName: str, exception: BaseException) -> str:
        try:
            if FileLog.firstTime == True:
                FileLog.createLogFileBackup()
                if FileLog.createLogFile() == False:
                    return str("Log File Creation Error")
            length: int = FileLog.logFile.length()
            if length > FileLog.logLength:
                if not (FileLog.createLogFileBackup()) or FileLog.createLogFile() == False:
                    return str("Couldn't Create a Backup file")
            className: str = str(FileLog.stringUtil.NULL_STRING)
            if functionName is None:
                functionName = str(FileLog.stringUtil.NULL_STRING)
            if specialMessage is None:
                specialMessage = str(FileLog.stringUtil.NULL_STRING)
            if type(anyType).__module__ + "." + type(anyType).__qualname__ is not None:
                className = str(type(anyType).__module__ + "." + type(anyType).__qualname__)
            message: str = LogFormatUtil.getInstance().get(className, functionName, specialMessage, exception)
            FileLog.fileOut.write(message, 0, len(message))
            FileLog.fileOut.newLine()
            FileLog.fileOut.flush()
            return str(str(FileLog.ORG_ALLBINARY) + message)
        except Exception as e:
            return str("Error: " + str(e))
    

    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def put(specialMessage: str, className: str, functionName: str) -> str:
        with FileLog._lock:
            return FileLog._put_unlocked(specialMessage, className, functionName)

    @staticmethod
    def _put_unlocked(specialMessage: str, className: str, functionName: str) -> str:
        return FileLog.put(specialMessage, className, functionName, None)
    

    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def put(specialMessage: str, className: str, functionName: str, exception: Exception) -> str:
        with FileLog._lock:
            return FileLog._put_unlocked(specialMessage, className, functionName, exception)

    @staticmethod
    def _put_unlocked(specialMessage: str, className: str, functionName: str, exception: Exception) -> str:
        try:
            if FileLog.firstTime == True:
                FileLog.createLogFileBackup()
                if FileLog.createLogFile() == False:
                    return str("Log File Creation Error")
            length: int = FileLog.logFile.length()
            if length > FileLog.logLength:
                if not (FileLog.createLogFileBackup()) or FileLog.createLogFile() == False:
                    return str("Couldn't Create a Backup file")
            if functionName is None:
                functionName = str(FileLog.stringUtil.NULL_STRING)
            if specialMessage is None:
                specialMessage = str(FileLog.stringUtil.NULL_STRING)
            message: str = LogFormatUtil.getInstance().get(className, functionName, specialMessage, exception)
            FileLog.fileOut.write(message, 0, len(message))
            FileLog.fileOut.newLine()
            FileLog.fileOut.flush()
            return str(str(FileLog.ORG_ALLBINARY) + message)
        except Exception as e:
            return str("Error: " + str(e))
    

    @staticmethod
    def getFilePath() -> str:
        return FileLog.logPath + FileLog.fileName
# from java.io.BufferedReader import BufferedReader
# from java.io.BufferedWriter import BufferedWriter
# from java.io.FileReader import FileReader
# from java.io.FileWriter import FileWriter
# from java.io.RandomAccessFile import RandomAccessFile
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
from org.allbinary.logic.string.StringMaker import StringMaker


FileLog.fileName = str("log." + str(FileLog.extension))

FileLog.backupFileName = FileLog.fileName.concat(".bak")

FileLog.logFile = File(FileLog.logPath, FileLog.fileName)

