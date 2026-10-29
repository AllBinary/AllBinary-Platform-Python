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

from org.allbinary.logic.string.StringUtil import StringUtil


class PaymentGatewayPageData:
    EXTENSION: str = ".jsp"
    NAME: str = StringUtil.getInstance().EMPTY_STRING
    FORWARDMAKEPAYMENT: str = "MakePayment.jsp"
    PAYMENTOPTIONS: str = None
    STARTCHECKOUT: str = None

    def _init_fields(self) -> None:
        self.MAKEPAYMENT: str = None
        self.CHECKOUT: str = None
        self.SHIPPING: str = None
        self.SHIPPINGADDRESS: str = None
        self.SHIPPINGADDRESSACTION: str = None
        self.BILLINGADDRESS: str = None
        self.PAYMENT: str = None
        self.AUTHORIZE: str = None
        self.FINISH: str = None
    

    def __init__(self, location: str, paymentMethod: str) -> None:
        self._init_fields()
        paymentMethodString: str = str(PaymentGatewayPageData.NAME) + paymentMethod
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append(location)
        stringBuffer.append("MakePayment")
        stringBuffer.append(PaymentGatewayPageData.EXTENSION)
        self.MAKEPAYMENT = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(paymentMethodString)
        stringBuffer.append("Checkout")
        stringBuffer.append(PaymentGatewayPageData.EXTENSION)
        self.CHECKOUT = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(paymentMethodString)
        stringBuffer.append("Shipping")
        stringBuffer.append(PaymentGatewayPageData.EXTENSION)
        self.SHIPPING = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(paymentMethodString)
        stringBuffer.append("ShippingAddress")
        stringBuffer.append(PaymentGatewayPageData.EXTENSION)
        self.SHIPPINGADDRESS = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(paymentMethodString)
        stringBuffer.append("ShippingAddressAction")
        stringBuffer.append(PaymentGatewayPageData.EXTENSION)
        self.SHIPPINGADDRESSACTION = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(paymentMethodString)
        stringBuffer.append("BillingAddress")
        stringBuffer.append(PaymentGatewayPageData.EXTENSION)
        self.BILLINGADDRESS = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(paymentMethodString)
        stringBuffer.append("Payment")
        stringBuffer.append(PaymentGatewayPageData.EXTENSION)
        self.PAYMENT = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(paymentMethodString)
        stringBuffer.append("Authorize")
        stringBuffer.append(PaymentGatewayPageData.EXTENSION)
        self.AUTHORIZE = str(stringBuffer)
        stringBuffer.delete(0, stringBuffer.length())
        stringBuffer.append(paymentMethodString)
        stringBuffer.append("PaymentFinish")
        stringBuffer.append(PaymentGatewayPageData.EXTENSION)
        self.FINISH = str(stringBuffer)
from org.allbinary.logic.string.StringMaker import StringMaker


PaymentGatewayPageData.PAYMENTOPTIONS = "PaymentOptions" + str(PaymentGatewayPageData.EXTENSION)

PaymentGatewayPageData.STARTCHECKOUT = "StartCheckout" + str(PaymentGatewayPageData.EXTENSION)

