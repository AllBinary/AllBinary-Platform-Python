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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.TagHelper import TagHelper


class OrderHelper(TagHelper):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.storeFrontInterface: StoreFrontInterface = None
        self.propertiesHashMap: dict = None
        self.pageContext: PageContext = None
        self.request: HttpServletRequest = None
    

    def __init__(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.propertiesHashMap = propertiesHashMap
        self.pageContext = pageContext
        self.request = pageContext.getRequest()
        storeName: str = propertiesHashMap.get(StoreFrontData.getInstance().NAME)
        if not StringValidationUtil.getInstance().isEmpty(storeName):
            self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
        self.weblisketSession = WeblisketSession(self.propertiesHashMap, self.pageContext)
    

    def setPaymentGateway(self) -> bool:
        try:
            paymentGatewayBoolean: bool = False
            orderInterface: OrderInterface = self.weblisketSession.getOrder()
            requestPaymentGateway: str = self.request.getParameter(str(PaymentGatewayData.NAME))
            if not StringValidationUtil.getInstance().isEmpty(requestPaymentGateway):
                self.weblisketSession.setPaymentMethod(requestPaymentGateway)
                orderInterface.setPaymentMethod(requestPaymentGateway)
                paymentGatewayBoolean = True
            paymentGatewayEntityInterface: PaymentGatewayEntity = PaymentGatewayEntityFactory.getInstance()
            paymentTypeVector: BasicArrayList = paymentGatewayEntityInterface.findPaymentTypeVectorByStore(self.weblisketSession.getStoreName())
            if paymentTypeVector.size() == 1:
                paymentType: BasicPaymentType = paymentTypeVector.get(0)
                paymentGatewayInterface: PaymentGatewayInterface = paymentGatewayEntityInterface.getPaymentGatewayInterface(self.weblisketSession.getStoreName(), paymentType)
                paymentGateway: str = paymentGatewayInterface.getName()
                self.weblisketSession.setPaymentMethod(paymentGateway)
                orderInterface.setPaymentMethod(paymentGateway)
                paymentGatewayBoolean = True
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Successfully set PaymentGateway Order: ")
                stringBuffer.append(orderInterface.getId())
                stringBuffer.append(" to: ")
                stringBuffer.append(orderInterface.getPaymentMethod())
                self.logUtil.putF(str(stringBuffer), self, "setPaymentGateway()")
            return paymentGatewayBoolean
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Failed to set PaymentGateway for Order: ")
                try:
                    orderInterface: OrderInterface = self.weblisketSession.getOrder()
                    if orderInterface is not None:
                        stringBuffer.append(orderInterface.getId())
                        stringBuffer.append(" to: ")
                        stringBuffer.append(orderInterface.getPaymentMethod())
                except Exception as ex:
                    stringBuffer.append(" Exception Getting")
                self.logUtil.put(str(stringBuffer), self, "setPaymentGateway()", e)
            return False
    

    def process(self) -> str:
        try:
            order: OrderInterface = self.weblisketSession.getOrder()
            order.setStoreName(self.storeFrontInterface.getName())
            result: str = OrderProcessorUtil.getInstance().process(self.weblisketSession.getUserName(), order)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Successfully Processed Order: " + result, self, "processOrder()")
            return result
        except Exception as e:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Failed to Process Order: ")
            try:
                stringBuffer.append(self.weblisketSession.getOrder().getId())
            except Exception as ex:
                stringBuffer.append(" Exception Getting Id")
            error: str = str(stringBuffer)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.PROCESS, e)
            return error
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.commerce.inventory.order.Order import Order
from org.allbinary.business.user.commerce.inventory.order.OrderInterface import OrderInterface
from org.allbinary.business.user.commerce.inventory.order.OrderProcessorUtil import OrderProcessorUtil
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterface import PaymentGatewayInterface
from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentType import BasicPaymentType
from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntity import PaymentGatewayEntity
from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil


