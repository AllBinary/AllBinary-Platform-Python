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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
import threading
from admin.taghelpers.ModifyTable import ModifyTable


@java_inherited_overloads
class StoreFrontsRequestHelper(ModifyTable):
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("abeClientInformation", None)
        vars(self).setdefault("pageContext", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("weblisketSession", None)
        vars(self).setdefault("storeName", None)
        vars(self).setdefault("modifyingStoreFrontInterface", None)
        vars(self).setdefault("portion", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        if "pageContext" not in vars(self): self.pageContext: PageContext = None
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "weblisketSession" not in vars(self): self.weblisketSession: WeblisketSession = None
        if "storeName" not in vars(self): self.storeName: str = None
        if "modifyingStoreFrontInterface" not in vars(self): self.modifyingStoreFrontInterface: StoreFrontInterface = None
        if "portion" not in vars(self): self.portion: Portion = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.installer.Portion import Portion
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        super().__init__()
        __class__._init_fields(self)
        self.pageContext = pageContext
        self.request = pageContext.getRequest()
        self.weblisketSession = WeblisketSession(hashMap, pageContext)
        self.portion = Portion(hashMap)
        self.getFormData()
    

    # throws Exception
    def getFormData(self) -> None:
        from org.allbinary.business.context.modules.storefront.StoreFront import StoreFront
        from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
        self.storeName = self.weblisketSession.getStoreName()
        self.modifyingStoreFrontInterface = StoreFront(self.request)
    

    def update(self) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.data.tables.context.module.storefronts.StoreFrontsEntityFactory import StoreFrontsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Updated Successfully"
            hashMapData: HashMap = self.modifyingStoreFrontInterface.toHashMap()
            StoreFrontsEntityFactory.getInstance().getStoreFrontsEntityInstance().update(hashMapData)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update storefronts table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    # throws Exception
    def sendStoreCreatedEmails(self) -> None:
        from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
        from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
        from org.allbinary.logic.communication.smtp.event.handler.factory.AdminUserEmailEventHandlerSingletons import AdminUserEmailEventHandlerSingletons
        from org.allbinary.logic.communication.smtp.event.handler.factory.StoreAdminUserEmailEventHandlerSingletons import StoreAdminUserEmailEventHandlerSingletons
        from org.allbinary.logic.communication.smtp.info.AdminEmailInfo import AdminEmailInfo
        from org.allbinary.logic.communication.smtp.info.BasicEmailInfo import BasicEmailInfo
        from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
        from org.allbinary.logic.communication.smtp.info.StoreEmailInfo import StoreEmailInfo
        from org.allbinary.logic.string.StringMaker import StringMaker
        storeManagerEmailSubject: str = "Store Manager Nofification For Store: " + self.modifyingStoreFrontInterface.getName()
        adminEmailSubject: str = "Admin Notification For Store: " + self.modifyingStoreFrontInterface.getName()
        stringBuffer: StringMaker = StringMaker()
        stringBuffer.append("Store Created: ")
        stringBuffer.append(self.modifyingStoreFrontInterface.getName())
        stringBuffer.append("\n\n")
        stringBuffer.append("Click here for the Admin Interface:\n")
        stringBuffer.append(self.modifyingStoreFrontInterface.getCurrentHomeHostName())
        stringBuffer.append("/admin/login.jsp\n\n")
        stringBuffer.append("Goto Your Store:\n")
        stringBuffer.append(self.modifyingStoreFrontInterface.getCurrentHomeHostName())
        stringBuffer.append(self.modifyingStoreFrontInterface.getName())
        stringBuffer.append("/index.jsp")
        stringBuffer.append("\n\n")
        stringBuffer.append("UserName: ")
        stringBuffer.append(self.weblisketSession.getUserName())
        adminEmailTextBody: str = str(stringBuffer)
        adminBasicEmailInfo: BasicEmailInfo = AdminEmailInfo(adminEmailSubject, adminEmailTextBody)
        storeAdminBasicEmailInfo: BasicEmailInfo = StoreEmailInfo(self.modifyingStoreFrontInterface, storeManagerEmailSubject, adminEmailTextBody)
        storeAdminEmailInfo: EmailInfo = EmailInfo(storeAdminBasicEmailInfo)
        adminEmailInfo: EmailInfo = EmailInfo(adminBasicEmailInfo)
        adminUserEmailEventHandler: UserEmailEventHandler = AdminUserEmailEventHandlerSingletons.getInstance().getInstance(self.abeClientInformation, UserEmailEventNameData.STORECREATED)
        storeAdminUserEmailEventHandler: UserEmailEventHandler = StoreAdminUserEmailEventHandlerSingletons.getInstance().getInstance(UserEmailEventNameData.STORECREATED, self.abeClientInformation, self.modifyingStoreFrontInterface)
        storeAdminUserEmailEventHandler.receiveEmailInfo(UserEmailEventNameData.STORECREATED, storeAdminEmailInfo)
        adminUserEmailEventHandler.receiveEmailInfo(UserEmailEventNameData.STORECREATED, adminEmailInfo)
    

    def install(self) -> str:
        with self._lock:
            return __class__.__dict__["_install_unlocked"].__get__(self, __class__)()

    def _install_unlocked(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Intall StoreFront Successfully: ")
            stringBuffer.appendint(int(int(self.portion.getCurrent())))
            stringBuffer.append(" of ")
            stringBuffer.appendint(int(int(self.portion.getTotal())))
            success: str = str(stringBuffer)
            self.modifyingStoreFrontInterface.install(int(self.portion.getCurrent()), int(self.portion.getTotal()))
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "install()")
            return success
        except Exception as e:
            error: str = "Failed to Install storefront"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "install()", e)
            return error
    

    def insert(self) -> str:
        with self._lock:
            return __class__.__dict__["_insert_unlocked"].__get__(self, __class__)()

    def _insert_unlocked(self) -> str:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.data.tables.context.module.storefronts.StoreFrontsEntityFactory import StoreFrontsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Added Successfully"
            values: BasicArrayList = self.modifyingStoreFrontInterface.toVector()
            StoreFrontsEntityFactory.getInstance().getStoreFrontsEntityInstance().insert(values)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert()")
            return success
        except Exception as e:
            error: str = "Failed to add storefront"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insert()", e)
            return error
    

    def delete(self) -> str:
        from org.allbinary.data.tables.context.module.storefronts.StoreFrontsEntityFactory import StoreFrontsEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Delete Successfully"
            StoreFrontsEntityFactory.getInstance().getStoreFrontsEntityInstance().delete(self.storeName)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            error: str = "Failed to delete storefronts table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFront import StoreFront
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.installer.Portion import Portion
# from org.allbinary.data.tables.context.module.storefronts.StoreFrontsEntityFactory import StoreFrontsEntityFactory
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.smtp.event.UserEmailEventNameData import UserEmailEventNameData
# from org.allbinary.logic.communication.smtp.event.handler.UserEmailEventHandler import UserEmailEventHandler
# from org.allbinary.logic.communication.smtp.event.handler.factory.AdminUserEmailEventHandlerSingletons import AdminUserEmailEventHandlerSingletons
# from org.allbinary.logic.communication.smtp.event.handler.factory.StoreAdminUserEmailEventHandlerSingletons import StoreAdminUserEmailEventHandlerSingletons
# from org.allbinary.logic.communication.smtp.info.AdminEmailInfo import AdminEmailInfo
# from org.allbinary.logic.communication.smtp.info.BasicEmailInfo import BasicEmailInfo
# from org.allbinary.logic.communication.smtp.info.EmailInfo import EmailInfo
# from org.allbinary.logic.communication.smtp.info.StoreEmailInfo import StoreEmailInfo
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
# from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


