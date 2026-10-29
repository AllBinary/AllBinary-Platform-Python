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



class PaymentGatewayData:
    CRYPTNUM: int = 5
    ID: PaymentGatewayData = None
    NAME: PaymentGatewayData = None
    VALUE: PaymentGatewayData = None
    PAYMENTTRANSACTIONINTERFACEFACTORYINTERFACE: PaymentGatewayData = None
    PAYMENTPROCESSORINTERFACEFACTORYINTERFACE: PaymentGatewayData = None
    MODE: PaymentGatewayData = None
    SERVERPROTOCOL: PaymentGatewayData = None
    SERVER: PaymentGatewayData = None
    SERVERPORT: PaymentGatewayData = None
    SERVERPATH: PaymentGatewayData = None
    TESTPROTOCOL: PaymentGatewayData = None
    TESTSERVER: PaymentGatewayData = None
    TESTPORT: PaymentGatewayData = None
    TESTPATH: PaymentGatewayData = None
    TIMEOUT: PaymentGatewayData = None
    PROXYPROTOCOL: PaymentGatewayData = None
    PROXYSERVER: PaymentGatewayData = None
    PROXYPATH: PaymentGatewayData = None
    PROXYUSERNAME: PaymentGatewayData = None
    PROXYPASSWORD: PaymentGatewayData = None
    PROXYPORT: PaymentGatewayData = None
    PROXYTIMEOUT: PaymentGatewayData = None
    SPECIAL1: PaymentGatewayData = None
    SPECIAL2: PaymentGatewayData = None
    SPECIAL3: PaymentGatewayData = None
    SPECIAL4: PaymentGatewayData = None
    SPECIAL5: PaymentGatewayData = None
    SPECIAL6: PaymentGatewayData = None
    SPECIAL7: PaymentGatewayData = None
    SPECIAL8: PaymentGatewayData = None
    SPECIAL9: PaymentGatewayData = None

    def _init_fields(self) -> None:
        self.key: str = None
    

    def __init__(self, value: str) -> None:
        self._init_fields()
        self.key = value
    

    def toString(self) -> str:
        return self.key

    def __str__(self) -> str:
        return self.toString()


PaymentGatewayData.ID = PaymentGatewayData("PAYMENTGATEWAY_ID")

PaymentGatewayData.NAME = PaymentGatewayData("PAYMENTGATEWAY_NAME")

PaymentGatewayData.VALUE = PaymentGatewayData("PAYMENTGATEWAY_VALUE")

PaymentGatewayData.PAYMENTTRANSACTIONINTERFACEFACTORYINTERFACE = PaymentGatewayData("PAYMENTGATEWAY_PAYMENTTRANSACTIONINTERFACEFACTORYINTERFACE")

PaymentGatewayData.PAYMENTPROCESSORINTERFACEFACTORYINTERFACE = PaymentGatewayData("PAYMENTGATEWAY_PAYMENTPROCESSORINTERFACEFACTORYINTERFACE")

PaymentGatewayData.MODE = PaymentGatewayData("MODE")

PaymentGatewayData.SERVERPROTOCOL = PaymentGatewayData("SERVERPROTOCOL")

PaymentGatewayData.SERVER = PaymentGatewayData("SERVER")

PaymentGatewayData.SERVERPORT = PaymentGatewayData("SERVERPORT")

PaymentGatewayData.SERVERPATH = PaymentGatewayData("SERVERPATH")

PaymentGatewayData.TESTPROTOCOL = PaymentGatewayData("TESTSERVERPROTOCOL")

PaymentGatewayData.TESTSERVER = PaymentGatewayData("TESTSERVER")

PaymentGatewayData.TESTPORT = PaymentGatewayData("TESTPORT")

PaymentGatewayData.TESTPATH = PaymentGatewayData("TESTSERVERPATH")

PaymentGatewayData.TIMEOUT = PaymentGatewayData("TIMEOUT")

PaymentGatewayData.PROXYPROTOCOL = PaymentGatewayData("PROXYPROTOCOL")

PaymentGatewayData.PROXYSERVER = PaymentGatewayData("PROXYSERVER")

PaymentGatewayData.PROXYPATH = PaymentGatewayData("PROXYPATH")

PaymentGatewayData.PROXYUSERNAME = PaymentGatewayData("PROXYUSERNAME")

PaymentGatewayData.PROXYPASSWORD = PaymentGatewayData("PROXYPASSWORD")

PaymentGatewayData.PROXYPORT = PaymentGatewayData("PROXYPORT")

PaymentGatewayData.PROXYTIMEOUT = PaymentGatewayData("PROXYTIMEOUT")

PaymentGatewayData.SPECIAL1 = PaymentGatewayData("SPECIAL1")

PaymentGatewayData.SPECIAL2 = PaymentGatewayData("SPECIAL2")

PaymentGatewayData.SPECIAL3 = PaymentGatewayData("SPECIAL3")

PaymentGatewayData.SPECIAL4 = PaymentGatewayData("SPECIAL4")

PaymentGatewayData.SPECIAL5 = PaymentGatewayData("SPECIAL5")

PaymentGatewayData.SPECIAL6 = PaymentGatewayData("SPECIAL6")

PaymentGatewayData.SPECIAL7 = PaymentGatewayData("SPECIAL7")

PaymentGatewayData.SPECIAL8 = PaymentGatewayData("SPECIAL8")

PaymentGatewayData.SPECIAL9 = PaymentGatewayData("SPECIAL9")

