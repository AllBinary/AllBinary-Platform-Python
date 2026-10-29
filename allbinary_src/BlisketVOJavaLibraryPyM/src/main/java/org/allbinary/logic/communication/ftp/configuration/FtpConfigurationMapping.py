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

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


class FtpConfigurationMapping(TableMappingInterface):

    def _init_fields(self) -> None:
        self.ftpConfigurationInterface: FtpConfigurationInterface = None
    

    def __init__(self, ftpConfigurationInterface: FtpConfigurationInterface) -> None:
        self._init_fields()
        self.ftpConfigurationInterface = ftpConfigurationInterface
    

    def toHashMap(self) -> dict:
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(FtpConfigurationData.SERVER, self.ftpConfigurationInterface.getServer())
        hashMap.put(FtpConfigurationData.USERNAME, self.ftpConfigurationInterface.getUserName())
        hashMap.put(FtpConfigurationData.PASSWORD, self.ftpConfigurationInterface.getPassword())
        hashMap.put(FtpConfigurationData.PATH, self.ftpConfigurationInterface.getPath())
        return hashMap
    

    # throws Exception
    def getKey(self) -> object:
        from org.allbinary.logic.communication.ftp.configuration.FtpConfigurationData import FtpConfigurationData
        return FtpConfigurationData.NAME
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        vector: BasicArrayList = BasicArrayListD()
        vector.add(self.ftpConfigurationInterface.getServer())
        vector.add(self.ftpConfigurationInterface.getUserName())
        vector.add(self.ftpConfigurationInterface.getPassword())
        vector.add(self.ftpConfigurationInterface.getPath())
        return vector
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil


