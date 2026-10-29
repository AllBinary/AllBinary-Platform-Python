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
# package org.allbinary.business.user.commerce.money.payment.gateway

from __future__ import annotations



class PaymentGatewayPrimaryKey(object):

    def _init_fields(self) -> None:
        self.storeName: str = None
        self.name: str = None
    

    def __init__(self, storeName: str, gatewayName: str) -> None:
        self._init_fields()
        self.setStoreName(storeName)
        self.setName(gatewayName)
    

    def getStoreName(self) -> str:
        return self.storeName
    

    def setStoreName(self, storeName: str) -> None:
        self.storeName = storeName
    

    def getName(self) -> str:
        return self.name
    

    def setName(self, name: str) -> None:
        self.name = name
    

    def toString(self) -> str:
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(PaymentGatewayPrimaryKey.getName())
        stringBuffer.append(StoreFront.getName())
        stringBuffer.append(" =")
        stringBuffer.append(self.getStoreName())
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(PaymentGateway.getName())
        stringBuffer.append("=")
        stringBuffer.append(self.getName())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.business.context.modules.storefront.StoreFront import StoreFront
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonSeps import CommonSeps


