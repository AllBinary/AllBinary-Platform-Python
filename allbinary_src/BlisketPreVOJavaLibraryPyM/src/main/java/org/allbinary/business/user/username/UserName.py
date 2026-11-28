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

from java.lang.JavaRuntimeStatic import lazy_static


class UserName:
    instance: UserName = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "userName" not in vars(self): self.userName: str = None

    def __init__(self, *args) -> None:
        if len(args) == 0:
            __class__._constructor0(self, *args)
        elif len(args) == 1:
            __class__._constructor1(self, *args)
    

    @staticmethod
    def getInstance() -> UserName:
        return UserName.instance
    

    def _constructor0(self) -> None:
        __class__._init_fields(self)
    

    def _constructor1(self, hashMap: HashMap) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.business.user.UserData import UserData
        __class__._init_fields(self)
        self.userName = hashMap.get(UserData.USERNAME)
    

    def isValid_j0(self) -> bool:
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            return self.isValid(self.userName)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, "isUserNameValid()", e)
            return False
    

    def get(self) -> str:
        return self.userName
    

    def isValid_j1(self, aUserName: str) -> bool:
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            booleanFactory: BooleanFactory = BooleanFactory.getInstance()
            valid: bool = booleanFactory.TRUE
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VALIDATION):
                self.logUtil.putF("UserName: " + aUserName, self, commonStrings.IS_VALID)
            if not (StringValidationUtil.getInstance().isValidRequired(aUserName, 5, UserData.MAXLEN)):
                if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VALIDATION):
                    self.logUtil.putF("UserName is invalid", self, commonStrings.IS_VALID)
                valid = booleanFactory.FALSE
            return valid
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, commonStrings.IS_VALID, e)
            return False

    def isValid(self, *args):
        implementation = __class__.__dict__.get("isValid_j" + str(len(args)))
        if implementation is not None: return implementation.__get__(self, __class__)(*args)
        return super().isValid(*args)
    

    @staticmethod
    def getValidationInfo(aUserName: str) -> str:
        from org.allbinary.business.user.UserData import UserData
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        if not (StringValidationUtil.getInstance().isValidRequired(aUserName, 5, UserData.MAXLEN)):
            return "Please enter a User Name with more than 5 characters.<br/>"
        return StringUtil.getInstance().EMPTY_STRING
# from java.util.HashMap import HashMap
# from org.allbinary.business.user.UserData import UserData
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.java.bool.BooleanFactory import BooleanFactory
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


def _UserName_instance() -> object:
    return UserName()

lazy_static(UserName, "instance", _UserName_instance)

