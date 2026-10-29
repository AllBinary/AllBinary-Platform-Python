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
# package org.allbinary.business.user.commerce.money.payment.gateway.transaction

from __future__ import annotations



class PaymentTransactionKeysFactory:
    instance: PaymentTransactionKeysFactory = None

    def _init_fields(self) -> None:
        self.TRXTYPE: PaymentTransactionKeys = PaymentTransactionKeys("TRXTYPE")
        self.TENDER: PaymentTransactionKeys = PaymentTransactionKeys("TENDER")
        self.ACCT: PaymentTransactionKeys = PaymentTransactionKeys("ACCT")
        self.EXPDATE: PaymentTransactionKeys = PaymentTransactionKeys("EXPDATE")
        self.AMT: PaymentTransactionKeys = PaymentTransactionKeys("AMT")
        self.AUTHCODE: PaymentTransactionKeys = PaymentTransactionKeys("AUTHCODE")
        self.MICR: PaymentTransactionKeys = PaymentTransactionKeys("MICR")
        self.CHECKNUM: PaymentTransactionKeys = PaymentTransactionKeys("CHECKNUM")
        self.NAME: PaymentTransactionKeys = PaymentTransactionKeys("NAME")
        self.STREET: PaymentTransactionKeys = PaymentTransactionKeys("STREET")
        self.CITY: PaymentTransactionKeys = PaymentTransactionKeys("CITY")
        self.STATE: PaymentTransactionKeys = PaymentTransactionKeys("STATE")
        self.ZIP: PaymentTransactionKeys = PaymentTransactionKeys("ZIP")
        self.DL: PaymentTransactionKeys = PaymentTransactionKeys("DL")
        self.EMAIL: PaymentTransactionKeys = PaymentTransactionKeys("EMAIL")
        self.COMMENT1: PaymentTransactionKeys = PaymentTransactionKeys("COMMENT1")
        self.COMMENT2: PaymentTransactionKeys = PaymentTransactionKeys("COMMENT2")
        self.ORIGID: PaymentTransactionKeys = PaymentTransactionKeys("ORIGID")
        self.PONUM: PaymentTransactionKeys = PaymentTransactionKeys("PONUM")
        self.DESC: PaymentTransactionKeys = PaymentTransactionKeys("PaymentTransactionDESC")
        self.DESC1TO4: PaymentTransactionKeys = PaymentTransactionKeys("DESC1TO4")
        self.INVNUM: PaymentTransactionKeys = PaymentTransactionKeys("INVNUM")
        self.SHIPTOZIP: PaymentTransactionKeys = PaymentTransactionKeys("SHIPTOZIP")
        self.SWIPE: PaymentTransactionKeys = PaymentTransactionKeys("SWIPE")
        self.TAXAMT: PaymentTransactionKeys = PaymentTransactionKeys("TAXAMT")
        self.COMMCARD: PaymentTransactionKeys = PaymentTransactionKeys("COMMCARD")
        self.DUTYAMT: PaymentTransactionKeys = PaymentTransactionKeys("DUTYAMT")
        self.FRIEGHTAMT: PaymentTransactionKeys = PaymentTransactionKeys("FRIEGHTAMT")
        self.ORDERDATE: PaymentTransactionKeys = PaymentTransactionKeys("ORDERDATE")
        self.TAXEXEMPT: PaymentTransactionKeys = PaymentTransactionKeys("TAXEXEMPT")
        self.COUNTRYCODE: PaymentTransactionKeys = PaymentTransactionKeys("COUNTRYCODE")
        self.CUSTCODE: PaymentTransactionKeys = PaymentTransactionKeys("CUSTCODE")
        self.CVV2: PaymentTransactionKeys = PaymentTransactionKeys("CVV2")
        self.ABA: PaymentTransactionKeys = PaymentTransactionKeys("ABA")
        self.ACCTTYPE: PaymentTransactionKeys = PaymentTransactionKeys("ACCTTYPE")
        self.DISCOUNT: PaymentTransactionKeys = PaymentTransactionKeys("DISCOUNT")
        self.FIRSTNAME: PaymentTransactionKeys = PaymentTransactionKeys("FIRSTNAME")
        self.LASTNAME: PaymentTransactionKeys = PaymentTransactionKeys("LASNAME")
        self.SHIPFROMZIP: PaymentTransactionKeys = PaymentTransactionKeys("SHIPFROMZIP")
        self.PRENOTE: PaymentTransactionKeys = PaymentTransactionKeys("PRENOTE")
        self.CHKTYPE: PaymentTransactionKeys = PaymentTransactionKeys("CHKTYPE")
        self.DOB: PaymentTransactionKeys = PaymentTransactionKeys("DOB")
        self.PHONENUM: PaymentTransactionKeys = PaymentTransactionKeys("PHONENUM")
        self.SS: PaymentTransactionKeys = PaymentTransactionKeys("SS")
        self.COMPANYNAME: PaymentTransactionKeys = PaymentTransactionKeys("COMPANYNAME")
        self.COUNTRY: PaymentTransactionKeys = PaymentTransactionKeys("COUNTRY")
        self.FREIGHTAMT: PaymentTransactionKeys = PaymentTransactionKeys("FREIGHTAMT")
        self.SHIPTOCITY: PaymentTransactionKeys = PaymentTransactionKeys("SHIPTOCITY")
        self.SHIPTOFIRSTNAME: PaymentTransactionKeys = PaymentTransactionKeys("SHIPTOFIRSTNAME")
        self.SHIPTOLASTNAME: PaymentTransactionKeys = PaymentTransactionKeys("SHIPTOLASTNAME")
        self.SHIPTOSTATE: PaymentTransactionKeys = PaymentTransactionKeys("SHIPTOSTATE")
        self.SHIPTOSTREET: PaymentTransactionKeys = PaymentTransactionKeys("SHIPTOSTREET")
        self.SPECIAL1: PaymentTransactionKeys = PaymentTransactionKeys("SPECIAL1")
        self.SPECIAL2: PaymentTransactionKeys = PaymentTransactionKeys("SPECIAL2")
        self.SPECIAL3: PaymentTransactionKeys = PaymentTransactionKeys("SPECIAL3")
        self.PARTNER: PaymentTransactionKeys = PaymentTransactionKeys("PARTNER")
        self.VENDOR: PaymentTransactionKeys = PaymentTransactionKeys("VENDOR")
        self.USER: PaymentTransactionKeys = PaymentTransactionKeys("USER")
        self.PWD: PaymentTransactionKeys = PaymentTransactionKeys("PWD")
        self.CHKNUM: PaymentTransactionKeys = PaymentTransactionKeys("CHKNUM")
        self.AVSADDR: PaymentTransactionKeys = PaymentTransactionKeys("AVSADDR")
        self.AVSZIP: PaymentTransactionKeys = PaymentTransactionKeys("AVSZIP")
        self.PNREF: PaymentTransactionKeys = PaymentTransactionKeys("PNREF")
        self.RESPMSG: PaymentTransactionKeys = PaymentTransactionKeys("RESPMSG")
        self.RESULT: PaymentTransactionKeys = PaymentTransactionKeys("RESULT")
        self.ORIGRESULT: PaymentTransactionKeys = PaymentTransactionKeys("ORIGRESULT")
        self.STATUS: PaymentTransactionKeys = PaymentTransactionKeys("STATUS")
        self.FRAUDCODE: PaymentTransactionKeys = PaymentTransactionKeys("FRAUDCODE")
        self.FRAUDMSG: PaymentTransactionKeys = PaymentTransactionKeys("FRAUDMSG")
        self.ERRCODE: PaymentTransactionKeys = PaymentTransactionKeys("ERRCODE")
        self.SCORE: PaymentTransactionKeys = PaymentTransactionKeys("SCORE")
        self.REASON1: PaymentTransactionKeys = PaymentTransactionKeys("REASON1")
        self.REASON2: PaymentTransactionKeys = PaymentTransactionKeys("REASON2")
        self.REASON3: PaymentTransactionKeys = PaymentTransactionKeys("REASON3")
        self.EXCEPTION1: PaymentTransactionKeys = PaymentTransactionKeys("EXCEPTION1")
        self.EXCEPTION2: PaymentTransactionKeys = PaymentTransactionKeys("EXCEPTION2")
        self.EXCEPTION3: PaymentTransactionKeys = PaymentTransactionKeys("EXCEPTION3")
        self.EXCEPTION4: PaymentTransactionKeys = PaymentTransactionKeys("EXCEPTION4")
        self.EXCEPTION5: PaymentTransactionKeys = PaymentTransactionKeys("EXCEPTION5")
        self.EXCEPTION6: PaymentTransactionKeys = PaymentTransactionKeys("EXCEPTION6")
        self.EXCEPTION7: PaymentTransactionKeys = PaymentTransactionKeys("EXCEPTION7")

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> PaymentTransactionKeysFactory:
        return PaymentTransactionKeysFactory.instance
from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeys import PaymentTransactionKeys


PaymentTransactionKeysFactory.instance = PaymentTransactionKeysFactory()

