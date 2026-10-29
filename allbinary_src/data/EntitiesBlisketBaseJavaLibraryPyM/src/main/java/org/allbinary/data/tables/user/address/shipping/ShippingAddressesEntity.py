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
# package org.allbinary.data.tables.user.address.shipping

from __future__ import annotations

from org.allbinary.data.tables.user.address.StreetAddressesEntity import StreetAddressesEntity


class ShippingAddressesEntity(StreetAddressesEntity):

    def _init_fields(self) -> None:
        self.TABLENAME: str = "shipping"
    

    def __init__(self, userName: str) -> None:
        super().__init__(userName)
        self._init_fields()
        self.setTableName(self.TABLENAME)


