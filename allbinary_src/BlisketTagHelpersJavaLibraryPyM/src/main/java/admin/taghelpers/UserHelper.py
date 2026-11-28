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
from admin.taghelpers.Table import Table


@java_inherited_overloads
class UserHelper(Table):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("hashMap", None)
        vars(self).setdefault("pageContext", None)
        vars(self).setdefault("request", None)
        vars(self).setdefault("path", None)
        vars(self).setdefault("portion", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "hashMap" not in vars(self): self.hashMap: HashMap = None
        if "pageContext" not in vars(self): self.pageContext: PageContext = None
        if "request" not in vars(self): self.request: HttpServletRequest = None
        if "path" not in vars(self): self.path: str = None
        if "portion" not in vars(self): self.portion: Portion = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.installer.Portion import Portion
        from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        super().__init__()
        __class__._init_fields(self)
        self.hashMap = hashMap
        self.pageContext = pageContext
        self.request = pageContext.getRequest()
        self.path = URLGLOBALS.getMainPath() + FREEBLISKET_PATH_GLOBALS.getInstance().XSLPATH
        self.portion = Portion(hashMap)
    

    def delete(self) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.business.user.username.UserName import UserName
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            requestHashMap: HashMap = RequestParams(self.request).toHashMap()
            userName: UserName = UserName(requestHashMap)
            UserEntityFactory.getInstance().deleteWhere(UserData.USERNAME, userName.get())
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Successfully Removed the user with ")
            stringBuffer.append(UserData.USERNAME)
            stringBuffer.append("=")
            stringBuffer.append(userName.get())
            stringBuffer.append(" from to the user table")
            success: str = str(stringBuffer)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "delete()")
            return success
        except Exception as e:
            error: str = "Failed to remove user with " + str(UserData.USERNAME) + " from User table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "delete()", e)
            return error
    

    # throws Exception
    def insert(self) -> str:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.business.entry.EntryData import EntryData
        from org.allbinary.business.user.NewUserFactory import NewUserFactory
        from org.allbinary.business.user.UserInterface import UserInterface
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            userInterface: UserInterface = NewUserFactory.getInstance(self.request, self.hashMap)
            enable: str = self.hashMap.get(EntryData.getInstance().ENABLE)
            if not (StringValidationUtil.getInstance().isEmpty(enable)):
                userInterface.setEnable(enable)
            values: BasicArrayList = userInterface.toVector()
            UserEntityFactory.getInstance().insert(values)
            success: str = "New User Successfully added to the Users Table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "add()")
            return success
        except Exception as e:
            error: str = "Failed to add User"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "add()", e)
            return error
    

    def update(self) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.NewUserFactory import NewUserFactory
        from org.allbinary.business.user.UserInterface import UserInterface
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            user: UserInterface = NewUserFactory.getInstance(self.request, self.hashMap)
            values: HashMap = user.toHashMap()
            UserEntityFactory.getInstance().update(user.getUserName(), values)
            success: str = "New User Successfully added to the Users Table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to add User"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    def drop(self) -> str:
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = UserEntityFactory.getInstance().dropTable()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF(success, self, self.commonStrings.DROP)
            return success
        except Exception as e:
            error: str = "Failed to drop user table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.DROP, e)
            return error
    

    def create(self) -> str:
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = UserEntityFactory.getInstance().createTable()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF(success, self, "create()")
            return success
        except Exception as e:
            error: str = "Failed to create user table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "create()", e)
            return error
    

    def restore(self) -> str:
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().restoreTable(UserEntityFactory.getInstance(), self.portion)
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "restore()")
            return result
        except Exception as e:
            error: str = "Failed to restore backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "restore()", e)
            return error
    

    def backup(self) -> str:
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            success: str = "Restore Successful"
            result: str = AbSqlTableUtil.getInstance().backupTable(UserEntityFactory.getInstance())
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF(success, self, "backup()")
            return result
        except Exception as e:
            error: str = "Failed to make backup"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "backup()", e)
            return error
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.entry.EntryData import EntryData
# from org.allbinary.business.installer.Portion import Portion
# from org.allbinary.business.user.NewUserFactory import NewUserFactory
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.business.user.UserInterface import UserInterface
# from org.allbinary.business.user.username.UserName import UserName
# from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
# from org.allbinary.globals.FREEBLISKET_PATH_GLOBALS import FREEBLISKET_PATH_GLOBALS
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.sql.AbSqlTableUtil import AbSqlTableUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


