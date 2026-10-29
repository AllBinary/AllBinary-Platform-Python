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

from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo


class DbInitInfo(DbConnectionInfo):

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.directory: Directory = Directory.getInstance()
        self.httpData: HttpData = HttpData.getInstance()
        self.GET_URL: str = "getUrl"
        self.PACKAGE: str = self.FREEBLISKET_PATH_GLOBALS.getInstance().DBINITPATH
        self.initFileName: str = None
        self.hasRead: bool = False
    

    def __init__(self, initFileName: str, read: bool) -> None:
        super().__init__()
        self._init_fields()
        self.initFileName = initFileName
        if read:
            self.updateIfNeeded()
        else:
            self.setHasRead(True)
    

    def getUrl(self) -> str:
        url: str = super().getUrl()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
            PreLogUtil.put(str(self.httpData.URL_LABEL) + url, self, self.GET_URL)
        return url
    

    # throws Exception
    def write(self) -> None:
        from org.allbinary.business.init.db.FILEABPATH import FILEABPATH
        PATH: AbPath = AbPath(str(self.URLGLOBALS.getWebappPath()) + self.PACKAGE, StringUtil.getInstance().EMPTY_STRING)
        self.directory.create(PATH)
        FILEABPATH: AbPath = AbPath(str(self.URLGLOBALS.getWebappPath()) + self.PACKAGE, self.initFileName)
        try:
            newFile: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
            newFile.createNewFile()
            dataOutputStream: AbDataOutputStream = DataOutputStreamFactory.getInstance().getInstanceForAbFile(newFile)
            try:
                cryptedJdbcDriver: list[int] = WeakCrypt(1).encrypt(self.getJdbcDriver()).getBytes()
                cryptedName: list[int] = WeakCrypt(2).encrypt(self.getName()).getBytes()
                cryptedUserName: list[int] = WeakCrypt(3).encrypt(self.getUserName()).getBytes()
                cryptedPassword: list[int] = WeakCrypt(4).encrypt(self.getPassword()).getBytes()
                cryptedSchema: list[int] = WeakCrypt(5).encrypt(self.getSchema()).getBytes()
                cryptedServer: list[int] = WeakCrypt(6).encrypt(self.getServer()).getBytes()
                cryptedPort: list[int] = WeakCrypt(7).encrypt(self.getPort()).getBytes()
                dataOutputStream.writeUTF(DatabaseEncoder.encode(cryptedJdbcDriver))
                dataOutputStream.writeUTF(DatabaseEncoder.encode(cryptedName))
                dataOutputStream.writeUTF(DatabaseEncoder.encode(cryptedUserName))
                dataOutputStream.writeUTF(DatabaseEncoder.encode(cryptedPassword))
                dataOutputStream.writeUTF(DatabaseEncoder.encode(cryptedSchema))
                dataOutputStream.writeUTF(DatabaseEncoder.encode(cryptedServer))
                dataOutputStream.writeUTF(DatabaseEncoder.encode(cryptedPort))
                self.hasRead = False
            finally:
                StreamUtil.getInstance().close(dataOutputStream)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE("Failed Write: " + str(FILEABPATH), self, "write", e)
    

    # throws Exception
    def load(self) -> None:
        from org.allbinary.business.init.db.FILEABPATH import FILEABPATH
        from org.allbinary.business.init.db.FILEABPATH import FILEABPATH
        FILEABPATH: AbPath = AbPath(str(self.URLGLOBALS.getWebappPath()) + self.PACKAGE, self.initFileName)
        try:
            file: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
            if file.isFile():
                iFile: AbFileInputStream = AbFileInputStream(file)
                iData: AbDataInputStream = AbDataInputStream(iFile)
                try:
                    decryptedJdbcDriver: str = str(DatabaseEncoder.decode(iData.readUTF()))
                    decryptedName: str = str(DatabaseEncoder.decode(iData.readUTF()))
                    decryptedUserName: str = str(DatabaseEncoder.decode(iData.readUTF()))
                    decryptedPassword: str = str(DatabaseEncoder.decode(iData.readUTF()))
                    decryptedSchema: str = str(DatabaseEncoder.decode(iData.readUTF()))
                    decryptedServer: str = str(DatabaseEncoder.decode(iData.readUTF()))
                    decryptedPort: str = str(DatabaseEncoder.decode(iData.readUTF()))
                    self.setJdbcDriver(WeakCrypt(1).decrypt(decryptedJdbcDriver))
                    self.setName(WeakCrypt(2).decrypt(decryptedName))
                    self.setUserName(WeakCrypt(3).decrypt(decryptedUserName))
                    self.setPassword(WeakCrypt(4).decrypt(decryptedPassword))
                    self.setSchema(WeakCrypt(5).decrypt(decryptedSchema))
                    self.setServer(WeakCrypt(6).decrypt(decryptedServer))
                    self.setPort(WeakCrypt(7).decrypt(decryptedPort))
                    stringUtil: StringUtil = StringUtil.getInstance()
                finally:
                    StreamUtil.getInstance().close(iData)
            else:
                self.hasRead = False
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
                    PreLogUtil.put("Not a File - Failed Loading: " + str(FILEABPATH), self, self.commonStrings.LOAD)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE("Failed Loading: " + str(FILEABPATH), self, self.commonStrings.LOAD, e)
    

    def setHasRead(self, value: bool) -> None:
        self.hasRead = value
    

    def updateIfNeeded(self) -> None:
        try:
            if not self.hasRead:
                self.hasRead = True
                self.load()
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, "updateIfNeeded", e)
    

    def getName(self) -> str:
        self.updateIfNeeded()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
            PreLogUtil.put("Name: " + super().getName(), self, "getName")
        return super().getName()
    

    def getUserName(self) -> str:
        self.updateIfNeeded()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
            PreLogUtil.put("Name: " + str(super().getUserName()), self, "getUserName")
        return super().getUserName()
    

    def getPassword(self) -> str:
        self.updateIfNeeded()
        return super().getPassword()
    

    def getSchema(self) -> str:
        self.updateIfNeeded()
        return super().getSchema()
    

    def getServer(self) -> str:
        self.updateIfNeeded()
        return super().getServer()
    

    def getPort(self) -> str:
        self.updateIfNeeded()
        return super().getPort()
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.http.HttpData import HttpData
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
from org.allbinary.logic.io.AbDataInputStream import AbDataInputStream
from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
from org.allbinary.logic.io.StreamUtil import StreamUtil
from org.allbinary.logic.io.file.AbFile import AbFile
from org.allbinary.logic.io.file.directory.Directory import Directory
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.crypt.DatabaseEncoder import DatabaseEncoder
from org.allbinary.logic.system.security.crypt.WeakCrypt import WeakCrypt
from org.allbinary.string.CommonStrings import CommonStrings


