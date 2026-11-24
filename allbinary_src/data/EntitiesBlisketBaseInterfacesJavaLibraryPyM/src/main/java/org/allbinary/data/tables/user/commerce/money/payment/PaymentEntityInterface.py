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
# package org.allbinary.data.tables.user.commerce.money.payment

from __future__ import annotations

from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
class PaymentEntityInterface(BasicDataTableInterface):
    

    def getLastId(self, userName: str) -> str:
        raise NotImplementedError()
    

    def setDefault(self, userName: str, index: int) -> None:
        raise NotImplementedError()
    

    def getDefault(self, userName: str) -> PaymentInterface:
        from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface
        raise NotImplementedError()
    

    def get(self, userName: str) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()
    

    def add(self, userName: str, paymentInterface: PaymentInterface) -> None:
        from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface
        raise NotImplementedError()
    

    def remove(self, userName: str, index: int) -> None:
        raise NotImplementedError()
    

    def insert(self, values: BasicArrayList) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        raise NotImplementedError()
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface


