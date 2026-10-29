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
# package org.allbinary.logic.communication.log

from __future__ import annotations



class LogData:

    def _init_fields(self) -> None:
        self.MAX: int = 5000000
        self.extension: str = "log"
        self.backupFileExt: str = str(AbPathData.getInstance().EXTENSION_SEP) + "bak" + str(AbPathData.getInstance().EXTENSION_SEP) + "txt"
        self.ALLBINARY: str = "allbinary"
        self.NAME: str = "LOG_NAME"
        self.DESCRIPTION: str = "LOG_DESCRIPTION"

    def __init__(self) -> None:
        self._init_fields()
from org.allbinary.logic.io.path.AbPathData import AbPathData


