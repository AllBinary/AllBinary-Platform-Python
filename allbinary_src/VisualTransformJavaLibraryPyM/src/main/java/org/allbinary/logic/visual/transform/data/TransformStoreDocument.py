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
# package org.allbinary.logic.visual.transform.data

from __future__ import annotations

from org.allbinary.logic.visual.transform.data.TransformHttpRequestDocument import TransformHttpRequestDocument


class TransformStoreDocument(TransformHttpRequestDocument):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self._constructor2(*args)
        elif len(args) == 1:
            self._constructor1(*args)
    

    def _constructor2(self, pageContext: PageContext, weblisketSession: WeblisketSession) -> None:
        super().__init__(pageContext, weblisketSession)
        self._init_fields()
        try:
            storeName: str = weblisketSession.getStoreName()
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEW):
                self.logUtil.putF("Using Session StoreName: " + storeName, self, self.commonStrings.CONSTRUCTOR)
            self.getBaseNode().appendChild(StoreFrontViewFactory.getInstance(storeName).toXmlNode(self.getDoc()))
            self.getBaseNode().appendChild(RequestParams(pageContext.getRequest()).toXmlNode(self.getDoc()))
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
            raise e
    

    def _constructor1(self, searchRequest: SearchRequest) -> None:
        super().__init__(searchRequest)
        self._init_fields()
        try:
            self.getBaseNode().appendChild(StoreFrontViewFactory.getInstance(searchRequest.getStoreFront().getName()).toXmlNode(self.getDoc()))
            self.getBaseNode().appendChild(searchRequest.getParams().getParamsNode(self.getDoc()))
        except Exception as e:
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().VIEWERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
            raise e
# from javax.servlet.http.HttpServletRequest import HttpServletRequest
# from javax.servlet.jsp.PageContext import PageContext
from org.allbinary.business.context.modules.storefront.StoreFrontViewFactory import StoreFrontViewFactory
from org.allbinary.logic.communication.http.request.RequestParams import RequestParams
from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.control.search.SearchRequest import SearchRequest


