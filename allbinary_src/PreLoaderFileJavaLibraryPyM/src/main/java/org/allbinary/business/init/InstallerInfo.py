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
from java.lang.JavaRuntimeStatic import lazy_static


class InstallerInfo:
    instance: InstallerInfo = None
    INITFILENAME: str = "installerdata.dat"
    PACKAGE: str = None
    userName: str = None
    password: str = None
    hasRead: bool = False
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def write(self) -> None:
        with self._lock:
            return self._write_unlocked()

    def _write_unlocked(self) -> None:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
        from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.system.security.crypt.DatabaseEncoder import DatabaseEncoder
        from org.allbinary.logic.system.security.crypt.WeakCrypt import WeakCrypt
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        FILEABPATH: AbPath = AbPath(URLGLOBALS.getMainPath() + InstallerInfo.PACKAGE, InstallerInfo.INITFILENAME)
        try:
            newFile: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
            newFile.createNewFile()
            dataOutputStream: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(newFile)
            cryptedUserName: list[int] = WeakCrypt(1).encrypt(self.getUserName()).getBytes()
            cryptedPassword: list[int] = WeakCrypt(2).encrypt(self.getPassword()).getBytes()
            dataOutputStream.writeUTF(DatabaseEncoder.encode(cryptedUserName))
            dataOutputStream.writeUTF(DatabaseEncoder.encode(cryptedPassword))
            InstallerInfo.hasRead = False
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                self.logUtil.putF("Failed", self, "write")
            raise e
    

    # throws Exception
    def read(self) -> None:
        with self._lock:
            return self._read_unlocked()

    def _read_unlocked(self) -> None:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.io.AbDataInputStream import AbDataInputStream
        from org.allbinary.logic.io.AbFileLocalInputStream import AbFileLocalInputStream
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.system.security.crypt.DatabaseEncoder import DatabaseEncoder
        from org.allbinary.logic.system.security.crypt.WeakCrypt import WeakCrypt
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        FILEABPATH: AbPath = AbPath(URLGLOBALS.getMainPath() + InstallerInfo.PACKAGE, InstallerInfo.INITFILENAME)
        try:
            file: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
            if file.isFile():
                iFile: AbFileLocalInputStream = AbFileLocalInputStream(file)
                iData: AbDataInputStream = AbDataInputStream(iFile)
                decryptedUserName: str = str(DatabaseEncoder.decode(iData.readUTF()))
                decryptedPassword: str = str(DatabaseEncoder.decode(iData.readUTF()))
                self.setUserName(WeakCrypt(1).decrypt(decryptedUserName))
                self.setPassword(WeakCrypt(2).decrypt(decryptedPassword))
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
                    self.logUtil.putF("Not a File - Failed Loading: " + str(FILEABPATH), self, "read")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                self.logUtil.putF("Failed", self, "read")
    

    @staticmethod
    def setHasRead(value: bool) -> None:
        with InstallerInfo._lock:
            return InstallerInfo._setHasRead_unlocked(value)

    @staticmethod
    def _setHasRead_unlocked(value: bool) -> None:
        InstallerInfo.hasRead = value
    

    def setUserName(self, userName: str) -> None:
        InstallerInfo.userName = userName
    

    def setPassword(self, password: str) -> None:
        InstallerInfo.password = password
    

    # throws Exception
    def updateIfNeeded(self) -> None:
        with self._lock:
            return self._updateIfNeeded_unlocked()

    def _updateIfNeeded_unlocked(self) -> None:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if not InstallerInfo.hasRead:
            InstallerInfo.hasRead = True
            self.read()
            if InstallerInfo.userName is None or InstallerInfo.password is None:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
                    self.logUtil.putF("Failed", self, "updateIfNeeded")
    

    # throws Exception
    def getUserName(self) -> str:
        self.updateIfNeeded()
        return InstallerInfo.userName
    

    # throws Exception
    def getPassword(self) -> str:
        self.updateIfNeeded()
        return InstallerInfo.password
    

    # throws Exception
    def isValid(self, userName: str, password: str) -> bool:
        self.updateIfNeeded()
        if self.userName is not None and ((self.userName > userName) - (self.userName < userName)) == 0 and self.password is not None and ((self.password > password) - (self.password < password)) == 0:
            return True
        return False
# from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.io.AbDataInputStream import AbDataInputStream
# from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
# from org.allbinary.logic.io.AbFileLocalInputStream import AbFileLocalInputStream
# from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.system.security.crypt.DatabaseEncoder import DatabaseEncoder
# from org.allbinary.logic.system.security.crypt.WeakCrypt import WeakCrypt
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _InstallerInfo_instance() -> object:
    return InstallerInfo()

lazy_static(InstallerInfo, "instance", _InstallerInfo_instance)

def _InstallerInfo_PACKAGE() -> object:
    from org.allbinary.globals.PATH_GLOBALS import PATH_GLOBALS
    return PATH_GLOBALS.getInstance().INIT_PATH

lazy_static(InstallerInfo, "PACKAGE", _InstallerInfo_PACKAGE)

def _InstallerInfo_userName() -> object:
    from org.allbinary.logic.string.StringUtil import StringUtil
    return StringUtil.getInstance().EMPTY_STRING

lazy_static(InstallerInfo, "userName", _InstallerInfo_userName)

def _InstallerInfo_password() -> object:
    from org.allbinary.logic.string.StringUtil import StringUtil
    return StringUtil.getInstance().EMPTY_STRING

lazy_static(InstallerInfo, "password", _InstallerInfo_password)

