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
# package org.allbinary.business.init

from __future__ import annotations

import threading


class LicenseInitInfoUtil:
    instance: LicenseInitInfoUtil = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.INITFILENAME: str = "licenseinitdata.dat"
        self.ABOUT: str = "about"
        self.PRIVACY_POLICY: str = "privacy_policy"
        self.OFFICIAL_ALLBINARY_SERVICES_SERVER: str = "https://services.allbinary.com/LicServ/serverssl.php"
    

    @staticmethod
    def getInstance() -> LicenseInitInfoUtil:
        return LicenseInitInfoUtil.instance
    

    def setFilePath(self, filePath: str) -> None:
        with self._lock:
            return self._setFilePath_unlocked(filePath)

    def _setFilePath_unlocked(self, filePath: str) -> None:
        pass
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def write(self, initData: LicenseInitInfo) -> None:
        with self._lock:
            return self._write_unlocked(initData)

    def _write_unlocked(self, initData: LicenseInitInfo) -> None:
        pass
    

    # throws Exception
    def read(self) -> LicenseInitInfo:
        with self._lock:
            return self._read_unlocked()

    def _read_unlocked(self) -> LicenseInitInfo:
        return self.readAgain(0)
    

    # throws Exception
    def readAgain(self, initializeCounter: int) -> LicenseInitInfo:
        with self._lock:
            return self._readAgain_unlocked(initializeCounter)

    def _readAgain_unlocked(self, initializeCounter: int) -> LicenseInitInfo:
        from org.allbinary.business.init.LicenseInitInfo import LicenseInitInfo
        licenseInitInfo: LicenseInitInfo = LicenseInitInfo()
        licenseInitInfo.clearServers()
        licenseInitInfo.addServer(self.OFFICIAL_ALLBINARY_SERVICES_SERVER)
        return licenseInitInfo


LicenseInitInfoUtil.instance = LicenseInitInfoUtil()

