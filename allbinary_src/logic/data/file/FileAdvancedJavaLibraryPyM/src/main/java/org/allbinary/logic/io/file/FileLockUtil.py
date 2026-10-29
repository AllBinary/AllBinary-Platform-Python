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



class FileLockUtil:
    instance: FileLockUtil = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> FileLockUtil:
        return FileLockUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getAll(self, vector: BasicArrayList, isReturnOnFailure: bool) -> BasicArrayList:
        fileLockVector: BasicArrayList = BasicArrayListD()
        size: int = vector.size()
        for index in range(0, size):
            file: AbFile = vector.get(index)
            fileLock: FileLock = self.getLock(file)
            if fileLock is not None:
                self.logUtil.putF("File Lock Obtained: " + str(file.getAbsolutePath()), self, "getAll")
                fileLockVector.add(fileLock)
            elif isReturnOnFailure:
                self.logUtil.putF("Total Locks Obtained: " + str(fileLockVector.size()), self, "getAll")
                return fileLockVector
        self.logUtil.putF("Total Locks Obtained: " + str(fileLockVector.size()), self, "getAll")
        return fileLockVector
    

    # throws Exception
    def getAllPossible(self, vector: BasicArrayList) -> BasicArrayList:
        return self.getAll(vector, False)
    

    # throws Exception
    def getAllOrNone(self, vector: BasicArrayList) -> BasicArrayList:
        fileLockVector: BasicArrayList = self.getAll(vector, True)
        if vector.size() != fileLockVector.size():
            return BasicArrayListD()
        else:
            return fileLockVector
    

    # throws Exception
    def getLock(self, file: AbFile) -> FileLock:
        try:
            return self.getLock(AbFileOutputStream.createFromAbFileAppend(file, True))
        except Exception as e:
            self.logUtil.put("Exception returns null", self, "getLock", e)
            return None
        finally:
            pass
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getLock(self, fileOutputStream: AbFileOutputStream) -> FileLock:
        try:
            fileLock: FileLock = self.getLock(fileOutputStream.getChannel())
            return fileLock
        except Exception as e:
            self.logUtil.put("Exception returns null", self, "getLock", e)
            return None
        finally:
            self.logUtil.putF("Finally - Closing FileOutputStream", self, "getLock")
            StreamUtil.getInstance().close(fileOutputStream)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getLock(self, fileChannel: FileChannel) -> FileLock:
        try:
            fileLock: FileLock = fileChannel.tryLock()
            return fileLock
        except Exception as e:
            self.logUtil.put("Exception returns null", self, "getLock", e)
            return None
        finally:
            self.logUtil.putF("Finally - Closing FileChannel", self, "getLock")
            fileChannel.close()
# from java.nio.channels.FileChannel import FileChannel
# from java.nio.channels.FileLock import FileLock
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
from org.allbinary.logic.io.StreamUtil import StreamUtil


FileLockUtil.instance = FileLockUtil()

