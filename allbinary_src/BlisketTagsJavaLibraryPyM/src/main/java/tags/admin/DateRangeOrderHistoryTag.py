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
# package tags.admin

from __future__ import annotations

from tags.StoreValidationTransformTag import StoreValidationTransformTag


class DateRangeOrderHistoryTag(StoreValidationTransformTag):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.status: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setStatus(self, value: str) -> None:
        self.status = value
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF("Tag Start", self, self.tagStrings.DO_START_TAG)
            self.setName("Range Order History View")
            self.setObjectFile("views.admin.orderhistory.DateRangeOrderHistoryView")
            if self.getCommand() is not None:
                if self.getCommand().compareTo(GLOBALS2.VIEW) == 0:
                    pass
                else:
                    raise Exception("No Such View Command: " + str(self.getCommand()))
                return super().doStartTag()
            raise Exception("Command Null")
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


