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

from admin.taghelpers.Table import Table


class BillingAddressHelper(Table):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.stringUtil: StringUtil = StringUtil.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.request: HttpServletRequest = None
        self.userName: str = None
        self.streetAddress: StreetAddress = None
        self.portion: Portion = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.request = pageContext.getRequest()
        self.weblisketSession = WeblisketSession(hashMap, pageContext)
        self.portion = Portion(hashMap)
        self.getAddressForm()
    

    def getAddressForm(self) -> None:
        self.userName = self.request.getParameter(UserData.USERNAME)
        if self.userName is None:
            self.userName = self.request.getParameter(WeblisketSessionData.REMOVABLEUSERNAME)
        self.streetAddress = StreetAddress(self.request)
    

    def drop(self) -> str:
        try:
            success: str = BillingAddressesEntity(self.stringUtil.EMPTY_STRING).drop()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, self.commonStrings.DROP)
            return success
        except Exception as e:
            error: str = "Failed to drop Admin table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.DROP, e)
            return error
    

    def create(self) -> str:
        try:
            success: str = BillingAddressesEntity(self.stringUtil.EMPTY_STRING).createTable()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "create()")
            return success
        except Exception as e:
            error: str = "Failed to create user table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "create()", e)
            return error
    

    def restore(self) -> str:
        try:
            success: str = "Restore Successful"
            billingAddressesEntity: BillingAddressesEntity = BillingAddressesEntity(StringUtil.getInstance().EMPTY_STRING)
            result: str = AbSqlTableUtil.getInstance().restoreTable(billingAddressesEntity, self.portion)
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
            success: str = "Backup Successful"
            result: str = AbSqlTableUtil.getInstance().backupTable(BillingAddressesEntity(StringUtil.getInstance().EMPTY_STRING))
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "backup()")
            return result
        except Exception as e:
            error: str = "Failed to make backup"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
            return error
    

    def insert(self) -> str:
        try:
            success: str = "Successfully Added Billing Address"
            BillingAddressesEntityFactory.getInstance().getInstance(self.weblisketSession.getUserName()).add(self.streetAddress)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "add()")
            return success
        except Exception as e:
            error: str = "Failed to add Billing Address"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "add()", e)
            return error
    

    def update(self) -> str:
        try:
            success: str = "Successfully Updated Billing Address"
            BillingAddressesEntityFactory.getInstance().getInstance(self.weblisketSession.getUserName()).update(self.streetAddress)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Successfull update of a user Billing Address table", self, "update()")
            return success
        except Exception as e:
            error: str = "Failed update of a User Billing Address Table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    def setToShippingAddress(self) -> str:
        try:
            shippingAddressesEntityFactory: ShippingAddressesEntityFactory = ShippingAddressesEntityFactory.getInstance()
            streetAddress: StreetAddress = shippingAddressesEntityFactory.getInstance(self.weblisketSession.getUserName()).getDefault()
            if streetAddress is not None:
                shippingAddressesEntityFactory.getInstance(self.weblisketSession.getUserName()).add(streetAddress)
            else:
                return "No Shipping Address"
            return StringUtil.getInstance().EMPTY_STRING
        except Exception as e:
            error: str = "Failed to Set Billing address to Shipping Address"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setToShippingAddress()", e)
            return error
    

    def delete(self) -> str:
        try:
            success: str = "Successfully Removed Billing Address"
            BillingAddressesEntityFactory.getInstance().getInstance(self.weblisketSession.getUserName()).remove(int(self.streetAddress.getId()))
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            error: str = "Failed to remove Billing Address"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
    

    def set(self) -> str:
        try:
            success: str = "Successfully Set Billing Address"
            BillingAddressesEntityFactory.getInstance().getInstance(self.weblisketSession.getUserName()).setDefault(self.streetAddress.getId())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "set()")
            return success
        except Exception as e:
            error: str = "Failed to set billing Address"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "set()", e)
            return error
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.installer.Portion import Portion
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.data.tables.user.address.billing.BillingAddressesEntity import BillingAddressesEntity
from org.allbinary.data.tables.user.address.billing.BillingAddressesEntityFactory import BillingAddressesEntityFactory
from org.allbinary.data.tables.user.address.shipping.ShippingAddressesEntityFactory import ShippingAddressesEntityFactory
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
from org.allbinary.logic.string.StringUtil import StringUtil


