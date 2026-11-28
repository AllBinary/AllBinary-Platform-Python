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
# package org.allbinary.data.tables.user.address.billing

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.data.tables.user.address.StreetAddressesEntity import StreetAddressesEntity


@java_inherited_overloads
class BillingAddressesEntity(StreetAddressesEntity):
    def _java_defaults(self):
        vars(self).setdefault("TABLENAME", None)

    def _init_fields(self) -> None:
        self.TABLENAME: str = "billing"
    

    def __init__(self, userName: str) -> None:
        __class__._java_defaults(self)
        super().__init__(userName)
        __class__._init_fields(self)
        self.setTableName(self.TABLENAME)


