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
# package org.allbinary.business.user

from __future__ import annotations

from org.allbinary.data.tables.TableMappingInterface import TableMappingInterface
from org.allbinary.logic.control.validate.ValidationInterface import ValidationInterface


# Java interface
class UserInterface(TableMappingInterface, ValidationInterface):
    

    def setUserName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPrefixName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setFirstName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setLastName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setMiddleName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSuffixName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setCompany(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPositionAtCompany(self, value: str) -> None:
        raise NotImplementedError()
    

    def setMainEmail(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSecondaryEmail(self, value: str) -> None:
        raise NotImplementedError()
    

    def setHomePhone(self, value: str) -> None:
        raise NotImplementedError()
    

    def setCellPhone(self, value: str) -> None:
        raise NotImplementedError()
    

    def setWorkPhone(self, value: str) -> None:
        raise NotImplementedError()
    

    def setOtherContact(self, value: str) -> None:
        raise NotImplementedError()
    

    def setElectronicContact(self, value: str) -> None:
        raise NotImplementedError()
    

    def setFax(self, value: str) -> None:
        raise NotImplementedError()
    

    def setRole(self, aRole: UserRole) -> None:
        raise NotImplementedError()
    

    def setEncryption(self, value: str) -> None:
        raise NotImplementedError()
    

    def setSecret(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPassword(self, value: str) -> None:
        raise NotImplementedError()
    

    def setPermissions(self, value: str) -> None:
        raise NotImplementedError()
    

    def enable(self) -> None:
        raise NotImplementedError()
    

    def setEnable(self, enable: str) -> None:
        raise NotImplementedError()
    

    def getUserName(self) -> str:
        raise NotImplementedError()
    

    def getPrefixName(self) -> str:
        raise NotImplementedError()
    

    def getFirstName(self) -> str:
        raise NotImplementedError()
    

    def getLastName(self) -> str:
        raise NotImplementedError()
    

    def getMiddleName(self) -> str:
        raise NotImplementedError()
    

    def getSuffixName(self) -> str:
        raise NotImplementedError()
    

    def getCompany(self) -> str:
        raise NotImplementedError()
    

    def getPositionAtCompany(self) -> str:
        raise NotImplementedError()
    

    def getMainEmail(self) -> str:
        raise NotImplementedError()
    

    def getSecondaryEmail(self) -> str:
        raise NotImplementedError()
    

    def getHomePhone(self) -> str:
        raise NotImplementedError()
    

    def getCellPhone(self) -> str:
        raise NotImplementedError()
    

    def getWorkPhone(self) -> str:
        raise NotImplementedError()
    

    def getOtherContact(self) -> str:
        raise NotImplementedError()
    

    def getElectronicContact(self) -> str:
        raise NotImplementedError()
    

    def getFax(self) -> str:
        raise NotImplementedError()
    

    def getRole(self) -> UserRole:
        raise NotImplementedError()
    

    def getEncryption(self) -> str:
        raise NotImplementedError()
    

    def getSecret(self) -> str:
        raise NotImplementedError()
    

    def getPassword(self) -> str:
        raise NotImplementedError()
    

    def getPermissions(self) -> str:
        raise NotImplementedError()
    

    def getUserConfigurationInterface(self) -> UserConfigurationInterface:
        raise NotImplementedError()
    

    def setUserConfigurationInterface(self, userConfigurationInterface: UserConfigurationInterface) -> None:
        raise NotImplementedError()
    

    def toPasswordHashMap(self) -> dict:
        raise NotImplementedError()
    

    def validateSession(self, weblisketSession: WeblisketSessionInterface) -> None:
        raise NotImplementedError()
    

    def updateSession(self, weblisketSession: WeblisketSessionInterface) -> None:
        raise NotImplementedError()
    

    def isSessionValid(self) -> bool:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.business.user.modules.configuration.UserConfigurationInterface import UserConfigurationInterface
from org.allbinary.business.user.role.UserRole import UserRole
from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface


