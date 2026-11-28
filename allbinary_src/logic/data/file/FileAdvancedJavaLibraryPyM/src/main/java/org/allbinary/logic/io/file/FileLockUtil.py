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

from java.lang.JavaRuntimeStatic import lazy_static


class FileLockUtil:
    instance: FileLockUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> FileLockUtil:
        return FileLockUtil.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def getAll(self, vector: BasicArrayList, isReturnOnFailure: bool) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
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
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.getAll(vector, False)
    

    # throws Exception
    def getAllOrNone(self, vector: BasicArrayList) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        fileLockVector: BasicArrayList = self.getAll(vector, True)
        if vector.size() != fileLockVector.size():
            return BasicArrayListD()
        else:
            return fileLockVector
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getLock_j1_1(self, file: AbFile) -> FileLock:
        from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
        try:
            return self.getLock(AbFileOutputStream.createFromAbFileAppend(file, True))
        except Exception as e:
            self.logUtil.put("Exception returns null", self, "getLock", e)
            return None
        finally:
            pass
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getLock_j1_2(self, fileOutputStream: AbFileOutputStream) -> FileLock:
        from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
        from org.allbinary.logic.io.StreamUtil import StreamUtil
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
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getLock_j1_3(self, fileChannel: FileChannel) -> FileLock:
        try:
            fileLock: FileLock = fileChannel.tryLock()
            return fileLock
        except Exception as e:
            self.logUtil.put("Exception returns null", self, "getLock", e)
            return None
        finally:
            self.logUtil.putF("Finally - Closing FileChannel", self, "getLock")
            fileChannel.close()

    def getLock(self, *args):
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "AbFile" for base in type(args[0]).__mro__)):
            return __class__.__dict__["getLock_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 1 and True and (args[0] is None or any(base.__name__ == "AbFileOutputStream" for base in type(args[0]).__mro__)):
            return __class__.__dict__["getLock_j1_2"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["getLock_j1_3"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("getLock_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getLock(*args)
# from java.nio.channels.FileChannel import FileChannel
# from java.nio.channels.FileLock import FileLock
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.AbFileOutputStream import AbFileOutputStream
# from org.allbinary.logic.io.StreamUtil import StreamUtil


def _FileLockUtil_instance() -> object:
    return FileLockUtil()

lazy_static(FileLockUtil, "instance", _FileLockUtil_instance)

