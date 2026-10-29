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
# package org.allbinary.business.user.commerce.money.payment.gateway.transaction

from __future__ import annotations



# Java interface
class TransactionResultInterface:
    

    def toString(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.toString()
    

    def getValues(self) -> BasicArrayList:
        raise NotImplementedError()
    

    def getResult(self) -> str:
        raise NotImplementedError()
    

    def getPnRef(self) -> str:
        raise NotImplementedError()
    

    def getRespMsg(self) -> str:
        raise NotImplementedError()
    

    def getAvsAddr(self) -> str:
        raise NotImplementedError()
    

    def getAvsZip(self) -> str:
        raise NotImplementedError()
    

    def getOrigResult(self) -> str:
        raise NotImplementedError()
    

    def getStatus(self) -> str:
        raise NotImplementedError()
    

    def getFraudCode(self) -> str:
        raise NotImplementedError()
    

    def getFraudMsg(self) -> str:
        raise NotImplementedError()
    

    def getErrCode(self) -> str:
        raise NotImplementedError()
    

    def getScore(self) -> str:
        raise NotImplementedError()
    

    def getReason1(self) -> str:
        raise NotImplementedError()
    

    def getReason2(self) -> str:
        raise NotImplementedError()
    

    def getReason3(self) -> str:
        raise NotImplementedError()
    

    def getException1(self) -> str:
        raise NotImplementedError()
    

    def getException2(self) -> str:
        raise NotImplementedError()
    

    def getException3(self) -> str:
        raise NotImplementedError()
    

    def getException4(self) -> str:
        raise NotImplementedError()
    

    def getException5(self) -> str:
        raise NotImplementedError()
    

    def getException6(self) -> str:
        raise NotImplementedError()
    

    def getException7(self) -> str:
        raise NotImplementedError()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


