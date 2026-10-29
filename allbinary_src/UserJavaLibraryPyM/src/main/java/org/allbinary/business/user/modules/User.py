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
# package org.allbinary.business.user.modules

from __future__ import annotations

import datetime
from org.allbinary.business.user.UserInterface import UserInterface


class User(UserInterface):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.userName: str = None
        self.prefixName: str = None
        self.firstName: str = None
        self.lastName: str = None
        self.middleName: str = None
        self.suffixName: str = None
        self.company: str = None
        self.positionAtCompany: str = None
        self.mainEmail: str = None
        self.secondaryEmail: str = None
        self.homePhone: str = None
        self.cellPhone: str = None
        self.workPhone: str = None
        self.otherContact: str = None
        self.electronicDevice: str = None
        self.fax: str = None
        self.role: UserRole = None
        self.encryption: str = None
        self.secret: str = None
        self.password: Password = None
        self.enable: str = None
        self.permissions: str = None
        self.userConfigurationInterface: UserConfigurationInterface = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor0(self) -> None:
        self._init_fields()
        self.userConfigurationInterface = UserConfigurationInterfaceFactory.getInstance()
        self.password = Password(StringUtil.getInstance().EMPTY_STRING)
    

    def _constructor1(self, request: HttpServletRequest) -> None:
        self._init_fields()
        self.getFormData(RequestParams(request).toHashMap())
        self.userConfigurationInterface = UserConfigurationInterfaceFactory.getInstance(self.getRole())
    

    def _constructor1(self, userHashMap: dict) -> None:
        self._init_fields()
        self.getFormData(userHashMap)
        self.userConfigurationInterface = UserConfigurationInterfaceFactory.getInstance(self.getRole())
    

    # throws Exception
    def getFormData(self, userHashMap: dict) -> None:
        self.userName = UserName(userHashMap).get()
        stringUtil: StringUtil = StringUtil.getInstance()
        passwordString: str = stringUtil.getNonNull(userHashMap.get(UserData.PASSWORD))
        stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
        if stringValidationUtil.isEmpty(self.userName) and stringValidationUtil.isEmpty(passwordString):
            self.userName = stringUtil.getNonNull(userHashMap.get(WeblisketSessionData.REMOVABLEUSERNAME))
            passwordString = stringUtil.getNonNull(userHashMap.get(WeblisketSessionData.REMOVABLEPASSWORD))
        encryption: str = stringUtil.getNonNull(userHashMap.get(EntryData.getInstance().ENCRYPTION))
        secret: str = stringUtil.getNonNull(userHashMap.get(UserData.SECRET))
        self.password = Password(passwordString)
        self.prefixName = stringUtil.getNonNull(userHashMap.get(UserData.PREFIXNAME))
        self.firstName = stringUtil.getNonNull(userHashMap.get(UserData.FIRSTNAME))
        self.lastName = stringUtil.getNonNull(userHashMap.get(UserData.LASTNAME))
        self.middleName = stringUtil.getNonNull(userHashMap.get(UserData.MIDDLENAME))
        self.suffixName = stringUtil.getNonNull(userHashMap.get(UserData.SUFFIXNAME))
        self.company = stringUtil.getNonNull(userHashMap.get(UserData.COMPANY))
        self.positionAtCompany = stringUtil.getNonNull(userHashMap.get(UserData.POSITIONATCOMPANY))
        self.mainEmail = stringUtil.getNonNull(userHashMap.get(UserData.MAINEMAIL))
        self.secondaryEmail = stringUtil.getNonNull(userHashMap.get(UserData.SECONDARYEMAIL))
        self.homePhone = stringUtil.getNonNull(userHashMap.get(UserData.HOMEPHONE))
        self.cellPhone = stringUtil.getNonNull(userHashMap.get(UserData.CELLPHONE))
        self.workPhone = stringUtil.getNonNull(userHashMap.get(UserData.WORKPHONE))
        self.otherContact = stringUtil.getNonNull(userHashMap.get(UserData.OTHERCONTACT))
        self.electronicDevice = stringUtil.getNonNull(userHashMap.get(UserData.ELECTRONICDEVICE))
        self.fax = stringUtil.getNonNull(userHashMap.get(UserData.FAX))
        self.role = UserRoleB.getRole(userHashMap.get(str(UserRoleData.NAME)))
        self.permissions = stringUtil.getNonNull(userHashMap.get(UserData.PERMISSIONS))
        if not stringValidationUtil.isEmpty(self.permissions) and ((self.permissions > StoreFrontData.getInstance().NAME) - (self.permissions < StoreFrontData.getInstance().NAME)) == 0:
            self.permissions = stringUtil.getNonNull(userHashMap.get(StoreFrontData.getInstance().NAME))
        elif self.permissions is None:
            self.permissions = "No Permissions"
        self.enable = stringUtil.getNonNull(userHashMap.get(EntryData.getInstance().ENABLE))
    

    def isValid(self) -> bool:
        try:
            valid: bool = True
            if not UserName.getInstance().isValid(self.userName):
                valid = False
            if not self.password.isValid():
                valid = False
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            if not stringValidationUtil.isValidRequired(self.firstName, 1, UserData.MAXLEN):
                valid = False
            if not stringValidationUtil.isValidRequired(self.lastName, 1, UserData.MAXLEN):
                valid = False
            if not stringValidationUtil.isValidRequired(self.mainEmail, 1, UserData.MAXLEN) or self.mainEmail.find("@") == -1:
                valid = False
            return valid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VALIDATIONERROR):
                commonStrings: CommonStrings = CommonStrings.getInstance()
                self.logUtil.put("Failed to validate form", self, commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringValidationUtil: StringValidationUtil = StringValidationUtil.getInstance()
            stringBuffer: StringMaker = StringMaker()
            stringBuffer.append(UserName.getValidationInfo(self.userName))
            stringBuffer.append(self.password.getValidationInfo())
            if not stringValidationUtil.isValidRequired(self.firstName, 1, UserData.MAXLEN):
                stringBuffer.append("Please enter a valid First Name.<br />")
            if not stringValidationUtil.isValidRequired(self.lastName, 1, UserData.MAXLEN):
                stringBuffer.append("Please enter a valid Last Name.<br />")
            if not stringValidationUtil.isValidRequired(self.mainEmail, 1, UserData.MAXLEN) or self.mainEmail.find("@") == -1:
                stringBuffer.append("Please enter a valid email address.<br />")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def setUserName(self, value: str) -> None:
        self.userName = value
    

    def setPrefixName(self, value: str) -> None:
        self.prefixName = value
    

    def setFirstName(self, value: str) -> None:
        self.firstName = value
    

    def setLastName(self, value: str) -> None:
        self.lastName = value
    

    def setMiddleName(self, value: str) -> None:
        self.middleName = value
    

    def setSuffixName(self, value: str) -> None:
        self.suffixName = value
    

    def setCompany(self, value: str) -> None:
        self.company = value
    

    def setPositionAtCompany(self, value: str) -> None:
        self.positionAtCompany = value
    

    def setMainEmail(self, value: str) -> None:
        self.mainEmail = value
    

    def setSecondaryEmail(self, value: str) -> None:
        self.secondaryEmail = value
    

    def setHomePhone(self, value: str) -> None:
        self.homePhone = value
    

    def setCellPhone(self, value: str) -> None:
        self.cellPhone = value
    

    def setWorkPhone(self, value: str) -> None:
        self.workPhone = value
    

    def setOtherContact(self, value: str) -> None:
        self.otherContact = value
    

    def setElectronicContact(self, value: str) -> None:
        self.electronicDevice = value
    

    def setFax(self, value: str) -> None:
        self.fax = value
    

    def setRole(self, role: UserRole) -> None:
        self.role = role
    

    def setPermissions(self, value: str) -> None:
        self.permissions = value
    

    def setEncryption(self, value: str) -> None:
        self.encryption = value
    

    def setSecret(self, value: str) -> None:
        self.secret = value
    

    def setPassword(self, value: str) -> None:
        self.password.set(value)
    

    def enable(self) -> None:
        self.setEnable("Yes")
    

    def disable(self) -> None:
        self.setEnable("No")
    

    def setEnable(self, enable: str) -> None:
        self.enable = enable
    

    def getUserName(self) -> str:
        return self.userName
    

    def getPrefixName(self) -> str:
        return self.prefixName
    

    def getFirstName(self) -> str:
        return self.firstName
    

    def getLastName(self) -> str:
        return self.lastName
    

    def getMiddleName(self) -> str:
        return self.middleName
    

    def getSuffixName(self) -> str:
        return self.suffixName
    

    def getCompany(self) -> str:
        return self.company
    

    def getPositionAtCompany(self) -> str:
        return self.positionAtCompany
    

    def getMainEmail(self) -> str:
        return self.mainEmail
    

    def getSecondaryEmail(self) -> str:
        return self.secondaryEmail
    

    def getHomePhone(self) -> str:
        return self.homePhone
    

    def getCellPhone(self) -> str:
        return self.cellPhone
    

    def getWorkPhone(self) -> str:
        return self.workPhone
    

    def getOtherContact(self) -> str:
        return self.otherContact
    

    def getElectronicContact(self) -> str:
        return self.electronicDevice
    

    def getFax(self) -> str:
        return self.fax
    

    def getRole(self) -> UserRole:
        return self.role
    

    def getPermissions(self) -> str:
        return self.permissions
    

    def getEncryption(self) -> str:
        return self.encryption
    

    def getSecret(self) -> str:
        return self.secret
    

    def getPassword(self) -> str:
        return self.password.get()
    

    # throws Exception
    def toVector(self) -> BasicArrayList:
        values: BasicArrayList = BasicArrayListD()
        values.add(self.userName)
        values.add(self.prefixName)
        values.add(self.firstName)
        values.add(self.lastName)
        values.add(self.middleName)
        values.add(self.suffixName)
        values.add(self.company)
        values.add(self.positionAtCompany)
        values.add(self.mainEmail)
        values.add(self.secondaryEmail)
        values.add(self.homePhone)
        values.add(self.cellPhone)
        values.add(self.workPhone)
        values.add(self.otherContact)
        values.add(self.electronicDevice)
        values.add(self.fax)
        values.add(str(self.getRole()))
        userConfigurationDomDocumentMapping: UserConfigurationDomDocumentMapping = UserConfigurationDomDocumentMapping(self.getUserConfigurationInterface())
        values.add(userConfigurationDomDocumentMapping.toDomDocumentString())
        values.add(self.permissions)
        values.addAllList(self.password.toVector(self.secret))
        values.add(self.enable)
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        values.add(time)
        values.add(time)
        return values
    

    # throws Exception
    def toHashMap(self) -> dict:
        values: dict = StdUtil.getInstance().createHashMap()
        values.put(UserData.USERNAME, self.userName)
        values.put(UserData.PREFIXNAME, self.prefixName)
        values.put(UserData.FIRSTNAME, self.firstName)
        values.put(UserData.LASTNAME, self.lastName)
        values.put(UserData.MIDDLENAME, self.middleName)
        values.put(UserData.SUFFIXNAME, self.suffixName)
        values.put(UserData.COMPANY, self.company)
        values.put(UserData.POSITIONATCOMPANY, self.positionAtCompany)
        values.put(UserData.MAINEMAIL, self.mainEmail)
        values.put(UserData.SECONDARYEMAIL, self.secondaryEmail)
        values.put(UserData.HOMEPHONE, self.homePhone)
        values.put(UserData.CELLPHONE, self.cellPhone)
        values.put(UserData.WORKPHONE, self.workPhone)
        values.put(UserData.OTHERCONTACT, self.otherContact)
        values.put(UserData.ELECTRONICDEVICE, self.electronicDevice)
        values.put(UserData.FAX, self.fax)
        if self.getRole() is not None:
            values.put(str(UserRoleData.NAME), str(self.getRole()))
        userConfigurationDomDocumentMapping: UserConfigurationDomDocumentMapping = UserConfigurationDomDocumentMapping(self.getUserConfigurationInterface())
        values.put(UserData.CONFIGURATION, userConfigurationDomDocumentMapping.toDomDocumentString())
        values.put(UserData.PERMISSIONS, self.permissions)
        values.putAll(self.password.toHashMap(self.secret))
        values.put(EntryData.getInstance().ENABLE, self.enable)
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        values.put(EntryData.getInstance().LASTMODIFIED, time)
        return values
    

    def toPasswordHashMap(self) -> dict:
        return self.password.toHashMap(self.secret)
    

    def validateSession(self, weblisketSession: WeblisketSessionInterface) -> None:
        weblisketSession.setAuthenticated()
        weblisketSession.setRole(self.getRole())
        weblisketSession.setUserName(self.getUserName())
    

    def updateSession(self, weblisketSession: WeblisketSessionInterface) -> None:
        pass
    

    def isSessionValid(self) -> bool:
        return True
    

    # throws Exception
    def getKey(self) -> object:
        return self.userName
    

    def toValidationInfoDoc(self) -> Document:
        return None
    

    def toValidationInfoNode(self, document: Document) -> Node:
        return None
    

    def getUserConfigurationInterface(self) -> UserConfigurationInterface:
        return self.userConfigurationInterface
    

    def setUserConfigurationInterface(self, userConfigurationInterface: UserConfigurationInterface) -> None:
        self.userConfigurationInterface = userConfigurationInterface
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.UserData import UserData
from org.allbinary.business.user.modules.configuration.UserConfigurationDomDocumentMapping import UserConfigurationDomDocumentMapping
from org.allbinary.business.user.modules.configuration.UserConfigurationInterface import UserConfigurationInterface
from org.allbinary.business.user.modules.configuration.UserConfigurationInterfaceFactory import UserConfigurationInterfaceFactory
from org.allbinary.business.user.password.Password import Password
from org.allbinary.business.user.role.UserRole import UserRole
from org.allbinary.business.user.role.UserRoleB import UserRoleB
from org.allbinary.business.user.role.UserRoleData import UserRoleData
from org.allbinary.business.user.username.UserName import UserName
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.communication.http.request.session.WeblisketSessionData import WeblisketSessionData
from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.w3c.dom.Document import Document
from org.w3c.dom.Node import Node


