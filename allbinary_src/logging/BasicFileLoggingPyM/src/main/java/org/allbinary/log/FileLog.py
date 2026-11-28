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

from java.lang.System import System
from java.lang.JavaRuntimeStatic import java_predicate
import threading
from java.lang.JavaRuntimeStatic import lazy_static


class FileLog:
    stringUtil: StringUtil = None
    logLength: int = 33000000
    logPath: str = "g:\\log\\"
    extension: str = None
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
        from java.io.File import File
        from java.io.FileWriter import FileWriter
        try:
            FileLog.logFile = File(FileLog.logPath, FileLog.fileName)
            if not (FileLog.firstTime):
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
        from java.io.BufferedReader import BufferedReader
        from java.io.File import File
        from java.io.FileWriter import FileWriter
        from org.allbinary.string.CommonSeps import CommonSeps
        from org.allbinary.logic.string.StringMaker import StringMaker
        try:
            stringMaker: StringMaker = StringMaker()
            FileLog.logFileBak = File(FileLog.logPath, str(stringMaker.append(FileLog.backupFileName).append(CommonSeps.getInstance().PERIOD).appendint(FileLog.backupIndex)))
            while java_predicate(FileLog.logFileBak, "isFile"):
                FileLog.backupIndex += 1
                stringMaker.delete(0, stringMaker.length())
                FileLog.logFileBak = File(FileLog.logPath, str(stringMaker.append(FileLog.backupFileName).append(CommonSeps.getInstance().PERIOD).appendint(FileLog.backupIndex)))
            line: str = ""
            tmpOut: BufferedWriter = BufferedWriter(FileWriter(FileLog.logFileBak))
            tmpIn: BufferedReader = BufferedReader(FileReader(FileLog.logFile))
            while tmpIn.ready():
                line = tmpIn.readLine()
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
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def put_j3_1(specialMessage: str, anyType: object, functionName: str) -> str:
        with FileLog._lock:
            return FileLog._put_j3_1_unlocked(specialMessage, anyType, functionName)

    @staticmethod
    def _put_j3_1_unlocked(specialMessage: str, anyType: object, functionName: str) -> str:
        return FileLog.put(specialMessage, anyType, functionName, None)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def put_j4_1(specialMessage: str, anyType: object, functionName: str, exception: BaseException) -> str:
        with FileLog._lock:
            return FileLog._put_j4_1_unlocked(specialMessage, anyType, functionName, exception)

    @staticmethod
    def _put_j4_1_unlocked(specialMessage: str, anyType: object, functionName: str, exception: BaseException) -> str:
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        try:
            if FileLog.firstTime == True:
                FileLog.createLogFileBackup()
                if FileLog.createLogFile() == False:
                    return str("Log File Creation Error")
            length: int = __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(FileLog.logFile)
            if length > FileLog.logLength:
                if not (FileLog.createLogFileBackup()) or FileLog.createLogFile() == False:
                    return str("Couldn't Create a Backup file")
            className: str = str(FileLog.stringUtil.NULL_STRING)
            if functionName is None:
                functionName = str(FileLog.stringUtil.NULL_STRING)
            if specialMessage is None:
                specialMessage = str(FileLog.stringUtil.NULL_STRING)
            if __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(anyType)) is not None:
                className = str(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(anyType)))
            message: str = LogFormatUtil.getInstance().get(className, functionName, specialMessage, exception)
            FileLog.fileOut.write(message, 0, len(message))
            FileLog.fileOut.newLine()
            FileLog.fileOut.flush()
            return str(str(FileLog.ORG_ALLBINARY) + message)
        except Exception as e:
            return str("Error: " + str(e))
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def put_j3_2(specialMessage: str, className: str, functionName: str) -> str:
        with FileLog._lock:
            return FileLog._put_j3_2_unlocked(specialMessage, className, functionName)

    @staticmethod
    def _put_j3_2_unlocked(specialMessage: str, className: str, functionName: str) -> str:
        return FileLog.put(specialMessage, className, functionName, None)
    

    # Java overloaded method with the same parameter count: Python keeps the last definition
    @staticmethod
    def put_j4_2(specialMessage: str, className: str, functionName: str, exception: Exception) -> str:
        with FileLog._lock:
            return FileLog._put_j4_2_unlocked(specialMessage, className, functionName, exception)

    @staticmethod
    def _put_j4_2_unlocked(specialMessage: str, className: str, functionName: str, exception: Exception) -> str:
        from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
        try:
            if FileLog.firstTime == True:
                FileLog.createLogFileBackup()
                if FileLog.createLogFile() == False:
                    return str("Log File Creation Error")
            length: int = __import__("java.lang.JavaRuntimeStatic", fromlist=["java_length"]).java_length(FileLog.logFile)
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
    def put(*args):
        if len(args) == 3 and True and (args[0] is None or isinstance(args[0], str)) and (args[2] is None or isinstance(args[2], str)):
            return FileLog.put_j3_1(*args)
        if len(args) == 4 and True and (args[0] is None or isinstance(args[0], str)) and (args[2] is None or isinstance(args[2], str)) and not isinstance(args[3], (str, list, int, float)):
            return FileLog.put_j4_1(*args)
        if len(args) == 3:
            return FileLog.put_j3_2(*args)
        if len(args) == 4:
            return FileLog.put_j4_2(*args)
        return getattr(FileLog, "put_j" + str(len(args)))(*args)
    

    @staticmethod
    def getFilePath() -> str:
        return FileLog.logPath + FileLog.fileName
# from java.io.BufferedReader import BufferedReader
# from java.io.BufferedWriter import BufferedWriter
# from java.io.File import File
# from java.io.FileReader import FileReader
# from java.io.FileWriter import FileWriter
# from java.io.RandomAccessFile import RandomAccessFile
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.communication.log.LogFormatUtil import LogFormatUtil
# from org.allbinary.logic.string.StringMaker import StringMaker


def _FileLog_stringUtil() -> object:
    from org.allbinary.logic.string.StringUtil import StringUtil
    return StringUtil.getInstance()

lazy_static(FileLog, "stringUtil", _FileLog_stringUtil)

def _FileLog_extension() -> object:
    return str("dat")

lazy_static(FileLog, "extension", _FileLog_extension)

def _FileLog_fileName() -> object:
    return str("log." + str(FileLog.extension))

lazy_static(FileLog, "fileName", _FileLog_fileName)

def _FileLog_backupFileName() -> object:
    return FileLog.fileName.concat(".bak")

lazy_static(FileLog, "backupFileName", _FileLog_backupFileName)

def _FileLog_logFile() -> object:
    from java.io.File import File
    return File(FileLog.logPath, FileLog.fileName)

lazy_static(FileLog, "logFile", _FileLog_logFile)

