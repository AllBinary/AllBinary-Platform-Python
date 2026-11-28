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

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from org.allbinary.business.user.modules.User import User


@java_inherited_overloads
class ProductStoreAdminUser(User):

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor0(self) -> None:
        super().__init__()
    

    def _constructor1(self, userHashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        super().__init__(userHashMap)
    

    def validateSession(self, weblisketSession: WeblisketSessionInterface) -> None:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
        java_super_call(super(), "validateSession", weblisketSession)
        self.updateSession(weblisketSession)
    

    def updateSession(self, weblisketSession: WeblisketSessionInterface) -> None:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
        weblisketSession.setStoreName(self.getPermissions())
# from java.util.HashMap import HashMap
# from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface


