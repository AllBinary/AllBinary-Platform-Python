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
        if "basicPaymentType" not in vars(self): self.basicPaymentType: BasicPaymentType = None
        if "paymentTransactionInterfaceFactoryInterface" not in vars(self): self.paymentTransactionInterfaceFactoryInterface: PaymentTransactionInterfaceFactoryInterface = None
        if "paymentProcessorInterfaceFactoryInterface" not in vars(self): self.paymentProcessorInterfaceFactoryInterface: PaymentProcessorInterfaceFactoryInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 3:
            __class__._constructor3(self, *args)
    

    def _constructor1(self, basicPaymentType: BasicPaymentType) -> None:
        from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
        __class__._init_fields(self)
        self.basicPaymentType = basicPaymentType
        self.paymentTransactionInterfaceFactoryInterface = None
        self.paymentProcessorInterfaceFactoryInterface = None
        PaymentTypeUtil.getInstance().add(self)
    

    def _constructor3(self, basicPaymentType: BasicPaymentType, paymentTransactionInterfaceFactoryInterface: PaymentTransactionInterfaceFactoryInterface, paymentProcessorInterfaceFactoryInterface: PaymentProcessorInterfaceFactoryInterface) -> None:
        from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
        from org.allbinary.business.user.commerce.money.payment.gateway.processor.PaymentProcessorInterfaceFactoryInterface import PaymentProcessorInterfaceFactoryInterface
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterfaceFactoryInterface import PaymentTransactionInterfaceFactoryInterface
        __class__._init_fields(self)
        self.basicPaymentType = basicPaymentType
        self.paymentTransactionInterfaceFactoryInterface = paymentTransactionInterfaceFactoryInterface
        self.paymentProcessorInterfaceFactoryInterface = paymentProcessorInterfaceFactoryInterface
        PaymentTypeUtil.getInstance().add(self)
    

    # throws Exception
    def getPaymentTransactionInterfaceFactoryInterface(self) -> PaymentTransactionInterfaceFactoryInterface:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterfaceFactoryInterface import PaymentTransactionInterfaceFactoryInterface
        if self.paymentTransactionInterfaceFactoryInterface is None:
            raise Exception("PaymentTransactionInterfaceFactoryInterface is Null")
        return self.paymentTransactionInterfaceFactoryInterface
    

    # throws Exception
    def getPaymentProcessorInterfaceFactoryInterface(self) -> PaymentProcessorInterfaceFactoryInterface:
        from org.allbinary.business.user.commerce.money.payment.gateway.processor.PaymentProcessorInterfaceFactoryInterface import PaymentProcessorInterfaceFactoryInterface
        if self.paymentProcessorInterfaceFactoryInterface is None:
            raise Exception("PaymentProcessorInterfaceFactoryInterface is Null")
        return self.paymentProcessorInterfaceFactoryInterface
    

    def toVector(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        vector: BasicArrayList = BasicArrayListD()
        vector.addAllList(self.getBasicPaymentType().toVector())
        if self.paymentTransactionInterfaceFactoryInterface is not None:
            vector.add(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self.paymentTransactionInterfaceFactoryInterface)))
        if self.paymentProcessorInterfaceFactoryInterface is not None:
            vector.add(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self.paymentProcessorInterfaceFactoryInterface)))
        return vector
    

    def toHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.putAll(self.getBasicPaymentType().toHashMap())
        if self.paymentTransactionInterfaceFactoryInterface is not None:
            hashMap.put(str(PaymentGatewayData.PAYMENTTRANSACTIONINTERFACEFACTORYINTERFACE), __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self.paymentTransactionInterfaceFactoryInterface)))
        if self.paymentProcessorInterfaceFactoryInterface is not None:
            hashMap.put(str(PaymentGatewayData.PAYMENTPROCESSORINTERFACEFACTORYINTERFACE), __import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(type(self.paymentProcessorInterfaceFactoryInterface)))
        return hashMap
    

    def getBasicPaymentType(self) -> BasicPaymentType:
        return self.basicPaymentType
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
# from org.allbinary.business.user.commerce.money.payment.gateway.processor.PaymentProcessorInterfaceFactoryInterface import PaymentProcessorInterfaceFactoryInterface
# from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterfaceFactoryInterface import PaymentTransactionInterfaceFactoryInterface
# from org.allbinary.logic.StdUtil import StdUtil


