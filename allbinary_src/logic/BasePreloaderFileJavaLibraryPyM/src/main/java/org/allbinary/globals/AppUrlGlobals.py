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


#implements
class AppUrlGlobals(UrlGlobalsInterface):
    NULL_APP_URL_GLOBALS: AppUrlGlobals = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.path: str = StringUtil.getInstance().EMPTY_STRING

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def isTestingMode(self) -> bool:
        return False
    

    def getWebappPath(self) -> str:
        return self.path
    

    def setWebappPath(self, path: str) -> None:
        with self._lock:
            return self._setWebappPath_unlocked(path)

    def _setWebappPath_unlocked(self, path: str) -> None:
        self.path = path
        if not (self.path.endswith("\\") or self.path.endswith("/")):
            self.path = self.path + "\\"
    

    def getTestHtmlPath(self) -> str:
        return StringUtil.getInstance().EMPTY_STRING
    

    # throws Exception
    def getMainPath(self) -> str:
        return self.path
from org.allbinary.logic.string.StringUtil import StringUtil


AppUrlGlobals.NULL_APP_URL_GLOBALS = AppUrlGlobals()

