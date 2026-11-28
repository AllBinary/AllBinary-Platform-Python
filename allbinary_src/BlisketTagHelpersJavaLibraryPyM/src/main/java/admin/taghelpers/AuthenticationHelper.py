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

from java.lang.JavaRuntimeStatic import java_equals
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
import datetime
from admin.taghelpers.TagHelper import TagHelper


@java_inherited_overloads
class AuthenticationHelper(TagHelper):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("weblisketSession", None)
        vars(self).setdefault("authenticated", None)
        vars(self).setdefault("sessionUserName", None)
        vars(self).setdefault("role", None)
        vars(self).setdefault("timeout", None)
        vars(self).setdefault("attemptsInteger", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "weblisketSession" not in vars(self): self.weblisketSession: WeblisketSession = None
        if "authenticated" not in vars(self): self.authenticated: str = None
        if "sessionUserName" not in vars(self): self.sessionUserName: str = None
        if "role" not in vars(self): self.role: UserRole = None
        if "timeout" not in vars(self): self.timeout: str = None
        if "attemptsInteger" not in vars(self): self.attemptsInteger: int = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            __class__.__jconstructor2(self, *args)

    def __jconstructor2(self, *args) -> None:
        if True and not isinstance(args[0], (str, list, int, float)) and (args[1] is None or any(base.__name__ == "PageContext" for base in type(args[1]).__mro__)):
            __class__._constructor2_1(self, *args)
        else:
            __class__._constructor2_2(self, *args)
    

    def _constructor2_1(self, hashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        __class__.__jconstructor2(self, hashMap, pageContext.getRequest())
    

    def _constructor2_2(self, hashMap: HashMap, httpServletRequest: HttpServletRequest) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        super().__init__()
        __class__._init_fields(self)
        self.weblisketSession = WeblisketSession(hashMap, httpServletRequest)
        self.getFormData()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATION):
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
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            self.weblisketSession.clear()
            return int(TagSupport.EVAL_BODY_INCLUDE)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "invalidateSession()", e)
            return None
    

    def isSessionOld(self) -> bool:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if self.role is not None:
            timeCreated: int = self.weblisketSession.getCreationTime()
            sessionTimout: int = self.role.getSessionTimeout()
            calendar: datetime.datetime = datetime.datetime.now()
            timeFirst: int = calendar.getTimeInMillis() - sessionTimout
            if timeFirst > timeCreated:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATION):
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
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATION):
                self.logUtil.putF("Role Is Not In Session", self, "isSessionOld()")
        return java_predicate(self, "isRarelyUsedSession")
    

    def isRarelyUsedSession(self) -> bool:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        if self.role is not None:
            timeCreated: int = self.weblisketSession.getCreationTime()
            lastAccess: int = self.weblisketSession.getLastAccessedTime()
            inactivityAllowed: int = self.role.getSessionInactivityTimeout()
            calendar: datetime.datetime = datetime.datetime.now()
            timeFirst: int = calendar.getTimeInMillis() - lastAccess
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATION):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Session Is Rarely Used - Timeout: ")
                stringBuffer.appendlong(lastAccess)
                stringBuffer.append(" Eval: ")
                stringBuffer.appendlong(timeFirst)
                stringBuffer.append(" > ")
                stringBuffer.appendlong(inactivityAllowed)
                self.logUtil.putF(str(stringBuffer), self, "isRarelyUsedSession()")
        else:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATION):
                self.logUtil.putF("Role Is Not In Session", self, "isRarelyUsedSession()")
        return False
    

    def validRole(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Trying New login<p/>")
            return str(stringBuffer)
        except Exception as e:
            error: str = "Failed to set valid role"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "validRole()", e)
            return error
    

    def invalidRole(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            self.weblisketSession.setAuthenticated(False)
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Sorry your username and password is invalid on this page. ")
            stringBuffer.append("Trying New login<p/>")
            return str(stringBuffer)
        except Exception as e:
            error: str = "Failed to set role invalid"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "invalidRole()", e)
            return error
    

    # throws Exception
    def isAuthenticated(self) -> bool:
        from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
        if BooleanUtil.getInstance().getFromString(self.authenticated):
            return True
        else:
            return False
    

    def isAuthenticationSessionValid(self, roles: BasicArrayList) -> bool:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.business.user.UserInterface import UserInterface
        from org.allbinary.business.user.role.BasicUserRole import BasicUserRole
        from org.allbinary.business.user.role.UserRoleFactory import UserRoleFactory
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.data.tables.user.UserEntityInterface import UserEntityInterface
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if self.role is not None:
                if java_predicate(self, "isAuthenticated"):
                    if self.sessionUserName is not None:
                        basicUserRole: BasicUserRole = self.role.getBasicUserRole()
                        basicUserRoleArray: list[object] = roles.toArray()
                        size: int = len(basicUserRoleArray)
                        for index in range(0, size):
                            mustBeOfRole: BasicUserRole = basicUserRoleArray[index]
                            if java_equals(basicUserRole, mustBeOfRole):
                                if java_equals(basicUserRole, UserRoleFactory.getInstance().CUSTOMER):
                                    userEntityInterface: UserEntityInterface = UserEntityFactory.getInstance()
                                    userInterface: UserInterface = userEntityInterface.getUser(self.sessionUserName)
                                    if not (java_predicate(userInterface, "isSessionValid")):
                                        return False
                                return True
                    return False
            else:
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATION):
                    self.logUtil.putF("Role Is Not In Session", self, "isAuthenticationSessionValid()")
            return False
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isAuthenticatedSessionValid()", e)
            return False
    

    def nextAttempt(self) -> None:
        if self.attemptsInteger is not None and int(self.attemptsInteger) > 0:
            self.weblisketSession.setAttempts(int(int(self.attemptsInteger) + 1))
        else:
            self.weblisketSession.setAttempts(int(1))
    

    def processIfNewLogin(self, userName: str, password: str) -> bool:
        from org.allbinary.business.user.UserInterface import UserInterface
        from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
        from org.allbinary.data.tables.user.UserEntityInterface import UserEntityInterface
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.putF("Starting: " + userName, self, "processIfNewLogin()")
            if userName is not None and ((userName > StringUtil.getInstance().EMPTY_STRING) - (userName < StringUtil.getInstance().EMPTY_STRING)) != 0 and password is not None and ((password > StringUtil.getInstance().EMPTY_STRING) - (password < StringUtil.getInstance().EMPTY_STRING)) != 0:
                login: str = None
                userEntityInterface: UserEntityInterface = UserEntityFactory.getInstance()
                login = userEntityInterface.login(userName, password)
                if ((login > GLOBALS2.LOGINSUCCESS) - (login < GLOBALS2.LOGINSUCCESS)) == 0:
                    userInterface: UserInterface = userEntityInterface.getUser(userName)
                    if java_predicate(userInterface, "isSessionValid"):
                        self.weblisketSession.setAttempts(int(0))
                        return True
                self.nextAttempt()
                return False
            self.nextAttempt()
            return False
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "processIfNewLogin()", e)
            return False
    

    def processInvalidation(self) -> bool:
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if BooleanUtil.getInstance().getFromString(self.timeout):
                self.invalidateSession()
                return True
            if True:
                self.weblisketSession.setTimeout(BooleanFactory.getInstance().TRUE_STRING)
                return False
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().AUTHENTICATIONERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "processInvalidation()", e)
            return False
    

    def outputSessionInfo(self) -> str:
        from org.allbinary.logic.string.StringMaker import StringMaker
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
        from org.allbinary.business.user.role.UserRole import UserRole
        return self.role
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from javax.servlet.jsp.tagext.TagSupport import TagSupport
# from org.allbinary.business.user.UserInterface import UserInterface
# from org.allbinary.business.user.role.BasicUserRole import BasicUserRole
# from org.allbinary.business.user.role.UserRole import UserRole
# from org.allbinary.business.user.role.UserRoleFactory import UserRoleFactory
# from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
# from org.allbinary.data.tables.user.UserEntityInterface import UserEntityInterface
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
# from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


