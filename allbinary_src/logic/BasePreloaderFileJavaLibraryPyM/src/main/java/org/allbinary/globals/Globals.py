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



class Globals:
    instance: Globals = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> Globals:
        return Globals.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def init(self, classLoader: ClassLoader, pathString: str) -> None:
        from org.allbinary.globals.AppUrlGlobals import AppUrlGlobals
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        commonStrings: CommonStrings = CommonStrings.getInstance()
        appUrlGlobals: AppUrlGlobals = AppUrlGlobals()
        appUrlGlobals.setWebappPath(pathString)
        self.URLGLOBALS.init(appUrlGlobals)
        WebappClassLoaderInfo.setLoader(classLoader)
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Setting Up AllBinary System Configuration Args: ")
        stringBuffer.append(pathString)
        stringBuffer.append(" ClassLoader: ")
        stringBuffer.append(type(classLoader).__module__ + "." + type(classLoader).__qualname__)
        self.logUtil.putF(str(stringBuffer), self, commonStrings.INIT)
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if stringValidationUtil.isEmpty(pathString):
            stringBuffer.delete(0, stringBuffer.length())
            stringBuffer.append("No Path Provided. Using Process Path: ")
            stringBuffer.append(pathString)
            stringBuffer.append(CommonSeps.getInstance().SPACE)
            stringBuffer.append(CommonSeps.getInstance().EQUALS)
            stringBuffer.append(CommonSeps.getInstance().SPACE)
            stringBuffer.append(self.URLGLOBALS.getWebappPath())
            self.logUtil.putF(str(stringBuffer), self, commonStrings.INIT)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append("Webapp Path Set To: ")
        stringBuffer.append(self.URLGLOBALS.getWebappPath())
        self.logUtil.putF(str(stringBuffer), self, commonStrings.INIT)
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.system.loader.WebappClassLoaderInfo import WebappClassLoaderInfo
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings


Globals.instance = Globals()

