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
# package org.allbinary.business.user.commerce.inventory.order.status

from __future__ import annotations



class OrderStatusEmail:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = None
        self.orderHistory: OrderHistory = None
        self.storeFrontInterface: StoreFrontInterface = None
        self.user: UserInterface = None
    

    def __init__(self, abeClientInformation: AbeClientInformationInterface, orderHistory: OrderHistory) -> None:
        self._init_fields()
        self.abeClientInformation = abeClientInformation
        self.orderHistory = orderHistory
        storeName: str = orderHistory.getStoreName()
        self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
        self.user = UserEntityFactory.getInstance().getUser(orderHistory.getUserName())
    

    # throws Exception
    def process(self) -> None:
        self.notifyStoreAdmin()
        self.notifyUser()
    

    # throws Exception
    def notifyStoreAdmin(self) -> None:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("Order Email", self, "emailStoreAdmin")
            adminEmailSubject: str = "Order " + str(self.orderHistory.getStatus()) + " Attempt"
            adminEmailTextBody: str = "Order attempt: " + str(self.orderHistory.getId()) + " Preprocessing by: " + str(self.user.getUserName())
            adminBasicEmailInfo: BasicEmailInfo = AdminEmailInfo(adminEmailSubject, adminEmailTextBody)
            storeAdminBasicEmailInfo: BasicEmailInfo = StoreEmailInfo(self.storeFrontInterface, adminEmailSubject, adminEmailTextBody)
            storeAdminEmailInfo: EmailInfo = EmailInfo(storeAdminBasicEmailInfo)
            adminEmailInfo: EmailInfo = EmailInfo(adminBasicEmailInfo)
            userEmailEventNameData: UserEmailEventNameData = UserEmailEventNameData.getInstance(self.orderHistory.getStatus())
            adminUserEmailEventHandler: UserEmailEventHandler = AdminUserEmailEventHandlerSingletons.getInstance().getInstance(self.abeClientInformation, userEmailEventNameData)
            storeAdminUserEmailEventHandler: UserEmailEventHandler = StoreAdminUserEmailEventHandlerSingletons.getInstance().getInstance(userEmailEventNameData, self.abeClientInformation, self.storeFrontInterface)
            storeAdminUserEmailEventHandler.receiveEmailInfo(userEmailEventNameData, storeAdminEmailInfo)
            adminUserEmailEventHandler.receiveEmailInfo(userEmailEventNameData, adminEmailInfo)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "emailAdmin", e)
    

    # throws Exception
    def notifyUser(self) -> None:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("Email User", self, "notifyUser()")
            subject: str = "Order " + str(self.orderHistory.getStatus()) + " Attempt"
            textBody: str = "Order attempt: " + str(self.orderHistory.getId()) + " Preprocessing by: " + str(self.user.getUserName())
            basicEmailInfo: BasicEmailInfo = StoreEmailInfo(self.storeFrontInterface, subject, textBody)
            emailInfo: EmailInfo = EmailInfo(basicEmailInfo)
            userEmailEventNameData: UserEmailEventNameData = UserEmailEventNameData.getInstance(self.orderHistory.getStatus())
            userEmailEventHandler: UserEmailEventHandler = UserEmailEventHandlerSingletons.getInstance().getInstance(self.abeClientInformation, userEmailEventNameData, self.user)
            userEmailEventHandler.receiveEmailInfo(userEmailEventNameData, emailInfo)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "notifyUser", e)
            raise e
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.business.user.commerce.inventory.order.OrderHistory import OrderHistory
from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
from org.allbinary.logic.communication.smtp.event.handler.factory.AdminUserEmailEventHandlerSingletons import AdminUserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.event.handler.factory.StoreAdminUserEmailEventHandlerSingletons import StoreAdminUserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.event.handler.factory.UserEmailEventHandlerSingletons import UserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.info.AdminEmailInfo import AdminEmailInfo
from org.allbinary.logic.communication.smtp.info.BasicEmailInfo import BasicEmailInfo
from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
from org.allbinary.logic.communication.smtp.info.StoreEmailInfo import StoreEmailInfo
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.string.CommonStrings import CommonStrings


