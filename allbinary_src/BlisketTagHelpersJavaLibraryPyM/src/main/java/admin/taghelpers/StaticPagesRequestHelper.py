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

from org.allbinary.business.context.AbContext import AbContext
from admin.taghelpers.TagHelperInterface import TagHelperInterface


class StaticPagesRequestHelper(AbContext, TagHelperInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.request: HttpServletRequest = None
        self.storeName: str = None
        self.searchParams: SearchParams = None
        self.xslFile: str = None
    

    def __init__(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__(propertiesHashMap, pageContext)
        self._init_fields()
        self.request = pageContext.getRequest()
        self.xslFile = propertiesHashMap.get(TransformInfoData.getInstance().TEMPLATEFILENAME)
        self.getFormData()
    

    def getFormData(self) -> None:
        self.storeName = self.request.getParameter(StoreFrontData.getInstance().NAME)
        self.searchParams = SearchParams(self.request)
    

    # throws Exception
    def email(self) -> None:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGING):
                self.logUtil.putF("Generated Static Pages Notification Email", self, "email")
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.storeName)
            adminEmailSubject: str = "Generated Static Pages Email Notification"
            adminEmailTextBody: str = "Generated static pages for store: " + self.storeName
            adminBasicEmailInfo: BasicEmailInfo = AdminEmailInfo(adminEmailSubject, adminEmailTextBody)
            storeAdminBasicEmailInfo: BasicEmailInfo = StoreEmailInfo(storeFrontInterface, adminEmailSubject, adminEmailTextBody)
            storeAdminEmailInfo: EmailInfo = EmailInfo(storeAdminBasicEmailInfo)
            adminEmailInfo: EmailInfo = EmailInfo(adminBasicEmailInfo)
            adminUserEmailEventHandler: UserEmailEventHandler = AdminUserEmailEventHandlerSingletons.getInstance().getInstance(self.abeClientInformation, UserEmailEventNameData.STOREGENERATINGSTATICPAGES)
            storeAdminUserEmailEventHandler: UserEmailEventHandler = StoreAdminUserEmailEventHandlerSingletons.getInstance().getInstance(UserEmailEventNameData.STOREGENERATINGSTATICPAGES, self.abeClientInformation, storeFrontInterface)
            storeAdminUserEmailEventHandler.receiveEmailInfo(UserEmailEventNameData.STOREGENERATINGSTATICPAGES, storeAdminEmailInfo)
            adminUserEmailEventHandler.receiveEmailInfo(UserEmailEventNameData.STOREGENERATINGSTATICPAGES, adminEmailInfo)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().EMAILLOGGINGERROR):
                self.logUtil.put(self.commonStrings.FAILURE, self, "email", e)
    

    def generateStaticPages(self) -> str:
        try:
            contentType: str = AcceptableResponseGenerator.getInstance().get(self.request)
            searchRequest: SearchRequest = SearchRequest(None, self.searchParams, self.xslFile, contentType, self.getPropertiesHashMap(), self.getPageContext())
            success: str = ProductListingFactory.getInstance(searchRequest).generateAll(self.storeName)
            self.email()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "generateStaticPages()")
            return success
        except Exception as e:
            error: str = "Failed to generate staticpages table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "generateStaticPages()", e)
            return error
    

    def makePublic(self) -> str:
        try:
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(self.storeName)
            fromAbPath: AbPath = AbPath(storeFrontInterface.getTestHtmlPath() + storeFrontInterface.getStaticPath(), StringUtil.getInstance().EMPTY_STRING)
            toAbPath: AbPath = AbPath(str(self.URLGLOBALS.getWebappPath()) + storeFrontInterface.getName() + str(AbPathData.getInstance().SEPARATOR) + str(storeFrontInterface.getStaticPath()), StringUtil.getInstance().EMPTY_STRING)
            FileUtil.getInstance().copy(fromAbPath, toAbPath)
            success: str = "Made Public"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "makePublic()")
            return success
        except Exception as e:
            error: str = "Failed to makePublic"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "makePublic()", e)
            return error
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.http.AcceptableResponseGenerator import AcceptableResponseGenerator
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
from org.allbinary.logic.communication.smtp.event.handler.factory.AdminUserEmailEventHandlerSingletons import AdminUserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.event.handler.factory.StoreAdminUserEmailEventHandlerSingletons import StoreAdminUserEmailEventHandlerSingletons
from org.allbinary.logic.communication.smtp.info.AdminEmailInfo import AdminEmailInfo
from org.allbinary.logic.communication.smtp.info.BasicEmailInfo import BasicEmailInfo
from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
from org.allbinary.logic.communication.smtp.info.StoreEmailInfo import StoreEmailInfo
from org.allbinary.logic.control.search.SearchParams import SearchParams
from org.allbinary.logic.control.search.SearchRequest import SearchRequest
from org.allbinary.logic.io.file.FileUtil import FileUtil
from org.allbinary.logic.io.path.AbPath import AbPath
from org.allbinary.logic.io.path.AbPathData import AbPathData
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from views.admin.inventory.listings.ProductListingFactory import ProductListingFactory


