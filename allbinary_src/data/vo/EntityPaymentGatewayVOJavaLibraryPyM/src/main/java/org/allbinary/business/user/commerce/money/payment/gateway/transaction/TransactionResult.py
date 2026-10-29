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

from org.allbinary.business.user.commerce.money.payment.gateway.transaction.TransactionResultInterface import TransactionResultInterface


class TransactionResult(TransactionResultInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.keyValuePairs: dict = None
        self.result: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor1(self, result: str) -> None:
        self._init_fields()
        try:
            self.result = result
            tokenizer: Tokenizer = Tokenizer(CommonSeps.getInstance().AMPERSAND)
            tokens: BasicArrayList = tokenizer.getTokensFromString(result, BasicArrayListD())
            tokenizer2: Tokenizer = Tokenizer(CommonSeps.getInstance().EQUALS)
            hashtable: ABHashtable[object, object] = tokenizer2.getTokens(tokens)
            self.keyValuePairs.putAll(hashtable)
        except Exception as e:
            exceptionMessage: str = "TransactionResult Constructor Failed"
            self.logUtil.putF(exceptionMessage, self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor1(self, keyValuePairs: dict) -> None:
        self._init_fields()
        keyValuePairs = keyValuePairs
        self.result = "Needs to have the hashmap converted to string for other constructor"
    

    def toString(self) -> str:
        return self.result

    def __str__(self) -> str:
        return self.toString()
    

    def toHashMap(self) -> dict:
        return self.keyValuePairs
    

    def getAllPossibleKeys(self) -> BasicArrayList:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        paymentTransactionKeysFactory: PaymentTransactionKeysFactory = PaymentTransactionKeysFactory.getInstance()
        verisignResponseKeys: BasicArrayList = BasicArrayListD()
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.RESULT))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.PNREF))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.RESPMSG))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.AUTHCODE))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.AVSADDR))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.AVSZIP))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.ORIGRESULT))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.STATUS))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.FRAUDCODE))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.FRAUDMSG))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.ERRCODE))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.SCORE))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.REASON1))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.REASON2))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.REASON3))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.EXCEPTION1))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.EXCEPTION2))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.EXCEPTION3))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.EXCEPTION4))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.EXCEPTION5))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.EXCEPTION6))
        verisignResponseKeys.add(str(paymentTransactionKeysFactory.EXCEPTION7))
        return verisignResponseKeys
    

    def getValues(self) -> BasicArrayList:
        keyVector: BasicArrayList = self.getAllPossibleKeys()
        valueVector: BasicArrayList = BasicArrayListD()
        size: int = keyVector.size()
        for i in range(0, size):
            key: str = keyVector.get(i)
            if self.keyValuePairs.containsKey(key):
                valueVector.add(self.keyValuePairs.get(key))
            else:
                stringUtil: StringUtil = StringUtil.getInstance()
                valueVector.add(stringUtil.EMPTY_STRING)
        return valueVector
    

    def getPnRef(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().PNREF))
    

    def getRespMsg(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().RESPMSG))
    

    def getResult(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().RESULT))
    

    def getScore(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().SCORE))
    

    def getStatus(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().STATUS))
    

    def getFraudCode(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().FRAUDCODE))
    

    def getFraudMsg(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().FRAUDMSG))
    

    def getOrigResult(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().ORIGRESULT))
    

    def getAvsAddr(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().AVSADDR))
    

    def getAvsZip(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().AVSZIP))
    

    def getErrCode(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().ERRCODE))
    

    def getException1(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().EXCEPTION1))
    

    def getException2(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().EXCEPTION2))
    

    def getException3(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().EXCEPTION3))
    

    def getException4(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().EXCEPTION4))
    

    def getException5(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().EXCEPTION5))
    

    def getException6(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().EXCEPTION6))
    

    def getException7(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().EXCEPTION7))
    

    def getReason1(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().REASON1))
    

    def getReason2(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().REASON2))
    

    def getReason3(self) -> str:
        from org.allbinary.business.user.commerce.money.payment.gateway.transaction.PaymentTransactionKeysFactory import PaymentTransactionKeysFactory
        return self.keyValuePairs.get(str(PaymentTransactionKeysFactory.getInstance().REASON3))
# from java.util.HashMap import HashMap
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.tokens.Tokenizer import Tokenizer
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.ABHashtable import ABHashtable
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


