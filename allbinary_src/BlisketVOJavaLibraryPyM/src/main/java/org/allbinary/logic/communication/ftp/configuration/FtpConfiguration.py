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
# package org.allbinary.logic.communication.ftp.configuration

from __future__ import annotations

from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationInterface import FtpConfigurationInterface


class FtpConfiguration(FtpConfigurationInterface):

    def _init_fields(self) -> None:
        self.ftpServer: str = None
        self.ftpPath: str = None
        self.ftpUserName: str = None
        self.ftpPassword: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
    

    def _constructor1(self, hashMap: dict) -> None:
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        self._init_fields()
        self.ftpServer = hashMap.get(FtpConfigurationData.SERVER)
        self.ftpPath = hashMap.get(FtpConfigurationData.PATH)
        self.ftpUserName = hashMap.get(FtpConfigurationData.USERNAME)
        self.ftpPassword = hashMap.get(FtpConfigurationData.PASSWORD)
    

    def getServer(self) -> str:
        return self.ftpServer
    

    def getPath(self) -> str:
        return self.ftpPath
    

    def getUserName(self) -> str:
        return self.ftpUserName
    

    def getPassword(self) -> str:
        return self.ftpPassword
    

    def setServer(self, value: str) -> None:
        self.ftpServer = value
    

    def setPath(self, value: str) -> None:
        self.ftpPath = value
    

    def setUserName(self, value: str) -> None:
        self.ftpUserName = value
    

    def setPassword(self, value: str) -> None:
        self.ftpPassword = value
# from java.util.HashMap import HashMap


