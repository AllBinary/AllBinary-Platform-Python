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

from tags.CustomTagSupport import CustomTagSupport


class AuthenticationTag(CustomTagSupport):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.command: str = None
        self.userName: str = None
        self.password: str = None
        self.newPassword: str = None
        self.roles: BasicArrayList = None
        self.propertiesHashMap: dict = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
        stringUtil: StringUtil = StringUtil.getInstance()
        self.userName = stringUtil.EMPTY_STRING
        self.password = stringUtil.EMPTY_STRING
    

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
    

    # throws LicensingException
    def changePassword(self) -> bool:
        try:
            anyType: object = AuthenticationRequestHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("changePassword", None)
            result: bool = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "changePassword()", e)
            return False
    

    # throws LicensingException
    def newPassword(self) -> bool:
        try:
            anyType: object = AuthenticationRequestHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("newPassword", None)
            result: bool = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "newPassword()", e)
            return False
    

    # throws LicensingException
    def invalidateSession(self) -> int:
        try:
            anyType: object = AuthenticationHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("invalidateSession", None)
            resultInteger: int = method.invoke(anyType, None)
            return int(resultInteger)
        except LicensingException as e:
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "invalidateSession()", e)
            return TagSupport.SKIP_BODY
    

    # throws LicensingException
    def isSessionOld(self) -> bool:
        try:
            anyType: object = AuthenticationHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            helperClass: type = type(anyType)
            method: Method = helperClass.getMethod("isSessionOld", None)
            resultBoolean: bool = method.invoke(anyType, None)
            return resultBoolean
        except LicensingException as e:
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isSessionOld()", e)
            return False
    

    # throws LicensingException
    def isRoleValid(self) -> bool:
        try:
            anyType: object = AuthenticationRequestHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            addressHelperClass: type = type(anyType)
            methodParams: list[type] = [type(self.userName), type(self.password), type(self.roles)]
            method: Method = addressHelperClass.getMethod("isRoleValid", methodParams)
            methodArgs: list[object] = [self.userName, self.password, self.roles]
            resultBoolean: bool = method.invoke(anyType, methodArgs)
            return resultBoolean
        except LicensingException as e:
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isRoleValid()", e)
            return False
    

    # throws LicensingException
    def validRole(self) -> str:
        try:
            anyType: object = AuthenticationHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("validRole", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to set valid role"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "validRole()", e)
            return error
    

    # throws LicensingException
    def invalidRole(self) -> str:
        try:
            anyType: object = AuthenticationHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("invalidRole", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to set role invalid"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "invalidRole()", e)
            return error
    

    # throws LicensingException
    def isAuthenticationSessionValid(self) -> bool:
        try:
            anyType: object = AuthenticationHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            addressHelperClass: type = type(anyType)
            methodParams: list[type] = [type(self.roles)]
            method: Method = addressHelperClass.getMethod("isAuthenticationSessionValid", methodParams)
            methodArgs: list[object] = [self.roles]
            resultBoolean: bool = method.invoke(anyType, methodArgs)
            return resultBoolean
        except LicensingException as e:
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isAuthenticationSessionValid()", e)
            return False
    

    # throws LicensingException
    def processIfNewLogin(self) -> bool:
        try:
            anyType: object = AuthenticationHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            helperClass: type = type(anyType)
            methodParams: list[type] = [type(self.userName), type(self.password)]
            method: Method = helperClass.getMethod("processIfNewLogin", methodParams)
            methodArgs: list[object] = [self.userName, self.password]
            resultBoolean: bool = method.invoke(anyType, methodArgs)
            return resultBoolean
        except LicensingException as e:
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "processIfNewLogin()", e)
            return False
    

    # throws LicensingException
    def processInvalidation(self) -> bool:
        try:
            anyType: object = AuthenticationHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            addressHelperClass: type = type(anyType)
            method: Method = addressHelperClass.getMethod("processInvalidation", None)
            resultBoolean: bool = method.invoke(anyType, None)
            return resultBoolean
        except LicensingException as e:
            raise e
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isSetToInvalidate()", e)
            return False
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            stringUtil: StringUtil = StringUtil.getInstance()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                request: HttpServletRequest = self.pageContext.getRequest()
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append(" Request URI: ")
                stringBuffer.append(request.getRequestURI())
                self.logUtil.putF(str(stringBuffer), self, self.tagStrings.DO_START_TAG)
            if self.command is not None:
                self.propertiesHashMap = StdUtil.getInstance().createHashMap()
                if ((self.command > org.allbinary.globals.GLOBALS2.NEWPASSWORD) - (self.command < org.allbinary.globals.GLOBALS2.NEWPASSWORD)) == 0:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                        self.logUtil.putF("New Password", self, self.tagStrings.DO_START_TAG)
                    if not self.newPassword():
                        self.pageContext.getOut().print_("New Password Request Failed.<p/>")
                        return self.EVAL_BODY_INCLUDE
                    else:
                        self.pageContext.getOut().print_("New Password Was Sent.<p/>")
                        return self.SKIP_BODY
                elif ((self.command > org.allbinary.globals.GLOBALS2.CHANGEPASSWORD) - (self.command < org.allbinary.globals.GLOBALS2.CHANGEPASSWORD)) == 0:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                        self.logUtil.putF("Change Password", self, self.tagStrings.DO_START_TAG)
                    if not self.changePassword():
                        self.pageContext.getOut().print_("Password Change Attempt Failed.<p/>")
                        return self.EVAL_BODY_INCLUDE
                    else:
                        self.pageContext.getOut().print_("Password Changed Successfully.<p/>")
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
                        if self.userName is not None and ((self.userName > stringUtil.EMPTY_STRING) - (self.userName < stringUtil.EMPTY_STRING)) != 0 and self.password is not None and ((self.password > stringUtil.EMPTY_STRING) - (self.password < stringUtil.EMPTY_STRING)) != 0:
                            self.pageContext.getOut().print_("Sorry your username and/or password is invalid.<p/>")
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().JSPTAG):
                        self.logUtil.putF(str(StringMaker().append("Major authentication error - userName: ").append(self.userName).append(" Password: ").append(self.password).append(" Command: ").append(self.command)), self, self.tagStrings.DO_START_TAG)
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
# from java.lang.reflect.Method import Method
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.JspTagException import JspTagException
# from javax.servlet.jsp.tagext.TagSupport import TagSupport
from admin.taghelpers.AuthenticationHelperFactory import AuthenticationHelperFactory
from admin.taghelpers.AuthenticationRequestHelperFactory import AuthenticationRequestHelperFactory
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


