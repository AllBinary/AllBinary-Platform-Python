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
# package admin.tags

from __future__ import annotations

from tags.CustomTagSupport import CustomTagSupport


class CustomLoaderTag(CustomTagSupport):

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.command: str = None
        self.webappPath: str = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setCommand(self, command: str) -> None:
        self.command = command
    

    def setWebappPath(self, value: str) -> None:
        self.webappPath = value
    

    # throws LicensingException
    def setCustomLoaderWebappPath(self) -> None:
        from org.allbinary.globals.AppUrlGlobals import AppUrlGlobals
        from org.allbinary.globals.URLGLOBALS import URLGLOBALS
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            urlGlobals: AppUrlGlobals = AppUrlGlobals()
            urlGlobals.setWebappPath(self.webappPath)
            URLGLOBALS.init(urlGlobals)
        except Exception as e:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAGERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "setCustomLoaderWebappPath()", e)
    

    # throws JspTagException
    def doStartTag(self) -> int:
        from org.allbinary.globals.GLOBALS2 import GLOBALS2
        from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
        from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
        from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
        from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes
        try:
            if LogConfigTypes.LOGGING.contains(LogConfigTypeFactory.getInstance().JSPTAG):
                self.logUtil.putF(self.commonStrings.START, self, self.tagStrings.DO_START_TAG)
            if self.command is not None:
                if ((self.command > GLOBALS2.SET) - (self.command < GLOBALS2.SET)) == 0:
                    self.setCustomLoaderWebappPath()
            return self.SKIP_BODY
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from javax.servlet.jsp.JspTagException import JspTagException
# from org.allbinary.globals.AppUrlGlobals import AppUrlGlobals
# from org.allbinary.globals.GLOBALS2 import GLOBALS2
# from org.allbinary.globals.URLGLOBALS import URLGLOBALS
# from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException
# from org.allbinary.logic.communication.log.config.type.LogConfigTypeFactory import LogConfigTypeFactory
# from org.allbinary.logic.communication.log.config.type.LogConfigTypes import LogConfigTypes


