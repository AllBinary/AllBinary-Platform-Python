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



class TenderTypeFactory:
    instance: TenderTypeFactory = None

    def _init_fields(self) -> None:
        self.CREDITCARD: TenderType = TenderType("Credit Card")
        self.CHECK: TenderType = TenderType("Check")
        self.ACH: TenderType = TenderType("Ach")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> TenderTypeFactory:
        return TenderTypeFactory.instance
from org.allbinary.business.user.commerce.money.payment.types.TenderType import TenderType


TenderTypeFactory.instance = TenderTypeFactory()

