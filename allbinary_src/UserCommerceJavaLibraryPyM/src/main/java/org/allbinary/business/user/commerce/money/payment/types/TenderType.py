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



class TenderType:

    def _init_fields(self) -> None:
        self.name: str = None
    

    def __init__(self, name: str) -> None:
        self._init_fields()
        self.name = name
    

    def isEqual(self, tenderType: TenderType) -> bool:
        if ((str(self) > str(tenderType)) - (str(self) < str(tenderType))) == 0:
            return True
        else:
            return False
    

    def toString(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.toString()


