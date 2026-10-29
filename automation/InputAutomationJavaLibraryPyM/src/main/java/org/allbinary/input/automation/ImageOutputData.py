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

import os
import platform
from org.allbinary.logic.io.file.FilePathData import FilePathData
from org.allbinary.logic.string.StringMaker import StringMaker


class ImageOutputData:
    SAVE_PATH: str = str(StringMaker().append({"os.name": platform.system(), "os.arch": platform.machine(), "os.version": platform.version(), "user.home": os.path.expanduser("~")}.get("user.dir", os.environ.get(str("user.dir")))).appendchar(FilePathData.getInstance().SEPARATORCHAR).append("saves").appendchar(FilePathData.getInstance().SEPARATORCHAR))
    

    def __init__(self) -> None:
        pass


