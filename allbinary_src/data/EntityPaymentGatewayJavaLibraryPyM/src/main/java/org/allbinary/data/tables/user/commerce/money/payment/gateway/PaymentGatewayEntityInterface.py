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
# package org.allbinary.data.tables.user.commerce.money.payment.gateway

from __future__ import annotations

from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
class PaymentGatewayEntityInterface(BasicDataTableInterface):
    

    def getPaymentGatewayInterface(self, storeName: str, paymentType: BasicPaymentType) -> PaymentGatewayInterface:
        raise NotImplementedError()
    

    def findPaymentTypeVectorByStore(self, storeName: str) -> BasicArrayList:
        raise NotImplementedError()
    

    def remove(self, storeName: str, paymentType: BasicPaymentType) -> None:
        raise NotImplementedError()
    

    def add(self, paymentGatewayInterface: PaymentGatewayInterface) -> None:
        raise NotImplementedError()
    

    def update(self, paymentGatewayInterface: PaymentGatewayInterface) -> None:
        raise NotImplementedError()
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterface import PaymentGatewayInterface
from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentType import BasicPaymentType


