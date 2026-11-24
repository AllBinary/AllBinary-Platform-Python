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


def _PaymentGatewayData_ID() -> object:
    return PaymentGatewayData("PAYMENTGATEWAY_ID")

lazy_static(PaymentGatewayData, "ID", _PaymentGatewayData_ID)

def _PaymentGatewayData_NAME() -> object:
    return PaymentGatewayData("PAYMENTGATEWAY_NAME")

lazy_static(PaymentGatewayData, "NAME", _PaymentGatewayData_NAME)

def _PaymentGatewayData_VALUE() -> object:
    return PaymentGatewayData("PAYMENTGATEWAY_VALUE")

lazy_static(PaymentGatewayData, "VALUE", _PaymentGatewayData_VALUE)

def _PaymentGatewayData_PAYMENTTRANSACTIONINTERFACEFACTORYINTERFACE() -> object:
    return PaymentGatewayData("PAYMENTGATEWAY_PAYMENTTRANSACTIONINTERFACEFACTORYINTERFACE")

lazy_static(PaymentGatewayData, "PAYMENTTRANSACTIONINTERFACEFACTORYINTERFACE", _PaymentGatewayData_PAYMENTTRANSACTIONINTERFACEFACTORYINTERFACE)

def _PaymentGatewayData_PAYMENTPROCESSORINTERFACEFACTORYINTERFACE() -> object:
    return PaymentGatewayData("PAYMENTGATEWAY_PAYMENTPROCESSORINTERFACEFACTORYINTERFACE")

lazy_static(PaymentGatewayData, "PAYMENTPROCESSORINTERFACEFACTORYINTERFACE", _PaymentGatewayData_PAYMENTPROCESSORINTERFACEFACTORYINTERFACE)

def _PaymentGatewayData_MODE() -> object:
    return PaymentGatewayData("MODE")

lazy_static(PaymentGatewayData, "MODE", _PaymentGatewayData_MODE)

def _PaymentGatewayData_SERVERPROTOCOL() -> object:
    return PaymentGatewayData("SERVERPROTOCOL")

lazy_static(PaymentGatewayData, "SERVERPROTOCOL", _PaymentGatewayData_SERVERPROTOCOL)

def _PaymentGatewayData_SERVER() -> object:
    return PaymentGatewayData("SERVER")

lazy_static(PaymentGatewayData, "SERVER", _PaymentGatewayData_SERVER)

def _PaymentGatewayData_SERVERPORT() -> object:
    return PaymentGatewayData("SERVERPORT")

lazy_static(PaymentGatewayData, "SERVERPORT", _PaymentGatewayData_SERVERPORT)

def _PaymentGatewayData_SERVERPATH() -> object:
    return PaymentGatewayData("SERVERPATH")

lazy_static(PaymentGatewayData, "SERVERPATH", _PaymentGatewayData_SERVERPATH)

def _PaymentGatewayData_TESTPROTOCOL() -> object:
    return PaymentGatewayData("TESTSERVERPROTOCOL")

lazy_static(PaymentGatewayData, "TESTPROTOCOL", _PaymentGatewayData_TESTPROTOCOL)

def _PaymentGatewayData_TESTSERVER() -> object:
    return PaymentGatewayData("TESTSERVER")

lazy_static(PaymentGatewayData, "TESTSERVER", _PaymentGatewayData_TESTSERVER)

def _PaymentGatewayData_TESTPORT() -> object:
    return PaymentGatewayData("TESTPORT")

lazy_static(PaymentGatewayData, "TESTPORT", _PaymentGatewayData_TESTPORT)

def _PaymentGatewayData_TESTPATH() -> object:
    return PaymentGatewayData("TESTSERVERPATH")

lazy_static(PaymentGatewayData, "TESTPATH", _PaymentGatewayData_TESTPATH)

def _PaymentGatewayData_TIMEOUT() -> object:
    return PaymentGatewayData("TIMEOUT")

lazy_static(PaymentGatewayData, "TIMEOUT", _PaymentGatewayData_TIMEOUT)

def _PaymentGatewayData_PROXYPROTOCOL() -> object:
    return PaymentGatewayData("PROXYPROTOCOL")

lazy_static(PaymentGatewayData, "PROXYPROTOCOL", _PaymentGatewayData_PROXYPROTOCOL)

def _PaymentGatewayData_PROXYSERVER() -> object:
    return PaymentGatewayData("PROXYSERVER")

lazy_static(PaymentGatewayData, "PROXYSERVER", _PaymentGatewayData_PROXYSERVER)

def _PaymentGatewayData_PROXYPATH() -> object:
    return PaymentGatewayData("PROXYPATH")

lazy_static(PaymentGatewayData, "PROXYPATH", _PaymentGatewayData_PROXYPATH)

def _PaymentGatewayData_PROXYUSERNAME() -> object:
    return PaymentGatewayData("PROXYUSERNAME")

lazy_static(PaymentGatewayData, "PROXYUSERNAME", _PaymentGatewayData_PROXYUSERNAME)

def _PaymentGatewayData_PROXYPASSWORD() -> object:
    return PaymentGatewayData("PROXYPASSWORD")

lazy_static(PaymentGatewayData, "PROXYPASSWORD", _PaymentGatewayData_PROXYPASSWORD)

def _PaymentGatewayData_PROXYPORT() -> object:
    return PaymentGatewayData("PROXYPORT")

lazy_static(PaymentGatewayData, "PROXYPORT", _PaymentGatewayData_PROXYPORT)

def _PaymentGatewayData_PROXYTIMEOUT() -> object:
    return PaymentGatewayData("PROXYTIMEOUT")

lazy_static(PaymentGatewayData, "PROXYTIMEOUT", _PaymentGatewayData_PROXYTIMEOUT)

def _PaymentGatewayData_SPECIAL1() -> object:
    return PaymentGatewayData("SPECIAL1")

lazy_static(PaymentGatewayData, "SPECIAL1", _PaymentGatewayData_SPECIAL1)

def _PaymentGatewayData_SPECIAL2() -> object:
    return PaymentGatewayData("SPECIAL2")

lazy_static(PaymentGatewayData, "SPECIAL2", _PaymentGatewayData_SPECIAL2)

def _PaymentGatewayData_SPECIAL3() -> object:
    return PaymentGatewayData("SPECIAL3")

lazy_static(PaymentGatewayData, "SPECIAL3", _PaymentGatewayData_SPECIAL3)

def _PaymentGatewayData_SPECIAL4() -> object:
    return PaymentGatewayData("SPECIAL4")

lazy_static(PaymentGatewayData, "SPECIAL4", _PaymentGatewayData_SPECIAL4)

def _PaymentGatewayData_SPECIAL5() -> object:
    return PaymentGatewayData("SPECIAL5")

lazy_static(PaymentGatewayData, "SPECIAL5", _PaymentGatewayData_SPECIAL5)

def _PaymentGatewayData_SPECIAL6() -> object:
    return PaymentGatewayData("SPECIAL6")

lazy_static(PaymentGatewayData, "SPECIAL6", _PaymentGatewayData_SPECIAL6)

def _PaymentGatewayData_SPECIAL7() -> object:
    return PaymentGatewayData("SPECIAL7")

lazy_static(PaymentGatewayData, "SPECIAL7", _PaymentGatewayData_SPECIAL7)

def _PaymentGatewayData_SPECIAL8() -> object:
    return PaymentGatewayData("SPECIAL8")

lazy_static(PaymentGatewayData, "SPECIAL8", _PaymentGatewayData_SPECIAL8)

def _PaymentGatewayData_SPECIAL9() -> object:
    return PaymentGatewayData("SPECIAL9")

lazy_static(PaymentGatewayData, "SPECIAL9", _PaymentGatewayData_SPECIAL9)

