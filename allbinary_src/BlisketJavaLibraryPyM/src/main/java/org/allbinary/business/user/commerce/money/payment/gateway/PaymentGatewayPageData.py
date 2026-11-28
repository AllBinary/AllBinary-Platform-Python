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

from java.lang.JavaRuntimeStatic import lazy_static


class PaymentGatewayPageData:
    EXTENSION: str = ".jsp"
    NAME: str = None
    FORWARDMAKEPAYMENT: str = "MakePayment.jsp"
    PAYMENTOPTIONS: str = None
    STARTCHECKOUT: str = None

    def _init_fields(self) -> None:
        if "MAKEPAYMENT" not in vars(self): self.MAKEPAYMENT: str = None
        if "CHECKOUT" not in vars(self): self.CHECKOUT: str = None
        if "SHIPPING" not in vars(self): self.SHIPPING: str = None
        if "SHIPPINGADDRESS" not in vars(self): self.SHIPPINGADDRESS: str = None
        if "SHIPPINGADDRESSACTION" not in vars(self): self.SHIPPINGADDRESSACTION: str = None
        if "BILLINGADDRESS" not in vars(self): self.BILLINGADDRESS: str = None
        if "PAYMENT" not in vars(self): self.PAYMENT: str = None
        if "AUTHORIZE" not in vars(self): self.AUTHORIZE: str = None
        if "FINISH" not in vars(self): self.FINISH: str = None
    

    def __init__(self, location: str, paymentMethod: str) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        __class__._init_fields(self)
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
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil


def _PaymentGatewayPageData_NAME() -> object:
    from org.allbinary.logic.string.StringUtil import StringUtil
    return StringUtil.getInstance().EMPTY_STRING

lazy_static(PaymentGatewayPageData, "NAME", _PaymentGatewayPageData_NAME)

def _PaymentGatewayPageData_PAYMENTOPTIONS() -> object:
    return "PaymentOptions" + str(PaymentGatewayPageData.EXTENSION)

lazy_static(PaymentGatewayPageData, "PAYMENTOPTIONS", _PaymentGatewayPageData_PAYMENTOPTIONS)

def _PaymentGatewayPageData_STARTCHECKOUT() -> object:
    return "StartCheckout" + str(PaymentGatewayPageData.EXTENSION)

lazy_static(PaymentGatewayPageData, "STARTCHECKOUT", _PaymentGatewayPageData_STARTCHECKOUT)

