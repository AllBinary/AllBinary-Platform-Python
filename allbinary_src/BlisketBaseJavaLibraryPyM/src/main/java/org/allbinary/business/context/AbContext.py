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
# package org.allbinary.business.context

from __future__ import annotations



class AbContext:

    def _init_fields(self) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.propertiesHashMap: HashMap = None
        self.pageContext: PageContext = None
    

    def __init__(self, propertiesHashMap: HashMap, pageContext: PageContext) -> None:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        self._init_fields()
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().VIEW):
            self.logUtil.putF("Properties HashMap: " + str(propertiesHashMap), self, self.commonStrings.CONSTRUCTOR)
        self.propertiesHashMap = propertiesHashMap
        self.pageContext = pageContext
    

    def getWeblisketSession(self) -> WeblisketSessionInterface:
        from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
        from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
        return WeblisketSession(self.propertiesHashMap, self.pageContext)
    

    def getPageContext(self) -> PageContext:
        return self.pageContext
    

    def getPropertiesHashMap(self) -> HashMap:
        from java.util.HashMap import HashMap
        return self.propertiesHashMap
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.logic.communication.http.request.session.WeblisketSession import WeblisketSession
# from org.allbinary.logic.communication.http.request.session.WeblisketSessionInterface import WeblisketSessionInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


