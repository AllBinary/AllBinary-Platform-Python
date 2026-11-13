# 
# AllBinary Open License Version 1 
# Copyright (c) 2025 AllBinary 
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

from java.lang.JavaRuntimeStatic import lazy_static
from java.io.Reader import Reader


class NullReader(Reader):
    NULL_READER: NullReader = None

    def __init__(self) -> None:
        super().__init__()
    

    # throws IOException
    def read(self) -> int:
        return -1
    

    # throws IOException
    # Java overloaded method: Python keeps the last definition
    def read(self, cbuf: list[str], off: int, len_: int) -> int:
        return -1
    

    # throws IOException
    def ready(self) -> bool:
        return False
    

    # throws IOException
    def skip(self, n: int) -> int:
        return 0
    

    def close(self) -> None:
        pass
# from java.io.IOException import IOException


def _NullReader_NULL_READER() -> object:
    return NullReader()

lazy_static(NullReader, "NULL_READER", _NullReader_NULL_READER)

