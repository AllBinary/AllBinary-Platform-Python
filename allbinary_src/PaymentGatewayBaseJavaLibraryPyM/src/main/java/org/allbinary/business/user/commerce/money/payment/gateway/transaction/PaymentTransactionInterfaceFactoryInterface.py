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
class PaymentTransactionInterfaceFactoryInterface:
    

    # throws Exception
    def getInstance(self, orderHistory: OrderHistory) -> PaymentTransactionInterface:
        raise NotImplementedError()
    

    # throws Exception
    def getSaleTransaction(self, tenderType: TenderType) -> PaymentTransactionInterface:
        raise NotImplementedError()
    

    # throws Exception
    def getCreditTransaction(self, tenderType: TenderType) -> PaymentTransactionInterface:
        raise NotImplementedError()
    

    # throws Exception
    def getAuthorizationTransaction(self, tenderType: TenderType) -> PaymentTransactionInterface:
        raise NotImplementedError()
    

    # throws Exception
    def getCaptureDelayedTransaction(self, tenderType: TenderType) -> PaymentTransactionInterface:
        raise NotImplementedError()
    

    # throws Exception
    def getVoidTransaction(self, tenderType: TenderType) -> PaymentTransactionInterface:
        raise NotImplementedError()
    

    # throws Exception
    def getInquiryTransaction(self, tenderType: TenderType) -> PaymentTransactionInterface:
        raise NotImplementedError()
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
from org.allbinary.business.user.commerce.money.payment.types.TenderType import TenderType


