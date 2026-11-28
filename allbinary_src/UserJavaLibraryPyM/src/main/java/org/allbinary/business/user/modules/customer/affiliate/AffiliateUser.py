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
# package org.allbinary.business.user.modules.customer.affiliate

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from org.allbinary.business.user.modules.User import User


@java_inherited_overloads
class AffiliateUser(User):
    def _java_defaults(self):
        vars(self).setdefault("affiliateSales", None)

    def _init_fields(self) -> None:
        if "affiliateSales" not in vars(self): self.affiliateSales: AffiliateSales = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    def _constructor0(self) -> None:
        __class__._java_defaults(self)
        from org.allbinary.business.advertisement.affiliate.sales.AffiliateSales import AffiliateSales
        super().__init__()
        __class__._init_fields(self)
        self.affiliateSales = AffiliateSales()
    

    def _constructor1(self, userHashMap: HashMap) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.advertisement.affiliate.sales.AffiliateSales import AffiliateSales
        super().__init__(userHashMap)
        __class__._init_fields(self)
        self.affiliateSales = AffiliateSales()
    

    def validateSession(self, weblisketSession: WeblisketSessionInterface) -> None:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
        java_super_call(super(), "validateSession", weblisketSession)
        self.updateSession(weblisketSession)
    

    def updateSession(self, weblisketSession: WeblisketSessionInterface) -> None:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
        weblisketSession.setStoreName(self.getPermissions())
    

    def isSessionValid(self) -> bool:
        return java_predicate(self.affiliateSales, "isValid")
# from java.util.HashMap import HashMap
# from org.allbinary.business.advertisement.affiliate.sales.AffiliateSales import AffiliateSales
# from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface


