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

from java.lang.JavaRuntimeStatic import java_equals
# from java.io.Serializable import Serializable


class BasicUserRole(object):

    def _init_fields(self) -> None:
        if "m_int_RoleId" not in vars(self): self.m_int_RoleId: int = 0
        if "role" not in vars(self): self.role: str = None
        if "displayValue" not in vars(self): self.displayValue: str = None
        if "sessionTimeout" not in vars(self): self.sessionTimeout: int = 0
        if "sessionInactivityTimeout" not in vars(self): self.sessionInactivityTimeout: int = 0

    def __init__(self, *args) -> None:
        if len(args) == 4:
            __class__._constructor4(self, *args)
        elif len(args) == 5:
            __class__._constructor5(self, *args)
    

    def _constructor4(self, aRole: str, a_int_RoleId: int, aSessionTimeout: int, aSessionInactivityTimeout: int) -> None:
        __class__._constructor5(self, aRole, aRole, a_int_RoleId, aSessionTimeout, aSessionInactivityTimeout)
    

    def _constructor5(self, aRole: str, aDisplayValue: str, a_int_RoleId: int, aSessionTimeout: int, aSessionInactivityTimeout: int) -> None:
        from org.allbinary.business.user.role.BasicUserRoles import BasicUserRoles
        __class__._init_fields(self)
        self.m_int_RoleId = a_int_RoleId
        self.role = aRole
        self.displayValue = aDisplayValue
        self.sessionTimeout = aSessionTimeout
        self.sessionInactivityTimeout = aSessionInactivityTimeout
        BasicUserRoles.getInstance().roleVector.add(self)
    

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

    __hash__ = object.__hash__
    

    def toString(self) -> str:
        return self.getRole()

    def __str__(self) -> str:
        return self.toString()


