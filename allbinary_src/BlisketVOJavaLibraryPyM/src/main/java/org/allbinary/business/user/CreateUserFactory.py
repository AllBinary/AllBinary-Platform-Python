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
# package org.allbinary.business.user

from __future__ import annotations



class CreateUserFactory:
    

    def __init__(self) -> None:
        pass
    

    # throws Exception
    @staticmethod
    def getInstance(hashMap: dict) -> UserInterface:
        if hashMap is not None:
            roleString: str = hashMap.get(str(UserRoleData.NAME))
            if not StringValidationUtil.getInstance().isEmpty(roleString):
                role: UserRole = UserRoleB.getRole(roleString)
                return role.getUserFactory().getInstance(hashMap)
            else:
                raise Exception("No Role Specified")
        else:
            raise Exception("Null HashMap")
# from java.util.HashMap import HashMap
from org.allbinary.business.user.role.UserRole import UserRole
from org.allbinary.business.user.role.UserRoleB import UserRoleB
from org.allbinary.business.user.role.UserRoleData import UserRoleData
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil


