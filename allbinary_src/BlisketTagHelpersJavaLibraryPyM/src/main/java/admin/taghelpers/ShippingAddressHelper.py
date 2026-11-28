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
from admin.taghelpers.BasicTable import BasicTable


@java_inherited_overloads
class ShippingAddressHelper(BasicTable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("stringUtil", None)
        vars(self).setdefault("weblisketSession", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("userName", None)
        vars(self).setdefault("streetAddress", None)
        vars(self).setdefault("portion", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        if "weblisketSession" not in vars(self): self.weblisketSession: WeblisketSession = None
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "userName" not in vars(self): self.userName: str = None
        if "streetAddress" not in vars(self): self.streetAddress: StreetAddress = None
        if "portion" not in vars(self): self.portion: Portion = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.installer.Portion import Portion
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        super().__init__()
        __class__._init_fields(self)
        self.request = pageContext.getRequest()
        self.weblisketSession = WeblisketSession(hashMap, pageContext)
        self.portion = Portion(hashMap)
        self.getAddressForm()
    

    def getAddressForm(self) -> None:
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
        self.userName = self.request.getParameter(UserData.USERNAME)
        if self.userName is None:
            self.userName = self.request.getParameter(WeblisketSessionData.REMOVABLEUSERNAME)
        self.streetAddress = StreetAddress(self.request)
    

    def drop(self) -> str:
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = ShippingAddressesEntity(self.stringUtil.EMPTY_STRING).drop()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, self.commonStrings.DROP)
            return success
        except Exception as e:
            error: str = "Failed to drop Admin table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.DROP, e)
            return error
    

    def create(self) -> str:
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = ShippingAddressesEntity(self.stringUtil.EMPTY_STRING).createTable()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "create()")
            return success
        except Exception as e:
            error: str = "Failed to create user table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "create()", e)
            return error
    

    def restore(self) -> str:
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
        from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().restoreTable(ShippingAddressesEntity(StringUtil.getInstance().EMPTY_STRING), self.portion)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "restore()")
            return result
        except Exception as e:
            error: str = "Failed to restore backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "restore()", e)
            return error
    

    def backup(self) -> str:
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
        from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Backup Successful"
            result: str = AbSqlTableUtil.getInstance().backupTable(ShippingAddressesEntity(StringUtil.getInstance().EMPTY_STRING))
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "backup()")
            return result
        except Exception as e:
            error: str = "Failed to make backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
            return error
    

    def insert(self) -> str:
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntityFactory import ShippingAddressesEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successfully Added Shipping Address"
            ShippingAddressesEntityFactory.getInstance().getInstance(self.weblisketSession.getUserName()).add(self.streetAddress)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "insert")
            return success
        except Exception as e:
            error: str = "Failed to add Shipping streetAddress"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "insert", e)
            return error
    

    def update(self) -> str:
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntityFactory import ShippingAddressesEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successfully Updated Shipping Address"
            ShippingAddressesEntityFactory.getInstance().getInstance(self.weblisketSession.getUserName()).update(self.streetAddress)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Successfull update of a Users Shipping Address table", self, "update()")
            return success
        except Exception as e:
            error: str = "Failed update of a Users Shipping Address Table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update", e)
            return error
    

    def setToBillingAddress(self) -> str:
        from org.allbinary.business.user.address.StreetAddress import StreetAddress
        from org.allbinary.data.tables.user.address.billing.BillingAddressesEntityFactory import BillingAddressesEntityFactory
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntityFactory import ShippingAddressesEntityFactory
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            streetAddress: StreetAddress = BillingAddressesEntityFactory.getInstance().getInstance(self.weblisketSession.getUserName()).getDefault()
            if streetAddress is not None:
                ShippingAddressesEntityFactory.getInstance().getInstance(self.weblisketSession.getUserName()).add(streetAddress)
            else:
                return "No Billing Address"
            return StringUtil.getInstance().EMPTY_STRING
        except Exception as e:
            error: str = "Failed Setting Shipping address to Billing Address"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setToBillingAddress()", e)
            return error
    

    def delete(self) -> str:
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntityFactory import ShippingAddressesEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successfully Removed Shipping Address"
            ShippingAddressesEntityFactory.getInstance().getInstance(self.weblisketSession.getUserName()).remove(int(self.streetAddress.getId()))
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "remove()")
            return success
        except Exception as e:
            error: str = "Failed to remove Shipping Address"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "remove()", e)
            return error
    

    def set(self) -> str:
        from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntityFactory import ShippingAddressesEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Successfully Set Shipping Address"
            ShippingAddressesEntityFactory.getInstance().getInstance(self.weblisketSession.getUserName()).setDefault(self.streetAddress.getId())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "set()")
            return success
        except Exception as e:
            error: str = "Failed to set Shipping Address"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "set()", e)
            return error
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.installer.Portion import Portion
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.business.user.address.StreetAddress import StreetAddress
# from org.allbinary.data.tables.user.address.billing.BillingAddressesEntityFactory import BillingAddressesEntityFactory
# from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntity import ShippingAddressesEntity
# from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntityFactory import ShippingAddressesEntityFactory
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


