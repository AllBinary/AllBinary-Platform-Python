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
# package org.allbinary.logic.system.security.licensing

from __future__ import annotations

import threading


class LicenseUtil:
    instance: LicenseUtil = None
    _lock = threading.RLock()
    

    @staticmethod
    def getInstance() -> LicenseUtil:
        return LicenseUtil.instance
    

    def init(self) -> None:
        pass
    

    def isRunning(self) -> bool:
        with self._lock:
            return self._isRunning_unlocked()

    def _isRunning_unlocked(self) -> bool:
        return False
    

    def setRunning(self, running: bool) -> None:
        with self._lock:
            return self._setRunning_unlocked(running)

    def _setRunning_unlocked(self, running: bool) -> None:
        pass
    

    def shouldWait(self, commandListener: CommandListener) -> bool:
        return self.isRunning()
# from javax.microedition.lcdui.CommandListener import CommandListener


LicenseUtil.instance = LicenseUtil()

