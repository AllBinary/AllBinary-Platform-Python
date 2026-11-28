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



class MultipartRequestParamForwardHelper:

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "pageContext" not in vars(self): self.pageContext: PageContext = None
        if "requestMapInterface" not in vars(self): self.requestMapInterface: RequestMapInterface = None
        if "page" not in vars(self): self.page: str = None
        if "command" not in vars(self): self.command: str = None
        if "paramVector" not in vars(self): self.paramVector: BasicArrayList = None
    

    def __init__(self, parentHelperTag: HelperTag, page: str, command: str, paramVector: BasicArrayList, pageContext: PageContext) -> None:
        from admin.taghelpers.InventoryItemViewParentTagHelper import InventoryItemViewParentTagHelper
        from org.allbinary.util.BasicArrayList import BasicArrayList
        from tags.HelperTag import HelperTag
        __class__._init_fields(self)
        self.pageContext = pageContext
        self.page = page
        self.command = command
        self.paramVector = paramVector
        self.requestMapInterface = InventoryItemViewParentTagHelper.getInstance().getRequestMapInterface(parentHelperTag)
    

    # throws Exception
    def forward(self) -> None:
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if self.shouldForward():
                params: str = self.getParams()
                stringBuffer: StringMaker = StringMaker()
                stringBuffer.append(self.page)
                stringBuffer.append(params)
                self.pageContext.forward(str(stringBuffer))
        except Exception as e:
            commonStrings: CommonStrings = CommonStrings.getInstance()
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(commonStrings.EXCEPTION, self, "forward()", e)
    

    def getParams(self) -> str:
        from java.util.HashMap import HashMap
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.string.CommonSeps import CommonSeps
        commonSeps: CommonSeps = CommonSeps.getInstance()
        AMP: str = commonSeps.AMPERSAND
        QUESTION: str = commonSeps.QUESTION
        EQUALS: str = commonSeps.EQUALS
        hashMap: HashMap = self.requestMapInterface.getRequestHashMap()
        stringBuffer: StringMaker = StringMaker()
        size: int = self.paramVector.size()
        for index in range(0, size):
            key: str = self.paramVector.get(index)
            value: str = hashMap.get(key)
            if index != 0:
                stringBuffer.append(AMP)
            else:
                stringBuffer.append(QUESTION)
            stringBuffer.append(key)
            stringBuffer.append(EQUALS)
            stringBuffer.append(value)
        return str(stringBuffer)
    

    def shouldForward(self) -> bool:
        from java.util.HashMap import HashMap
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
        hashMap: HashMap = self.requestMapInterface.getRequestHashMap()
        requestCommand: str = hashMap.get(GLOBALS2.ADMINCOMMAND)
        if StringValidationUtil.getInstance().isEmpty(self.command) or (not (StringValidationUtil.getInstance().isEmpty(requestCommand)) and ((self.command > requestCommand) - (self.command < requestCommand)) == 0):
            return True
        return False
# from java.util.HashMap import HashMap
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListD import BasicArrayListD
# from javax.servlet.jsp.PageContext import PageContext
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.logic.communication.http.request.RequestMapInterface import RequestMapInterface
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringValidationUtil import StringValidationUtil
# from org.allbinary.string.CommonSeps import CommonSeps
# from org.allbinary.string.CommonStrings import CommonStrings
# from tags.HelperTag import HelperTag
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


