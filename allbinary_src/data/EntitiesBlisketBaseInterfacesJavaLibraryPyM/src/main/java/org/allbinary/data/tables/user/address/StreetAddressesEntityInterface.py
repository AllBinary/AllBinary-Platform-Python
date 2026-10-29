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
# package org.allbinary.data.tables.user.address

from __future__ import annotations

from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
class StreetAddressesEntityInterface(BasicDataTableInterface):
    

    def remove(self, index: int) -> None:
        raise NotImplementedError()
    

    def add(self, address: StreetAddress) -> None:
        raise NotImplementedError()
    

    def update(self, address: StreetAddress) -> None:
        raise NotImplementedError()
    

    def getLastId(self) -> str:
        raise NotImplementedError()
    

    def getDefault(self) -> StreetAddress:
        raise NotImplementedError()
    

    def setDefault(self, value: str) -> None:
        raise NotImplementedError()
from org.allbinary.business.user.address.StreetAddress import StreetAddress


