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
# package taghelpers

from __future__ import annotations

from admin.taghelpers.TagHelper import TagHelper


class InventoryHelper(TagHelper):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.basicItemData: BasicItemData = BasicItemData.getInstance()
        self.weblisketSession: WeblisketSession = None
        self.response: HttpServletResponse = None
        self.request: HttpServletRequest = None
        self.streetAddress: StreetAddress = None
        self.id: str = None
        self.searchRequest: SearchRequest = None
    

    def __init__(self, propertiesHashMap: dict, pageContext: PageContext) -> None:
        super().__init__()
        self._init_fields()
        self.response = pageContext.getResponse()
        self.request = pageContext.getRequest()
        storeName: str = propertiesHashMap.get(StoreFrontData.getInstance().NAME)
        xslFile: str = propertiesHashMap.get(TransformInfoData.getInstance().TEMPLATEFILENAME)
        if storeName is not None:
            storeFrontInterface: StoreFrontInterface = StoreFrontFactory.getInstance(storeName)
            contentType: str = AcceptableResponseGenerator.getInstance().get(self.request)
            searchParams: SearchParams = SearchParams(self.request)
            self.searchRequest = SearchRequest(storeFrontInterface, searchParams, xslFile, contentType, propertiesHashMap, pageContext)
        self.getFormData()
    

    def getFormData(self) -> None:
        self.id = self.request.getParameter(self.basicItemData.ID)
    

    def viewSummary(self) -> str:
        try:
            inventoryViewSearchInterface: InventoryViewSearchInterface = InventoryViewFactory.getInstance(self.searchRequest)
            result: str = inventoryViewSearchInterface.getProduct(self.id)
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Successfull Inventory View Summary", self, "viewSummary()")
            return result
        except Exception as e:
            error: str = "Failed to View Summary"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "viewSummary()", e)
            return error + "<br>" + "Exception: " + str(e) + "<br>"
    

    def search(self) -> str:
        try:
            stringUtil: StringUtil = StringUtil.getInstance()
            keywords: str = self.searchRequest.getParams().get().get(self.basicItemData.KEYWORDS)
            if keywords is None or ((keywords > stringUtil.EMPTY_STRING) - (keywords < stringUtil.EMPTY_STRING)) == 0:
                return "Please enter a keyword in the search field above the Search button."
            inventoryViewSearchInterface: InventoryViewSearchInterface = InventoryViewFactory.getInstance(self.searchRequest)
            result: str = inventoryViewSearchInterface.searchSingleDynamicPage()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGS):
                self.logUtil.putF("Successful Inventory Dynamic Search", self, "searchSingleDynamicPage()")
            return result
        except Exception as e:
            error: str = "Failed to search Inventory by keyword"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "searchSingleDynamicPage()", e)
            return error + "<br>" + "Exception: " + str(e) + "<br>"
# from java.util.HashMap import HashMap
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.http.HttpServletResponse import HttpServletResponse
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.business.context.modules.storefront.StoreFrontFactory import StoreFrontFactory
from org.allbinary.business.context.modules.storefront.StoreFrontInterface import StoreFrontInterface
from org.allbinary.business.user.address.StreetAddress import StreetAddress
from org.allbinary.business.user.commerce.inventory.item.BasicItemData import BasicItemData
from org.allbinary.logic.communication.http.AcceptableResponseGenerator import AcceptableResponseGenerator
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.search.SearchParams import SearchParams
from org.allbinary.logic.control.search.SearchRequest import SearchRequest
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.logic.visual.transform.info.TransformInfoData import TransformInfoData
from views.admin.inventory.listings.InventoryViewFactory import InventoryViewFactory
from views.admin.inventory.listings.InventoryViewSearchInterface import InventoryViewSearchInterface


