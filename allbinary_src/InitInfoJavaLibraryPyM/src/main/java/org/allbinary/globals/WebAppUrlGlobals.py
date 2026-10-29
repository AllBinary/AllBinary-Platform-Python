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

import threading
from org.allbinary.globals.UrlGlobalsInterface import UrlGlobalsInterface


class WebAppUrlGlobals(UrlGlobalsInterface):
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.path: str = None
        self.isWebappPathSet: bool = False

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def isTestingMode(self) -> bool:
        return InitInfo.getInstance().isTesting()
    

    def getWebappPath(self) -> str:
        return self.path
    

    def setWebappPath(self, path: str) -> None:
        with self._lock:
            return self._setWebappPath_unlocked(path)

    def _setWebappPath_unlocked(self, path: str) -> None:
        path = path
        self.isWebappPathSet = True
    

    def getTestHtmlPath(self) -> str:
        return InitInfo.getInstance().getTestHtmlPath()
    

    # throws Exception
    def getMainPath(self) -> str:
        mainPath: str = InitInfo.getInstance().getMainPath()
        if not StringValidationUtil.getInstance().isEmpty(mainPath):
            return mainPath
        elif self.isWebappPathSet:
            return self.getWebappPath()
        else:
            raise Exception("Webapp Path is not set")
from org.allbinary.business.init.InitInfo import InitInfo
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil


