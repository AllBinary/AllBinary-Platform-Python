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

# from java.io.Serializable import Serializable


class UserRole(object):

    def _init_fields(self) -> None:
        self.basicUserRole: BasicUserRole = None
        self.userFactoryInterface: UserFactoryInterface = None
    

    def __init__(self, aBasicUserRole: BasicUserRole, aUserFactoryInterface: UserFactoryInterface) -> None:
        self._init_fields()
        self.basicUserRole = aBasicUserRole
        self.userFactoryInterface = aUserFactoryInterface
    

    def toString(self) -> str:
        return str(self.basicUserRole)

    def __str__(self) -> str:
        return self.toString()
    

    def getBasicUserRole(self) -> BasicUserRole:
        return self.basicUserRole
    

    # throws Exception
    def getUserFactory(self) -> UserFactoryInterface:
        return self.userFactoryInterface
    

    def getSessionTimeout(self) -> int:
        return self.basicUserRole.getSessionTimeout()
    

    def getSessionInactivityTimeout(self) -> int:
        return self.basicUserRole.getSessionInactivityTimeout()
from org.allbinary.business.user.UserFactoryInterface import UserFactoryInterface


