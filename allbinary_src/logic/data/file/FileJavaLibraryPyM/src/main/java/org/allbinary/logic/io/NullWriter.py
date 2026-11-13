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
from java.io.Writer import Writer


class NullWriter(Writer):
    NULL_WRITER: NullWriter = None

    def __init__(self) -> None:
        super().__init__()
    

    # throws IOException
    def write(self, c: int) -> None:
        pass
    

    # throws IOException
    # Java overloaded method: Python keeps the last definition
    def write(self, cbuf: list[str], off: int, len_: int) -> None:
        pass
    

    # throws IOException
    # Java overloaded method: Python keeps the last definition
    def write(self, str_: str) -> None:
        pass
    

    # throws IOException
    # Java overloaded method: Python keeps the last definition
    def write(self, str_: str, off: int, len_: int) -> None:
        pass
    

    # throws IOException
    def flush(self) -> None:
        pass
    

    # throws IOException
    def close(self) -> None:
        pass
# from java.io.IOException import IOException


def _NullWriter_NULL_WRITER() -> object:
    return NullWriter()

lazy_static(NullWriter, "NULL_WRITER", _NullWriter_NULL_WRITER)

