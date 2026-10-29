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
# package org.allbinary.business.user.commerce.money.payment.gateway.transaction

from __future__ import annotations



class PaymentTransactionInterfaceRequestFactory:
    instance: PaymentTransactionInterfaceRequestFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
    

    @staticmethod
    def getInstance() -> PaymentTransactionInterfaceRequestFactory:
        return PaymentTransactionInterfaceRequestFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, transformInfoInterface: TransformInfoInterface) -> PaymentTransactionInterface:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterfaceFactory import PaymentTransactionInterfaceFactory
        try:
            httpTransformInfoInterface: TransformInfoHttpInterface = transformInfoInterface
            pageContext: PageContext = httpTransformInfoInterface.getPageContext()
            httpServletRequest: HttpServletRequest = pageContext.getRequest()
            command: str = httpServletRequest.getParameter(org.allbinary.globals.GLOBALS2.ADMINCOMMAND)
            if command is not None and ((command > org.allbinary.globals.GLOBALS2.AUTHORIZEFORMEVALBODYONERROR) - (command < org.allbinary.globals.GLOBALS2.AUTHORIZEFORMEVALBODYONERROR)) == 0:
                return self.generateFromTestData(transformInfoInterface)
            else:
                propertiesHashMap: dict = httpTransformInfoInterface.getPropertiesHashMap()
                weblisketSession: WeblisketSession = WeblisketSession(propertiesHashMap, pageContext)
                storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(weblisketSession.getStoreName())
                order: OrderInterface = weblisketSession.getOrder()
                orderId: str = order.getId()
                orderHistoryEntityInterface: OrderHistoryEntityInterface = OrderHistoryEntityFactory.getInstance()
                orderReview: OrderHistory = orderHistoryEntityInterface.getOrder(orderId)
                orderPaymentInfo: Payment = orderReview.getPaymentInfo()
                orderPaymentInfo.setTransactionType(str(TransactionTypeFactory.getInstance().SALE))
                orderPaymentInfo.setTenderType(str(TenderTypeFactory.getInstance().CREDITCARD))
                orderReview.setPaymentInfo(orderPaymentInfo)
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PAYMENT):
                    self.logUtil.putF(orderReview.getId(), self, "getPaymentTransactionInterface()")
                paymentTransactionInterface: PaymentTransactionInterface = PaymentTransactionInterfaceFactory.getInstance().getInstance(orderReview)
                return paymentTransactionInterface
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PAYMENTERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getPaymentTransactionInterface()", e)
            raise e
    

    # throws Exception
    def generateFromTestData(self, transformInfoInterface: TransformInfoInterface) -> PaymentTransactionInterface:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterfaceFactory import PaymentTransactionInterfaceFactory
        try:
            httpTransformInfoInterface: TransformInfoHttpInterface = transformInfoInterface
            propertiesHashMap: dict = httpTransformInfoInterface.getPropertiesHashMap()
            pageContext: PageContext = httpTransformInfoInterface.getPageContext()
            weblisketSession: WeblisketSession = WeblisketSession(propertiesHashMap, pageContext)
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(weblisketSession.getStoreName())
            httpServletRequest: HttpServletRequest = pageContext.getRequest()
            gatewayName: str = weblisketSession.getPaymentMethod()
            if StringValidationUtil.getInstance().isEmpty(gatewayName):
                gatewayName = httpServletRequest.getParameter(str(PaymentGatewayData.NAME))
            transactionType: str = httpServletRequest.getParameter(PaymentData.TRANSACTIONTYPE)
            tenderType: str = httpServletRequest.getParameter(PaymentData.TENDERTYPE)
            payment: Payment = Payment()
            payment.setTransactionType(transactionType)
            payment.setTenderType(tenderType)
            orderReview: OrderHistory = OrderHistory(Basket())
            orderReview.setStoreName(storeFrontInterface.getName())
            orderReview.setPaymentMethod(gatewayName)
            orderReview.setUserName("testing")
            orderId: str = httpServletRequest.getParameter("orderNumber")
            if orderId is None or ((orderId > StringUtil.getInstance().EMPTY_STRING) - (orderId < StringUtil.getInstance().EMPTY_STRING)) == 0:
                orderId = OrderIdGenerator().getNext()
                orderReview.setId(orderId)
                account: str = httpServletRequest.getParameter("account")
                expirationDate: str = httpServletRequest.getParameter("expirationDate")
                checkNumber: str = httpServletRequest.getParameter("checkNumber")
                driversLicense: str = httpServletRequest.getParameter("driversLicense")
                magneticInkCheckReader: str = httpServletRequest.getParameter("magneticInkCheckReader")
                aba: str = httpServletRequest.getParameter("aba")
                accountType: str = httpServletRequest.getParameter("accountType")
                name: str = httpServletRequest.getParameter("name")
                payment.setName(name)
                payment.setNumber(account)
                payment.setExpiration(expirationDate)
                payment.setCheckNumber(checkNumber)
                payment.setDriversLicense(driversLicense)
                payment.setMagneticInkCheckReader(magneticInkCheckReader)
                payment.setAba(aba)
                payment.setAccountType(accountType)
                street: str = httpServletRequest.getParameter("street")
                city: str = httpServletRequest.getParameter("city")
                state: str = httpServletRequest.getParameter("state")
                zip: str = httpServletRequest.getParameter("zip")
                streetAddress: StreetAddress = StreetAddress()
                streetAddress.setName(name)
                streetAddress.setStreet(street)
                streetAddress.setCity(city)
                streetAddress.setState(state)
                streetAddress.setCode(zip)
                email: str = httpServletRequest.getParameter("email")
                amount: str = httpServletRequest.getParameter("amount")
                orderReview.setTotal(Money(amount))
                orderReview.setBillingAddress(streetAddress)
            else:
                orderReview.setId(orderId)
            orderReview.setPaymentInfo(payment)
            paymentTransactionInterface: PaymentTransactionInterface = PaymentTransactionInterfaceFactory.getInstance().getInstance(orderReview)
            return paymentTransactionInterface
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PAYMENTERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "generatePaymentTransactionInterfaceFromTestData()", e)
            raise e
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.business.user.commerce.inventory.basket.Basket import Basket
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
from org.allbinary.business.user.commerce.money.Money import Money
from org.allbinary.business.user.commerce.money.payment.Payment import Payment
from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
from org.allbinary.business.user.commerce.money.payment.types.TenderTypeFactory import TenderTypeFactory
from org.allbinary.business.user.commerce.money.payment.types.TransactionTypeFactory import TransactionTypeFactory
from org.allbinary.data.generator.OrderIdGenerator import OrderIdGenerator
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityFactory import OrderHistoryEntityFactory
from org.allbinary.data.tables.user.commerce.inventory.order.OrderHistoryEntityInterface import OrderHistoryEntityInterface
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.TransformInfoHttpInterface import TransformInfoHttpInterface
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonStrings import CommonStrings


PaymentTransactionInterfaceRequestFactory.instance = PaymentTransactionInterfaceRequestFactory()

