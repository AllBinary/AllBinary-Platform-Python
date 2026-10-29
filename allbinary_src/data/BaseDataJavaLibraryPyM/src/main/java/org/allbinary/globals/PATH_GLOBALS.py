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
# package org.allbinary.globals

from __future__ import annotations



class PATH_GLOBALS:
    instance: PATH_GLOBALS = None

    def _init_fields(self) -> None:
        self.DATA_PATH: str = None
        self.INIT_PATH: str = None
        self.VIEWS_PATH: str = None
        self.LOG_PATH: str = None
        self.BACKUP_PATH: str = None
    

    @staticmethod
    def getInstance() -> PATH_GLOBALS:
        return self.PATH_GLOBALS.instance
    

    def __init__(self) -> None:
        self._init_fields()
        stringBuffer: StringMaker = StringMaker()
        abPathData: AbPathData = AbPathData.getInstance()
        stringBuffer.append("data")
        stringBuffer.append(abPathData.SEPARATOR)
        self.DATA_PATH = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(self.DATA_PATH)
        stringBuffer.append(CommonStrings.getInstance().INIT)
        stringBuffer.append(abPathData.SEPARATOR)
        self.INIT_PATH = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(self.DATA_PATH)
        stringBuffer.append("log")
        stringBuffer.append(abPathData.SEPARATOR)
        self.LOG_PATH = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(self.DATA_PATH)
        stringBuffer.append("backup")
        stringBuffer.append(abPathData.SEPARATOR)
        self.BACKUP_PATH = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(self.INIT_PATH)
        stringBuffer.append("views")
        stringBuffer.append(abPathData.SEPARATOR)
        self.VIEWS_PATH = str(stringBuffer)
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonStrings import CommonStrings


PATH_GLOBALS.instance = PATH_GLOBALS()

