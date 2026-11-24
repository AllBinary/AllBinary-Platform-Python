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
# package org.allbinary.business.user.commerce.money.payment.gateway

from __future__ import annotations

from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterfaceFactoryInterface import PaymentGatewayInterfaceFactoryInterface


class PaymentGatewayInterfaceFactory(PaymentGatewayInterfaceFactoryInterface):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j1_1(self, httpServletRequest: HttpServletRequest) -> PaymentGatewayInterface:
        from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PAYMENT):
                self.logUtil.putF("Getting", self, commonStrings.GET_INSTANCE)
            return self.getInstance(RequestParams(httpServletRequest).toHashMap())
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PAYMENTERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, "getInstance(HttpServletRequest)", e)
            raise e
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j1_2(self, paymentType: BasicPaymentType) -> PaymentGatewayInterface:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentType import BasicPaymentType
        from org.allbinary.logic.StdUtil import StdUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
        hashMap.put(str(PaymentGatewayData.NAME), paymentType.getName())
        return self.getInstance(hashMap)
    

    # throws Exception
    # Java overloaded method with the same parameter count: Python keeps the last definition
    def getInstance_j1_3(self, hashMap: HashMap) -> PaymentGatewayInterface:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentType import BasicPaymentType
        from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentTypeUtil import BasicPaymentTypeUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            gatewayName: str = hashMap.get(str(PaymentGatewayData.NAME))
            paymentType: BasicPaymentType = BasicPaymentTypeUtil.getInstance().get(gatewayName)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PAYMENT):
                self.logUtil.putF("Getting PaymentGatewayInterface for PaymentType: " + paymentType.getName() + " with: " + str(hashMap), self, commonStrings.GET_INSTANCE)
            paymentGatewayInterfaceFactoryInterface: PaymentGatewayInterfaceFactoryInterface = paymentType.getPaymentGatewayInterfaceFactoryInterface()
            return paymentGatewayInterfaceFactoryInterface.getInstance(hashMap)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PAYMENTERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            raise e

    def getInstance(self, *args):
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return self.getInstance_j1_1(*args)
        if len(args) == 1 and True and not isinstance(args[0], (str, list, int, float)):
            return self.getInstance_j1_2(*args)
        if len(args) == 1:
            return self.getInstance_j1_3(*args)
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentType import BasicPaymentType
# from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentTypeUtil import BasicPaymentTypeUtil
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


