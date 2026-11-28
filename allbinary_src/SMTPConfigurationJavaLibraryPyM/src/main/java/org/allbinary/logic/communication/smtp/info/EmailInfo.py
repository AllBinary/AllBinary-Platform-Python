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
# package org.allbinary.logic.communication.smtp.info

from __future__ import annotations



class EmailInfo:

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        if "basicEmailInfo" not in vars(self): self.basicEmailInfo: BasicEmailInfo = None
        if "htmlAttachment" not in vars(self): self.htmlAttachment: str = None
        if "contentBase" not in vars(self): self.contentBase: str = None

    def __init__(self, *args) -> None:
        if len(args) == 1:
            __class__._constructor1(self, *args)
        elif len(args) == 3:
            __class__._constructor3(self, *args)
    

    def _constructor1(self, basicEmailInfo: BasicEmailInfo) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, commonStrings.CONSTRUCTOR)
        self.init(basicEmailInfo, None, None)
    

    def _constructor3(self, basicEmailInfo: BasicEmailInfo, htmlAttachment: str, contentBase: str) -> None:
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        __class__._init_fields(self)
        if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().EMAILLOGGING):
            commonStrings: CommonStrings = CommonStrings.getInstance()
            self.logUtil.putF(commonStrings.START, self, commonStrings.CONSTRUCTOR)
        self.init(basicEmailInfo, None, None)
    

    def init(self, basicEmailInfo: BasicEmailInfo, htmlAttachment: str, contentBase: str) -> None:
        self.basicEmailInfo = basicEmailInfo
        self.htmlAttachment = htmlAttachment
        self.contentBase = contentBase
    

    def getBasicEmailInfo(self) -> BasicEmailInfo:
        return self.basicEmailInfo
    

    def getHtmlAttachment(self) -> str:
        return self.htmlAttachment
    

    def getContentBase(self) -> str:
        return self.contentBase
    

    def toString(self) -> str:
        return "Email Info: \n " + str(self.getBasicEmailInfo())

    def __str__(self) -> str:
        return self.toString()
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


