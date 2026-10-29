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
# package org.allbinary.business.user.commerce.money.payment

from __future__ import annotations

from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface


class Payment(PaymentInterface, DomNodeInterface):

    def _init_fields(self) -> None:
        self.name: str = None
        self.expiration: str = None
        self.encryption: str = None
        self.number: str = None
        self.id: str = None
        self.type_: str = None
        self.tenderType: str = None
        self.transactionType: str = None
        self.aba: str = None
        self.account: str = None
        self.accountType: str = None
        self.authorizationCode: str = None
        self.checkNumber: str = None
        self.checkType: str = None
        self.driversLicense: str = None
        self.magneticInkCheckReader: str = None
        self.isDefault: bool = False

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 0:
            self._constructor0(*args)
    

    def _constructor1(self, payment: dict) -> None:
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        self._init_fields()
        self.name = payment.get(PaymentData.NAME)
        self.type_ = payment.get(PaymentData.TYPE)
        self.expiration = payment.get(PaymentData.EXPIRATION)
        self.encryption = payment.get(EntryData.getInstance().ENCRYPTION)
        self.number = SuperCrypt(int(int(self.encryption))).decrypt(payment.get(PaymentData.NUMBER))
        self.id = payment.get(PaymentData.ID)
        def_: str = payment.get(EntryData.getInstance().DEFAULT)
        if def_ is not None and ((def_ > EntryData.getInstance().DEFAULT) - (def_ < EntryData.getInstance().DEFAULT)) == 0:
            self.isDefault = True
        else:
            self.isDefault = False
        self.tenderType = payment.get(PaymentData.TENDERTYPE)
        self.transactionType = payment.get(PaymentData.TRANSACTIONTYPE)
        self.aba = payment.get(PaymentData.ABA)
        self.account = payment.get(PaymentData.ACCOUNT)
        self.accountType = payment.get(PaymentData.ACCOUNTTYPE)
        self.authorizationCode = payment.get(PaymentData.AUTHORIZATIONCODE)
        self.checkNumber = payment.get(PaymentData.CHECKNUMBER)
        self.checkType = payment.get(PaymentData.CHECKTYPE)
        self.driversLicense = payment.get(PaymentData.DRIVERSLICENSE)
        self.magneticInkCheckReader = payment.get(PaymentData.MAGNETICINKCHECKREADER)
    

    def _constructor1(self, request: ServletRequest) -> None:
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        self._init_fields()
        self.name = request.getParameter(PaymentData.NAME)
        self.type_ = request.getParameter(PaymentData.TYPE)
        self.expiration = request.getParameter(PaymentData.EXPIRATION)
        self.number = request.getParameter(PaymentData.NUMBER)
        self.tenderType = request.getParameter(PaymentData.TENDERTYPE)
        self.transactionType = request.getParameter(PaymentData.TRANSACTIONTYPE)
        self.aba = request.getParameter(PaymentData.ABA)
        self.account = request.getParameter(PaymentData.ACCOUNT)
        self.accountType = request.getParameter(PaymentData.ACCOUNTTYPE)
        self.authorizationCode = request.getParameter(PaymentData.AUTHORIZATIONCODE)
        self.checkNumber = request.getParameter(PaymentData.CHECKNUMBER)
        self.checkType = request.getParameter(PaymentData.CHECKTYPE)
        self.driversLicense = request.getParameter(PaymentData.DRIVERSLICENSE)
        self.magneticInkCheckReader = request.getParameter(PaymentData.MAGNETICINKCHECKREADER)
    

    def _constructor0(self) -> None:
        self._init_fields()
    

    def isValid(self) -> bool:
        stringUtil: StringUtil = StringUtil.getInstance()
        aFalse: bool = False
        if self.name is None or ((self.name > stringUtil.EMPTY_STRING) - (self.name < stringUtil.EMPTY_STRING)) == 0:
            return aFalse
        if self.type_ is None or ((self.type_ > stringUtil.EMPTY_STRING) - (self.type_ < stringUtil.EMPTY_STRING)) == 0:
            return aFalse
        if self.expiration is None or ((self.expiration > stringUtil.EMPTY_STRING) - (self.expiration < stringUtil.EMPTY_STRING)) == 0:
            return aFalse
        if self.number is None or ((self.number > stringUtil.EMPTY_STRING) - (self.number < stringUtil.EMPTY_STRING)) == 0:
            return aFalse
        if len(self.number) > org.allbinary.business.user.commerce.money.payment.types.CreditCardType.MAXLEN:
            return aFalse
        return True
    

    def setTenderType(self, value: str) -> None:
        self.tenderType = value
    

    def setTransactionType(self, value: str) -> None:
        self.transactionType = value
    

    def setAuthorizationCode(self, value: str) -> None:
        self.authorizationCode = value
    

    def setCheckType(self, value: str) -> None:
        self.checkType = value
    

    def setCheckNumber(self, value: str) -> None:
        self.checkNumber = value
    

    def setDriversLicense(self, value: str) -> None:
        self.driversLicense = value
    

    def setMagneticInkCheckReader(self, value: str) -> None:
        self.magneticInkCheckReader = value
    

    def setAba(self, value: str) -> None:
        self.aba = value
    

    def setAccountType(self, value: str) -> None:
        self.accountType = value
    

    def setName(self, value: str) -> None:
        self.name = value
    

    def setType(self, value: str) -> None:
        self.type_ = value
    

    def setExpiration(self, value: str) -> None:
        self.expiration = value
    

    def setNumber(self, value: str) -> None:
        self.number = value
    

    def getId(self) -> str:
        return self.id
    

    def getName(self) -> str:
        return self.name
    

    def getType(self) -> str:
        return self.type_
    

    def getExpiration(self) -> str:
        return self.expiration
    

    def getEncryption(self) -> str:
        return self.encryption
    

    def getNumber(self) -> str:
        return self.number
    

    def getTenderType(self) -> str:
        return self.tenderType
    

    def getTransactionType(self) -> str:
        return self.transactionType
    

    def getAba(self) -> str:
        return self.aba
    

    def getAccount(self) -> str:
        return self.account
    

    def getAccountType(self) -> str:
        return self.accountType
    

    def getAuthorizationCode(self) -> str:
        return self.authorizationCode
    

    def getCheckNumber(self) -> str:
        return self.checkNumber
    

    def getCheckType(self) -> str:
        return self.checkType
    

    def getDriversLicense(self) -> str:
        return self.driversLicense
    

    def getMagneticInkCheckReader(self) -> str:
        return self.magneticInkCheckReader
    

    def getLastFour(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        if len(self.number) > PaymentData.MIN and len(self.number) <= PaymentData.MAX:
            return self.number[len(self.number) - 4:]
        else:
            return "Invalid #"
    

    def isDefault(self) -> bool:
        return self.isDefault
    

    def toHashMap(self) -> dict:
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        hashMap: dict = StdUtil.getInstance().createHashMap()
        hashMap.put(PaymentData.NAME, self.name)
        hashMap.put(PaymentData.TYPE, self.type_)
        hashMap.put(PaymentData.EXPIRATION, self.expiration)
        hashMap.put(PaymentData.NUMBER, self.getLastFour())
        hashMap.put(PaymentData.TENDERTYPE, self.tenderType)
        hashMap.put(PaymentData.TRANSACTIONTYPE, self.transactionType)
        hashMap.put(PaymentData.ABA, self.aba)
        hashMap.put(PaymentData.ACCOUNT, self.account)
        hashMap.put(PaymentData.ACCOUNTTYPE, self.accountType)
        hashMap.put(PaymentData.AUTHORIZATIONCODE, self.authorizationCode)
        hashMap.put(PaymentData.CHECKNUMBER, self.checkNumber)
        hashMap.put(PaymentData.DRIVERSLICENSE, self.driversLicense)
        hashMap.put(PaymentData.MAGNETICINKCHECKREADER, self.magneticInkCheckReader)
        if self.isDefault:
            hashMap.put(EntryData.getInstance().DEFAULT, EntryData.getInstance().DEFAULT)
        else:
            hashMap.put(EntryData.getInstance().DEFAULT, StringUtil.getInstance().EMPTY_STRING)
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        hashMap: dict = self.toHashMap()
        node: Node = ModDomHelper.createNameValueNodes(document, PaymentData.PAYMENT, hashMap)
        return node
    

    def toXmlDoc(self) -> Document:
        return None
    

    def view(self) -> str:
        return None
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    def validationInfo(self) -> str:
        return None
# from java.util.HashMap import HashMap
# from javax.servlet.ServletRequest import ServletRequest
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.control.crypt.SuperCrypt import SuperCrypt
from org.allbinary.logic.string.StringUtil import StringUtil
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


