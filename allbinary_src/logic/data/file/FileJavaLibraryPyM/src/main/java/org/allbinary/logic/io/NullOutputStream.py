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
from java.io.OutputStream import OutputStream


class NullOutputStream(OutputStream):
    NULL_OUTPUT_STREAM: NullOutputStream = None

    def __init__(self) -> None:
        super().__init__()
    

    # throws IOException
    def write(self, b: int) -> None:
        pass
    

    # throws IOException
    # Java overloaded method: Python keeps the last definition
    def write(self, b: list[int], off: int, len_: int) -> None:
        pass
    

    def close(self) -> None:
        pass
# from java.io.IOException import IOException


def _NullOutputStream_NULL_OUTPUT_STREAM() -> object:
    return NullOutputStream()

lazy_static(NullOutputStream, "NULL_OUTPUT_STREAM", _NullOutputStream_NULL_OUTPUT_STREAM)

