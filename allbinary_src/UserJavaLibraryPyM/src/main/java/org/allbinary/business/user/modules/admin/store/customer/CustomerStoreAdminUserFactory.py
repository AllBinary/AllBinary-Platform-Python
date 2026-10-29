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
# package org.allbinary.business.user.modules.admin.store.customer

from __future__ import annotations

from org.allbinary.business.user.UserFactoryInterface import UserFactoryInterface


class CustomerStoreAdminUserFactory(UserFactoryInterface):
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def getInstance(self) -> UserInterface:
        from org.allbinary.business.user.modules.admin.store.customer.CustomerStoreAdminUser import CustomerStoreAdminUser
        return CustomerStoreAdminUser()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, hashMap: dict) -> UserInterface:
        from org.allbinary.business.user.modules.admin.store.customer.CustomerStoreAdminUser import CustomerStoreAdminUser
        return CustomerStoreAdminUser(hashMap)
# from java.util.HashMap import HashMap
from org.allbinary.business.user.UserInterface import UserInterface


