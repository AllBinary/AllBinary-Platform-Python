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
# package org.allbinary.business.user.role

from __future__ import annotations



class StoreRoleFactory:
    instance: StoreRoleFactory = None

    def _init_fields(self) -> None:
        self.roles: BasicArrayList = BasicArrayListD()
        self.subscriberRoles: BasicArrayList = BasicArrayListD()
        self.wholesaleRoles: BasicArrayList = BasicArrayListD()
    

    @staticmethod
    def getInstance() -> StoreRoleFactory:
        return StoreRoleFactory.instance
    

    def __init__(self) -> None:
        from org.allbinary.business.user.role.BasicUserRoleFactory import BasicUserRoleFactory
        self._init_fields()
        basicUserRoleFactory: BasicUserRoleFactory = BasicUserRoleFactory.getInstance()
        self.roles.add(basicUserRoleFactory.CUSTOMER)
        self.roles.add(basicUserRoleFactory.SUBSCRIBERCUSTOMER)
        self.roles.add(basicUserRoleFactory.WHOLESALECUSTOMER)
        self.subscriberRoles.add(basicUserRoleFactory.SUBSCRIBERCUSTOMER)
        self.wholesaleRoles.add(basicUserRoleFactory.WHOLESALECUSTOMER)
    

    def getRoles(self) -> BasicArrayList:
        return self.roles
    

    def getSubscriberRoles(self) -> BasicArrayList:
        return self.subscriberRoles
    

    def getWholesaleRoles(self) -> BasicArrayList:
        return self.wholesaleRoles
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


StoreRoleFactory.instance = StoreRoleFactory()

