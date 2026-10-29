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



class CreditCardTypeFactory:
    instance: CreditCardTypeFactory = None

    def _init_fields(self) -> None:
        self.VISA: CreditCardType = CreditCardType("Visa")
        self.MASTERCARD: CreditCardType = CreditCardType("MasterCard")
        self.DISCOVER: CreditCardType = CreditCardType("Discover")
        self.AMERICANEXPRESS: CreditCardType = CreditCardType("AMX")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> CreditCardTypeFactory:
        return CreditCardTypeFactory.instance
from org.allbinary.business.user.commerce.money.payment.types.CreditCardType import CreditCardType


CreditCardTypeFactory.instance = CreditCardTypeFactory()

