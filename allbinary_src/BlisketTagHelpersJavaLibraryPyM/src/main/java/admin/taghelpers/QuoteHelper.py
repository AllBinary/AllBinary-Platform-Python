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
# package admin.taghelpers

from __future__ import annotations

from admin.taghelpers.BasicTable import BasicTable


class QuoteHelper(BasicTable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.storeFrontInterface: StoreFrontInterface = None
        self.portion: Portion = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        storeName: str = hashMap.get(StoreFrontData.getInstance().NAME)
        if storeName is not None:
            self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
        else:
            self.storeFrontInterface = StoreFront()
        self.weblisketSession = WeblisketSession(hashMap, pageContext)
        self.portion = Portion(hashMap)
    

    # throws Exception
    def emailUser(self, quoteRequest: QuoteRequest) -> None:
        user: UserInterface = UserEntityFactory.getInstance().getUser(quoteRequest.getUserName())
        userEmailSubject: str = "Quote Request Receipt"
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("This is just a verification email. ")
        stringBuffer.append("We usually respond to quote request within 24 hours.")
        stringBuffer.append("\n\nThank You For Your Business.")
        userEmailTextBody: str = str(stringBuffer)
        basicEmailInfo: BasicEmailInfo = StoreEmailInfo(self.storeFrontInterface, userEmailSubject, userEmailTextBody)
        emailInfo: EmailInfo = EmailInfo(basicEmailInfo)
        userEmailEventHandler: UserEmailEventHandler = UserEmailEventHandlerSingletons.getInstance().getInstance(self.abeClientInformation, UserEmailEventNameData.QUOTEREQUEST, user)
        userEmailEventHandler.receiveEmailInfo(UserEmailEventNameData.QUOTEREQUEST, emailInfo)
    

    # throws Exception
    def emailAdmins(self, quoteRequest: QuoteRequest) -> None:
        adminEmailSubject: str = "Quote Request"
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("\nUserName: ")
        stringBuffer.append(quoteRequest.getUserName())
        stringBuffer.append("\nProject Info: \n")
        stringBuffer.append(quoteRequest.getProjectInfo())
        stringBuffer.append("\nUser Comments: \n")
        stringBuffer.append(quoteRequest.getUserComments())
        stringBuffer.append("\nBudget: \n")
        stringBuffer.append(quoteRequest.getBudget())
        stringBuffer.append("\nTime Frame: \n")
        stringBuffer.append(quoteRequest.getTimeFrame())
        stringBuffer.append("\nComments: \n")
        stringBuffer.append(quoteRequest.getComments())
        adminEmailTextBody: str = str(stringBuffer)
        basicEmailInfo: BasicEmailInfo = StoreEmailInfo(self.storeFrontInterface, adminEmailSubject, adminEmailTextBody)
        emailInfo: EmailInfo = EmailInfo(basicEmailInfo)
        storeAdminUserEmailEventHandler: UserEmailEventHandler = AdminUserEmailEventHandlerSingletons.getInstance().getInstance(self.abeClientInformation, UserEmailEventNameData.QUOTEREQUEST)
        adminUserEmailEventHandler: UserEmailEventHandler = StoreAdminUserEmailEventHandlerSingletons.getInstance().getInstance(UserEmailEventNameData.QUOTEREQUEST, self.abeClientInformation, self.storeFrontInterface)
        storeAdminUserEmailEventHandler.receiveEmailInfo(UserEmailEventNameData.QUOTEREQUEST, emailInfo)
        adminUserEmailEventHandler.receiveEmailInfo(UserEmailEventNameData.QUOTEREQUEST, emailInfo)
    

    # throws Exception
    def email(self) -> str:
        try:
            quoteRequestEntity: QuoteRequestEntity = QuoteRequestEntityFactory.getInstance().getQuoteRequestEntityInstance()
            userName: str = self.weblisketSession.getUserName()
            vector: BasicArrayList = quoteRequestEntity.getIds(userName)
            id: int = 0
            size: int = vector.size()
            for index in range(0, size):
                nextId: int = int((vector.get(index)))
                if id < nextId:
                    id = nextId
            quoteRequest: QuoteRequest = quoteRequestEntity.get(userName, id)
            if quoteRequest is not None:
                self.emailUser(quoteRequest)
                self.emailAdmins(quoteRequest)
                return "Thank You For Your Business.<p/>"
            else:
                raise Exception("No Quote Request")
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "email", e)
            return "Thank You For Your Business.<p>"
    

    def drop(self) -> str:
        try:
            success: str = QuoteRequestEntityFactory.getInstance().getQuoteRequestEntityInstance().dropTable()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, self.commonStrings.DROP)
            return success
        except Exception as e:
            error: str = "Failed to drop QuoteRequest table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.DROP, e)
            return error
    

    def create(self) -> str:
        try:
            success: str = QuoteRequestEntityFactory.getInstance().getQuoteRequestEntityInstance().createTable()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "create()")
            return success
        except Exception as e:
            error: str = "Failed to create new QuoteRequest table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "create()", e)
            return error
    

    def restore(self) -> str:
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().restoreTable(QuoteRequestEntityFactory.getInstance().getQuoteRequestEntityInstance(), self.portion)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "restore()")
            return result
        except Exception as e:
            error: str = "Failed to restore backup"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "restore()", e)
            return error
    

    def backup(self) -> str:
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().backupTable(QuoteRequestEntityFactory.getInstance().getQuoteRequestEntityInstance())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "backup()")
            return result
        except Exception as e:
            error: str = "Failed to make backup"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
            return error
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFront import StoreFront
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.installer.Portion import Portion
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.business.user.quoterequest.QuoteRequest import QuoteRequest
from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
from org.allbinary.data.tables.user.quoterequest.QuoteRequestEntity import QuoteRequestEntity
from org.allbinary.data.tables.user.quoterequest.QuoteRequestEntityFactory import QuoteRequestEntityFactory
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
from org.allbinary.logic.communication.smtp.event.handler.factory.AdminUserEmailEventHandlerSingletons import AdminUserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.event.handler.factory.StoreAdminUserEmailEventHandlerSingletons import StoreAdminUserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.event.handler.factory.UserEmailEventHandlerSingletons import UserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.info.BasicEmailInfo import BasicEmailInfo
from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
from org.allbinary.logic.communication.smtp.info.StoreEmailInfo import StoreEmailInfo
from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory


