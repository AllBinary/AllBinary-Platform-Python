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



class BasicPaymentTypeUtil:
    instance: BasicPaymentTypeUtil = None

    def _init_fields(self) -> None:
        self.paymentTypeVector: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def _static_init() -> None:
        pass
    

    @staticmethod
    def getInstance() -> BasicPaymentTypeUtil:
        return BasicPaymentTypeUtil.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    def add(self, paymentType: BasicPaymentType) -> None:
        self.paymentTypeVector.add(paymentType)
    

    # throws Exception
    def get(self, paymentTypeString: str) -> BasicPaymentType:
        size: int = self.paymentTypeVector.size()
        for i in range(0, size):
            paymentType: BasicPaymentType = self.paymentTypeVector.get(i)
            if paymentType.getName().compareTo(paymentTypeString) == 0:
                return paymentType
        raise Exception("Unknown PaymentType: " + paymentTypeString)
    

    def isContain(self, paymentType: BasicPaymentType) -> bool:
        return self.paymentTypeVector.contains(paymentType)
    

    def difference(self, a_PaymentTypeVector: BasicArrayList) -> BasicArrayList:
        diff: BasicArrayList = BasicArrayListD()
        size: int = self.paymentTypeVector.size()
        for i in range(0, size):
            paymentType: BasicPaymentType = self.paymentTypeVector.get(i)
            if not a_PaymentTypeVector.contains(paymentType):
                diff.add(paymentType)
        return diff
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.logic.StdUtil import StdUtil


BasicPaymentTypeUtil.instance = BasicPaymentTypeUtil()

BasicPaymentTypeUtil._static_init()

