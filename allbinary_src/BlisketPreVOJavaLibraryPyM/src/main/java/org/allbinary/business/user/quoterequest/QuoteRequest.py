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
# package org.allbinary.business.user.quoterequest

from __future__ import annotations

import datetime


class QuoteRequest:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.id: str = None
        self.userName: str = None
        self.projectInfo: str = None
        self.userComments: str = None
        self.budget: str = None
        self.timeFrame: str = None
        self.comments: str = None

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor2(self, userName: str, request: HttpServletRequest) -> None:
        self._init_fields()
        quoteRequestData: QuoteRequestData = QuoteRequestData.getInstance()
        self.id = QuoteRequestIdGenerator().getNext()
        self.setUserName(userName)
        self.setProjectInfo(request.getParameter(quoteRequestData.PROJECT_INFO))
        self.setUserComments(request.getParameter(quoteRequestData.CUSTOMER_COMMENTS))
        self.setBudget(request.getParameter(quoteRequestData.BUDGET))
        self.setTimeFrame(request.getParameter(quoteRequestData.TIMEFRAME))
        self.setComments(request.getParameter(quoteRequestData.COMMENTS))
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
            self.logUtil.putF("Created with: " + str(self.toHashMap()), self, self.commonStrings.CONSTRUCTOR)
    

    def _constructor1(self, hashMap: dict) -> None:
        self._init_fields()
        quoteRequestData: QuoteRequestData = QuoteRequestData.getInstance()
        self.id = hashMap.get(quoteRequestData.ID)
        self.setUserName(hashMap.get(UserData.USERNAME))
        self.setProjectInfo(hashMap.get(quoteRequestData.PROJECT_INFO))
        self.setUserComments(hashMap.get(quoteRequestData.CUSTOMER_COMMENTS))
        self.setBudget(hashMap.get(quoteRequestData.BUDGET))
        self.setTimeFrame(hashMap.get(quoteRequestData.TIMEFRAME))
        self.setComments(hashMap.get(quoteRequestData.COMMENTS))
        if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().TAGHELPER):
            self.logUtil.putF("Created with: " + str(self.toHashMap()), self, self.commonStrings.CONSTRUCTOR)
    

    def isValid(self) -> bool:
        try:
            valid: bool = True
            if self.userName is None or len(self.userName) < 4 or len(self.userName) > 250:
                valid = False
            if self.projectInfo is None or len(self.projectInfo) < 0 or len(self.projectInfo) > AbSqlData.MAXBLOB:
                valid = False
            if self.userComments is None or len(self.userComments) < 0 or len(self.userComments) > AbSqlData.MAXBLOB:
                valid = False
            if self.budget is None or len(self.budget) < 0 or len(self.budget) > AbSqlData.MAXBLOB:
                valid = False
            if self.timeFrame is None or len(self.timeFrame) < 0 or len(self.timeFrame) > AbSqlData.MAXBLOB:
                valid = False
            if self.comments is None or len(self.comments) < 0 or len(self.comments) > AbSqlData.MAXBLOB:
                valid = False
            return valid
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to validate form", self, self.commonStrings.IS_VALID, e)
            return False
    

    def validationInfo(self) -> str:
        try:
            stringBuffer: StringMaker = StringMaker()
            if self.userName is None or len(self.userName) < 4 or len(self.userName) > 250:
                stringBuffer.append("Please enter a User Name with more than 4 characters.<br>")
            if self.projectInfo is None or len(self.projectInfo) < 0 or len(self.projectInfo) > AbSqlData.MAXBLOB:
                stringBuffer.append("Please enter Project Info with less than " + str(AbSqlData.MAXBLOB) + " characters.<br>")
            if self.userComments is None or len(self.userComments) < 0 or len(self.userComments) > AbSqlData.MAXBLOB:
                stringBuffer.append("Please enter User Comments with less than " + str(AbSqlData.MAXBLOB) + " characters.<br>")
            if self.budget is None or len(self.budget) < 0 or len(self.budget) > AbSqlData.MAXBLOB:
                stringBuffer.append("Please enter Budget with less than " + str(AbSqlData.MAXBLOB) + " characters.<br>")
            if self.timeFrame is None or len(self.timeFrame) < 0 or len(self.timeFrame) > AbSqlData.MAXBLOB:
                stringBuffer.append("Please enter time frame with less than " + str(AbSqlData.MAXBLOB) + " characters.<br>")
            if self.comments is None or len(self.comments) < 0 or len(self.comments) > AbSqlData.MAXBLOB:
                stringBuffer.append("Please enter comments with less than " + str(AbSqlData.MAXBLOB) + " characters.<br>")
            return str(stringBuffer)
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put("Failed to generate validation error info", self, "validationInfo()", e)
            return "Error Validating Form"
    

    def toVector(self) -> BasicArrayList:
        values: BasicArrayList = BasicArrayListD()
        values.add(self.id)
        values.add(self.userName)
        values.add(self.projectInfo)
        values.add(self.userComments)
        values.add(self.budget)
        values.add(self.timeFrame)
        values.add(self.comments)
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        values.add(time)
        values.add(time)
        return values
    

    def toHashMap(self) -> dict:
        quoteRequestData: QuoteRequestData = QuoteRequestData.getInstance()
        values: dict = StdUtil.getInstance().createHashMap()
        values.put(UserData.USERNAME, self.userName)
        values.put(quoteRequestData.PROJECT_INFO, self.projectInfo)
        values.put(quoteRequestData.CUSTOMER_COMMENTS, self.userComments)
        values.put(quoteRequestData.BUDGET, self.budget)
        values.put(quoteRequestData.TIMEFRAME, self.timeFrame)
        values.put(quoteRequestData.COMMENTS, self.comments)
        calendar: datetime.datetime = datetime.datetime.now()
        time: str = str(str(int(calendar.getTimeInMillis())))
        values.put(EntryData.getInstance().LASTMODIFIED, time)
        return values
    

    def setUserName(self, value: str) -> None:
        self.userName = value
    

    def setProjectInfo(self, value: str) -> None:
        self.projectInfo = value
    

    def setUserComments(self, value: str) -> None:
        self.userComments = value
    

    def setBudget(self, value: str) -> None:
        self.budget = value
    

    def setTimeFrame(self, value: str) -> None:
        self.timeFrame = value
    

    def setComments(self, value: str) -> None:
        self.comments = value
        stringUtil: StringUtil = StringUtil.getInstance()
        if self.comments is None:
            self.comments = stringUtil.EMPTY_STRING
    

    def getUserName(self) -> str:
        return self.userName
    

    def getProjectInfo(self) -> str:
        return self.projectInfo
    

    def getUserComments(self) -> str:
        return self.userComments
    

    def getBudget(self) -> str:
        return self.budget
    

    def getTimeFrame(self) -> str:
        return self.timeFrame
    

    def getComments(self) -> str:
        return self.comments
# from java.util.Calendar import Calendar
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
from org.allbinary.business.entry.EntryData import EntryData
from org.allbinary.business.quoterequest.QuoteRequestData import QuoteRequestData
from org.allbinary.business.user.UserData import UserData
from org.allbinary.data.generator.QuoteRequestIdGenerator import QuoteRequestIdGenerator
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.communication.sql.AbSqlData import AbSqlData
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings


