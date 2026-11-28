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

from java.lang.JavaRuntimeStatic import java_bases
from org.allbinary.data.tree.dom.DomNodeInterface import DomNodeInterface
from org.allbinary.business.user.commerce.money.payment.PaymentInterface import PaymentInterface


class Payment(*java_bases(PaymentInterface, DomNodeInterface)):

    def _init_fields(self) -> None:
        if "name" not in vars(self): self.name: str = None
        if "expiration" not in vars(self): self.expiration: str = None
        if "encryption" not in vars(self): self.encryption: str = None
        if "number" not in vars(self): self.number: str = None
        if "id" not in vars(self): self.id: str = None
        if "type_" not in vars(self): self.type_: str = None
        if "tenderType" not in vars(self): self.tenderType: str = None
        if "transactionType" not in vars(self): self.transactionType: str = None
        if "aba" not in vars(self): self.aba: str = None
        if "account" not in vars(self): self.account: str = None
        if "accountType" not in vars(self): self.accountType: str = None
        if "authorizationCode" not in vars(self): self.authorizationCode: str = None
        if "checkNumber" not in vars(self): self.checkNumber: str = None
        if "checkType" not in vars(self): self.checkType: str = None
        if "driversLicense" not in vars(self): self.driversLicense: str = None
        if "magneticInkCheckReader" not in vars(self): self.magneticInkCheckReader: str = None
        self.isDefault_field: bool = False

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__.__jconstructor1(self, *args)
        elif len(args) == 0:
            __class__._constructor0(self, *args)

    def __jconstructor1(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)):
            __class__._constructor1_1(self, *args)
        else:
            __class__._constructor1_2(self, *args)
    

    def _constructor1_1(self, payment: HashMap) -> None:
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
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.logic.control.crypt.SuperCrypt import SuperCrypt
        __class__._init_fields(self)
        self.name = payment.get(PaymentData.NAME)
        self.type_ = payment.get(PaymentData.TYPE)
        self.expiration = payment.get(PaymentData.EXPIRATION)
        self.encryption = payment.get(EntryData.getInstance().ENCRYPTION)
        self.number = SuperCrypt(int(int(self.encryption))).decrypt(payment.get(PaymentData.NUMBER))
        self.id = payment.get(PaymentData.ID)
        def_: str = payment.get(EntryData.getInstance().DEFAULT)
        if def_ is not None and ((def_ > EntryData.getInstance().DEFAULT) - (def_ < EntryData.getInstance().DEFAULT)) == 0:
            self.isDefault_field = True
        else:
            self.isDefault_field = False
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
    

    def _constructor1_2(self, request: ServletRequest) -> None:
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
        __class__._init_fields(self)
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
        __class__._init_fields(self)
    

    def isValid(self) -> bool:
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.business.user.commerce.money.payment.types.CreditCardType import CreditCardType
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
        if len(self.number) > CreditCardType.MAXLEN:
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
        return self.isDefault_field
    

    def toHashMap(self) -> HashMap:
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
        from java.util.HashMap import HashMap
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.logic.StdUtil import StdUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        hashMap: HashMap = StdUtil.getInstance().createHashMap()
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
        if self.isDefault_field:
            hashMap.put(EntryData.getInstance().DEFAULT, EntryData.getInstance().DEFAULT)
        else:
            hashMap.put(EntryData.getInstance().DEFAULT, StringUtil.getInstance().EMPTY_STRING)
        return hashMap
    

    # throws Exception
    def toXmlNode(self, document: Document) -> Node:
        from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
        from java.util.HashMap import HashMap
        from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        hashMap: HashMap = self.toHashMap()
        node: Node = ModDomHelper.createNameValueNodes(document, PaymentData.PAYMENT, hashMap)
        return node
    

    def toXmlDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def view(self) -> str:
        return None
    

    def toValidationInfoDoc(self) -> Document:
        from org.w3c.dom.Document import Document
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        from org.w3c.dom.Document import Document
        from org.w3c.dom.Node import Node
        return None
    

    def validationInfo(self) -> str:
        return None
# from java.util.HashMap import HashMap
# from javax.servlet.ServletRequest import ServletRequest
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.data.tree.dom.ModDomHelper import ModDomHelper
# from org.allbinary.logic.StdUtil import StdUtil
# from org.allbinary.logic.control.crypt.SuperCrypt import SuperCrypt
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.w3c.dom.Document import Document
# from org.w3c.dom.Node import Node
# from org.allbinary.business.user.commerce.money.payment.types.CreditCardType import CreditCardType


