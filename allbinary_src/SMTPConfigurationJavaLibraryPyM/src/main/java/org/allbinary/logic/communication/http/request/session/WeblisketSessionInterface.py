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
# package org.allbinary.logic.communication.http.request.session

from __future__ import annotations



# Java interface
class WeblisketSessionInterface:
    

    def clear(self) -> None:
        raise NotImplementedError()
    

    def getAttempts(self) -> int:
        raise NotImplementedError()
    

    def getAuthentication(self) -> str:
        raise NotImplementedError()
    

    def getCreationTime(self) -> int:
        raise NotImplementedError()
    

    def getId(self) -> str:
        raise NotImplementedError()
    

    def getLastAccessedTime(self) -> int:
        raise NotImplementedError()
    

    # throws Exception
    def getOrder(self) -> OrderInterface:
        raise NotImplementedError()
    

    def getPassword(self) -> str:
        raise NotImplementedError()
    

    def getPaymentMethod(self) -> str:
        raise NotImplementedError()
    

    # throws Exception
    def getRole(self) -> UserRole:
        raise NotImplementedError()
    

    def getStoreName(self) -> str:
        raise NotImplementedError()
    

    def getTimeout(self) -> str:
        raise NotImplementedError()
    

    def getUserName(self) -> str:
        raise NotImplementedError()
    

    def getWebAppPath(self) -> str:
        raise NotImplementedError()
    

    def removeBasket(self) -> None:
        raise NotImplementedError()
    

    def setAttempts(self, value: int) -> None:
        raise NotImplementedError()
    

    def setAuthenticated(self) -> None:
        raise NotImplementedError()
    

    # Java overloaded method: Python keeps the last definition
    def setAuthenticated(self, value: bool) -> None:
        raise NotImplementedError()
    

    def setPassword(self, password: str) -> None:
        raise NotImplementedError()
    

    def setPaymentMethod(self, value: str) -> None:
        raise NotImplementedError()
    

    def setRole(self, aRole: UserRole) -> None:
        raise NotImplementedError()
    

    def setStoreName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setTimeout(self, value: str) -> None:
        raise NotImplementedError()
    

    def setUserName(self, userName: str) -> None:
        raise NotImplementedError()
from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
from org.allbinary.business.user.role.UserRole import UserRole


