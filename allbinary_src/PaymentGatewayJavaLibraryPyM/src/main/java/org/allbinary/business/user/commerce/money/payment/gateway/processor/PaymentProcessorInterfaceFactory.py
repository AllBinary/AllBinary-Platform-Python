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

from java.lang.JavaRuntimeStatic import java_predicate
import threading
from java.lang.JavaRuntimeStatic import lazy_static


class PaymentProcessorInterfaceFactory:
    instance: PaymentProcessorInterfaceFactory = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    @staticmethod
    def getInstance_j0() -> PaymentProcessorInterfaceFactory:
        return PaymentProcessorInterfaceFactory.instance
    

    def __init__(self) -> None:
        __class__._init_fields(self)
    

    # throws Exception
    def getInstance_j1(self, transformInfoInterface: TransformInfoInterface) -> PaymentProcessorInterface:
        with self._lock:
            return __class__.__dict__["_getInstance_j1_unlocked"].__get__(self, __class__)(transformInfoInterface)

    def _getInstance_j1_unlocked(self, transformInfoInterface: TransformInfoInterface) -> PaymentProcessorInterface:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterface import PaymentTransactionInterface
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterfaceRequestFactory import PaymentTransactionInterfaceRequestFactory
        from org.allbinary.business.user.commerce.money.payment.types.PaymentType import PaymentType
        from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            paymentTransactionInterface: PaymentTransactionInterface = PaymentTransactionInterfaceRequestFactory.getInstance().getInstance(transformInfoInterface)
            gatewayName: str = paymentTransactionInterface.getOrderHistory().getPaymentMethod()
            if not (StringValidationUtil.getInstance().isEmpty(gatewayName)):
                paymentType: PaymentType = PaymentTypeUtil.getInstance().get(gatewayName)
                paymentProcessorInterfaceFactoryInterface: PaymentProcessorInterfaceFactoryInterface = paymentType.getPaymentProcessorInterfaceFactoryInterface()
                return paymentProcessorInterfaceFactoryInterface.getInstance(transformInfoInterface, paymentTransactionInterface)
            raise Exception("Error Getting PaymentProcessorInterface")
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().PAYMENTERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put(commonStrings.EXCEPTION, self, commonStrings.GET_INSTANCE, e)
            raise e

    def getInstance(self=None, *args):
        if self is None and not args: return __class__.getInstance_j0()
        implementation = __class__.__dict__.get("getInstance_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().getInstance(*args)
# from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterface import PaymentTransactionInterface
# from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionInterfaceRequestFactory import PaymentTransactionInterfaceRequestFactory
# from org.allbinary.business.user.commerce.money.payment.types.PaymentType import PaymentType
# from org.allbinary.business.user.commerce.money.payment.types.PaymentTypeUtil import PaymentTypeUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _PaymentProcessorInterfaceFactory_instance() -> object:
    return PaymentProcessorInterfaceFactory()

lazy_static(PaymentProcessorInterfaceFactory, "instance", _PaymentProcessorInterfaceFactory_instance)

