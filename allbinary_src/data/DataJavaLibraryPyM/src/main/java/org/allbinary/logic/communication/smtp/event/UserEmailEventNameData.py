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
# package org.allbinary.logic.communication.smtp.event

from __future__ import annotations

import threading
from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
from org.allbinary.logic.StdUtil import StdUtil


class UserEmailEventNameData:
    userNameEvenNameHashMap: dict = StdUtil.getInstance().createHashMap()
    nextId: int = 0
    INSTALLER: UserEmailEventNameData = None
    EXCEPTION: UserEmailEventNameData = None
    LOGGEDEXCEPTION: UserEmailEventNameData = None
    ERROR: UserEmailEventNameData = None
    OUTOFMEMORY: UserEmailEventNameData = None
    ADMINGENERATINGSTATICPAGES: UserEmailEventNameData = None
    STOREERROROCCURRED: UserEmailEventNameData = None
    STOREOUTOFMEMORY: UserEmailEventNameData = None
    STORECREATED: UserEmailEventNameData = None
    STOREOPENED: UserEmailEventNameData = None
    STORECLOSED: UserEmailEventNameData = None
    STOREGENERATINGSTATICPAGES: UserEmailEventNameData = None
    PRODUCTISOUT: UserEmailEventNameData = None
    PRODUCTISAVAILABLE: UserEmailEventNameData = None
    PRODUCTISOLD: UserEmailEventNameData = None
    PRODUCTISONSALE: UserEmailEventNameData = None
    PRODUCTSALEISOVER: UserEmailEventNameData = None
    ORDERPREPROCESSING: UserEmailEventNameData = None
    ORDERPROCESSING: UserEmailEventNameData = None
    ORDERCANCELLED: UserEmailEventNameData = None
    ORDERPARTIALLYSHIPPED: UserEmailEventNameData = None
    ORDERSHIPPED: UserEmailEventNameData = None
    QUOTEREQUEST: UserEmailEventNameData = None
    NEWPASSWORD: UserEmailEventNameData = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.eventNameId: int = 0
        self.eventHandlerName: str = None
    

    def __init__(self, eventHandlerName: str) -> None:
        self._init_fields()
        self.eventHandlerName = eventHandlerName
        self.initNextId()
        UserEmailEventNameData.userNameEvenNameHashMap.put(self.eventHandlerName, self)
    

    def initNextId(self) -> None:
        with self._lock:
            return self._initNextId_unlocked()

    def _initNextId_unlocked(self) -> None:
        self.eventNameId = UserEmailEventNameData.nextId
        UserEmailEventNameData.nextId += 1
    

    def isEvent(self, userEmailEventNameString: str) -> bool:
        return UserEmailEventNameData.userNameEvenNameHashMap.containsKey(userEmailEventNameString)
    

    # throws Exception
    @staticmethod
    def getInstance(userEmailEventNameString: str) -> UserEmailEventNameData:
        with UserEmailEventNameData._lock:
            return UserEmailEventNameData._getInstance_unlocked(userEmailEventNameString)

    @staticmethod
    def _getInstance_unlocked(userEmailEventNameString: str) -> UserEmailEventNameData:
        userEmailEventNameData: UserEmailEventNameData = UserEmailEventNameData.userNameEvenNameHashMap.get(userEmailEventNameString)
        if userEmailEventNameData is None:
            raise Exception()
        else:
            return userEmailEventNameData
    

    def toString(self) -> str:
        return self.eventHandlerName

    def __str__(self) -> str:
        return self.toString()
# from java.util.HashMap import HashMap


UserEmailEventNameData.INSTALLER = UserEmailEventNameData("Installer")

UserEmailEventNameData.EXCEPTION = UserEmailEventNameData("Exception")

UserEmailEventNameData.LOGGEDEXCEPTION = UserEmailEventNameData("Logged Exception")

UserEmailEventNameData.ERROR = UserEmailEventNameData("Error")

UserEmailEventNameData.OUTOFMEMORY = UserEmailEventNameData("Out Of Memory Error")

UserEmailEventNameData.ADMINGENERATINGSTATICPAGES = UserEmailEventNameData("Admin Generating Static Pages")

UserEmailEventNameData.STOREERROROCCURRED = UserEmailEventNameData("Store Error Occurred")

UserEmailEventNameData.STOREOUTOFMEMORY = UserEmailEventNameData("Store Out Of Memory Error")

UserEmailEventNameData.STORECREATED = UserEmailEventNameData("Store Created")

UserEmailEventNameData.STOREOPENED = UserEmailEventNameData("Store Opened")

UserEmailEventNameData.STORECLOSED = UserEmailEventNameData("Store Closed")

UserEmailEventNameData.STOREGENERATINGSTATICPAGES = UserEmailEventNameData("Store Generating Static Pages")

UserEmailEventNameData.PRODUCTISOUT = UserEmailEventNameData("Product Is Out")

UserEmailEventNameData.PRODUCTISAVAILABLE = UserEmailEventNameData("Product Is Available")

UserEmailEventNameData.PRODUCTISOLD = UserEmailEventNameData("Product Is Old")

UserEmailEventNameData.PRODUCTISONSALE = UserEmailEventNameData("Product Is On Sale")

UserEmailEventNameData.PRODUCTSALEISOVER = UserEmailEventNameData("Product Sale Is Over")

UserEmailEventNameData.ORDERPREPROCESSING = UserEmailEventNameData(OrderHistoryData.PREPROCESSING)

UserEmailEventNameData.ORDERPROCESSING = UserEmailEventNameData(OrderHistoryData.PROCESSING)

UserEmailEventNameData.ORDERCANCELLED = UserEmailEventNameData(OrderHistoryData.CANCELLED)

UserEmailEventNameData.ORDERPARTIALLYSHIPPED = UserEmailEventNameData(OrderHistoryData.PARTIALLYSHIPPED)

UserEmailEventNameData.ORDERSHIPPED = UserEmailEventNameData(OrderHistoryData.SHIPPED)

UserEmailEventNameData.QUOTEREQUEST = UserEmailEventNameData("Quote Request")

UserEmailEventNameData.NEWPASSWORD = UserEmailEventNameData("New Password")

