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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.business.init.db.DbConnectionInfo import DbConnectionInfo


@java_inherited_overloads
class DbInitInfo(DbConnectionInfo):
    def _java_defaults(self):
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("directory", None)
        vars(self).setdefault("httpData", None)
        vars(self).setdefault("GET_URL", None)
        vars(self).setdefault("PACKAGE", None)
        vars(self).setdefault("initFileName", None)
        vars(self).setdefault("hasRead", False)

    def _init_fields(self) -> None:
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.logic.communication.http.HttpData import HttpData
        from org.allbinary.logic.io.file.directory.Directory import Directory
        from org.allbinary.string.CommonStrings import CommonStrings
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.directory: Directory = Directory.getInstance()
        self.httpData: HttpData = HttpData.getInstance()
        self.GET_URL: str = "getUrl"
        self.PACKAGE: str = FREEBLISKET_PATH_GLOBALS.getInstance().DBINITPATH
        if "initFileName" not in vars(self): self.initFileName: str = None
        self.hasRead: bool = False
    

    def __init__(self, initFileName: str, read: bool) -> None:
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
        self.initFileName = initFileName
        if read:
            self.updateIfNeeded()
        else:
            self.setHasRead(True)
    

    def getUrl(self) -> str:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        url: str = java_super_call(super(), "getUrl")
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
            PreLogUtil.put(str(self.httpData.URL_LABEL) + url, self, self.GET_URL)
        return url
    

    # throws Exception
    def write(self) -> None:
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
        from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
        from org.allbinary.logic.io.StreamUtil import StreamUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.system.security.crypt.DatabaseEncoder import DatabaseEncoder
        from org.allbinary.logic.system.security.crypt.WeakCrypt import WeakCrypt
        PATH: AbPath = AbPath(str(URLGLOBALS.getWebappPath()) + self.PACKAGE, StringUtil.getInstance().EMPTY_STRING)
        self.directory.create(PATH)
        FILEABPATH: AbPath = AbPath(str(URLGLOBALS.getWebappPath()) + self.PACKAGE, self.initFileName)
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
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        from org.allbinary.logic.io.AbDataInputStream import AbDataInputStream
        from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
        from org.allbinary.logic.io.StreamUtil import StreamUtil
        from org.allbinary.logic.io.file.AbFile import AbFile
        from org.allbinary.logic.io.path.AbPath import AbPath
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.system.security.crypt.DatabaseEncoder import DatabaseEncoder
        from org.allbinary.logic.system.security.crypt.WeakCrypt import WeakCrypt
        FILEABPATH: AbPath = AbPath(str(URLGLOBALS.getWebappPath()) + self.PACKAGE, self.initFileName)
        try:
            file: AbFile = AbFile.createAbFileFromAbPath(FILEABPATH)
            if java_predicate(file, "isFile"):
                iFile: AbFileInputStream = AbFileInputStream.createFromAbFile(file)
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
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if not (self.hasRead):
                self.hasRead = True
                self.load()
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADERERROR):
                PreLogUtil.putOE(self.commonStrings.EXCEPTION, self, "updateIfNeeded", e)
    

    def getName(self) -> str:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        self.updateIfNeeded()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
            PreLogUtil.put("Name: " + java_super_call(super(), "getName"), self, "getName")
        return java_super_call(super(), "getName")
    

    def getUserName(self) -> str:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        self.updateIfNeeded()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PRELOADER):
            PreLogUtil.put("Name: " + str(java_super_call(super(), "getUserName")), self, "getUserName")
        return java_super_call(super(), "getUserName")
    

    def getPassword(self) -> str:
        self.updateIfNeeded()
        return java_super_call(super(), "getPassword")
    

    def getSchema(self) -> str:
        self.updateIfNeeded()
        return java_super_call(super(), "getSchema")
    

    def getServer(self) -> str:
        self.updateIfNeeded()
        return java_super_call(super(), "getServer")
    

    def getPort(self) -> str:
        self.updateIfNeeded()
        return java_super_call(super(), "getPort")
# from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.http.HttpData import HttpData
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
# from org.allbinary.logic.io.AbDataInputStream import AbDataInputStream
# from org.allbinary.logic.io.AbDataOutputStream import AbDataOutputStream
# from org.allbinary.logic.io.AbFileInputStream import AbFileInputStream
# from org.allbinary.logic.io.DataOutputStreamFactory import DataOutputStreamFactory
# from org.allbinary.logic.io.StreamUtil import StreamUtil
# from org.allbinary.logic.io.file.AbFile import AbFile
# from org.allbinary.logic.io.file.directory.Directory import Directory
# from org.allbinary.logic.io.path.AbPath import AbPath
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.system.security.crypt.DatabaseEncoder import DatabaseEncoder
# from org.allbinary.logic.system.security.crypt.WeakCrypt import WeakCrypt
# from org.allbinary.string.CommonStrings import CommonStrings


