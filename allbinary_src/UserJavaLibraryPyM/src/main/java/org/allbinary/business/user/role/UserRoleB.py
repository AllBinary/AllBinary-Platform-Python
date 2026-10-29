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

import threading
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.user.role.UserRole import UserRole


class UserRoleB(UserRole):
    roleVector: BasicArrayList = BasicArrayListD()
    _lock = threading.RLock()
    

    def __init__(self, aBasicUserRole: BasicUserRole, aUserFactoryInterface: UserFactoryInterface) -> None:
        super().__init__(aBasicUserRole, aUserFactoryInterface)
        UserRoleB.roleVector.add(self)
    

    # throws Exception
    @staticmethod
    def getRole(role: str) -> UserRole:
        with UserRoleB._lock:
            return UserRoleB._getRole_unlocked(role)

    @staticmethod
    def _getRole_unlocked(role: str) -> UserRole:
        from org.allbinary.business.user.role.UserRoleFactory import UserRoleFactory
        UserRoleFactory.getInstance()
        if not StringValidationUtil.getInstance().isEmpty(role):
            roleVector: BasicArrayList = UserRoleB.getAll()
            size: int = roleVector.size()
            for index in range(0, size):
                userRole: UserRole = roleVector.get(index)
                if ((role > str(userRole)) - (role < str(userRole))) == 0:
                    return userRole
        raise Exception("Unable to get role - Unknown Role = " + role)
    

    @staticmethod
    def getAll() -> BasicArrayList:
        from org.allbinary.business.user.role.UserRoleFactory import UserRoleFactory
        UserRoleFactory.getInstance()
        return UserRoleB.roleVector
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.business.user.UserFactoryInterface import UserFactoryInterface
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil


