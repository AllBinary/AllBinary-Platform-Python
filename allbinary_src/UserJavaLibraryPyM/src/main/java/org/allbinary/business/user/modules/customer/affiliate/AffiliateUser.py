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

from org.allbinary.business.user.modules.User import User


class AffiliateUser(User):

    def _init_fields(self) -> None:
        self.affiliateSales: AffiliateSales = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        super().__init__()
        self._init_fields()
        self.affiliateSales = AffiliateSales()
    

    def _constructor1(self, userHashMap: dict) -> None:
        super().__init__(userHashMap)
        self._init_fields()
        self.affiliateSales = AffiliateSales()
    

    def validateSession(self, weblisketSession: WeblisketSessionInterface) -> None:
        super().validateSession(weblisketSession)
        self.updateSession(weblisketSession)
    

    def updateSession(self, weblisketSession: WeblisketSessionInterface) -> None:
        weblisketSession.setStoreName(self.getPermissions())
    

    def isSessionValid(self) -> bool:
        return self.affiliateSales.isValid()
# from java.util.HashMap import HashMap
from org.allbinary.business.advertisement.affiliate.sales.AffiliateSales import AffiliateSales
from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface


