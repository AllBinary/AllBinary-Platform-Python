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

# from java.io.OutputStream import OutputStream


class AbFileOutputStream(OutputStream):

    def _init_fields(self) -> None:
        self.fileOutputStream: FileOutputStream = None
    

    # throws FileNotFoundException
    @staticmethod
    def createFromAbFile(file: AbFile) -> AbFileOutputStream:
        return AbFileOutputStream(FileOutputStream(AbFileNativeUtil.get(file)))
    

    # throws FileNotFoundException
    @staticmethod
    def createFromAbFileAppend(file: AbFile, append: bool) -> AbFileOutputStream:
        return AbFileOutputStream(FileOutputStream(file.getPath()))
    

    # throws FileNotFoundException
    @staticmethod
    def createFromFilePath(name: str) -> AbFileOutputStream:
        return AbFileOutputStream(FileOutputStream(name))
    

    # throws FileNotFoundException
    @staticmethod
    def createFromFilePathAppend(name: str, append: bool) -> AbFileOutputStream:
        return AbFileOutputStream(FileOutputStream(name))
    

    def __init__(self, fileOutputStream: FileOutputStream) -> None:
        super().__init__()
        self._init_fields()
        self.fileOutputStream = fileOutputStream
    

    # throws IOException
    def close(self) -> None:
        self.fileOutputStream.close()
    

    def getChannel(self) -> FileChannel:
        return self.fileOutputStream.getChannel()
    

    # throws IOException
    def write(self, buffer: list[int]) -> None:
        self.fileOutputStream.write(buffer)
    

    # throws IOException
    # Java overloaded method: Python keeps the last definition
    def write(self, buffer: list[int], offset: int, count: int) -> None:
        self.fileOutputStream.write(buffer, offset, count)
    

    # throws IOException
    # Java overloaded method: Python keeps the last definition
    def write(self, b: int) -> None:
        self.fileOutputStream.write(b)
# from java.io.FileNotFoundException import FileNotFoundException
# from java.io.FileOutputStream import FileOutputStream
# from java.io.IOException import IOException
# from java.nio.channels.FileChannel import FileChannel
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.AbFileNativeUtil import AbFileNativeUtil


