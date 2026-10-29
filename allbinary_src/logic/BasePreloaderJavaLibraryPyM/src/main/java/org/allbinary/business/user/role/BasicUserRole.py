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
# from java.io.Serializable import Serializable
from org.allbinary.util.BasicArrayListD import BasicArrayListD


class BasicUserRole(object):
    roleVector: BasicArrayList = BasicArrayListD()
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.m_int_RoleId: int = None
        self.role: str = None
        self.displayValue: str = None
        self.sessionTimeout: int = None
        self.sessionInactivityTimeout: int = None

    def __init__(self, *args) -> None:
        if len(args) == 4:
            self._constructor4(*args)
        elif len(args) == 5:
            self._constructor5(*args)
    

    def _constructor4(self, aRole: str, a_int_RoleId: int, aSessionTimeout: int, aSessionInactivityTimeout: int) -> None:
        self._constructor5(aRole, aRole, a_int_RoleId, aSessionTimeout, aSessionInactivityTimeout)
    

    def _constructor5(self, aRole: str, aDisplayValue: str, a_int_RoleId: int, aSessionTimeout: int, aSessionInactivityTimeout: int) -> None:
        self._init_fields()
        self.m_int_RoleId = a_int_RoleId
        self.role = aRole
        self.displayValue = aDisplayValue
        self.sessionTimeout = aSessionTimeout
        self.sessionInactivityTimeout = aSessionInactivityTimeout
        BasicUserRole.roleVector.add(self)
    

    def getRoleId(self) -> int:
        return self.m_int_RoleId
    

    def getRole(self) -> str:
        return self.role
    

    def getSessionTimeout(self) -> int:
        return self.sessionTimeout
    

    def getSessionInactivityTimeout(self) -> int:
        return self.sessionInactivityTimeout
    

    def equals(self, basicUserRole: BasicUserRole) -> bool:
        if self.getRoleId() == basicUserRole.getRoleId():
            return True
        return False

    def __eq__(self, other: object) -> bool:
        return self.equals(other)
    

    def toString(self) -> str:
        return self.getRole()

    def __str__(self) -> str:
        return self.toString()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    @staticmethod
    def getRole(role: str) -> BasicUserRole:
        with BasicUserRole._lock:
            return BasicUserRole._getRole_unlocked(role)

    @staticmethod
    def _getRole_unlocked(role: str) -> BasicUserRole:
        roleVector: BasicArrayList = BasicUserRole.getAll()
        size: int = roleVector.size()
        for index in range(0, size):
            userRole: BasicUserRole = roleVector.get(index)
            if ((role > str(userRole)) - (role < str(userRole))) == 0:
                return userRole
        raise Exception("Unable to get role - Unknown Role")
    

    @staticmethod
    def getAll() -> BasicArrayList:
        return BasicUserRole.roleVector
from org.allbinary.util.BasicArrayList import BasicArrayList


