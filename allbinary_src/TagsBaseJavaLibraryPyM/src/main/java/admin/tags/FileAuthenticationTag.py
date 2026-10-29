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
# package admin.tags

from __future__ import annotations

import datetime
from tags.CustomTagSupport import CustomTagSupport


class FileAuthenticationTag(CustomTagSupport):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.attemptsInteger: int = None
        self.weblisketSession: BasicWeblisketSession = None
        self.request: HttpServletRequest = None
        self.command: str = None
        self.userName: str = None
        self.password: str = None
        self.newPassword: str = None
        self.authenticated: str = None
        self.sessionUserName: str = None
        self.role: BasicUserRole = None
        self.timeout: str = None
        self.roles: BasicArrayList = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setCommand(self, command: str) -> None:
        self.command = command
    

    def setUserName(self, userName: str) -> None:
        self.userName = userName
    

    def setPassword(self, value: str) -> None:
        self.password = value
    

    def setNewPassword(self, value: str) -> None:
        self.newPassword = value
    

    def setRoles(self, values: BasicArrayList) -> None:
        self.roles = values
    

    def makeSessionValid(self, storedRole: BasicUserRole, userName: str) -> None:
        self.weblisketSession.setAuthenticated()
        self.weblisketSession.setRole(storedRole)
        self.weblisketSession.setUserName(userName)
        self.request.removeAttribute(WeblisketSessionData.REMOVABLEUSERNAME)
        self.request.removeAttribute(WeblisketSessionData.REMOVABLEPASSWORD)
    

    def getFormData(self) -> None:
        self.authenticated = self.weblisketSession.getAuthentication()
        self.sessionUserName = self.weblisketSession.getUserName()
        self.role = self.weblisketSession.getRole()
        self.attemptsInteger = self.weblisketSession.getAttempts()
        self.timeout = self.weblisketSession.getTimeout()
    

    def nextAttempt(self) -> None:
        if self.attemptsInteger is not None and int(self.attemptsInteger) > 0:
            self.weblisketSession.setAttempts(int(int(self.attemptsInteger) + 1))
        else:
            self.weblisketSession.setAttempts(int(1))
    

    # throws LicensingException
    def changePassword(self) -> bool:
        try:
            userName: str = self.request.getParameter(WeblisketSessionData.REMOVABLEUSERNAME)
            password: str = self.request.getParameter(WeblisketSessionData.REMOVABLEPASSWORD)
            newPassword: str = self.request.getParameter(WeblisketSessionData.REMOVABLENEWPASSWORD)
            newReenteredPassword: str = self.request.getParameter(WeblisketSessionData.REMOVABLEREENTERNEWPASSWORD)
            if ((newPassword > newReenteredPassword) - (newPassword < newReenteredPassword)) != 0:
                return False
            installerInfo: InstallerInfo = InstallerInfo()
            if installerInfo.isValid(userName, password):
                installerInfo.setPassword(newPassword)
                installerInfo.write()
                self.weblisketSession.setUserName(userName)
                self.weblisketSession.setPassword(newPassword)
                return True
            return False
        except LicensingException as e:
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "invalidateSession()", e)
            return False
    

    def invalidateSession(self) -> int:
        try:
            self.weblisketSession.clear()
            return int(int(TagSupport.EVAL_BODY_INCLUDE))
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "invalidateSession()", e)
            return TagSupport.SKIP_BODY
    

    # throws LicensingException
    def isSessionOld(self) -> bool:
        try:
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
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isSessionOld()", e)
            return False
    

    def isRarelyUsedSession(self) -> bool:
        if self.role is not None:
            timeCreated: int = self.weblisketSession.getCreationTime()
            lastAccess: int = self.weblisketSession.getLastAccessedTime()
            timePassed: int = self.role.getSessionInactivityTimeout()
            calendar: datetime.datetime = datetime.datetime.now()
            timeFirst: int = calendar.getTimeInMillis() - lastAccess
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATION):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Session Is Rarely Used - Timeout: ")
                stringBuffer.appendlong(lastAccess)
                stringBuffer.append(" Eval: ")
                stringBuffer.appendlong(timeFirst)
                stringBuffer.append(" > ")
                stringBuffer.appendlong(timePassed)
                self.logUtil.putF(str(stringBuffer), self, "isRarelyUsedSession()")
        else:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().AUTHENTICATION):
                self.logUtil.putF("Role Is Not In Session", self, "isRarelyUsedSession()")
        return False
    

    # throws LicensingException
    def isRoleValid(self) -> bool:
        try:
            self.makeSessionValid(BasicUserRoleFactory.getInstance().INSTALLER, self.userName)
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isRoleValid()", e)
            return False
    

    # throws LicensingException
    def validRole(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Trying New login<p>")
            return str(stringBuffer)
        except Exception as e:
            error: str = "Failed to set valid role"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "validRole()", e)
            return error
    

    # throws LicensingException
    def invalidRole(self) -> str:
        try:
            self.weblisketSession.setAuthenticated(False)
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append("Sorry your username and password is invalid on this page.")
            stringBuffer.append("Trying New login<p>")
            return str(stringBuffer)
        except Exception as e:
            error: str = "Failed to set role invalid"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "invalidRole()", e)
            return error
    

    # throws LicensingException
    def isAuthenticationSessionValid(self) -> bool:
        try:
            if BooleanUtil.getInstance().getFromString(self.authenticated):
                size: int = self.roles.size()
                for index in range(0, size):
                    mustBeOfRole: BasicUserRole = self.roles.get(index)
                    if self.sessionUserName is not None and self.role.equals(mustBeOfRole):
                        return True
                return False
            return False
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isAuthenticationSessionValid()", e)
            return False
    

    # throws LicensingException
    def processIfNewLogin(self) -> bool:
        try:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.putF("Starting for User: " + self.userName + " Attempt: " + str(self.weblisketSession.getAttempts()), self, "processIfNewLogin()")
            if self.userName is not None and ((self.userName > StringUtil.getInstance().EMPTY_STRING) - (self.userName < StringUtil.getInstance().EMPTY_STRING)) != 0 and self.password is not None and ((self.password > StringUtil.getInstance().EMPTY_STRING) - (self.password < StringUtil.getInstance().EMPTY_STRING)) != 0:
                login: str = None
                installerInfo: InstallerInfo = InstallerInfo()
                if installerInfo.isValid(self.userName, self.password):
                    login = org.allbinary.globals.GLOBALS2.LOGINSUCCESS
                else:
                    login = org.allbinary.globals.GLOBALS2.LOGINFAILED
                if ((login > org.allbinary.globals.GLOBALS2.LOGINSUCCESS) - (login < org.allbinary.globals.GLOBALS2.LOGINSUCCESS)) == 0:
                    self.weblisketSession.setAttempts(int(0))
                    return True
                self.nextAttempt()
                return False
            self.nextAttempt()
            return False
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "processIfNewLogin()", e)
            return False
    

    # throws LicensingException
    def processInvalidation(self) -> bool:
        try:
            if BooleanUtil.getInstance().getFromString(self.timeout):
                self.invalidateSession()
                return True
            if True:
                self.weblisketSession.setTimeout(BooleanFactory.getInstance().TRUE_STRING)
                return False
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isSetToInvalidate()", e)
            return False
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            stringUtil: StringUtil = StringUtil.getInstance()
            self.request = self.pageContext.getRequest()
            self.weblisketSession = BasicWeblisketSession(self.pageContext)
            self.getFormData()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF("Started", self, self.tagStrings.DO_START_TAG)
            if self.command is not None:
                if ((self.command > org.allbinary.globals.GLOBALS2.CHANGEPASSWORD) - (self.command < org.allbinary.globals.GLOBALS2.CHANGEPASSWORD)) == 0:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                        self.logUtil.putF("Change Password", self, self.tagStrings.DO_START_TAG)
                    if not self.changePassword():
                        self.pageContext.getOut().print_("Password Change Attempt Failed.<p>")
                        return self.EVAL_BODY_INCLUDE
                    else:
                        self.pageContext.getOut().print_("Password Changed Successfully.<p>")
                        return self.SKIP_BODY
                elif ((self.command > WeblisketSessionData.INVALIDATESESSION) - (self.command < WeblisketSessionData.INVALIDATESESSION)) == 0:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                        self.logUtil.putF("INVALIDATESESSION", self, self.tagStrings.DO_START_TAG)
                    return self.invalidateSession()
                else:
                    if self.isSessionOld():
                        if self.processInvalidation():
                            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                                self.logUtil.putF("Processing Invalidation", self, self.tagStrings.DO_START_TAG)
                            self.pageContext.getOut().print_("Please login again.<p>")
                            if ((self.command > org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED) - (self.command < org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED)) == 0:
                                return TagSupport.SKIP_BODY
                            else:
                                return TagSupport.EVAL_BODY_INCLUDE
                        else:
                            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                                self.logUtil.putF("Preparing session for invalidation", self, self.tagStrings.DO_START_TAG)
                            if ((self.command > org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED) - (self.command < org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED)) == 0:
                                return TagSupport.SKIP_BODY
                            else:
                                return TagSupport.EVAL_BODY_INCLUDE
                    if (self.userName is None or ((self.userName > stringUtil.EMPTY_STRING) - (self.userName < stringUtil.EMPTY_STRING)) == 0) and (self.password is None or ((self.password > stringUtil.EMPTY_STRING) - (self.password < stringUtil.EMPTY_STRING)) == 0) and self.roles is not None and self.isAuthenticationSessionValid():
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                            self.logUtil.putF("Authenticated session is valid", self, self.tagStrings.DO_START_TAG)
                        if ((self.command > org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED) - (self.command < org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED)) == 0:
                            return TagSupport.EVAL_BODY_INCLUDE
                        else:
                            return TagSupport.SKIP_BODY
                    if self.userName is not None and self.password is not None and self.processIfNewLogin():
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                            self.logUtil.putF("Processing new login.", self, self.tagStrings.DO_START_TAG)
                        if self.isRoleValid():
                            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                                self.logUtil.putF("Role is valid - Processing new login", self, self.tagStrings.DO_START_TAG)
                            self.pageContext.getOut().print_(self.validRole())
                            if ((self.command > org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED) - (self.command < org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED)) == 0:
                                return self.EVAL_BODY_INCLUDE
                            else:
                                return self.SKIP_BODY
                        else:
                            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                                self.logUtil.putF("Role is not valid - Processing new login", self, self.tagStrings.DO_START_TAG)
                            self.pageContext.getOut().print_(self.invalidRole())
                            if ((self.command > org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED) - (self.command < org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED)) == 0:
                                return self.SKIP_BODY
                            else:
                                return self.EVAL_BODY_INCLUDE
                    else:
                        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                            self.logUtil.putF("Invalid Login", self, self.tagStrings.DO_START_TAG)
                        if self.userName is not None and ((self.userName > StringUtil.getInstance().EMPTY_STRING) - (self.userName < StringUtil.getInstance().EMPTY_STRING)) != 0 and self.password is not None and ((self.password > StringUtil.getInstance().EMPTY_STRING) - (self.password < StringUtil.getInstance().EMPTY_STRING)) != 0:
                            self.pageContext.getOut().print_("Sorry your username and/or password is invalid.<p>")
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                        stringBuffer: StringMaker = StringMaker()
                        stringBuffer.append("Major authentication error - userName: ")
                        stringBuffer.append(self.userName)
                        stringBuffer.append(" Password: ")
                        stringBuffer.append(self.password)
                        stringBuffer.append(" Command: ")
                        stringBuffer.append(self.command)
                        self.logUtil.putF(str(stringBuffer), self, self.tagStrings.DO_START_TAG)
                    if ((self.command > org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED) - (self.command < org.allbinary.globals.GLOBALS2.PROCESSBODYIFAUTHENTICATED)) == 0:
                        return TagSupport.SKIP_BODY
                    else:
                        return TagSupport.EVAL_BODY_INCLUDE
            return self.SKIP_BODY
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.util.Calendar import Calendar
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.JspTagException import JspTagException
# from javax.servlet.jsp.tagext.TagSupport import TagSupport
from org.allbinary.business.init.InstallerInfo import InstallerInfo
from org.allbinary.business.user.role.BasicUserRole import BasicUserRole
from org.allbinary.business.user.role.BasicUserRoleFactory import BasicUserRoleFactory
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.http.request.session.BasicWeblisketSession import BasicWeblisketSession
from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.java.bool.BooleanUtil import BooleanUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


