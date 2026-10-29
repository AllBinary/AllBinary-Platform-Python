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



# Java interface
class EmailServerConfigurationInterface:
    

    def setSmtpServer(self, value: str) -> None:
        raise NotImplementedError()
    

    def getSmtpServer(self) -> str:
        raise NotImplementedError()
    

    def getAccountName(self) -> str:
        raise NotImplementedError()
    

    def setAccountName(self, accountName: str) -> None:
        raise NotImplementedError()
    

    def getPassword(self) -> str:
        raise NotImplementedError()
    

    def setPassword(self, password: str) -> None:
        raise NotImplementedError()
    

    def log(self) -> None:
        raise NotImplementedError()
    

    def toString(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.toString()


