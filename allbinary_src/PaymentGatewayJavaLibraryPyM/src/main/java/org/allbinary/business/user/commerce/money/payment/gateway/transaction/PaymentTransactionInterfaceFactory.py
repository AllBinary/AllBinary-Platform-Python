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

from java.lang.JavaRuntimeStatic import lazy_static


class PaymentTransactionInterfaceFactory:
    instance: PaymentTransactionInterfaceFactory = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> PaymentTransactionInterfaceFactory:
        return PaymentTransactionInterfaceFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    def getInstance_j1(self, orderReview: OrderHistory) -> PaymentTransactionInterface:
        from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
        from org.allbinary.business.user.commerce.money.payment.types.PaymentType import PaymentType
        from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            gatewayName: str = orderReview.getPaymentMethod()
            if gatewayName is not None:
                paymentType: PaymentType = PaymentTypeUtil.getInstance().get(gatewayName)
                paymentTransactionInterfaceFactoryInterface: PaymentTransactionInterfaceFactoryInterface = paymentType.getPaymentTransactionInterfaceFactoryInterface()
                paymentTransactionInterface: PaymentTransactionInterface = paymentTransactionInterfaceFactoryInterface.getInstance(orderReview)
                return paymentTransactionInterface
            raise Exception("Failed to create PaymentTransactionInterface: " + "GatewayName is: " + gatewayName)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PAYMENTERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put("Failed to generate test data", self, commonStrings.GET_INSTANCE, e)
            raise e

    def getInstance(self, *args):
        return getattr(self, "getInstance_j" + str(len(args)))(*args)
# from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
# from org.allbinary.business.user.commerce.money.payment.types.PaymentType import PaymentType
# from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _PaymentTransactionInterfaceFactory_instance() -> object:
    return PaymentTransactionInterfaceFactory()

lazy_static(PaymentTransactionInterfaceFactory, "instance", _PaymentTransactionInterfaceFactory_instance)

