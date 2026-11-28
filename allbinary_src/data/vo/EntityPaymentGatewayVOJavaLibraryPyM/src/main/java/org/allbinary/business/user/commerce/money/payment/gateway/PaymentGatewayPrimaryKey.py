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

# from java.io.Serializable import Serializable


class PaymentGatewayPrimaryKey(object):

    def _init_fields(self) -> None:
        if "storeName" not in vars(self): self.storeName: str = None
        if "name" not in vars(self): self.name: str = None
    

    def __init__(self, storeName: str, gatewayName: str) -> None:
        __class__._init_fields(self)
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
        from org.allbinary.business.context.modules.storefront.StoreFront import StoreFront
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(PaymentGatewayPrimaryKey))
        stringBuffer.append(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(StoreFront))
        stringBuffer.append(" =")
        stringBuffer.append(self.getStoreName())
        stringBuffer.append(CommonSeps.getInstance().SPACE)
        stringBuffer.append(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(PaymentGateway))
        stringBuffer.append("=")
        stringBuffer.append(self.getName())
        return str(stringBuffer)

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.business.context.modules.storefront.StoreFront import StoreFront
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonSeps import CommonSeps


