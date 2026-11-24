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
# package org.allbinary.logic.java.number

from __future__ import annotations

from java.lang.JavaRuntimeStatic import lazy_static


class LongData:
    MAX_LONG_LENGTH: int = None
    

    def __init__(self) -> None:
        pass


def _LongData_MAX_LONG_LENGTH() -> object:
    return len(str(int(9223372036854775807)))

lazy_static(LongData, "MAX_LONG_LENGTH", _LongData_MAX_LONG_LENGTH)

