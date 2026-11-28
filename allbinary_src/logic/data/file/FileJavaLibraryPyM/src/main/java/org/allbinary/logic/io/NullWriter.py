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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import lazy_static
from java.io.Writer import Writer


@java_inherited_overloads
class NullWriter(Writer):
    NULL_WRITER: NullWriter = None

    def __init__(self) -> None:
        super().__init__()
    

    # throws IOException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def write_j1_1(self, c: int) -> None:
        pass
    

    # throws IOException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def write_j3_1(self, cbuf: list[str], off: int, len_: int) -> None:
        pass
    

    # throws IOException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def write_j1_2(self, str_: str) -> None:
        pass
    

    # throws IOException
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def write_j3_2(self, str_: str, off: int, len_: int) -> None:
        pass

    def write(self, *args):
        if len(args) == 1 and True and isinstance(args[0], int) and not isinstance(args[0], bool):
            return __class__.__dict__["write_j1_1"].__get__(self, __class__)(*args)
        if len(args) == 3 and True and (args[0] is None or isinstance(args[0], list)) and isinstance(args[1], int) and not isinstance(args[1], bool) and isinstance(args[2], int) and not isinstance(args[2], bool):
            return __class__.__dict__["write_j3_1"].__get__(self, __class__)(*args)
        if len(args) == 1:
            return __class__.__dict__["write_j1_2"].__get__(self, __class__)(*args)
        if len(args) == 3:
            return __class__.__dict__["write_j3_2"].__get__(self, __class__)(*args)
        implementation = __class__.__dict__.get("write_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().write(*args)
    

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

