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

from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface


class WeblisketSession(WeblisketSessionInterface):

    def _init_fields(self) -> None:
        if "session" not in vars(self): self.session: HttpSession = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            __class__.__jconstructor2(self, *args)

    def __jconstructor2(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)) and (args[1] is None or any(base.__name__ == "PageContext" for base in type(args[1]).__mro__)):
            __class__._constructor2_1(self, *args)
        else:
            __class__._constructor2_2(self, *args)
    

    def _constructor2_1(self, hashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        __class__.__jconstructor2(self, hashMap, pageContext.getRequest())
    

    def _constructor2_2(self, hashMap: HashMap, httpServletRequest: HttpServletRequest) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        __class__._init_fields(self)
        propertiesHashMap: HashMap = hashMap
        request: HttpServletRequest = httpServletRequest
        self.session = request.getSession(True)
        if self.getStoreName() is None:
            self.setStoreName(propertiesHashMap.get(StoreFrontData.getInstance().NAME))
    

    def getId(self) -> str:
        return self.session.getId()
    

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
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        self.session.setAttribute(WeblisketSessionData.AUTHENTICATED, BooleanFactory.getInstance().TRUE_STRING)
    

    def setRole(self, aRole: UserRole) -> None:
        from org.allbinary.business.user.role.UserRole import UserRole
        from org.allbinary.business.user.role.UserRoleData import UserRoleData
        self.session.setAttribute(str(UserRoleData.NAME), aRole)
    

    def setAttempts(self, value: int) -> None:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
        self.session.setAttribute(WeblisketSessionData.ATTEMPTS, value)
    

    def setTimeout(self, value: str) -> None:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
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
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
        return self.session.getAttribute(WeblisketSessionData.AUTHENTICATED)
    

    def getAttempts(self) -> int:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
        return self.session.getAttribute(WeblisketSessionData.ATTEMPTS)
    

    def getTimeout(self) -> str:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
        return self.session.getAttribute(WeblisketSessionData.TIMEOUT)
    

    def getStoreName(self) -> str:
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        return self.session.getAttribute(StoreFrontData.getInstance().NAME)
    

    # throws Exception
    def getRole(self) -> UserRole:
        from org.allbinary.business.user.role.UserRole import UserRole
        from org.allbinary.business.user.role.UserRoleB import UserRoleB
        from org.allbinary.business.user.role.UserRoleData import UserRoleData
        userRole: UserRole = self.session.getAttribute(str(UserRoleData.NAME))
        if userRole is not None:
            return UserRoleB.getRole(userRole.getBasicUserRole().getRole())
        else:
            return None
    

    # throws Exception
    def getOrder(self) -> OrderInterface:
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.business.user.commerce.inventory.basket.Basket import Basket
        from org.allbinary.business.user.commerce.inventory.order.Order import Order
        from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getStoreName())
        basketName: str = storeFrontInterface.getBasketName()
        if not (StringValidationUtil.getInstance().isEmpty(basketName)):
            orderInterface: OrderInterface = self.session.getAttribute(basketName)
            if orderInterface is None:
                orderInterface = Order(Basket())
            self.session.setAttribute(basketName, orderInterface)
            return orderInterface
        else:
            raise Exception("Basket Name Not Found")
    

    def setAuthenticated_j1(self, value: bool) -> None:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        self.session.setAttribute(WeblisketSessionData.AUTHENTICATED, BooleanFactory.getInstance().FALSE_STRING)

    def setAuthenticated(self, *args):
        implementation = __class__.__dict__.get("setAuthenticated_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().setAuthenticated(*args)
    

    def clear(self) -> None:
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.role.UserRoleData import UserRoleData
        self.session.removeAttribute(WeblisketSessionData.AUTHENTICATED)
        self.session.removeAttribute(WeblisketSessionData.TIMEOUT)
        self.session.removeAttribute(str(UserRoleData.NAME))
        self.session.removeAttribute(UserData.USERNAME)
    

    def getCreationTime(self) -> int:
        return self.session.getCreationTime()
    

    def getLastAccessedTime(self) -> int:
        return self.session.getLastAccessedTime()
    

    def removeBasket(self) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.getStoreName())
        basketName: str = storeFrontInterface.getBasketName()
        if not (StringValidationUtil.getInstance().isEmpty(basketName)):
            self.session.removeAttribute(basketName)
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.http.HttpSession import HttpSession
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.business.user.commerce.inventory.basket.Basket import Basket
# from org.allbinary.business.user.commerce.inventory.order.Order import Order
# from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
# from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
# from org.allbinary.business.user.role.UserRole import UserRole
# from org.allbinary.business.user.role.UserRoleB import UserRoleB
# from org.allbinary.business.user.role.UserRoleData import UserRoleData
# from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.globals.GLOBALS2 import GLOBALS2


