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

from admin.taghelpers.TagHelper import TagHelper


class AuthenticationRequestHelper(TagHelper):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.abeClientInformation: AbeClientInformationInterface = ServiceClientInformationInterfaceFactory.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.request: HttpServletRequest = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 2:
            self._constructor2(*args)
    

    def _constructor2(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.weblisketSession = WeblisketSession(hashMap, pageContext)
        self.request = pageContext.getRequest()
    

    def _constructor2(self, hashMap: dict, httpServletRequest: HttpServletRequest) -> None:
        super().__init__()
        self._init_fields()
        self.weblisketSession = WeblisketSession(hashMap, httpServletRequest)
        self.request = httpServletRequest
    

    # throws Exception
    def generateNewPassword(self) -> str:
        if self.weblisketSession is not None and self.weblisketSession.getId() is not None:
            startIndex: int = self.weblisketSession.getId().length()
            if startIndex >= 8:
                return self.weblisketSession.getId().substring(startIndex - 8)
            else:
                raise Exception("Error Generating New Password")
        else:
            raise Exception("No Session Available For Generating New Password")
    

    def newPassword(self) -> bool:
        try:
            userName: str = self.request.getParameter(WeblisketSessionData.REMOVABLEUSERNAME)
            email: str = self.request.getParameter(UserData.MAINEMAIL)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF("Generating New Password For: " + userName, self, "newPassword()")
            userEntityInterface: UserEntityInterface = UserEntityFactory.getInstance()
            userInterface: UserInterface = userEntityInterface.getUser(userName)
            if userInterface.getMainEmail().compareTo(email) != 0:
                if userInterface.getSecondaryEmail() is not None and userInterface.getSecondaryEmail().compareTo(email) != 0:
                    if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                        self.logUtil.putF("Requested Email Is Not In User Profile", self, "newPassword()")
                    return False
            newPassword: str = self.generateNewPassword()
            userInterface.setPassword(newPassword)
            newPasswordHashMap: dict = userInterface.toPasswordHashMap()
            UserEntityFactory.getInstance().update(userName, newPasswordHashMap)
            NewPasswordEmail(self.abeClientInformation, userInterface, newPassword).process()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF("Generated New Password For: " + userName, self, "newPassword()")
            return True
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "newPassword()", e)
            return False
    

    def changePassword(self) -> bool:
        try:
            userName: str = self.request.getParameter(WeblisketSessionData.REMOVABLEUSERNAME)
            passwordString: str = self.request.getParameter(WeblisketSessionData.REMOVABLEPASSWORD)
            newPassword: str = self.request.getParameter(WeblisketSessionData.REMOVABLENEWPASSWORD)
            newReenteredPassword: str = self.request.getParameter(WeblisketSessionData.REMOVABLEREENTERNEWPASSWORD)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF("Changing Password For User: " + userName, self, "changePassword()")
            password: Password = Password(newPassword)
            if not password.isValid():
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                    self.logUtil.putF("New Password Is Not Valid", self, "changePassword()")
                return False
            if ((newPassword > newReenteredPassword) - (newPassword < newReenteredPassword)) != 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                    self.logUtil.putF("New Password Fields Do Not Match", self, "changePassword()")
                return False
            sessionPassword: str = self.weblisketSession.getPassword()
            userEntityInterface: UserEntityInterface = UserEntityFactory.getInstance()
            userInterface: UserInterface = userEntityInterface.getUser(userName)
            login: str = userEntityInterface.login(userName, passwordString)
            if ((login > self.GLOBALS2.LOGINSUCCESS) - (login < self.GLOBALS2.LOGINSUCCESS)) == 0:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                    self.logUtil.putF("Authentication Successful", self, "changePassword()")
                newPasswordHashMap: dict = password.toHashMap(None)
                UserEntityFactory.getInstance().update(userName, newPasswordHashMap)
                NewPasswordEmail(self.abeClientInformation, userInterface, newPassword).process()
                return True
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                self.logUtil.putF("Authentication Failed", self, "changePassword()")
            return False
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put("Authentication Failed", self, "changePassword()", e)
            return False
    

    def isRoleValid(self, userName: str, password: str, roles: BasicArrayList) -> bool:
        try:
            userEntityInterface: UserEntityInterface = UserEntityFactory.getInstance()
            userInterface: UserInterface = userEntityInterface.getUser(userName)
            if userInterface.getRole() is None:
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                    self.logUtil.putF("Role is null: " + str(userInterface.getRole()) + " Valid Roles: " + str(roles), self, "isRoleValid()")
                return False
            basicUserRoleArray: list[object] = roles.toArray()
            size: int = len(basicUserRoleArray)
            for index in range(0, size):
                nextRole: BasicUserRole = basicUserRoleArray[index]
                if userInterface.getRole().getBasicUserRole().equals(nextRole):
                    userInterface.validateSession(self.weblisketSession)
                    self.request.removeAttribute(WeblisketSessionData.REMOVABLEUSERNAME)
                    self.request.removeAttribute(WeblisketSessionData.REMOVABLEPASSWORD)
                    return True
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append("Role is not valid: ")
                stringBuffer.append(str(userInterface.getRole()))
                stringBuffer.append(" Valid Roles: ")
                stringBuffer.append(str(roles))
                self.logUtil.putF(str(stringBuffer), self, "isRoleValid()")
            return False
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPERERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "isRoleValid()", e)
            return False
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.UserInterface import UserInterface
from org.allbinary.business.user.password.Password import Password
from org.allbinary.business.user.role.BasicUserRole import BasicUserRole
from org.allbinary.data.tables.user.UserEntityFactory import UserEntityFactory
from org.allbinary.data.tables.user.UserEntityInterface import UserEntityInterface
from org.allbinary.globals.GLOBALS2 import GLOBALS2
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.smtp.email.NewPasswordEmail import NewPasswordEmail
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.system.security.licensing.AbeClientInformationInterface import AbeClientInformationInterface
from org.allbinary.logic.system.security.licensing.ServiceClientInformationInterfaceFactory import ServiceClientInformationInterfaceFactory


