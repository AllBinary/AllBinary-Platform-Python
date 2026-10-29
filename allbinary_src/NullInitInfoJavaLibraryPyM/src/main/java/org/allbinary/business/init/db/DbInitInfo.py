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
# package org.allbinary.business.init.db

from __future__ import annotations

import threading
from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo


#import org.allbinary.logic.communication.log.config.type.LogConfigTypes;
class DbInitInfo(DbConnectionInfo):
    _lock = threading.RLock()
    

    def __init__(self, initFileName: str, read: bool) -> None:
        super().__init__()
    

    def getUrl(self) -> str:
        url: str = super().getUrl()
        PreLogUtil.put("Url: " + url, self, "getUrl")
        return url
    

    # throws Exception
    def write(self) -> None:
        with self._lock:
            return self._write_unlocked()

    def _write_unlocked(self) -> None:
        pass
    

    # throws Exception
    def load(self) -> None:
        with self._lock:
            return self._load_unlocked()

    def _load_unlocked(self) -> None:
        pass
    

    def setHasRead(self, value: bool) -> None:
        with self._lock:
            return self._setHasRead_unlocked(value)

    def _setHasRead_unlocked(self, value: bool) -> None:
        pass
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil


