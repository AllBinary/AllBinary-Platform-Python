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
# package org.allbinary.data.tables.user.commerce.money.payment.transaction

from __future__ import annotations

from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
class TransactionEntityInterface(BasicDataTableInterface):
    

    def remove(self, userName: str, orderNumber: str) -> None:
        raise NotImplementedError()
    

    def add(self, userName: str, orderNumber: str, paymentTransactionInterface: PaymentTransactionInterface) -> None:
        raise NotImplementedError()
from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterface import PaymentTransactionInterface


