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
# package org.allbinary.input.automation

from __future__ import annotations

from java.lang.System import System
import os
import platform
from java.lang.JavaRuntimeStatic import lazy_static


class ImageOutputData:
    SAVE_PATH: str = None
    

    def __init__(self) -> None:
        pass
# from org.allbinary.logic.io.file.FilePathData import FilePathData
# from org.allbinary.logic.string.StringMaker import StringMaker


def _ImageOutputData_SAVE_PATH() -> object:
    from org.allbinary.logic.io.file.FilePathData import FilePathData
    from org.allbinary.logic.string.StringMaker import StringMaker
    return str(StringMaker().append(System.getProperty("user.dir")).appendchar(FilePathData.getInstance().SEPARATORCHAR).append("saves").appendchar(FilePathData.getInstance().SEPARATORCHAR))

lazy_static(ImageOutputData, "SAVE_PATH", _ImageOutputData_SAVE_PATH)

