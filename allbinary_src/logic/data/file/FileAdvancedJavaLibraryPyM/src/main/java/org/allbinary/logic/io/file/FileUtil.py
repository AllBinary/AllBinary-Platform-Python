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
# package org.allbinary.logic.io.file

from __future__ import annotations

import os
import threading


#data/init/views/TestStore/template/type/genericTemplateObjectConfig.xml
class FileUtil:
    instance: FileUtil = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.directory: Directory = Directory.getInstance()
        self.logConfigTypeFactory: LogConfigTypeFactory = LogConfigTypeFactory.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.streamUtil: StreamUtil = StreamUtil.getInstance()
        self.WRITE_LABEL: str = "Write file: "
        self.DATA_LABEL: str = " data: "
        self.WRITE_METHOD: str = "write"
    

    @staticmethod
    def getInstance() -> FileUtil:
        return FileUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def write(self, inputStream: InputStream, file: AbFile) -> None:
        dataOutputStream: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(file)
        self.write(inputStream, dataOutputStream)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def write(self, inputStream: InputStream, dataOutputStream: AbDataOutputStream) -> None:
        try:
            dataOutputStream = StreamUtil.getInstance().get(inputStream, dataOutputStream, [0] * (16384))
            dataOutputStream.flush()
        finally:
            StreamUtil.getInstance().close(dataOutputStream)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def write(self, inputStream: InputStream, dataOutputStream: AbDataOutputStream, buffer: list[int]) -> None:
        try:
            dataOutputStream = StreamUtil.getInstance().get(inputStream, dataOutputStream, buffer)
            dataOutputStream.flush()
        finally:
            StreamUtil.getInstance().close(dataOutputStream)
    

    # throws Exception
    def copy(self, dataInputStream: AbFileInputStream, dataOutputStream: AbDataOutputStream) -> None:
        try:
            dataOutputStream = StreamUtil.getInstance().get(dataInputStream, dataOutputStream, [0] * (16384))
            dataOutputStream.flush()
        finally:
            StreamUtil.getInstance().close(dataOutputStream)
            StreamUtil.getInstance().close(dataInputStream)
    

    # throws Exception
    def fixPath(self, file: AbFile, path: AbPath, realPath: AbPath, cloud: str) -> AbPath:
        beginIndex: int = file.getPath().indexOf(cloud) + len(cloud)
        endIndex: int = file.getPath().indexOf(file.getName())
        fixedPathString: str = str(realPath.toFileSystemString()) + file.getPath().substring(beginIndex, endIndex)
        fixedPath: AbPath = AbPath(fixedPathString, StringUtil.getInstance().EMPTY_STRING)
        self.directory.create(fixedPath)
        string: str = fixedPath.toFileSystemString()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
            self.logUtil.putF(string, self, "fixPath")
        outPath: AbPath = AbPath(string, file.getName())
        return outPath
    

    # throws Exception
    def copyToCloud(self, file: AbFile, path: AbPath, realPath: AbPath, cloud: str) -> None:
        self.copyToCloud(file, path, realPath, cloud, False, False)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def copyToCloud(self, file: AbFile, path: AbPath, realPath: AbPath, cloud: str, overwriteNewer: bool, overwriteAll: bool) -> None:
        from org.allbinary.logic.io.file.AbFile import AbFile
        try:
            outPath: AbPath = self.fixPath(file, path, realPath, cloud)
            outFile: AbFile = AbFile.createAbFileFromAbPath(outPath)
            if not self.copyPrepare(file, outFile, overwriteNewer, overwriteAll):
                return
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("Out File: ")
                    stringBuffer.append(outFile.getPath())
                    stringBuffer.append(" In File: ")
                    stringBuffer.append(file.getPath())
                    stringBuffer.append(" to cloud.")
                    self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), "copyToCloud")
            dataOutputStream: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(outFile)
            fileInputStream: AbFileInputStream = AbFileLocalInputStream(file)
            self.copy(fileInputStream, dataOutputStream)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILEERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Error Copying File File: ")
                stringBuffer.append(str(file))
                stringBuffer.append(" to cloud.")
                self.logUtil.put(str(stringBuffer), FileUtil.getInstance(), "copyToCloud", e)
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def copyToCloud(self, file: AbFile, outFile: AbFile) -> None:
        self.copyToCloud(file, outFile, False, False)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def copyToCloud(self, file: AbFile, outFile: AbFile, overwriteNewer: bool, overwriteAll: bool) -> None:
        try:
            stringBuffer: StringMaker = StringMaker()
            if not self.copyPrepare(file, outFile, overwriteNewer, overwriteAll):
                return
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append("Out File: ")
                    stringBuffer.append(outFile.getPath())
                    stringBuffer.append(" In File: ")
                    stringBuffer.append(file.getPath())
                    stringBuffer.append(" to cloud.")
                    self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), "copyToCloud")
            dataOutputStream: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(outFile)
            fileInputStream: AbFileInputStream = AbFileLocalInputStream(file)
            self.copy(fileInputStream, dataOutputStream)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILEERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Error Copying File File: ")
                stringBuffer.append(str(file))
                stringBuffer.append(" to cloud.")
                self.logUtil.put(str(stringBuffer), FileUtil.getInstance(), "copyToCloud", e)
            raise e
    

    # throws Exception
    def copyPrepare(self, fromFile: AbFile, toFile: AbFile, overwriteNewer: bool, overwriteAll: bool) -> bool:
        if toFile.exists():
            stringBuffer: StringMaker = StringMaker()
            if overwriteAll:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append("Overwriting File: ")
                    stringBuffer.append(toFile.getPath())
                    self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), "copyFile")
                toFile.delete()
                toFile.createNewFile()
            elif toFile.lastModified() < fromFile.lastModified() and overwriteNewer:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append("Newer by: ")
                    stringBuffer.appendlong(int(fromFile.lastModified() - toFile.lastModified()))
                    stringBuffer.append("ms ")
                    stringBuffer.append("Copying File: ")
                    stringBuffer.append(toFile.getPath())
                    self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), "copyFile")
                toFile.delete()
                toFile.createNewFile()
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                    stringBuffer.delete(0, stringBuffer.length())
                    stringBuffer.append("File Already Exists")
                    if overwriteNewer:
                        stringBuffer.append(" And Is Not Older")
                    else:
                        stringBuffer.append(" And Not A In Overwrite Mode")
                    stringBuffer.append(CommonLabels.getInstance().COLON_SEP)
                    stringBuffer.append(toFile.getPath())
                    self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), "copyFile")
                return False
        else:
            toFile.createNewFile()
        return True
    

    # throws Exception
    def copyFile(self, fromFile: AbFile, toFile: AbFile) -> None:
        self.copyFile(fromFile, toFile, False, False)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def copyFile(self, fromFile: AbFile, toFile: AbFile, overwriteNewer: bool, overwriteAll: bool) -> None:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Copying ")
                stringBuffer.appendlong(fromFile.length())
                stringBuffer.append(" bytes from File: ")
                stringBuffer.append(fromFile.getPath())
                stringBuffer.append(" to: ")
                stringBuffer.append(toFile.getPath())
                self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), "copyFile")
            if not self.copyPrepare(fromFile, toFile, overwriteNewer, overwriteAll):
                return
            dataOutputStream: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(toFile)
            fileInputStream: AbFileInputStream = AbFileInputStream(fromFile)
            self.copy(fileInputStream, dataOutputStream)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILEERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Error Copying File fromFile: ")
                stringBuffer.append(str(fromFile))
                stringBuffer.append(" to: ")
                stringBuffer.append(str(toFile))
                self.logUtil.put(str(stringBuffer), FileUtil.getInstance(), "copyFile", e)
            raise e
    

    @staticmethod
    def getNewDirectory(fromFile: AbFile) -> str:
        from org.allbinary.logic.io.file.FilePathData import FilePathData
        newDirectory: str = fromFile.getPath()
        separatorChar: str = FilePathData.getInstance().PATH_START
        if AbIOSystem.getInstance().isType("com.vobject.appengine.java.io"):
            separatorChar = AbPathData.getInstance().SEPARATOR
        lastIndex: int = newDirectory.rfind(separatorChar)
        if lastIndex >= len(newDirectory):
            newDirectory = newDirectory[0:len(newDirectory) - 1]
            lastIndex = newDirectory.rfind(separatorChar)
        return newDirectory[lastIndex:len(newDirectory)]
    

    # throws Exception
    def copyDirectoryPortion(self, fromDirectoryAbPath: AbPath, toDirectoryAbPath: AbPath, overwriteNewer: bool, overwriteAll: bool, current: int, total: int) -> None:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.AbFile import AbFile
        file: AbFile = AbFile.createAbFileFromAbPath(fromDirectoryAbPath)
        if not file.isDirectory():
            raise Exception("Not a directory: " + str(file.getPath()))
        fileList: BasicArrayList = self.directory.search(file, True)
        size: int = fileList.size()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Searched: ")
        stringBuffer.append(file.getPath())
        stringBuffer.append(" Total: ")
        stringBuffer.appendint(size)
        portion: int = int(size / total) + 1
        start: int = portion * current
        end: int = start + portion
        if end > size:
            end = size
        stringBuffer.append(" Section: ")
        stringBuffer.appendint(start)
        stringBuffer.append(" - ")
        stringBuffer.appendint(end)
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
            self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), "copySomeFilesToDirectory()")
        nextFile: AbFile = None
        for index in range(start, end):
            nextFile = fileList.get(index)
            if nextFile.isDirectory():
                pass
            else:
                path: str = AbPath(nextFile.getPath(), StringUtil.getInstance().EMPTY_STRING).getPath()
                beginIndex: int = fromDirectoryAbPath.getPath().length()
                if path.indexOf(self.URLGLOBALS.getWebappPath()) < 0:
                    beginIndex -= AbPath(self.URLGLOBALS.getWebappPath(), StringUtil.getInstance().EMPTY_STRING).getPath().length()
                newPath: str = str(toDirectoryAbPath.toFileSystemString()) + path.substring(beginIndex)
                toFile: AbFile = AbFile.createAbFileFromAbPath(AbPath(newPath, StringUtil.getInstance().EMPTY_STRING))
                self.copyFile(nextFile, toFile, overwriteNewer, overwriteAll)
    

    # throws Exception
    def copyDirectory(self, fromFile: AbFile, to: AbFile) -> None:
        from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.AbFile import AbFile
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Copying Directory from: ")
                stringBuffer.append(fromFile.getPath())
                stringBuffer.append(" to: ")
                stringBuffer.append(to.getPath())
                self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), "copyDirectory")
            newDirectory: str = FileUtil.getNewDirectory(fromFile)
            newDirectoryAbPath: AbPath = AbPath(str(to.getPath() + AbPathData.getInstance().SEPARATOR) + newDirectory, StringUtil.getInstance().EMPTY_STRING)
            if not self.directory.create(newDirectoryAbPath):
                raise Exception("Failed to create directory: " + str(newDirectoryAbPath))
            fileArray: list[AbFile] = FileWrapperUtil.wrapFiles(fromFile.listFiles())
            size: int = len(fileArray)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Copying ")
                stringBuffer.appendint(size)
                stringBuffer.append(" files from: ")
                stringBuffer.append(fromFile.getPath())
                stringBuffer.append(" to: ")
                stringBuffer.append(to.getPath())
                self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), "copyDirectory")
            file: AbFile = None
            for index in range(0, size):
                file = fileArray[index]
                if file.isFile():
                    self.copyFile(file, AbFile.createAbFilePathAndName(str(newDirectoryAbPath), file.getName()))
                elif file.isDirectory():
                    self.copyDirectory(file, AbFile.createAbFileFromAbPath(newDirectoryAbPath))
                else:
                    raise Exception("File Copy Error")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILEERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Error Copying Directory fromFile: ")
                stringBuffer.append(str(fromFile))
                stringBuffer.append(" to: ")
                stringBuffer.append(str(to))
                self.logUtil.put(str(stringBuffer), FileUtil.getInstance(), "copyDirectory", e)
            raise e
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def copy(self, fromAbPath: AbPath, to: AbPath) -> bool:
        with self._lock:
            return self._copy_unlocked(fromAbPath, to)

    def _copy_unlocked(self, fromAbPath: AbPath, to: AbPath) -> bool:
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.FileWrapperUtil import FileWrapperUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.AbFile import AbFile
        COPY: str = "copy"
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Copying AbPaths from: ")
                stringBuffer.append(str(fromAbPath))
                stringBuffer.append(" to: ")
                stringBuffer.append(str(to))
                self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), COPY)
            if fromAbPath is None:
                raise Exception("Cannot Copy From A Null Location")
            if to is None:
                raise Exception("Cannot Copy To A Null Location")
            fromLocationFile: AbFile = AbFile.createAbFileFromAbPath(fromAbPath)
            toLocationFile: AbFile = AbFile.createAbFileFromAbPath(to)
            if fromLocationFile.isFile():
                if toLocationFile.isDirectory():
                    file: AbFile = AbFile.createAbFileWithChild(toLocationFile, fromLocationFile.getName())
                    self.copyFile(fromLocationFile, file)
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                        stringBuffer: StringMaker = StringMaker()
                        stringBuffer.append("Copied file=")
                        stringBuffer.append(fromLocationFile.getName())
                        stringBuffer.append(" from: ")
                        stringBuffer.append(fromLocationFile.getPath())
                        stringBuffer.append(" to: ")
                        stringBuffer.append(toLocationFile.getPath())
                        self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), COPY)
                else:
                    self.copyFile(fromLocationFile, toLocationFile)
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                        stringBuffer: StringMaker = StringMaker()
                        stringBuffer.append("Copied file with new name ")
                        stringBuffer.append(" from: ")
                        stringBuffer.append(fromLocationFile.getPath())
                        stringBuffer.append(" to: ")
                        stringBuffer.append(toLocationFile.getPath())
                        self.logUtil.putF(str(stringBuffer), FileUtil.getInstance(), COPY)
            elif fromLocationFile.isDirectory() and toLocationFile.isDirectory():
                if fromAbPath.toFileSystemString().charAt(fromAbPath.toFileSystemString().length() - 1) == os.sep:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                        self.logUtil.putF("Copying subdirectories", FileUtil.getInstance(), COPY)
                    fileArray: list[AbFile] = FileWrapperUtil.wrapFiles(fromLocationFile.listFiles())
                    for index in range(0, len(fileArray)):
                        file: AbFile = fileArray[index]
                        if file.isFile():
                            aFile: AbFile = AbFile.createAbFileWithChild(toLocationFile, file.getName())
                            self.copyFile(file, aFile)
                        elif file.isDirectory():
                            self.copyDirectory(file, toLocationFile)
                        else:
                            raise Exception("File Copy Error")
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                        self.logUtil.putF("Copied subdirectories", FileUtil.getInstance(), COPY)
                else:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                        self.logUtil.putF("Copyinhg directory", FileUtil.getInstance(), COPY)
                    self.copyDirectory(fromLocationFile, toLocationFile)
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILE):
                        self.logUtil.putF("Copied directory", FileUtil.getInstance(), COPY)
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(self.logConfigTypeFactory.FILEERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Error Copying fromAbPath: ")
                stringBuffer.append(str(fromAbPath))
                stringBuffer.append(" to: ")
                stringBuffer.append(str(to))
                self.logUtil.put(str(stringBuffer), FileUtil.getInstance(), COPY, e)
            raise e
    

    def shouldSkip(self, file: AbFile, skipFiles: list[str]) -> bool:
        size: int = len(skipFiles)
        skipFile: str = None
        for index in range(0, size):
            skipFile = skipFiles[index]
            if file.getPath().compareTo(skipFile) == 0:
                return True
        return False
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def write(self, filePath: str, string: str) -> None:
        dataOutputStream: AbDataOutputStream = None
        try:
            PreLogUtil.put(str(StringMaker().append(self.WRITE_LABEL).append(filePath).append(self.DATA_LABEL).append(string)), self, self.WRITE_METHOD)
            fileInputStreamFactory: FileStreamFactory = FileStreamFactory.getInstance()
            fileOutputStream: OutputStream = fileInputStreamFactory.getFileOutputStreamInstance(StringUtil.getInstance().EMPTY_STRING, filePath)
            dataOutputStream = AbDataOutputStream(fileOutputStream)
            dataOutputStream.write(list(string.encode()), 0, len(string))
            dataOutputStream.flush()
        finally:
            StreamUtil.getInstance().close(dataOutputStream)
    

    def loadFileAsList(self, file: AbFile, max: int, byteArray1: list[int]) -> BasicArrayList:
        from org.allbinary.logic.io.file.FileUtil2 import FileUtil2
        return FileUtil2.getInstance().loadFileAsList(file, max, byteArray1)
# from java.io.InputStream import InputStream
# from java.io.OutputStream import OutputStream
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
from org.allbinary.logic.io.AbFileLocalInputStream import AbFileLocalInputStream
from org.allbinary.logic.io.AbIOSystem import AbIOSystem
from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
from org.allbinary.logic.io.FileStreamFactory import FileStreamFactory
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.directory.Directory import Directory
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList


FileUtil.instance = FileUtil()

