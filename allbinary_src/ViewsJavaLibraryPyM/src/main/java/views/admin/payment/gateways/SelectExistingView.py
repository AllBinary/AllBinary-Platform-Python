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
# package views.admin.payment.gateways

from __future__ import annotations

from views.admin.payment.gateway.PaymentGatewayViewAbstract import PaymentGatewayViewAbstract


class SelectExistingView(PaymentGatewayViewAbstract):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
    

    def __init__(self, transformInfoInterface: TransformInfoInterface) -> None:
        from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
        super().__init__(transformInfoInterface)
        self._init_fields()
    

    # throws Exception
    def view(self) -> str:
        from views.admin.payment.gateways.PaymentGatewaysView import PaymentGatewaysView
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
        from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityInterface import PaymentGatewayEntityInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            paymentGatewayEntityInterface: PaymentGatewayEntityInterface = PaymentGatewayEntityFactory.getInstance()
            existingGateways: BasicArrayList = paymentGatewayEntityInterface.findPaymentTypeVectorByStore(self.getPaymentGatewayPrimaryKey().getStoreName())
            return PaymentGatewaysView(self.getTransformInfoInterface(), existingGateways).view()
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "view", e)
            raise e
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityFactory import PaymentGatewayEntityFactory
# from org.allbinary.data.tables.user.commerce.money.payment.gateway.PaymentGatewayEntityInterface import PaymentGatewayEntityInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.visual.transform.info.TransformInfoInterface import TransformInfoInterface
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


