# 
# AllBinary Open License Version 1 
# Copyright (c) 2026 AllBinary 
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

from java.lang.JavaRuntimeStatic import lazy_static


class BasicUserRoles:
    instance: BasicUserRoles = None

    def _init_fields(self) -> None:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.util.BasicArrayListD import BasicArrayListD
        self.roleVector: BasicArrayList = BasicArrayListD()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> BasicUserRoles:
        return BasicUserRoles.instance
    

    # throws Exception
    def getRole(self, role: str) -> BasicUserRole:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        roleVector: BasicArrayList = self.getAll()
        size: int = roleVector.size()
        for index in range(0, size):
            userRole: BasicUserRole = roleVector.get(index)
            if ((role > str(userRole)) - (role < str(userRole))) == 0:
                return userRole
        raise Exception("Unable to get role - Unknown Role")
    

    def getAll(self) -> BasicArrayList:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        return self.roleVector
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD


def _BasicUserRoles_instance() -> object:
    return BasicUserRoles()

lazy_static(BasicUserRoles, "instance", _BasicUserRoles_instance)

