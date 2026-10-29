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
# package org.allbinary.business.user.username

from __future__ import annotations



class UserName:
    instance: UserName = None

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.userName: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            self._constructor0(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    @staticmethod
    def getInstance() -> UserName:
        return UserName.instance
    

    def _constructor0(self) -> None:
        self._init_fields()
    

    def _constructor1(self, hashMap: dict) -> None:
        self._init_fields()
        self.userName = hashMap.get(UserData.USERNAME)
    

    def isValid(self) -> bool:
        try:
            return self.isValid(self.userName)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, "isUserNameValid()", e)
            return False
    

    def get(self) -> str:
        return self.userName
    

    # Java overloaded method: Python keeps the last definition
    def isValid(self, aUserName: str) -> bool:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            booleanFactory: BooleanFactory = BooleanFactory.getInstance()
            valid: bool = booleanFactory.TRUE
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VALIDATION):
                self.logUtil.putF("UserName: " + aUserName, self, commonStrings.IS_VALID)
            if not StringValidationUtil.getInstance().isValidRequired(aUserName, 5, UserData.MAXLEN):
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VALIDATION):
                    self.logUtil.putF("UserName is invalid", self, commonStrings.IS_VALID)
                valid = booleanFactory.FALSE
            return valid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, commonStrings.IS_VALID, e)
            return False
    

    @staticmethod
    def getValidationInfo(aUserName: str) -> str:
        if not StringValidationUtil.getInstance().isValidRequired(aUserName, 5, UserData.MAXLEN):
            return "Please enter a User Name with more than 5 characters.<br/>"
        return StringUtil.getInstance().EMPTY_STRING
# from java.util.HashMap import HashMap
from org.allbinary.business.user.UserData import UserData
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonStrings import CommonStrings


UserName.instance = UserName()

