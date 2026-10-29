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


class StoreFrontTag(CustomTagSupport):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.command: str = None
        self.storeName: str = None
        self.propertiesHashMap: dict = None
    

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def setCommand(self, command: str) -> None:
        self.command = command
    

    def setStoreName(self, value: str) -> None:
        self.storeName = value
    

    # throws LicensingException
    def getCurrentLocation(self) -> str:
        try:
            anyType: object = StoreFrontHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            method: Method = type(anyType).getMethod("getCurrentLocation", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to retrieve current location"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getCurrentLocation()", e)
            return error
    

    # throws LicensingException
    def getCurrentHomeLocation(self) -> str:
        try:
            anyType: object = StoreFrontHelperFactory().getInstance(self.propertiesHashMap, self.pageContext)
            method: Method = type(anyType).getMethod("getCurrentHomeLocation", None)
            result: str = method.invoke(anyType, None)
            return result
        except LicensingException as e:
            raise e
        except Exception as e:
            error: str = "Failed to retrieve current home location"
            if org.allbinary.logic.communication.log.config.type_.LogConfigTypes.LOGGING.contains(org.allbinary.logic.communication.log.config.type_.LogConfigTypeFactory.getInstance().SQLTAGSERROR):
                self.logUtil.put(self.commonStrings.EXCEPTION, self, "getCurrentHomeLocation()", e)
            return error
    

    # throws JspTagException
    def doStartTag(self) -> int:
        try:
            if self.command is not None:
                self.propertiesHashMap = StdUtil.getInstance().createHashMap()
                self.propertiesHashMap.put(StoreFrontData.getInstance().NAME, self.storeName)
                if ((self.command > org.allbinary.globals.GLOBALS2.GETCURRENTLOCATION) - (self.command < org.allbinary.globals.GLOBALS2.GETCURRENTLOCATION)) == 0:
                    self.pageContext.getOut().print_(self.getCurrentLocation())
                elif ((self.command > org.allbinary.globals.GLOBALS2.GETCURRENTHOMELOCATION) - (self.command < org.allbinary.globals.GLOBALS2.GETCURRENTHOMELOCATION)) == 0:
                    self.pageContext.getOut().print_(self.getCurrentHomeLocation())
            return self.SKIP_BODY
        except LicensingException as e:
            AbResponseHandler.sendJspTagLicensingRedirect(self.pageContext, e)
            return self.SKIP_BODY
        except Exception as e:
            AbResponseHandler.sendJspTagRedirect(self.pageContext, e)
            return self.SKIP_BODY
# from java.lang.reflect.Method import Method
# from java.util.HashMap import HashMap
# from javax.servlet.jsp.JspTagException import JspTagException
from admin.taghelpers.StoreFrontHelperFactory import StoreFrontHelperFactory
from org.allbinary.business.context.modules.storefront.StoreFrontData import StoreFrontData
from org.allbinary.logic.StdUtil import StdUtil
from org.allbinary.logic.communication.http.request.AbResponseHandler import AbResponseHandler
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.system.security.licensing.LicensingException import LicensingException


