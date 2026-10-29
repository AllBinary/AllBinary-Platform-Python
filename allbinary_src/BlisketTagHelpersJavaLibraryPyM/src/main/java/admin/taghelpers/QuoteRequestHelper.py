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

from admin.taghelpers.ModifyTable import ModifyTable


#TWB - Am I missing the correct Quote Request? Probably not
class QuoteRequestHelper(ModifyTable):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.storeFrontInterface: StoreFrontInterface = None
        self.quoteRequest: QuoteRequest = None
    

    def __init__(self, hashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        request: HttpServletRequest = pageContext.getRequest()
        self.weblisketSession = WeblisketSession(hashMap, pageContext)
        self.quoteRequest = QuoteRequest(self.weblisketSession.getUserName(), request)
        storeName: str = hashMap.get(StoreFrontData.getInstance().NAME)
        if storeName is not None:
            self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
    

    def isValid(self) -> bool:
        return self.quoteRequest.isValid()
    

    def validationInfo(self) -> str:
        return self.quoteRequest.validationInfo()
    

    def insert(self) -> str:
        try:
            values: BasicArrayList = self.quoteRequest.toVector()
            QuoteRequestEntityFactory.getInstance().getQuoteRequestEntityInstance().insert(values)
            success: str = "New QuoteRequest Successfully added to the QuoteRequest Table"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "add()")
            return success
        except Exception as e:
            error: str = "Failed to add QuoteRequest"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "add()", e)
            return error
    

    def update(self) -> str:
        try:
            values: dict = self.quoteRequest.toHashMap()
            QuoteRequestEntityFactory.getInstance().getQuoteRequestEntityInstance().update(self.quoteRequest.getUserName(), values)
            success: str = "New QuoteRequest Successfully updated"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update QuoteRequest"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    def delete(self) -> str:
        return self.commonStrings.NOT_IMPLEMENTED
# from java.util.HashMap import HashMap
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.quoterequest.QuoteRequest import QuoteRequest
from org.allbinary.data.tables.user.quoterequest.QuoteRequestEntityFactory import QuoteRequestEntityFactory
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.log.LogUtil import LogUtil


