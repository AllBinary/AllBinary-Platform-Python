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
# package org.allbinary.business.user.commerce.money.payment

from __future__ import annotations



# Java interface
class PaymentInterface:
    

    def setName(self, value: str) -> None:
        raise NotImplementedError()
    

    def setType(self, value: str) -> None:
        raise NotImplementedError()
    

    def setExpiration(self, value: str) -> None:
        raise NotImplementedError()
    

    def setNumber(self, value: str) -> None:
        raise NotImplementedError()
    

    def getId(self) -> str:
        raise NotImplementedError()
    

    def getName(self) -> str:
        raise NotImplementedError()
    

    def getType(self) -> str:
        raise NotImplementedError()
    

    def getExpiration(self) -> str:
        raise NotImplementedError()
    

    def getEncryption(self) -> str:
        raise NotImplementedError()
    

    def getNumber(self) -> str:
        raise NotImplementedError()
    

    def getLastFour(self) -> str:
        raise NotImplementedError()
    

    def isDefault(self) -> bool:
        raise NotImplementedError()


