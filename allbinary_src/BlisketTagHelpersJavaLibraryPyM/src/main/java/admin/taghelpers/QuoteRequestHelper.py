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

from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from admin.taghelpers.ModifyTable import ModifyTable


#TWB - Am I missing the correct Quote Request? Probably not
@java_inherited_overloads
class QuoteRequestHelper(ModifyTable):
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("weblisketSession", None)
        vars(self).setdefault("storeFrontInterface", None)
        vars(self).setdefault("quoteRequest", None)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "weblisketSession" not in vars(self): self.weblisketSession: WeblisketSession = None
        if "storeFrontInterface" not in vars(self): self.storeFrontInterface: StoreFrontInterface = None
        if "quoteRequest" not in vars(self): self.quoteRequest: QuoteRequest = None
    

    def __init__(self, hashMap: HashMap, pageContext: PageContext) -> None:
        __class__._java_defaults(self)
        from java.util.HashMap import HashMap
        from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
        from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
        from org.allbinary.business.user.quoterequest.QuoteRequest import QuoteRequest
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        super().__init__()
        __class__._init_fields(self)
        request: HttpServletRequest = pageContext.getRequest()
        self.weblisketSession = WeblisketSession(hashMap, pageContext)
        self.quoteRequest = QuoteRequest(self.weblisketSession.getUserName(), request)
        storeName: str = hashMap.get(StoreFrontData.getInstance().NAME)
        if storeName is not None:
            self.storeFrontInterface = StoreFrontFactory.getInstance(storeName)
    

    def isValid(self) -> bool:
        return java_predicate(self.quoteRequest, "isValid")
    

    def validationInfo(self) -> str:
        return self.quoteRequest.validationInfo()
    

    def insert(self) -> str:
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from org.allbinary.data.tables.user.quoterequest.QuoteRequestEntityFactory import QuoteRequestEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            values: BasicArrayList = self.quoteRequest.toVector()
            QuoteRequestEntityFactory.getInstance().getQuoteRequestEntityInstance().insert(values)
            success: str = "New QuoteRequest Successfully added to the QuoteRequest Table"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "add()")
            return success
        except Exception as e:
            error: str = "Failed to add QuoteRequest"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "add()", e)
            return error
    

    def update(self) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.data.tables.user.quoterequest.QuoteRequestEntityFactory import QuoteRequestEntityFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            values: HashMap = self.quoteRequest.toHashMap()
            QuoteRequestEntityFactory.getInstance().getQuoteRequestEntityInstance().update(self.quoteRequest.getUserName(), values)
            success: str = "New QuoteRequest Successfully updated"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF(success, self, "update()")
            return success
        except Exception as e:
            error: str = "Failed to update QuoteRequest"
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "update()", e)
            return error
    

    def delete(self) -> str:
        return self.commonStrings.NOT_IMPLEMENTED
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
# from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
# from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
# from org.allbinary.business.user.quoterequest.QuoteRequest import QuoteRequest
# from org.allbinary.data.tables.user.quoterequest.QuoteRequestEntityFactory import QuoteRequestEntityFactory
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


