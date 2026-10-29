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
# package org.allbinary.business.user.password

from __future__ import annotations

import random


class Password:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.password: str = None
    

    def __init__(self, password: str) -> None:
        self._init_fields()
        self.password = password
    

    def set(self, value: str) -> None:
        self.password = value
    

    def get(self) -> str:
        return self.password
    

    def isValid(self) -> bool:
        commonStrings: CommonStrings = CommonStrings.getInstance()
        try:
            valid: bool = True
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VALIDATION):
                self.logUtil.putF("Password: " + self.password, self, commonStrings.IS_VALID)
            if not StringValidationUtil.getInstance().isValidRequired(self.password, 6, UserData.MAXLEN):
                if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VALIDATION):
                    self.logUtil.putF("Password is invalid", self, commonStrings.IS_VALID)
                valid = False
            return valid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VALIDATIONERROR):
                self.logUtil.put("Failed to validate form", "Password", commonStrings.IS_VALID, e)
            return False
    

    def getValidationInfo(self) -> str:
        if not StringValidationUtil.getInstance().isValidRequired(self.password, 6, UserData.MAXLEN):
            return "Please enter a Password with more than 6 characters.<br />"
        stringUtil: StringUtil = StringUtil.getInstance()
        return stringUtil.EMPTY_STRING
    

    def toVector(self, secret: str) -> BasicArrayList:
        self.password = StringUtil.getInstance().getNonNull(self.password)
        random: int = random.Random().nextInt(SuperCrypt.KEYMAX)
        vector: BasicArrayList = BasicArrayListD()
        vector.add(str(int(random)))
        vector.add(secret)
        vector.add(SuperCrypt(random).encrypt(self.password))
        return vector
    

    def toHashMap(self, secret: str) -> dict:
        self.password = StringUtil.getInstance().getNonNull(self.password)
        values: dict = StdUtil.getInstance().createHashMap()
        random: int = random.Random().nextInt(SuperCrypt.KEYMAX)
        values.put(EntryData.getInstance().ENCRYPTION, str(int(random)))
        values.put(UserData.SECRET, secret)
        values.put(UserData.PASSWORD, SuperCrypt(random).encrypt(self.password))
        return values
# from java.util.HashMap import HashMap
# from java.util.Random import Random
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.user.UserData import UserData
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.crypt.SuperCrypt import SuperCrypt
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
from org.allbinary.string.CommonStrings import CommonStrings


