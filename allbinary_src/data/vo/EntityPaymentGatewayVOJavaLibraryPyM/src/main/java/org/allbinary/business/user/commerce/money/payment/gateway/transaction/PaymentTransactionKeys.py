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



class PaymentTransactionKeys:

    def _init_fields(self) -> None:
        self.key: str = None
    

    def __init__(self, value: str) -> None:
        self._init_fields()
        self.key = value
    

    def toString(self) -> str:
        return self.key

    def __str__(self) -> str:
        return self.toString()


