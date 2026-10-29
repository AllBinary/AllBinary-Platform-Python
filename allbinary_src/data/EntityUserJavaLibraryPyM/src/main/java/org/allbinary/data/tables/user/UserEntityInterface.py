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
# package org.allbinary.data.tables.user

from __future__ import annotations

from org.allbinary.data.tables.BasicDataTableInterface import BasicDataTableInterface


# Java interface
class UserEntityInterface(BasicDataTableInterface):
    

    # throws Exception
    def getAdministrators(self) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getStoreManagers(self, storeFrontInterface: StoreFrontInterface) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getCustomers(self) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getUsersWithRole(self, userRole: UserRole) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getUsers(self, storeFrontInterface: StoreFrontInterface) -> BasicArrayList:
        raise NotImplementedError()
    

    # throws Exception
    def getUser(self, userName: str) -> UserInterface:
        raise NotImplementedError()
    

    def login(self, userName: str, password: str) -> str:
        raise NotImplementedError()
    

    def deleteWhere(self, key: str, value: str) -> None:
        raise NotImplementedError()
    

    def insert(self, values: BasicArrayList) -> None:
        raise NotImplementedError()
    

    def update(self, userName: str, updatedValues: dict) -> None:
        raise NotImplementedError()
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.business.user.role.UserRole import UserRole


