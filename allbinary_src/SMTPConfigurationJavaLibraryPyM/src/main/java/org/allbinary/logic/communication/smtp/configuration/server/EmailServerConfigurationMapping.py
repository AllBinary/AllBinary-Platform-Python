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
# package org.allbinary.logic.communication.smtp.configuration.server

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface


class EmailServerConfigurationMapping(TableMappingInterface):

    def _init_fields(self) -> None:
        self.emailServerConfigurationInterface: EmailServerConfigurationInterface = None
    

    def __init__(self, emailServerConfigurationInterface: EmailServerConfigurationInterface) -> None:
        self._init_fields()
        self.emailServerConfigurationInterface = emailServerConfigurationInterface
    

    def toHashMap(self) -> dict:
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(EmailServerConfigurationData.SERVER, self.emailServerConfigurationInterface.getSmtpServer())
        hashMap.put(EmailServerConfigurationData.ACCOUNT, self.emailServerConfigurationInterface.getAccountName())
        hashMap.put(EmailServerConfigurationData.PASSWORD, self.emailServerConfigurationInterface.getPassword())
        return hashMap
    

    # throws Exception
    def getKey(self) -> object:
        from org.allbinary.logic.communication.smtp.configuration.server.EmailServerConfigurationData import EmailServerConfigurationData
        return EmailServerConfigurationData.NAME
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        vector: BasicArrayList = BasicArrayListD()
        vector.add(self.emailServerConfigurationInterface.getSmtpServer())
        return vector
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil


