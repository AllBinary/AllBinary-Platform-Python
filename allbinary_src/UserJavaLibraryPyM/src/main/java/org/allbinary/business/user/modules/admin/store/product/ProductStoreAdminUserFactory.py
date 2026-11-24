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
# package org.allbinary.business.user.modules.admin.store.product

from __future__ import annotations

from org.allbinary.business.user.UserFactoryInterface import UserFactoryInterface


class ProductStoreAdminUserFactory(UserFactoryInterface):
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    def getInstance_j0(self) -> UserInterface:
        from org.allbinary.business.user.modules.admin.store.product.ProductStoreAdminUser import ProductStoreAdminUser
        from org.allbinary.business.user.UserInterface import UserInterface
        return ProductStoreAdminUser()
    

    # throws Exception
    def getInstance_j1(self, hashMap: HashMap) -> UserInterface:
        from org.allbinary.business.user.modules.admin.store.product.ProductStoreAdminUser import ProductStoreAdminUser
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserInterface import UserInterface
        return ProductStoreAdminUser(hashMap)

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from org.allbinary.business.user.UserInterface import UserInterface


