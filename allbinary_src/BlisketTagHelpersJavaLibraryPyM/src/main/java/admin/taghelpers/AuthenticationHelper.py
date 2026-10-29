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

import datetime
from admin.taghelpers.TagHelper import TagHelper


class AuthenticationHelper(TagHelper):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.authenticated: str = None
        self.sessionUserName: str = None
        self.role: UserRole = None
        self.timeout: str = None
        self.attemptsInteger: int = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor2(self, hashMap: dict, pageContext: PageContext) -> None:
        self._constructor2(hashMap, pageContext.getRequest())
    

    def _constructor2(self, hashMap: dict, httpServletRequest: HttpServletRequest) -> None:
        super().__init__()
        self._init_fields()
        self.weblisketSession = WeblisketSession(hashMap, httpServletRequest)
        self.getFormData()
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATION):
            self.logUtil.putF(self.outputSessionInfo(), self, self.commonStrings.CONSTRUCTOR)
    

    # throws Exception
    def getFormData(self) -> None:
        self.authenticated = self.weblisketSession.getAuthentication()
        self.sessionUserName = self.weblisketSession.getUserName()
        self.role = self.weblisketSession.getRole()
        self.attemptsInteger = self.weblisketSession.getAttempts()
        self.timeout = self.weblisketSession.getTimeout()
    

    # throws Exception
    def invalidateSession(self) -> int:
        try:
            self.weblisketSession.clear()
            return int(TagSupport.EVAL_BODY_INCLUDE)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "invalidateSession()", e)
            return None
    

    def isSessionOld(self) -> bool:
        if self.role is not None:
            timeCreated: int = self.weblisketSession.getCreationTime()
            sessionTimout: int = self.role.getSessionTimeout()
            calendar: datetime.datetime = datetime.datetime.now()
            timeFirst: int = calendar.getTimeInMillis() - sessionTimout
            if timeFirst > timeCreated:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATION):
                    stringBuffer: StringMaker = StringMaker()
                    stringBuffer.append("Session Is Old - Timeout: ")
                    stringBuffer.appendlong(sessionTimout)
                    stringBuffer.append(" Eval: ")
                    stringBuffer.appendlong(timeFirst)
                    stringBuffer.append(" > ")
                    stringBuffer.appendlong(timeCreated)
                    self.logUtil.putF(str(stringBuffer), self, "isSessionOld()")
                return True
        else:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATION):
                self.logUtil.putF("Role Is Not In Session", self, "isSessionOld()")
        return self.isRarelyUsedSession()
    

    def isRarelyUsedSession(self) -> bool:
        if self.role is not None:
            timeCreated: int = self.weblisketSession.getCreationTime()
            lastAccess: int = self.weblisketSession.getLastAccessedTime()
            inactivityAllowed: int = self.role.getSessionInactivityTimeout()
            calendar: datetime.datetime = datetime.datetime.now()
            timeFirst: int = calendar.getTimeInMillis() - lastAccess
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATION):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Session Is Rarely Used - Timeout: ")
                stringBuffer.appendlong(lastAccess)
                stringBuffer.append(" Eval: ")
                stringBuffer.appendlong(timeFirst)
                stringBuffer.append(" > ")
                stringBuffer.appendlong(inactivityAllowed)
                self.logUtil.putF(str(stringBuffer), self, "isRarelyUsedSession()")
        else:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATION):
                self.logUtil.putF("Role Is Not In Session", self, "isRarelyUsedSession()")
        return False
    

    def validRole(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Trying New login<p/>")
            return str(stringBuffer)
        except Exception as e:
            error: str = "Failed to set valid role"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "validRole()", e)
            return error
    

    def invalidRole(self) -> str:
        try:
            self.weblisketSession.setAuthenticated(False)
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Sorry your username and password is invalid on this page. ")
            stringBuffer.append("Trying New login<p/>")
            return str(stringBuffer)
        except Exception as e:
            error: str = "Failed to set role invalid"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "invalidRole()", e)
            return error
    

    # throws Exception
    def isAuthenticated(self) -> bool:
        if BooleanUtil.getInstance().getFromString(self.authenticated):
            return True
        else:
            return False
    

    def isAuthenticationSessionValid(self, roles: BasicArrayList) -> bool:
        try:
            if self.role is not None:
                if self.isAuthenticated():
                    if self.sessionUserName is not None:
                        basicUserRole: BasicUserRole = self.role.getBasicUserRole()
                        basicUserRoleArray: list[object] = roles.toArray()
                        size: int = len(basicUserRoleArray)
                        for index in range(0, size):
                            mustBeOfRole: BasicUserRole = basicUserRoleArray[index]
                            if basicUserRole.equals(mustBeOfRole):
                                if basicUserRole.equals(UserRoleFactory.getInstance().CUSTOMER):
                                    userEntityInterface: UserEntityInterface = UserEntityFactory.getInstance()
                                    userInterface: UserInterface = userEntityInterface.getUser(self.sessionUserName)
                                    if not userInterface.isSessionValid():
                                        return False
                                return True
                    return False
            else:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATION):
                    self.logUtil.putF("Role Is Not In Session", self, "isAuthenticationSessionValid()")
            return False
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isAuthenticatedSessionValid()", e)
            return False
    

    def nextAttempt(self) -> None:
        if self.attemptsInteger is not None and int(self.attemptsInteger) > 0:
            self.weblisketSession.setAttempts(int(int(self.attemptsInteger) + 1))
        else:
            self.weblisketSession.setAttempts(int(1))
    

    def processIfNewLogin(self, userName: str, password: str) -> bool:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.putF("Starting: " + userName, self, "processIfNewLogin()")
            if userName is not None and ((userName > StringUtil.getInstance().EMPTY_STRING) - (userName < StringUtil.getInstance().EMPTY_STRING)) != 0 and password is not None and ((password > StringUtil.getInstance().EMPTY_STRING) - (password < StringUtil.getInstance().EMPTY_STRING)) != 0:
                login: str = None
                userEntityInterface: UserEntityInterface = UserEntityFactory.getInstance()
                login = userEntityInterface.login(userName, password)
                if ((login > self.GLOBALS2.LOGINSUCCESS) - (login < self.GLOBALS2.LOGINSUCCESS)) == 0:
                    userInterface: UserInterface = userEntityInterface.getUser(userName)
                    if userInterface.isSessionValid():
                        self.weblisketSession.setAttempts(int(0))
                        return True
                self.nextAttempt()
                return False
            self.nextAttempt()
            return False
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "processIfNewLogin()", e)
            return False
    

    def processInvalidation(self) -> bool:
        try:
            if BooleanUtil.getInstance().getFromString(self.timeout):
                self.invalidateSession()
                return True
            if True:
                self.weblisketSession.setTimeout(BooleanFactory.getInstance().TRUE_STRING)
                return False
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "processInvalidation()", e)
            return False
    

    def outputSessionInfo(self) -> str:
        try:
            calendar: datetime.datetime = datetime.datetime.now()
            timeCreated: int = self.weblisketSession.getCreationTime()
            stringBuffer: StringMaker = StringMaker()
            lastAccess: int = self.weblisketSession.getLastAccessedTime()
            stringBuffer.append("Time Since Last Access: " + str((calendar.getTimeInMillis() - lastAccess)) + "<br/>\n")
            if self.role is not None:
                stringBuffer.append("Auth: ")
                stringBuffer.append(self.authenticated)
                stringBuffer.append(" UserName: ")
                stringBuffer.append(self.sessionUserName)
                stringBuffer.append(" Role: ")
                stringBuffer.append(str(self.role))
                stringBuffer.append("<br/>\n")
                stringBuffer.append("Time Left: ")
                stringBuffer.appendlong(int((self.role.getSessionTimeout() - (calendar.getTimeInMillis() - timeCreated))))
                stringBuffer.append("<br/>\n")
                stringBuffer.append("Inactivity Time Allowed: ")
                stringBuffer.appendlong(int(self.role.getSessionTimeout()))
                stringBuffer.append("<br/>\n")
                stringBuffer.append("Inactivity Time Allowed: ")
                stringBuffer.appendlong(int(self.role.getSessionInactivityTimeout()))
                stringBuffer.append("<br/>\n")
            else:
                stringBuffer.append("Role Is Not Set<br/>\n")
            return str(stringBuffer)
        except Exception as e:
            return "Error"
    

    def getRole(self) -> UserRole:
        return self.role
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from javax.servlet.jsp.tagext.TagSupport import TagSupport
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.business.user.role.BasicUserRole import BasicUserRole
from org.allbinary.business.user.role.UserRole import UserRole
from org.allbinary.business.user.role.UserRoleFactory import UserRoleFactory
from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
from org.allbinary.data.tables.user.UserEntityInterface import UserEntityInterface
from org.allbinary.globals.GLOBALS2 import GLOBALS2
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


