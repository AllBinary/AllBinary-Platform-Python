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

from org.allbinary.globals.AppUrlGlobals import AppUrlGlobals


class URLGLOBALS:
    urlGlobalsInterface: UrlGlobalsInterface = AppUrlGlobals.NULL_APP_URL_GLOBALS
    

    @staticmethod
    def init(urlGlobalsInterface: UrlGlobalsInterface) -> None:
        self.URLGLOBALS.urlGlobalsInterface = urlGlobalsInterface
    

    @staticmethod
    def isTestingMode() -> bool:
        return self.URLGLOBALS.urlGlobalsInterface.isTestingMode()
    

    @staticmethod
    def getWebappPath() -> str:
        return self.URLGLOBALS.urlGlobalsInterface.getWebappPath()
    

    @staticmethod
    def getTestHtmlPath() -> str:
        return self.URLGLOBALS.urlGlobalsInterface.getTestHtmlPath()
    

    # throws Exception
    @staticmethod
    def getMainPath() -> str:
        return self.URLGLOBALS.urlGlobalsInterface.getMainPath()


