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

import threading
# from java.io.InputStream import InputStream


class AbFileInputStream(InputStream):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.fileInputStream: FileInputStream = None
    

    def __init__(self, fileInputStream: FileInputStream) -> None:
        super().__init__()
        self._init_fields()
        self.fileInputStream = fileInputStream
    

    def mark(self, readlimit: int) -> None:
        self.fileInputStream.mark(readlimit)
    

    def markSupported(self) -> bool:
        return self.fileInputStream.markSupported()
    

    # throws IOException
    def reset(self) -> None:
        with self._lock:
            return self._reset_unlocked()

    def _reset_unlocked(self) -> None:
        self.fileInputStream.reset()
    

    # throws IOException
    def available(self) -> int:
        return self.fileInputStream.available()
    

    # throws IOException
    def close(self) -> None:
        self.fileInputStream.close()
    

    def getChannel(self) -> FileChannel:
        return self.fileInputStream.getChannel()
    

    # throws IOException
    def read(self) -> int:
        return self.fileInputStream.read()
    

    # throws IOException
    # Java overloaded method: Python keeps the last definition
    def read(self, b: list[int]) -> int:
        return self.fileInputStream.read(b)
    

    # throws IOException
    # Java overloaded method: Python keeps the last definition
    def read(self, buffer: list[int], offset: int, count: int) -> int:
        return self.fileInputStream.read(buffer, offset, count)
    

    # throws IOException
    def skip(self, n: int) -> int:
        return self.fileInputStream.skip(n)
# from java.io.FileInputStream import FileInputStream
# from java.io.FileNotFoundException import FileNotFoundException
# from java.io.IOException import IOException
# from java.nio.channels.FileChannel import FileChannel


