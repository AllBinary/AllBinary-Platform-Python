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
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.INITFILENAME: str = "licenseinitdata.dat"
        self.ABOUT: str = "about"
        self.PRIVACY_POLICY: str = "privacy_policy"
        self.filePath: str = self.stringUtil.EMPTY_STRING

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> LicenseInitInfoUtil:
        return LicenseInitInfoUtil.instance
    

    def setFilePath(self, filePath: str) -> None:
        with self._lock:
            return self._setFilePath_unlocked(filePath)

    def _setFilePath_unlocked(self, filePath: str) -> None:
        self.filePath = filePath
    

    # throws Exception
    def write(self, initData: LicenseInitInfo) -> None:
        with self._lock:
            return self._write_unlocked(initData)

    def _write_unlocked(self, initData: LicenseInitInfo) -> None:
        if self.filePath == self.stringUtil.EMPTY_STRING:
            self.filePath = self.URLGLOBALS.getMainPath() + self.PATH_GLOBALS.getInstance().INIT_PATH
        try:
            tsUtil: TsUtil = TsUtil.getInstance()
            dataOutputStream: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstance(self.filePath, self.INITFILENAME)
            licenseIdCrypted: list[int] = tsUtil.getByteArray(WeakCrypt(1).encrypt(initData.getLicenseId()))
            dataOutputStream.writeUTF(DatabaseEncoder.encode(licenseIdCrypted))
            numberOfLicenseServers: int = initData.getNumberOfServers()
            dataOutputStream.writeInt(numberOfLicenseServers)
            licenseServerCrypted: list[int] = None
            for index in range(0, numberOfLicenseServers):
                licenseServerCrypted = tsUtil.getByteArray(WeakCrypt(3).encrypt(initData.getServer(index)))
                dataOutputStream.writeUTF(DatabaseEncoder.encode(licenseServerCrypted))
        except Exception as e:
            self.logUtil.put("Command Failed: " + self.INITFILENAME, self, "write", e)
            FileStreamFactory.getInstance().delete(self.filePath, self.INITFILENAME)
            raise e
    

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
        METHOD_NAME: str = "readAgain"
        if self.filePath == self.stringUtil.EMPTY_STRING:
            self.filePath = self.URLGLOBALS.getMainPath() + self.PATH_GLOBALS.getInstance().INIT_PATH
        try:
            self.logUtil.putF("LicenseInitInfo File: " + self.INITFILENAME, self, METHOD_NAME)
            fileStreamFactory: FileStreamFactory = FileStreamFactory.getInstance()
            iFile: AbFileInputStream = fileStreamFactory.getFileInputStreamInstance(self.filePath, self.INITFILENAME)
            if iFile is not None:
                iData: AbDataInputStream = AbDataInputStream(iFile)
                initInfo: LicenseInitInfo = LicenseInitInfo()
                decodedByteArray: list[int] = DatabaseEncoder.decode(iData.readUTF())
                licenseIdDecoded: str = bytes(decodedByteArray).decode()
                initInfo.setLicenseId(WeakCrypt(1).decrypt(licenseIdDecoded))
                numberOfLicenseServers: int = iData.readInt()
                NEXT_FILE: str = str(StringMaker().append(CommonLabels.getInstance().NEXT).append(" License Server From File: "))
                licenseServerDecoded: str = None
                for index in range(0, numberOfLicenseServers):
                    decodedByteArray = DatabaseEncoder.decode(iData.readUTF())
                    licenseServerDecoded = bytes(decodedByteArray).decode()
                    initInfo.setServer(WeakCrypt(3).decrypt(licenseServerDecoded), index)
                    self.logUtil.putF(NEXT_FILE + str(initInfo.getServer(index)), self, METHOD_NAME)
                return initInfo
            else:
                raise Exception("Could Not Load License InitInfo: " + self.INITFILENAME)
        except Exception as e:
            try:
                self.logUtil.put("Command Failed: " + self.INITFILENAME, self, METHOD_NAME, e)
            except Exception as e2:
                self.logUtil.put("LicenseInitInfo Read Retry: " + self.INITFILENAME, self, "readAgain()", e2)
            raise Exception("LicenseInitInfo Read Error: " + self.INITFILENAME)
    

    def getFilePath(self) -> str:
        return self.filePath
from org.allbinary.TsUtil import TsUtil
from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.io.AbDataInputStream import AbDataInputStream
from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
from org.allbinary.logic.io.FileStreamFactory import FileStreamFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.crypt.DatabaseEncoder import DatabaseEncoder
from org.allbinary.logic.system.security.crypt.WeakCrypt import WeakCrypt
from org.allbinary.string.CommonLabels import CommonLabels


LicenseInitInfoUtil.instance = LicenseInitInfoUtil()

