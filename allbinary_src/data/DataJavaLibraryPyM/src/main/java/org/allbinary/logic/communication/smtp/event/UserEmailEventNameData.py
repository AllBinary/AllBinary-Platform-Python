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
from java.lang.JavaRuntimeStatic import lazy_static


class UserEmailEventNameData:
    userNameEvenNameHashMap: HashMap = None
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
# from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
# from org.allbinary.logic.StdUtil import StdUtil


def _UserEmailEventNameData_userNameEvenNameHashMap() -> object:
    from java.util.HashMap import HashMap
    from org.allbinary.logic.StdUtil import StdUtil
    return StdUtil.getInstance().createHashMap()

lazy_static(UserEmailEventNameData, "userNameEvenNameHashMap", _UserEmailEventNameData_userNameEvenNameHashMap)

def _UserEmailEventNameData_INSTALLER() -> object:
    return UserEmailEventNameData("Installer")

lazy_static(UserEmailEventNameData, "INSTALLER", _UserEmailEventNameData_INSTALLER)

def _UserEmailEventNameData_EXCEPTION() -> object:
    return UserEmailEventNameData("Exception")

lazy_static(UserEmailEventNameData, "EXCEPTION", _UserEmailEventNameData_EXCEPTION)

def _UserEmailEventNameData_LOGGEDEXCEPTION() -> object:
    return UserEmailEventNameData("Logged Exception")

lazy_static(UserEmailEventNameData, "LOGGEDEXCEPTION", _UserEmailEventNameData_LOGGEDEXCEPTION)

def _UserEmailEventNameData_ERROR() -> object:
    return UserEmailEventNameData("Error")

lazy_static(UserEmailEventNameData, "ERROR", _UserEmailEventNameData_ERROR)

def _UserEmailEventNameData_OUTOFMEMORY() -> object:
    return UserEmailEventNameData("Out Of Memory Error")

lazy_static(UserEmailEventNameData, "OUTOFMEMORY", _UserEmailEventNameData_OUTOFMEMORY)

def _UserEmailEventNameData_ADMINGENERATINGSTATICPAGES() -> object:
    return UserEmailEventNameData("Admin Generating Static Pages")

lazy_static(UserEmailEventNameData, "ADMINGENERATINGSTATICPAGES", _UserEmailEventNameData_ADMINGENERATINGSTATICPAGES)

def _UserEmailEventNameData_STOREERROROCCURRED() -> object:
    return UserEmailEventNameData("Store Error Occurred")

lazy_static(UserEmailEventNameData, "STOREERROROCCURRED", _UserEmailEventNameData_STOREERROROCCURRED)

def _UserEmailEventNameData_STOREOUTOFMEMORY() -> object:
    return UserEmailEventNameData("Store Out Of Memory Error")

lazy_static(UserEmailEventNameData, "STOREOUTOFMEMORY", _UserEmailEventNameData_STOREOUTOFMEMORY)

def _UserEmailEventNameData_STORECREATED() -> object:
    return UserEmailEventNameData("Store Created")

lazy_static(UserEmailEventNameData, "STORECREATED", _UserEmailEventNameData_STORECREATED)

def _UserEmailEventNameData_STOREOPENED() -> object:
    return UserEmailEventNameData("Store Opened")

lazy_static(UserEmailEventNameData, "STOREOPENED", _UserEmailEventNameData_STOREOPENED)

def _UserEmailEventNameData_STORECLOSED() -> object:
    return UserEmailEventNameData("Store Closed")

lazy_static(UserEmailEventNameData, "STORECLOSED", _UserEmailEventNameData_STORECLOSED)

def _UserEmailEventNameData_STOREGENERATINGSTATICPAGES() -> object:
    return UserEmailEventNameData("Store Generating Static Pages")

lazy_static(UserEmailEventNameData, "STOREGENERATINGSTATICPAGES", _UserEmailEventNameData_STOREGENERATINGSTATICPAGES)

def _UserEmailEventNameData_PRODUCTISOUT() -> object:
    return UserEmailEventNameData("Product Is Out")

lazy_static(UserEmailEventNameData, "PRODUCTISOUT", _UserEmailEventNameData_PRODUCTISOUT)

def _UserEmailEventNameData_PRODUCTISAVAILABLE() -> object:
    return UserEmailEventNameData("Product Is Available")

lazy_static(UserEmailEventNameData, "PRODUCTISAVAILABLE", _UserEmailEventNameData_PRODUCTISAVAILABLE)

def _UserEmailEventNameData_PRODUCTISOLD() -> object:
    return UserEmailEventNameData("Product Is Old")

lazy_static(UserEmailEventNameData, "PRODUCTISOLD", _UserEmailEventNameData_PRODUCTISOLD)

def _UserEmailEventNameData_PRODUCTISONSALE() -> object:
    return UserEmailEventNameData("Product Is On Sale")

lazy_static(UserEmailEventNameData, "PRODUCTISONSALE", _UserEmailEventNameData_PRODUCTISONSALE)

def _UserEmailEventNameData_PRODUCTSALEISOVER() -> object:
    return UserEmailEventNameData("Product Sale Is Over")

lazy_static(UserEmailEventNameData, "PRODUCTSALEISOVER", _UserEmailEventNameData_PRODUCTSALEISOVER)

def _UserEmailEventNameData_ORDERPREPROCESSING() -> object:
    from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
    return UserEmailEventNameData(OrderHistoryData.PREPROCESSING)

lazy_static(UserEmailEventNameData, "ORDERPREPROCESSING", _UserEmailEventNameData_ORDERPREPROCESSING)

def _UserEmailEventNameData_ORDERPROCESSING() -> object:
    from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
    return UserEmailEventNameData(OrderHistoryData.PROCESSING)

lazy_static(UserEmailEventNameData, "ORDERPROCESSING", _UserEmailEventNameData_ORDERPROCESSING)

def _UserEmailEventNameData_ORDERCANCELLED() -> object:
    from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
    return UserEmailEventNameData(OrderHistoryData.CANCELLED)

lazy_static(UserEmailEventNameData, "ORDERCANCELLED", _UserEmailEventNameData_ORDERCANCELLED)

def _UserEmailEventNameData_ORDERPARTIALLYSHIPPED() -> object:
    from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
    return UserEmailEventNameData(OrderHistoryData.PARTIALLYSHIPPED)

lazy_static(UserEmailEventNameData, "ORDERPARTIALLYSHIPPED", _UserEmailEventNameData_ORDERPARTIALLYSHIPPED)

def _UserEmailEventNameData_ORDERSHIPPED() -> object:
    from org.allbinary.business.user.commerce.inventory.order.OrderHistoryData import OrderHistoryData
    return UserEmailEventNameData(OrderHistoryData.SHIPPED)

lazy_static(UserEmailEventNameData, "ORDERSHIPPED", _UserEmailEventNameData_ORDERSHIPPED)

def _UserEmailEventNameData_QUOTEREQUEST() -> object:
    return UserEmailEventNameData("Quote Request")

lazy_static(UserEmailEventNameData, "QUOTEREQUEST", _UserEmailEventNameData_QUOTEREQUEST)

def _UserEmailEventNameData_NEWPASSWORD() -> object:
    return UserEmailEventNameData("New Password")

lazy_static(UserEmailEventNameData, "NEWPASSWORD", _UserEmailEventNameData_NEWPASSWORD)

