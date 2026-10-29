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



class PaymentType:

    def _init_fields(self) -> None:
        self.basicPaymentType: BasicPaymentType = None
        self.paymentTransactionInterfaceFactoryInterface: PaymentTransactionInterfaceFactoryInterface = None
        self.paymentProcessorInterfaceFactoryInterface: PaymentProcessorInterfaceFactoryInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 3:
            self._constructor3(*args)
    

    def _constructor1(self, basicPaymentType: BasicPaymentType) -> None:
        from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
        self._init_fields()
        self.basicPaymentType = basicPaymentType
        self.paymentTransactionInterfaceFactoryInterface = None
        self.paymentProcessorInterfaceFactoryInterface = None
        PaymentTypeUtil.getInstance().add(self)
    

    def _constructor3(self, basicPaymentType: BasicPaymentType, paymentTransactionInterfaceFactoryInterface: PaymentTransactionInterfaceFactoryInterface, paymentProcessorInterfaceFactoryInterface: PaymentProcessorInterfaceFactoryInterface) -> None:
        from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
        self._init_fields()
        self.basicPaymentType = basicPaymentType
        self.paymentTransactionInterfaceFactoryInterface = paymentTransactionInterfaceFactoryInterface
        self.paymentProcessorInterfaceFactoryInterface = paymentProcessorInterfaceFactoryInterface
        PaymentTypeUtil.getInstance().add(self)
    

    # throws Exception
    def getPaymentTransactionInterfaceFactoryInterface(self) -> PaymentTransactionInterfaceFactoryInterface:
        if self.paymentTransactionInterfaceFactoryInterface is None:
            raise Exception("PaymentTransactionInterfaceFactoryInterface is Null")
        return self.paymentTransactionInterfaceFactoryInterface
    

    # throws Exception
    def getPaymentProcessorInterfaceFactoryInterface(self) -> PaymentProcessorInterfaceFactoryInterface:
        if self.paymentProcessorInterfaceFactoryInterface is None:
            raise Exception("PaymentProcessorInterfaceFactoryInterface is Null")
        return self.paymentProcessorInterfaceFactoryInterface
    

    def toVector(self) -> BasicArrayList:
        vector: BasicArrayList = BasicArrayListD()
        vector.addAllList(self.getBasicPaymentType().toVector())
        if self.paymentTransactionInterfaceFactoryInterface is not None:
            vector.add(type(self.paymentTransactionInterfaceFactoryInterface).__module__ + "." + type(self.paymentTransactionInterfaceFactoryInterface).__qualname__)
        if self.paymentProcessorInterfaceFactoryInterface is not None:
            vector.add(type(self.paymentProcessorInterfaceFactoryInterface).__module__ + "." + type(self.paymentProcessorInterfaceFactoryInterface).__qualname__)
        return vector
    

    def toHashMap(self) -> dict:
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.putAll(self.getBasicPaymentType().toHashMap())
        if self.paymentTransactionInterfaceFactoryInterface is not None:
            hashMap.put(str(PaymentGatewayData.PAYMENTTRANSACTIONINTERFACEFACTORYINTERFACE), type(self.paymentTransactionInterfaceFactoryInterface).__module__ + "." + type(self.paymentTransactionInterfaceFactoryInterface).__qualname__)
        if self.paymentProcessorInterfaceFactoryInterface is not None:
            hashMap.put(str(PaymentGatewayData.PAYMENTPROCESSORINTERFACEFACTORYINTERFACE), type(self.paymentProcessorInterfaceFactoryInterface).__module__ + "." + type(self.paymentProcessorInterfaceFactoryInterface).__qualname__)
        return hashMap
    

    def getBasicPaymentType(self) -> BasicPaymentType:
        return self.basicPaymentType
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
from org.allbinary.business.user.commerce.money.payment.gateway.processor.PaymentProcessorInterfaceFactoryInterface import PaymentProcessorInterfaceFactoryInterface
from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterfaceFactoryInterface import PaymentTransactionInterfaceFactoryInterface
from org.allbinary.logic.StdUtil import StdUtil


