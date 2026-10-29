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

from views.admin.payment.gateway.PaymentGatewayViewAbstract import PaymentGatewayViewAbstract


class GatewayView(PaymentGatewayViewAbstract):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    def getFormData(self, request: HttpServletRequest) -> None:
        super().getFormData(request)
        if StringValidationUtil.getInstance().isEmpty(self.getPaymentGatewayPrimaryKey().getName()):
            self.getPaymentGatewayPrimaryKey().setName(self.getWeblisketSession().getPaymentMethod())
    

    # throws Exception
    def view(self) -> str:
        from views.admin.payment.gateway.PaymentGatewayComponent import PaymentGatewayComponent
        try:
            paymentGatewayInterface: PaymentGatewayInterface = PaymentGatewayEntityFactory.getInstance().getPaymentGatewayInterface(self.getPaymentGatewayPrimaryKey().getStoreName(), BasicPaymentTypeUtil.getInstance().get(self.getPaymentGatewayPrimaryKey().getName()))
            return PaymentGatewayComponent(self.getTransformInfoInterface(), paymentGatewayInterface).view()
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "edit()", e)
            raise e
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterface import PaymentGatewayInterface
from org.allbinary.business.user.commerce.money.payment.types.BasicPaymentTypeUtil import BasicPaymentTypeUtil
from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface


