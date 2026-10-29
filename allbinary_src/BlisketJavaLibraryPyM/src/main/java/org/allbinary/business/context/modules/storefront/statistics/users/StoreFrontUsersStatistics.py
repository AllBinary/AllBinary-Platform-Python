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
# package org.allbinary.business.context.modules.storefront.statistics.users

from __future__ import annotations

from org.allbinary.business.context.modules.storefront.statistics.users.StoreFrontUsersStatisticsInterface import StoreFrontUsersStatisticsInterface


class StoreFrontUsersStatistics(StoreFrontUsersStatisticsInterface):

    def _init_fields(self) -> None:
        self.totalNumberOfUsers: int = None
        self.totalUsersByRoleHashMap: dict = None
    

    def __init__(self, storeFrontInterface: StoreFrontInterface) -> None:
        self._init_fields()
        self.totalUsersByRoleHashMap = StdUtil.getInstance().createHashMap()
        userEntityInterface: UserEntityInterface = UserEntityFactory.getInstance()
        userVector: BasicArrayList = userEntityInterface.getCustomers()
        self.totalNumberOfUsers = int(userVector.size())
        size: int = userVector.size()
        for index in range(0, size):
            userInterface: UserInterface = userVector.get(index)
            nextUserRole: UserRole = userInterface.getRole()
            currentNumberOfUsersForRole: int = self.getNewTotal(nextUserRole)
            self.totalUsersByRoleHashMap.put(nextUserRole, currentNumberOfUsersForRole)
    

    def getNewTotal(self, userRole: UserRole) -> int:
        numberOfUsersForRoleLong: int = self.totalUsersByRoleHashMap.get(userRole)
        if numberOfUsersForRoleLong is None:
            numberOfUsersForRoleLong = int(0)
        return int(int(numberOfUsersForRoleLong) + 1)
    

    def getNumberOfUsers(self) -> int:
        return self.totalNumberOfUsers
    

    def getNumberOfUsersByRole(self, role: str) -> int:
        totalForRole: int = self.totalUsersByRoleHashMap.get(role)
        return totalForRole
    

    def toHashMap(self) -> dict:
        from org.allbinary.business.context.modules.storefront.statistics.users.StoreFrontUsersStatisticsData import StoreFrontUsersStatisticsData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(StoreFrontUsersStatisticsData.getInstance().NUMBEROFUSERS, str(self.getNumberOfUsers()))
        setOfUserRoles: Set = self.totalUsersByRoleHashMap.keySet()
        nextUserRole: UserRole = None
        userRoleArray: list[object] = setOfUserRoles.toArray()
        size: int = len(userRoleArray)
        for index in range(0, size):
            nextUserRole = userRoleArray[index]
            totalForRole: int = self.totalUsersByRoleHashMap.get(nextUserRole)
            hashMap.put(str(nextUserRole), str(totalForRole))
        return hashMap
    

    def toVector(self) -> BasicArrayList:
        return None
    

    def getKey(self) -> object:
        return None
# from java.util.HashMap import HashMap
# from java.util.Set import Set
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.business.user.role.UserRole import UserRole
from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
from org.allbinary.data.tables.user.UserEntityInterface import UserEntityInterface
from org.allbinary.logic.StdUtil import StdUtil


