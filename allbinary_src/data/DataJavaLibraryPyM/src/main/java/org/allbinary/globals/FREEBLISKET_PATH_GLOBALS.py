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



class FREEBLISKET_PATH_GLOBALS:
    instance: FREEBLISKET_PATH_GLOBALS = None

    def _init_fields(self) -> None:
        self.INSTALLPATH: str = None
        self.XSLPATH: str = None
        self.TEMPLATEPATH: str = "template" + str(AbPathData.getInstance().SEPARATOR)
        self.STYLEPATH: str = self.TEMPLATEPATH + "style" + str(AbPathData.getInstance().SEPARATOR)
        self.THEMEPATH: str = self.STYLEPATH + "theme" + str(AbPathData.getInstance().SEPARATOR)
        self.DBINITPATH: str = str(self.PATH_GLOBALS.getInstance().INIT_PATH) + "db" + str(AbPathData.getInstance().SEPARATOR)
        self.LINEDATAPATH: str = str(self.PATH_GLOBALS.getInstance().INIT_PATH) + "lineData" + str(AbPathData.getInstance().SEPARATOR)
        self.CONFIGURATIONPATH: str = None
        self.USERCONFIGURATIONPATH: str = None
        self.CONTEXTCONFIGURATIONPATH: str = None
        self.LICENSEERRORPAGE: str = "LicensingError.jsp"
        self.ERRORPAGE: str = "Error.jsp"
    

    @staticmethod
    def getInstance() -> FREEBLISKET_PATH_GLOBALS:
        return self.FREEBLISKET_PATH_GLOBALS.instance
    

    def __init__(self) -> None:
        from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
        self._init_fields()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("install")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        self.INSTALLPATH = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(self.PATH_GLOBALS.getInstance().INIT_PATH)
        stringBuffer.append("views")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        self.XSLPATH = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(self.XSLPATH)
        stringBuffer.append("configuration")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        self.CONFIGURATIONPATH = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(self.CONFIGURATIONPATH)
        stringBuffer.append("user")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        self.USERCONFIGURATIONPATH = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(self.CONFIGURATIONPATH)
        stringBuffer.append("context")
        stringBuffer.append(AbPathData.getInstance().SEPARATOR)
        self.CONTEXTCONFIGURATIONPATH = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS


FREEBLISKET_PATH_GLOBALS.instance = FREEBLISKET_PATH_GLOBALS()

