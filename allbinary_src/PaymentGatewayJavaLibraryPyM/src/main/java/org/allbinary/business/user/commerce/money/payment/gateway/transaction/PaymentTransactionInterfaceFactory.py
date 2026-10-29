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



class PaymentTransactionInterfaceFactory:
    instance: PaymentTransactionInterfaceFactory = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> PaymentTransactionInterfaceFactory:
        return PaymentTransactionInterfaceFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, orderReview: OrderHistory) -> PaymentTransactionInterface:
        try:
            gatewayName: str = orderReview.getPaymentMethod()
            if gatewayName is not None:
                paymentType: PaymentType = PaymentTypeUtil.getInstance().get(gatewayName)
                paymentTransactionInterfaceFactoryInterface: PaymentTransactionInterfaceFactoryInterface = paymentType.getPaymentTransactionInterfaceFactoryInterface()
                paymentTransactionInterface: PaymentTransactionInterface = paymentTransactionInterfaceFactoryInterface.getInstance(orderReview)
                return paymentTransactionInterface
            raise Exception("Failed to create PaymentTransactionInterface: " + "GatewayName is: " + gatewayName)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PAYMENTERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put("Failed to generate test data", self, commonStrings.GET_INSTANCE, e)
            raise e
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
from org.allbinary.business.user.commerce.money.payment.types.PaymentType import PaymentType
from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonStrings import CommonStrings


PaymentTransactionInterfaceFactory.instance = PaymentTransactionInterfaceFactory()

