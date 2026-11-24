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
# package org.allbinary.logic.io

from __future__ import annotations

from java.io.OutputStream import OutputStream


class AbFileOutputStream(OutputStream):

    def _init_fields(self) -> None:
        from java.io.FileOutputStream import FileOutputStream
        self.fileOutputStream: FileOutputStream = None
    

    # throws FileNotFoundException
    @staticmethod
    def createFromAbFile(file: AbFile) -> AbFileOutputStream:
        from java.io.FileOutputStream import FileOutputStream
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil
        return AbFileOutputStream(FileOutputStream(AbFileNativeUtil.get(file)))
    

    # throws FileNotFoundException
    @staticmethod
    def createFromAbFileAppend(file: AbFile, append: bool) -> AbFileOutputStream:
        from java.io.FileOutputStream import FileOutputStream
        from org.allbinary.logic.io.file.AbFile import AbFile
        return AbFileOutputStream(FileOutputStream(file.getPath()))
    

    # throws FileNotFoundException
    @staticmethod
    def createFromFilePath(name: str) -> AbFileOutputStream:
        from java.io.FileOutputStream import FileOutputStream
        return AbFileOutputStream(FileOutputStream(name))
    

    # throws FileNotFoundException
    @staticmethod
    def createFromFilePathAppend(name: str, append: bool) -> AbFileOutputStream:
        from java.io.FileOutputStream import FileOutputStream
        return AbFileOutputStream(FileOutputStream(name))
    

    def __init__(self, fileOutputStream: FileOutputStream) -> None:
        from java.io.FileOutputStream import FileOutputStream
        super().__init__()
        self._init_fields()
        self.fileOutputStream = fileOutputStream
    

    # throws IOException
    def close(self) -> None:
        self.fileOutputStream.close()
    

    def getChannel(self) -> FileChannel:
        return self.fileOutputStream.getChannel()
    

    # throws IOException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def write_j1_1(self, buffer: list[int]) -> None:
        self.fileOutputStream.write(buffer)
    

    # throws IOException
    def write_j3(self, buffer: list[int], offset: int, count: int) -> None:
        self.fileOutputStream.write(buffer, offset, count)
    

    # throws IOException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def write_j1_2(self, b: int) -> None:
        self.fileOutputStream.write(b)

    def write(self, *args):
        if len(args) == 1 and True and (args[0] is None or isinstance(args[0], list)):
            return self.write_j1_1(*args)
        if len(args) == 1:
            return self.write_j1_2(*args)
        return getattr(self, "write_j" + str(len(args)))(*args)
# from java.io.FileNotFoundException import FileNotFoundException
# from java.io.FileOutputStream import FileOutputStream
# from java.io.IOException import IOException
# from java.nio.channels.FileChannel import FileChannel
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil


