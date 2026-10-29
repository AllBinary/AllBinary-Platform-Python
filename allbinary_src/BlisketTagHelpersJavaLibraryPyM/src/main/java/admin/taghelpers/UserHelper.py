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


class UserHelper(Table):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.hashMap: dict = None
        self.pageContext: PageContext = None
        self.request: HttpServletRequest = None
        self.path: str = None
        self.portion: Portion = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.hashMap = hashMap
        self.pageContext = pageContext
        self.request = pageContext.getRequest()
        self.path = self.URLGLOBALS.getMainPath() + self.FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH
        self.portion = Portion(hashMap)
    

    def delete(self) -> str:
        try:
            requestHashMap: dict = RequestParams(self.request).toHashMap()
            userName: UserName = UserName(requestHashMap)
            UserEntityFactory.getInstance().deleteWhere(UserData.USERNAME, userName.get())
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Successfully Removed the user with ")
            stringBuffer.append(UserData.USERNAME)
            stringBuffer.append("=")
            stringBuffer.append(userName.get())
            stringBuffer.append(" from to the user table")
            success: str = str(stringBuffer)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            error: str = "Failed to remove user with " + str(UserData.USERNAME) + " from User table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
    

    # throws Exception
    def insert(self) -> str:
        try:
            userInterface: UserInterface = NewUserFactory.getInstance(self.request, self.hashMap)
            enable: str = self.hashMap.get(EntryData.getInstance().ENABLE)
            if not StringValidationUtil.getInstance().isEmpty(enable):
                userInterface.setEnable(enable)
            values: BasicArrayList = userInterface.toVector()
            UserEntityFactory.getInstance().insert(values)
            success: str = "New User Successfully added to the Users Table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "add()")
            return success
        except Exception as e:
            error: str = "Failed to add User"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "add()", e)
            return error
    

    def update(self) -> str:
        try:
            user: UserInterface = NewUserFactory.getInstance(self.request, self.hashMap)
            values: dict = user.toHashMap()
            UserEntityFactory.getInstance().update(user.getUserName(), values)
            success: str = "New User Successfully added to the Users Table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to add User"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    def drop(self) -> str:
        try:
            success: str = UserEntityFactory.getInstance().dropTable()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF(success, self, self.commonStrings.DROP)
            return success
        except Exception as e:
            error: str = "Failed to drop user table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.DROP, e)
            return error
    

    def create(self) -> str:
        try:
            success: str = UserEntityFactory.getInstance().createTable()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF(success, self, "create()")
            return success
        except Exception as e:
            error: str = "Failed to create user table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "create()", e)
            return error
    

    def restore(self) -> str:
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().restoreTable(UserEntityFactory.getInstance(), self.portion)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "restore()")
            return result
        except Exception as e:
            error: str = "Failed to restore backup"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "restore()", e)
            return error
    

    def backup(self) -> str:
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().backupTable(UserEntityFactory.getInstance())
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF(success, self, "backup()")
            return result
        except Exception as e:
            error: str = "Failed to make backup"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
            return error
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.installer.Portion import Portion
from org.allbinary.business.user.NewUserFactory import NewUserFactory
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.business.user.username.UserName import UserName
from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
from org.allbinary.globals.URLGLOBALS import URLGLOBALS
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil


