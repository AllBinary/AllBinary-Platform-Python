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
# package org.allbinary.business.user.commerce.money.payment.types

from __future__ import annotations



class BasicPaymentType:

    def _init_fields(self) -> None:
        self.name: str = None
        self.value: str = None
        self.paymentGatewayInterfaceFactoryInterface: PaymentGatewayInterfaceFactoryInterface = None
        self.paymentGatewayDomNodeFactoryInterface: PaymentGatewayDomNodeFactoryInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 3:
            self._constructor3(*args)
    

    def _constructor1(self, paymentMethod: str) -> None:
        self._init_fields()
        self.init(paymentMethod)
    

    def _constructor3(self, paymentMethod: str, paymentGatewayInterfaceFactoryInterface: PaymentGatewayInterfaceFactoryInterface, paymentGatewayDomNodeFactoryInterface: PaymentGatewayDomNodeFactoryInterface) -> None:
        self._init_fields()
        self.init(paymentMethod)
        self.paymentGatewayInterfaceFactoryInterface = paymentGatewayInterfaceFactoryInterface
        self.paymentGatewayDomNodeFactoryInterface = paymentGatewayDomNodeFactoryInterface
    

    def init(self, paymentMethod: str) -> None:
        from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentTypeUtil import BasicPaymentTypeUtil
        hashMap: dict = StdUtil.getInstance().createHashMap()
        UNDERSCORE: str = "_"
        hashMap.put(CommonSeps.getInstance().SPACE, UNDERSCORE)
        hashMap.put(AbPathData.getInstance().EXTENSION_SEP, UNDERSCORE)
        hashMap.put("-", UNDERSCORE)
        replace: Replace = Replace(hashMap)
        self.name = replace.all(paymentMethod)
        self.value = paymentMethod
        BasicPaymentTypeUtil.getInstance().add(self)
    

    def getName(self) -> str:
        return self.name
    

    def getValue(self) -> str:
        return self.value
    

    # throws Exception
    def getPaymentGatewayInterfaceFactoryInterface(self) -> PaymentGatewayInterfaceFactoryInterface:
        if self.paymentGatewayInterfaceFactoryInterface is None:
            raise Exception("PaymentGatewayInterfaceFactoryInterface is Null")
        return self.paymentGatewayInterfaceFactoryInterface
    

    # throws Exception
    def getPaymentGatewayDomNodeFactoryInterface(self) -> PaymentGatewayDomNodeFactoryInterface:
        if self.paymentGatewayDomNodeFactoryInterface is None:
            raise Exception("PaymentGatewayDomNodeFactoryInterface is Null")
        return self.paymentGatewayDomNodeFactoryInterface
    

    def getKey(self) -> object:
        return self.getName()
    

    def toVector(self) -> BasicArrayList:
        vector: BasicArrayList = BasicArrayListD()
        vector.add(self.name)
        vector.add(self.value)
        return vector
    

    def toHashMap(self) -> dict:
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(str(PaymentGatewayData.NAME), self.name)
        hashMap.put(str(PaymentGatewayData.VALUE), self.value)
        return hashMap
    

    def toString(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.toString()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterfaceFactoryInterface import PaymentGatewayInterfaceFactoryInterface
from org.allbinary.business.user.commerce.money.payment.gateway.modules.gateway.PaymentGatewayDomNodeFactoryInterface import PaymentGatewayDomNodeFactoryInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.regex.replace.Replace import Replace
from org.allbinary.string.CommonSeps import CommonSeps


