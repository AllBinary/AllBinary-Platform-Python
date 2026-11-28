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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from java.io.InputStream import InputStream


@java_inherited_overloads
class AbFileInputStream(InputStream):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("fileInputStream", None)

    def _init_fields(self) -> None:
        if "fileInputStream" not in vars(self): self.fileInputStream: FileInputStream = None
    

    def __init__(self, fileInputStream: FileInputStream) -> None:
        __class__._java_defaults(self)
        from java.io.FileInputStream import FileInputStream
        from java.io.FileNotFoundException import FileNotFoundException
        super().__init__()
        __class__._init_fields(self)
        self.fileInputStream = fileInputStream
    

    def mark(self, readlimit: int) -> None:
        self.fileInputStream.mark(readlimit)
    

    def markSupported(self) -> bool:
        return self.fileInputStream.markSupported()
    

    # throws IOException
    def reset(self) -> None:
        with self._lock:
            return __class__.__dict__["_reset_unlocked"].__get__(self, __class__)()

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
    def read_j0(self) -> int:
        return self.fileInputStream.read()
    

    # throws IOException
    def read_j1(self, b: list[int]) -> int:
        return self.fileInputStream.read(b)
    

    # throws IOException
    def read_j3(self, buffer: list[int], offset: int, count: int) -> int:
        return self.fileInputStream.read(buffer, offset, count)

    def read(self, *args):
        implementation = __class__.__dict__.get("read_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().read(*args)
    

    # throws IOException
    def skip(self, n: int) -> int:
        return self.fileInputStream.skip(n)
# from java.io.FileInputStream import FileInputStream
# from java.io.FileNotFoundException import FileNotFoundException
# from java.io.IOException import IOException
# from java.nio.channels.FileChannel import FileChannel


