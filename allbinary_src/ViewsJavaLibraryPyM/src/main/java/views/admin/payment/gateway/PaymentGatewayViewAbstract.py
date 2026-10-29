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

from org.allbinary.logic.visual.transform.info.TransformInfoHttpComposite import TransformInfoHttpComposite


class PaymentGatewayViewAbstract(TransformInfoHttpComposite):

    def _init_fields(self) -> None:
        self.paymentGatewayPrimaryKey: PaymentGatewayPrimaryKey = None
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
        self.getFormData(self.getPageContext().getRequest())
    

    def getFormData(self, request: HttpServletRequest) -> None:
        storeName: str = self.getWeblisketSession().getStoreName()
        gatewayName: str = request.getParameter(str(PaymentGatewayData.NAME))
        self.setPaymentGatewayPrimaryKey(PaymentGatewayPrimaryKey(storeName, gatewayName))
    

    def getPaymentGatewayPrimaryKey(self) -> PaymentGatewayPrimaryKey:
        return self.paymentGatewayPrimaryKey
    

    def setPaymentGatewayPrimaryKey(self, paymentGatewayPrimaryKey: PaymentGatewayPrimaryKey) -> None:
        self.paymentGatewayPrimaryKey = paymentGatewayPrimaryKey
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayPrimaryKey import PaymentGatewayPrimaryKey
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


