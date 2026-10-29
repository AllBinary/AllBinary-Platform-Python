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
# package views.admin.payment.gateway

from __future__ import annotations

from views.business.context.modules.storefront.HttpStoreComponentView import HttpStoreComponentView


class PaymentGatewayComponent(HttpStoreComponentView):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.paymentGatewayInterface: PaymentGatewayInterface = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface, paymentGatewayInterface: PaymentGatewayInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.paymentGatewayInterface = paymentGatewayInterface
    

    # throws Exception
    def addDomNodeInterfaces(self) -> None:
        paymentType: BasicPaymentType = BasicPaymentTypeUtil.getInstance().get(self.paymentGatewayInterface.getName())
        paymentGatewayDomNodeFactoryInterface: PaymentGatewayDomNodeFactoryInterface = paymentType.getPaymentGatewayDomNodeFactoryInterface()
        domNodeInterface: DomNodeInterface = paymentGatewayDomNodeFactoryInterface.getInstance(self.paymentGatewayInterface)
        self.addDomNodeInterface(domNodeInterface)
    

    def view(self) -> str:
        try:
            self.addDomNodeInterfaces()
            return super().view()
        except Exception as e:
            error: str = "Failed to view payment gateway"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view()", e)
            return error
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterface import PaymentGatewayInterface
from org.allbinary.business.user.commerce.money.payment.gateway.modules.gateway.PaymentGatewayDomNodeFactoryInterface import PaymentGatewayDomNodeFactoryInterface
from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentType import BasicPaymentType
from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentTypeUtil import BasicPaymentTypeUtil
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


