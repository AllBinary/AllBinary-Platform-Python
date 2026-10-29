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

from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayInterface import PaymentGatewayInterface


class PaymentGateway(PaymentGatewayInterface):

    def _init_fields(self) -> None:
        self.storeName: str = None
        self.name: str = None
        self.enable: str = None
        self.paymentMethod: str = None
        self.mode: str = None
        self.testProtocol: str = None
        self.testServer: str = None
        self.testPort: str = None
        self.testPath: str = None
        self.serverProtocol: str = None
        self.server: str = None
        self.serverPort: str = None
        self.serverPath: str = None
        self.timeout: str = None
        self.userName: str = None
        self.password: str = None
        self.proxyProtocol: str = None
        self.proxyServer: str = None
        self.proxyPort: str = None
        self.proxyPath: str = None
        self.proxyUserName: str = None
        self.proxyPassword: str = None
        self.proxyTimeout: str = None
        self.special1: str = None
        self.special2: str = None
        self.special3: str = None
        self.special4: str = None
        self.special5: str = None
        self.special6: str = None
        self.special7: str = None
        self.special8: str = None
        self.special9: str = None
        self.lastModified: str = None
        self.timeEntered: str = None
    

    def __init__(self, hashMap: dict) -> None:
        self._init_fields()
        self.getFormData(hashMap)
    

    def getFormData(self, hashMap: dict) -> None:
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        stringUtil: StringUtil = StringUtil.getInstance()
        empty: str = stringUtil.EMPTY_STRING
        self.storeName = hashMap.get(str(StoreFrontData.getInstance().NAME))
        self.name = hashMap.get(str(PaymentGatewayData.NAME))
        self.enable = stringUtil.getNonNull(hashMap.get(str(EntryData.getInstance().ENABLE)))
        self.paymentMethod = stringUtil.getNonNull(hashMap.get(str(PaymentData.METHOD)))
        self.mode = stringUtil.getNonNull(hashMap.get(str(PaymentGatewayData.MODE)))
        self.testProtocol = stringUtil.getNonNull(hashMap.get(str(PaymentGatewayData.TESTPROTOCOL)))
        self.testServer = stringUtil.getNonNull(hashMap.get(str(PaymentGatewayData.TESTSERVER)))
        self.testPort = stringUtil.getNonNull(hashMap.get(str(PaymentGatewayData.TESTPORT)))
        self.testPath = hashMap.get(str(PaymentGatewayData.TESTPATH))
        if self.testPath is None:
            self.testPath = empty
        self.serverProtocol = hashMap.get(str(PaymentGatewayData.SERVERPROTOCOL))
        if self.serverProtocol is None:
            self.serverProtocol = empty
        self.server = hashMap.get(str(PaymentGatewayData.SERVER))
        if self.server is None:
            self.server = empty
        self.serverPort = hashMap.get(str(PaymentGatewayData.SERVERPORT))
        if self.serverPort is None:
            self.serverPort = empty
        self.serverPath = hashMap.get(str(PaymentGatewayData.SERVERPATH))
        if self.serverPath is None:
            self.serverPath = empty
        self.userName = hashMap.get(str(UserData.USERNAME))
        if self.userName is None:
            self.userName = empty
        self.password = hashMap.get(str(UserData.PASSWORD))
        if self.password is None:
            self.password = empty
        self.timeout = hashMap.get(str(PaymentGatewayData.TIMEOUT))
        if self.timeout is None:
            self.timeout = empty
        self.proxyProtocol = hashMap.get(str(PaymentGatewayData.PROXYPROTOCOL))
        if self.proxyProtocol is None:
            self.proxyProtocol = empty
        self.proxyServer = hashMap.get(str(PaymentGatewayData.PROXYSERVER))
        if self.proxyServer is None:
            self.proxyServer = empty
        self.proxyPort = hashMap.get(str(PaymentGatewayData.PROXYPORT))
        if self.proxyPort is None:
            self.proxyPort = empty
        self.proxyPath = hashMap.get(str(PaymentGatewayData.PROXYPATH))
        if self.proxyPath is None:
            self.proxyPath = empty
        self.proxyUserName = hashMap.get(str(PaymentGatewayData.PROXYUSERNAME))
        if self.proxyUserName is None:
            self.proxyUserName = empty
        self.proxyPassword = hashMap.get(str(PaymentGatewayData.PROXYPASSWORD))
        if self.proxyPassword is None:
            self.proxyPassword = empty
        self.proxyTimeout = hashMap.get(str(PaymentGatewayData.PROXYTIMEOUT))
        if self.proxyTimeout is None:
            self.proxyTimeout = empty
        self.special1 = hashMap.get(str(PaymentGatewayData.SPECIAL1))
        if self.special1 is None:
            self.special1 = empty
        self.special2 = hashMap.get(str(PaymentGatewayData.SPECIAL2))
        if self.special2 is None:
            self.special2 = empty
        self.special3 = hashMap.get(str(PaymentGatewayData.SPECIAL3))
        if self.special3 is None:
            self.special3 = empty
        self.special4 = hashMap.get(str(PaymentGatewayData.SPECIAL4))
        if self.special4 is None:
            self.special4 = empty
        self.special5 = hashMap.get(str(PaymentGatewayData.SPECIAL5))
        if self.special5 is None:
            self.special5 = empty
        self.special6 = hashMap.get(str(PaymentGatewayData.SPECIAL6))
        if self.special6 is None:
            self.special6 = empty
        self.special7 = hashMap.get(str(PaymentGatewayData.SPECIAL7))
        if self.special7 is None:
            self.special7 = empty
        self.special8 = hashMap.get(str(PaymentGatewayData.SPECIAL8))
        if self.special8 is None:
            self.special8 = empty
        self.special9 = hashMap.get(str(PaymentGatewayData.SPECIAL9))
        if self.special9 is None:
            self.special9 = empty
        self.lastModified = hashMap.get(str(EntryData.getInstance().LASTMODIFIED))
        if self.lastModified is None:
            self.lastModified = empty
        self.timeEntered = hashMap.get(str(EntryData.getInstance().TIMECREATED))
        if self.timeEntered is None:
            self.timeEntered = empty
    

    def getStoreName(self) -> str:
        return self.storeName
    

    def getName(self) -> str:
        return self.name
    

    def getEnable(self) -> str:
        return self.enable
    

    def getPaymentMethod(self) -> str:
        return self.paymentMethod
    

    def getMode(self) -> str:
        return self.mode
    

    def getTestProtocol(self) -> str:
        return self.testProtocol
    

    def getTestServer(self) -> str:
        return self.testServer
    

    def getTestPort(self) -> str:
        return self.testPort
    

    def getTestPath(self) -> str:
        return self.testPath
    

    def getServerProtocol(self) -> str:
        return self.serverProtocol
    

    def getServer(self) -> str:
        return self.server
    

    def getServerPort(self) -> str:
        return self.serverPort
    

    def getServerPath(self) -> str:
        return self.serverPath
    

    def getUserName(self) -> str:
        return self.userName
    

    def getPassword(self) -> str:
        return self.password
    

    def getProxyProtocol(self) -> str:
        return self.proxyProtocol
    

    def getProxyServer(self) -> str:
        return self.proxyServer
    

    def getProxyPath(self) -> str:
        return self.proxyPath
    

    def getProxyPort(self) -> str:
        return self.proxyPort
    

    def getProxyUserName(self) -> str:
        return self.proxyUserName
    

    def getProxyPassword(self) -> str:
        return self.proxyPassword
    

    def getTimeout(self) -> str:
        return self.timeout
    

    def getProxyTimeout(self) -> str:
        return self.proxyTimeout
    

    def getSpecial1(self) -> str:
        return self.special1
    

    def getSpecial2(self) -> str:
        return self.special2
    

    def getSpecial3(self) -> str:
        return self.special3
    

    def getSpecial4(self) -> str:
        return self.special4
    

    def getSpecial5(self) -> str:
        return self.special5
    

    def getSpecial6(self) -> str:
        return self.special6
    

    def getSpecial7(self) -> str:
        return self.special7
    

    def getSpecial8(self) -> str:
        return self.special8
    

    def getSpecial9(self) -> str:
        return self.special9
    

    def getLastModified(self) -> str:
        return self.lastModified
    

    def getTimeEntered(self) -> str:
        return self.timeEntered
    

    def setEnable(self, value: str) -> None:
        self.enable = value
    

    def setStoreName(self, value: str) -> None:
        self.storeName = value
    

    def setName(self, value: str) -> None:
        self.name = value
    

    def setPaymentMethod(self, value: str) -> None:
        self.paymentMethod = value
    

    def setMode(self, value: str) -> None:
        self.mode = value
    

    def setTestProtocol(self, value: str) -> None:
        self.testProtocol = value
    

    def setTestServer(self, value: str) -> None:
        self.testServer = value
    

    def setTestPort(self, value: str) -> None:
        self.testPort = value
    

    def setTestPath(self, value: str) -> None:
        self.testPath = value
    

    def setServerProtocol(self, value: str) -> None:
        self.serverProtocol = value
    

    def setServer(self, value: str) -> None:
        self.server = value
    

    def setServerPort(self, value: str) -> None:
        self.serverPort = value
    

    def setServerPath(self, value: str) -> None:
        self.serverPath = value
    

    def setTimeout(self, value: str) -> None:
        self.timeout = value
    

    def setUserName(self, value: str) -> None:
        self.userName = value
    

    def setPassword(self, value: str) -> None:
        self.password = value
    

    def setProxyProtocol(self, value: str) -> None:
        self.proxyProtocol = value
    

    def setProxyServer(self, value: str) -> None:
        self.proxyServer = value
    

    def setProxyPort(self, value: str) -> None:
        self.proxyPort = value
    

    def setProxyPath(self, value: str) -> None:
        self.proxyPath = value
    

    def setProxyUserName(self, value: str) -> None:
        self.proxyUserName = value
    

    def setProxyPassword(self, value: str) -> None:
        self.proxyPassword = value
    

    def setProxyTimeout(self, value: str) -> None:
        self.proxyTimeout = value
    

    def setSpecial1(self, value: str) -> None:
        self.special1 = value
    

    def setSpecial2(self, value: str) -> None:
        self.special2 = value
    

    def setSpecial3(self, value: str) -> None:
        self.special3 = value
    

    def setSpecial4(self, value: str) -> None:
        self.special4 = value
    

    def setSpecial5(self, value: str) -> None:
        self.special5 = value
    

    def setSpecial6(self, value: str) -> None:
        self.special6 = value
    

    def setSpecial7(self, value: str) -> None:
        self.special7 = value
    

    def setSpecial8(self, value: str) -> None:
        self.special8 = value
    

    def setSpecial9(self, value: str) -> None:
        self.special9 = value
    

    def setLastModified(self, value: str) -> None:
        self.lastModified = value
    

    def setTimeEntered(self, value: str) -> None:
        self.timeEntered = value
    

    # throws Exception
    def toHashMap(self) -> dict:
        return self.toHashMap(True)
    

    # throws Exception
    # Java overloaded method: Python keeps the last definition
    def toHashMap(self, isEncrypted: bool) -> dict:
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        paymentGatewayHashMap: dict = StdUtil.getInstance().createHashMap()
        paymentGatewayHashMap.put(EntryData.getInstance().ENABLE, self.enable)
        paymentGatewayHashMap.put(str(StoreFrontData.getInstance().NAME), self.storeName)
        paymentGatewayHashMap.put(str(PaymentGatewayData.NAME), self.getName())
        paymentGatewayHashMap.put(str(PaymentData.METHOD), self.paymentMethod)
        paymentGatewayHashMap.put(str(PaymentGatewayData.MODE), self.mode)
        paymentGatewayHashMap.put(str(PaymentGatewayData.TESTPROTOCOL), self.testProtocol)
        paymentGatewayHashMap.put(str(PaymentGatewayData.TESTSERVER), self.testServer)
        paymentGatewayHashMap.put(str(PaymentGatewayData.TESTPORT), self.testPort)
        paymentGatewayHashMap.put(str(PaymentGatewayData.TESTPATH), self.testPath)
        paymentGatewayHashMap.put(str(PaymentGatewayData.SERVERPROTOCOL), self.serverProtocol)
        paymentGatewayHashMap.put(str(PaymentGatewayData.SERVER), self.server)
        paymentGatewayHashMap.put(str(PaymentGatewayData.SERVERPORT), self.serverPort)
        paymentGatewayHashMap.put(str(PaymentGatewayData.SERVERPATH), self.serverPath)
        if isEncrypted:
            superCrypt: SuperCrypt = SuperCrypt(PaymentGatewayData.CRYPTNUM)
            paymentGatewayHashMap.put(str(UserData.USERNAME), superCrypt.encrypt(self.userName))
            paymentGatewayHashMap.put(str(UserData.PASSWORD), superCrypt.encrypt(self.password))
        else:
            paymentGatewayHashMap.put(str(UserData.USERNAME), self.userName)
            paymentGatewayHashMap.put(str(UserData.PASSWORD), self.password)
        paymentGatewayHashMap.put(str(PaymentGatewayData.TIMEOUT), self.timeout)
        paymentGatewayHashMap.put(str(PaymentGatewayData.PROXYPROTOCOL), self.proxyProtocol)
        paymentGatewayHashMap.put(str(PaymentGatewayData.PROXYSERVER), self.proxyServer)
        paymentGatewayHashMap.put(str(PaymentGatewayData.PROXYPORT), self.proxyPort)
        paymentGatewayHashMap.put(str(PaymentGatewayData.PROXYPATH), self.proxyPath)
        paymentGatewayHashMap.put(str(PaymentGatewayData.PROXYUSERNAME), self.proxyUserName)
        paymentGatewayHashMap.put(str(PaymentGatewayData.PROXYPASSWORD), self.proxyPassword)
        paymentGatewayHashMap.put(str(PaymentGatewayData.PROXYTIMEOUT), self.proxyTimeout)
        if isEncrypted:
            superCrypt: SuperCrypt = SuperCrypt(PaymentGatewayData.CRYPTNUM)
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL1), superCrypt.encrypt(self.special1))
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL2), superCrypt.encrypt(self.special2))
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL3), superCrypt.encrypt(self.special3))
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL4), superCrypt.encrypt(self.special4))
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL5), superCrypt.encrypt(self.special5))
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL6), superCrypt.encrypt(self.special6))
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL7), superCrypt.encrypt(self.special7))
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL8), superCrypt.encrypt(self.special8))
        else:
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL1), self.special1)
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL2), self.special2)
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL3), self.special3)
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL4), self.special4)
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL5), self.special5)
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL6), self.special6)
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL7), self.special7)
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL8), self.special8)
            paymentGatewayHashMap.put(str(PaymentGatewayData.SPECIAL9), self.special9)
        paymentGatewayHashMap.put(str(EntryData.getInstance().LASTMODIFIED), self.lastModified)
        return paymentGatewayHashMap
    

    def toVector(self) -> BasicArrayList:
        return self.toVector(True)
    

    # Java overloaded method: Python keeps the last definition
    def toVector(self, isEncrypted: bool) -> BasicArrayList:
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayData import PaymentGatewayData
        updateVector: BasicArrayList = BasicArrayListD()
        updateVector.add(self.enable)
        updateVector.add(self.storeName)
        updateVector.add(self.getName())
        updateVector.add(self.paymentMethod)
        updateVector.add(self.mode)
        updateVector.add(self.testProtocol)
        updateVector.add(self.testServer)
        updateVector.add(self.testPort)
        updateVector.add(self.testPath)
        updateVector.add(self.serverProtocol)
        updateVector.add(self.server)
        updateVector.add(self.serverPort)
        updateVector.add(self.serverPath)
        if isEncrypted:
            superCrypt: SuperCrypt = SuperCrypt(PaymentGatewayData.CRYPTNUM)
            updateVector.add(superCrypt.encrypt(self.userName))
            updateVector.add(superCrypt.encrypt(self.password))
        else:
            updateVector.add(self.userName)
            updateVector.add(self.password)
        updateVector.add(self.timeout)
        updateVector.add(self.proxyProtocol)
        updateVector.add(self.proxyServer)
        updateVector.add(self.proxyPort)
        updateVector.add(self.proxyPath)
        updateVector.add(self.proxyUserName)
        updateVector.add(self.proxyPassword)
        updateVector.add(self.proxyTimeout)
        if isEncrypted:
            superCrypt: SuperCrypt = SuperCrypt(PaymentGatewayData.CRYPTNUM)
            updateVector.add(superCrypt.encrypt(self.special1))
            updateVector.add(superCrypt.encrypt(self.special2))
            updateVector.add(superCrypt.encrypt(self.special3))
            updateVector.add(superCrypt.encrypt(self.special4))
            updateVector.add(superCrypt.encrypt(self.special5))
            updateVector.add(superCrypt.encrypt(self.special6))
            updateVector.add(superCrypt.encrypt(self.special7))
            updateVector.add(superCrypt.encrypt(self.special8))
            updateVector.add(superCrypt.encrypt(self.special9))
        else:
            updateVector.add(self.special1)
            updateVector.add(self.special2)
            updateVector.add(self.special3)
            updateVector.add(self.special4)
            updateVector.add(self.special5)
            updateVector.add(self.special6)
            updateVector.add(self.special7)
            updateVector.add(self.special8)
            updateVector.add(self.special9)
        return updateVector
    

    # throws Exception
    def getKey(self) -> object:
        from org.allbinary.business.user.commerce.money.payment.gateway.PaymentGatewayPrimaryKey import PaymentGatewayPrimaryKey
        return PaymentGatewayPrimaryKey(self.getStoreName(), self.getName())
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.commerce.money.payment.PaymentData import PaymentData
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.control.crypt.SuperCrypt import SuperCrypt
from org.allbinary.logic.string.StringUtil import StringUtil


