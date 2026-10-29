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



class TransactionTypeFactory:
    instance: TransactionTypeFactory = None

    def _init_fields(self) -> None:
        self.SALE: TransactionType = TransactionType("Sale")
        self.CREDIT: TransactionType = TransactionType("Credit")
        self.AUTHORIZATION: TransactionType = TransactionType("Authorization")
        self.DELAYEDCAPTURE: TransactionType = TransactionType("Delayed Capture")
        self.VOID: TransactionType = TransactionType("Void")
        self.INQUIRY: TransactionType = TransactionType("Inquiry")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TransactionTypeFactory:
        return TransactionTypeFactory.instance
from org.allbinary.business.user.commerce.money.payment.types.TransactionType import TransactionType


TransactionTypeFactory.instance = TransactionTypeFactory()

