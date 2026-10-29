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
# package org.allbinary.business.user.commerce.money.payment.gateway.processor

from __future__ import annotations

import threading


class PaymentProcessorInterfaceFactory:
    instance: PaymentProcessorInterfaceFactory = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance() -> PaymentProcessorInterfaceFactory:
        return PaymentProcessorInterfaceFactory.instance
    

    def __init__(self) -> None:
        self._init_fields()
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def getInstance(self, transformInfoInterface: TransformInfoInterface) -> PaymentProcessorInterface:
        with self._lock:
            return self._getInstance_unlocked(transformInfoInterface)

    def _getInstance_unlocked(self, transformInfoInterface: TransformInfoInterface) -> PaymentProcessorInterface:
        try:
            paymentTransactionInterface: PaymentTransactionInterface = PaymentTransactionInterfaceRequestFactory.getInstance().getInstance(transformInfoInterface)
            gatewayName: str = paymentTransactionInterface.getOrderHistory().getPaymentMethod()
            if not StringValidationUtil.getInstance().isEmpty(gatewayName):
                paymentType: PaymentType = PaymentTypeUtil.getInstance().get(gatewayName)
                paymentProcessorInterfaceFactoryInterface: PaymentProcessorInterfaceFactoryInterface = paymentType.getPaymentProcessorInterfaceFactoryInterface()
                return paymentProcessorInterfaceFactoryInterface.getInstance(transformInfoInterface, paymentTransactionInterface)
            raise Exception("Error Getting PaymentProcessorInterface")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().PAYMENTERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            raise e
from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterface import PaymentTransactionInterface
from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterfaceRequestFactory import PaymentTransactionInterfaceRequestFactory
from org.allbinary.business.user.commerce.money.payment.types.PaymentType import PaymentType
from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
from org.allbinary.string.CommonStrings import CommonStrings


PaymentProcessorInterfaceFactory.instance = PaymentProcessorInterfaceFactory()

