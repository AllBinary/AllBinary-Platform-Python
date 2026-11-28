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
from java.io.OutputStream import OutputStream


@java_inherited_overloads
class NullOutputStream(OutputStream):
    NULL_OUTPUT_STREAM: NullOutputStream = None

    def __init__(self) -> None:
        super().__init__()
    

    # throws IOException
    def write_j1(self, b: int) -> None:
        pass
    

    # throws IOException
    def write_j3(self, b: list[int], off: int, len_: int) -> None:
        pass

    def write(self, *args):
        implementation = __class__.__dict__.get("write_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().write(*args)
    

    def close(self) -> None:
        pass
# from java.io.IOException import IOException


def _NullOutputStream_NULL_OUTPUT_STREAM() -> object:
    return NullOutputStream()

lazy_static(NullOutputStream, "NULL_OUTPUT_STREAM", _NullOutputStream_NULL_OUTPUT_STREAM)

