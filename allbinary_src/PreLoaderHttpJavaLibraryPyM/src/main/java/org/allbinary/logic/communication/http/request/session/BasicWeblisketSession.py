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
# package org.allbinary.logic.communication.http.request.session

from __future__ import annotations



class BasicWeblisketSession:

    def _init_fields(self) -> None:
        self.session: HttpSession = None
        self.pageContext: PageContext = None
    

    def __init__(self, pageContext: PageContext) -> None:
        self._init_fields()
        self.pageContext = pageContext
        request: HttpServletRequest = pageContext.getRequest()
        self.session = request.getSession(True)
    

    def setRole(self, aRole: BasicUserRole) -> None:
        from org.allbinary.business.user.role.BasicUserRole import BasicUserRole
        from org.allbinary.business.user.role.BasicUserRoleData import BasicUserRoleData
        self.session.setAttribute(str(BasicUserRoleData.NAME), aRole)
    

    def getRole(self) -> BasicUserRole:
        from org.allbinary.business.user.role.BasicUserRole import BasicUserRole
        from org.allbinary.business.user.role.BasicUserRoleData import BasicUserRoleData
        return self.session.getAttribute(str(BasicUserRoleData.NAME))
    

    def setPassword(self, password: str) -> None:
        from org.allbinary.business.user.UserData import UserData
        self.session.setAttribute(UserData.PASSWORD, password)
    

    def setUserName(self, userName: str) -> None:
        from org.allbinary.business.user.UserData import UserData
        self.session.setAttribute(UserData.USERNAME, userName)
    

    def setPaymentMethod(self, value: str) -> None:
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        self.session.setAttribute(str(PaymentGatewayData.NAME), value)
    

    def setAuthenticated_j0(self) -> None:
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        self.session.setAttribute(WeblisketSessionData.AUTHENTICATED, BooleanFactory.getInstance().TRUE_STRING)
    

    def setAttempts(self, value: int) -> None:
        self.session.setAttribute(WeblisketSessionData.ATTEMPTS, value)
    

    def setTimeout(self, value: str) -> None:
        self.session.setAttribute(WeblisketSessionData.TIMEOUT, value)
    

    def setStoreName(self, value: str) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        self.session.setAttribute(StoreFrontData.getInstance().NAME, value)
    

    def getWebAppPath(self) -> str:
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        return self.session.getAttribute(GLOBALS2.WEBAPPPATH)
    

    def getUserName(self) -> str:
        from org.allbinary.business.user.UserData import UserData
        return self.session.getAttribute(UserData.USERNAME)
    

    def getPassword(self) -> str:
        from org.allbinary.business.user.UserData import UserData
        return self.session.getAttribute(UserData.PASSWORD)
    

    def getPaymentMethod(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        return self.session.getAttribute(str(PaymentGatewayData.NAME))
    

    def getAuthentication(self) -> str:
        return self.session.getAttribute(WeblisketSessionData.AUTHENTICATED)
    

    def getAttempts(self) -> int:
        return self.session.getAttribute(WeblisketSessionData.ATTEMPTS)
    

    def getTimeout(self) -> str:
        return self.session.getAttribute(WeblisketSessionData.TIMEOUT)
    

    def getStoreName(self) -> str:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        return self.session.getAttribute(StoreFrontData.getInstance().NAME)
    

    def setAuthenticated_j1(self, value: bool) -> None:
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        self.session.setAttribute(WeblisketSessionData.AUTHENTICATED, BooleanFactory.getInstance().FALSE_STRING)

    def setAuthenticated(self, *args):
        return getattr(self, "setAuthenticated_j" + str(len(args)))(*args)
    

    def clear(self) -> None:
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.role.BasicUserRoleData import BasicUserRoleData
        self.session.removeAttribute(WeblisketSessionData.AUTHENTICATED)
        self.session.removeAttribute(WeblisketSessionData.TIMEOUT)
        self.session.removeAttribute(str(BasicUserRoleData.NAME))
        self.session.removeAttribute(UserData.USERNAME)
    

    def getCreationTime(self) -> int:
        return self.session.getCreationTime()
    

    def getLastAccessedTime(self) -> int:
        lastAccessedTime: int = self.session.getLastAccessedTime()
        return lastAccessedTime
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.http.HttpSession import HttpSession
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
# from org.allbinary.business.user.role.BasicUserRole import BasicUserRole
# from org.allbinary.business.user.role.BasicUserRoleData import BasicUserRoleData
# from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
# from org.allbinary.globals.GLOBALS2 import GLOBALS2


